from .base import BaseDeobfuscator
import jsbeautifier

class FormatCodeDeobfuscator(BaseDeobfuscator):
    def deobfuscate(self, code: str) -> str:
        return jsbeautifier.beautify(code) 