from openai import OpenAI


class AIJSDeobfuscator:
    def __init__(self, api_key, base_url="https://api.deepseek.com"):
        """初始化AI反混淆器"""
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def deobfuscate_file(self, input_path, output_path=None, model="deepseek-chat"):
        """
        读取混淆JS文件并通过AI反混淆
        :param input_path: 混淆JS文件路径
        :param output_path: 反混淆结果保存路径（可选）
        :param model: 使用的AI模型
        :return: 反混淆后的代码
        """
        # 1. 读取混淆代码
        with open(input_path, 'r', encoding='utf-8') as f:
            obfuscated_code = f.read()

        # 2. 构建提示词（关键：明确反混淆要求）
        system_prompt = """
        你是专业的JavaScript反混淆工具，请对提供的混淆代码进行处理：
        1. 还原变量名、函数名（使用有意义的名称）
        2. 解密加密字符串、展开数组引用
        3. 简化控制流（去除冗余跳转、扁平化结构）
        4. 如果有vmp虚拟机混淆加固的话，也需要还原
        4. 保留原始功能逻辑，只优化可读性
        5. 输出整理后的完整代码，不添加额外解释
        6. 需要确保还原的代码可以正确执行和完整性
        7. 需要标明代码使用了那些混淆方式
        """
        user_prompt = f"请反混淆以下JavaScript代码：\n```javascript\n{obfuscated_code}\n```"

        # 3. 调用AI接口
        # response = self.client.chat.completions.create(
        #     model=model,
        #     messages=[
        #         {"role": "system", "content": system_prompt},
        #         {"role": "user", "content": user_prompt}
        #     ],
        #     temperature=0.3  # 低随机性，保证代码准确性
        # )
        response = self.client.chat.completions.create(
            model="qwen-long",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3  # 低随机性，保证代码准确性
        )
        deobfuscated_code = response.choices[0].message.content.strip()

        # 4. 提取代码块（去除可能的markdown标记）
        if deobfuscated_code.startswith('```javascript'):
            deobfuscated_code = deobfuscated_code.split('```javascript')[1].split('```')[0].strip()

        # 5. 保存结果（如果指定输出路径）
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(deobfuscated_code)
            print(f"反混淆完成，结果已保存至：{output_path}")

        return deobfuscated_code


# 使用示例
if __name__ == "__main__":
    # 初始化（替换为你的API密钥）
    # de_obfuscator = AIJSDeobfuscator(
    #     api_key="sk-bc6d895f807447f1b706c41f1ce1f4d4",
    #     base_url="https://api.deepseek.com"
    # )
    de_obfuscator = AIJSDeobfuscator(
        api_key="sk-3caf28ae9b084173b8f48dce107645d7",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    # api_key="sk-3caf28ae9b084173b8f48dce107645d7",
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    # 执行反混淆（输入文件→输出文件）
    result = de_obfuscator.deobfuscate_file(
        input_path="obfuscated.js",  # 混淆的JS文件
        output_path="deobfuscated.js"  # 反混淆结果保存路径
    )

    # 打印结果（可选）
    print("\n反混淆结果：")
    print(result)
