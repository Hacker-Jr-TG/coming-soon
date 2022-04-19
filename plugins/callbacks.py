from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import Client
from plugins.buttons import KGF_BUTTON
import asyncio
import random


@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    elif msg.data == "downlod":
        await msg.message.edit(
            text="""<b>• Nᴀᴍᴇ : KGF
• Yᴇᴀʀ : 2022
• Sɪᴢᴇ : - 1400MB</b>""",
            reply_markup=InlineKeyboardMarkup(KGF_BUTTON)
        )
