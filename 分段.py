from openai import OpenAI
import os
import json
import time
from termcolor import colored


class AIJSDeobfuscator:
    def __init__(self, api_key, base_url="https://api.deepseek.com"):
        """初始化AI反混淆器"""
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.context = []  # 存储对话上下文
        self.current_chunk = 0  # 当前处理的代码块
        self.total_chunks = 0  # 代码块总数
        self.obfuscated_code = ""  # 完整混淆代码
        self.deobfuscated_code = ""  # 完整反混淆代码
        self.chunks = []  # 代码块列表
        self.progress_file = "deobfuscation_progress.json"  # 进度保存文件

    def load_code_from_file(self, input_path):
        """从文件加载混淆代码"""
        with open(input_path, 'r', encoding='utf-8') as f:
            self.obfuscated_code = f.read()
        print(f"已加载混淆代码，共{len(self.obfuscated_code)}个字符")

    def split_code_into_chunks(self, chunk_size=4000):
        """将代码分割成多个块，每块不超过指定大小"""
        if not self.obfuscated_code:
            print("请先加载混淆代码")
            return

        # 尝试按函数、类和关键语法分割代码
        # 使用正则表达式找到函数、类和其他可能的分割点
        split_points = []

        # 查找函数定义
        for match in re.finditer(
                r'(function\s+|async\s+function\s+|const\s+\w+\s*=\s*function\s+|let\s+\w+\s*=\s*function\s+|var\s+\w+\s*=\s*function\s+|arrow function)',
                self.obfuscated_code):
            split_points.append(match.start())

        # 查找类定义
        for match in re.finditer(r'class\s+\w+', self.obfuscated_code):
            split_points.append(match.start())

        # 如果找不到足够的分割点，按固定大小分割
        if len(split_points) < 2:
            self.chunks = [self.obfuscated_code[i:i + chunk_size] for i in
                           range(0, len(self.obfuscated_code), chunk_size)]
            self.total_chunks = len(self.chunks)
            print(f"代码被分割为{self.total_chunks}块（按固定大小）")
            return

        # 基于分割点进行分割
        split_points.sort()
        self.chunks = []
        last_point = 0

        for i, point in enumerate(split_points):
            # 如果距离上一个分割点太远，或者是最后一个分割点
            if point - last_point > chunk_size or i == len(split_points) - 1:
                # 找到一个合适的结束点（例如函数结束的大括号）
                end_point = self.find_code_block_end(self.obfuscated_code, point)
                if end_point == -1:
                    end_point = point + chunk_size

                self.chunks.append(self.obfuscated_code[last_point:end_point])
                last_point = end_point

                if len(self.chunks) * chunk_size > len(self.obfuscated_code):
                    break

        # 添加剩余的代码
        if last_point < len(self.obfuscated_code):
            self.chunks.append(self.obfuscated_code[last_point:])

        self.total_chunks = len(self.chunks)
        print(f"代码被分割为{self.total_chunks}块（按逻辑结构）")

    def find_code_block_end(self, code, start_pos):
        """找到代码块的结束位置（匹配的大括号）"""
        open_braces = 0
        in_string = False
        string_quote = None

        for i in range(start_pos, len(code)):
            char = code[i]

            # 处理字符串
            if char in ['"', "'", "`"]:
                if not in_string:
                    in_string = True
                    string_quote = char
                elif in_string and string_quote == char:
                    # 检查是否是转义的引号
                    if i > 0 and code[i - 1] == '\\':
                        continue
                    in_string = False
                    string_quote = None

            if in_string:
                continue

            # 处理大括号
            if char == '{':
                open_braces += 1
            elif char == '}':
                open_braces -= 1
                if open_braces == 0:
                    return i + 1  # 返回大括号之后的位置

        return -1  # 没有找到匹配的结束

    def build_chunk_prompt(self, chunk_index):
        """构建当前代码块的提示词"""
        chunk = self.chunks[chunk_index]

        system_prompt = f"""
        你是专业的JavaScript反混淆工具。当前正在处理第{chunk_index + 1}/{self.total_chunks}部分代码。
        请对提供的混淆代码进行处理：
        1. 还原变量名、函数名（使用有意义的名称）
        2. 解密加密字符串、展开数组引用
        3. 简化控制流（去除冗余跳转、扁平化结构）
        4. 如果有vmp虚拟机混淆加固的话，也需要还原
        5. 保留原始功能逻辑，只优化可读性
        6. 输出整理后的完整代码块，不添加额外解释
        7. 需要确保还原的代码可以正确执行和完整性
        8. 请在代码块前标明"// 第{chunk_index + 1}/{self.total_chunks}部分"
        9. 请在代码块后标明"// 第{chunk_index + 1}/{self.total_chunks}部分结束"
        """

        user_prompt = f"请反混淆以下JavaScript代码块：\n```javascript\n{chunk}\n```"

        return system_prompt, user_prompt

    def deobfuscate_chunk(self, chunk_index, model="deepseek-chat"):
        """反混淆单个代码块"""
        if chunk_index >= self.total_chunks:
            print("已处理完所有代码块")
            return

        print(f"\n正在处理第{chunk_index + 1}/{self.total_chunks}部分...")

        system_prompt, user_prompt = self.build_chunk_prompt(chunk_index)

        # 调用AI接口
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3  # 低随机性，保证代码准确性
        )

        deobfuscated_chunk = response.choices[0].message.content.strip()

        # 提取代码块（去除可能的markdown标记）
        if deobfuscated_chunk.startswith('```javascript'):
            deobfuscated_chunk = deobfuscated_chunk.split('```javascript')[1].split('```')[0].strip()

        # 添加到完整结果
        self.deobfuscated_code += deobfuscated_chunk + "\n\n"

        # 更新当前处理的块
        self.current_chunk = chunk_index + 1

        # 保存进度
        self.save_progress()

        return deobfuscated_chunk

    def save_progress(self):
        """保存当前进度"""
        progress_data = {
            "current_chunk": self.current_chunk,
            "total_chunks": self.total_chunks,
            "deobfuscated_code": self.deobfuscated_code
        }

        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, indent=2)

        print(f"进度已保存至 {self.progress_file}")

    def load_progress(self):
        """加载保存的进度"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                progress_data = json.load(f)

            self.current_chunk = progress_data.get("current_chunk", 0)
            self.total_chunks = progress_data.get("total_chunks", 0)
            self.deobfuscated_code = progress_data.get("deobfuscated_code", "")

            print(f"已加载进度：已处理{self.current_chunk}/{self.total_chunks}部分")
            return True
        return False

    def interactive_deobfuscate(self, input_path, output_path=None, model="deepseek-chat"):
        """交互式反混淆流程"""
        # 加载代码
        self.load_code_from_file(input_path)

        # 尝试加载进度
        if not self.load_progress():
            # 分割代码
            self.split_code_into_chunks()

        # 开始交互式处理
        while self.current_chunk < self.total_chunks:
            # 处理当前块
            deobfuscated_chunk = self.deobfuscate_chunk(self.current_chunk, model)

            # 显示处理结果摘要
            print(colored(f"\n第{self.current_chunk}/{self.total_chunks}部分处理完成", "green"))
            print(f"代码长度: {len(deobfuscated_chunk)} 字符")

            # 显示前几行作为预览
            preview_lines = deobfuscated_chunk.split('\n')[:5]
            print(colored("\n预览:", "blue"))
            for line in preview_lines:
                print(line)
            if len(preview_lines) < len(deobfuscated_chunk.split('\n')):
                print("...")

            # 询问用户是否继续
            while True:
                user_input = input("\n是否继续处理下一部分？(y/n/s:保存并退出): ").lower().strip()
                if user_input == 'y':
                    break
                elif user_input == 'n':
                    print("已暂停处理。下次运行时将从当前位置继续。")
                    return
                elif user_input == 's':
                    if output_path:
                        self.save_deobfuscated_code(output_path)
                    print("已保存结果并暂停处理。下次运行时将从当前位置继续。")
                    return
                else:
                    print("无效输入，请输入 y、n 或 s")

        # 处理完成
        print(colored(f"\n🎉 全部{self.total_chunks}部分处理完成！", "cyan"))

        # 保存最终结果
        if output_path:
            self.save_deobfuscated_code(output_path)

        return self.deobfuscated_code

    def save_deobfuscated_code(self, output_path):
        """保存反混淆后的完整代码"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.deobfuscated_code)
        print(f"反混淆完成，结果已保存至：{output_path}")


# 使用示例
if __name__ == "__main__":
    # 初始化（替换为你的API密钥）
    de_obfuscator = AIJSDeobfuscator(
        api_key="sk-bc6d895f807447f1b706c41f1ce1f4d4",
        base_url="https://api.deepseek.com"
    )

    # 开始交互式反混淆
    de_obfuscator.interactive_deobfuscate(
        input_path="obfuscated.js",  # 混淆的JS文件
        output_path="deobfuscated.js"  # 反混淆结果保存路径
    )