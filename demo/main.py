# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import sys
from utils.file_io import read_file, write_file
from deobfuscators.rename_vars import RenameVarsDeobfuscator
from deobfuscators.format_code import FormatCodeDeobfuscator


def main(input_path, output_path):
    code = read_file(input_path)
    # 依次应用反混淆器
    deobfuscators = [
        RenameVarsDeobfuscator(),
        FormatCodeDeobfuscator(),
    ]
    for deob in deobfuscators:
        code = deob.deobfuscate(code)
    write_file(output_path, code)
    print(f"反混淆完成，输出文件：{output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python main.py 输入文件.js 输出文件.js")
    else:
        main(sys.argv[1], sys.argv[2])

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
