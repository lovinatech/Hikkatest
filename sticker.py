from hikkatl.types import Message
from .. import loader

@loader.tds
class TestModule(loader.Module):
    """Тестовый модуль"""
    
    @loader.command
    async def test(self, message: Message):
        """Приветственное сообщение"""
        await message.edit("Привет")
