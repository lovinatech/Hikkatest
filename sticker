from hikkatl.types import Message
from .. import loader
from telethon.tl.types import Document

@loader.tds
class StickerModule(loader.Module):
    """Module for sending stickers by ID"""
    
    strings = {"name": "StickerModule"}
    
    @loader.command
    async def sticker(self, message: Message):
        """Sends a sticker by ID: .sticker <sticker_id>"""
        args = message.text.split(" ")
        
        if len(args) != 2:
            await message.answer("Usage: .sticker <sticker_id>")
            return
        
        sticker_id = args[1]
        
        try:
            sticker_id = int(sticker_id)
        except ValueError:
            await message.answer("Invalid sticker ID.")
            return
        
        sticker = Document(document=await message.client.get_input_document(sticker_id))
        
        await message.client.send_file(message.chat_id, file=sticker)
