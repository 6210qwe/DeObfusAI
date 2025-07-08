from .base import BaseDeobfuscator
import re


class RenameVarsDeobfuscator(BaseDeobfuscator):
    def deobfuscate(self, code: str) -> str:
        # 简单示例：将a、b、c等变量名替换为var1、var2、var3
        var_map = {}
        var_count = 1

        def repl(match):
            nonlocal var_count
            var = match.group(0)
            if var not in var_map:
                var_map[var] = f"var{var_count}"
                var_count += 1
            return var_map[var]

        return re.sub(r'\b[a-zA-Z]\b', repl, code)
