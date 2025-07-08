class BaseDeobfuscator:
    def deobfuscate(self, code: str) -> str:
        raise NotImplementedError("deobfuscate方法需要子类实现") 