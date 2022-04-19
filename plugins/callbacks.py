from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import Client
from plugins.buttons import KGF_BUTTON
import asyncio
import random



@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "next":
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
            reply_markup=InlineKeyboardMarkup()
        )
    elif msg.data == "downlod":
        await msg.message.edit(
            text="""<b>• Nᴀᴍᴇ : KGF
• Yᴇᴀʀ : 2022
• Sɪᴢᴇ : - 1400MB</b>""",
            reply_markup=InlineKeyboardMarkup(KGF_BUTTON)
        )

    elif msg.data == "smovies":
        await msg.answer("Tᴏ Dᴏᴡɴʟᴏᴀᴅ Kɢғ 𝟸 Sᴇɴᴅ Tʜɪs Tᴇxᴛ kgf 2", show_alert=True)

    elif msg.data == "scommands":
        await msg.answer("/start - Tᴏ Sᴛᴀʀᴛ Tʜɪs Bᴏᴛ\n/id - Tᴏ Gᴇᴛ Iᴅ ( ᵒⁿˡʸ ʷᵒʳᵏˢ ⁱⁿ ᵍʳᵒᵘᵖ )", show_alert=True)
