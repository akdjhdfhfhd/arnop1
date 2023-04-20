import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين ارنوب","المطورين","مطورين","مطورين ar"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝒅𝒊𝒗 𝒏𝒂𝒅𝒆𝒓  ", url=f"https://t.me/Ng_103"), 
                 ],[
                    InlineKeyboardButton(
                        "𝒅𝒊𝒗 𝒎𝒂𝒉𝒎𝒐𝒅 ", url=f"https://t.me/FM_3omda"),
                ],[
                    InlineKeyboardButton(
                        "𝒅𝒊𝒗 𝒂𝒇𝒚𝒐𝒏𝒂 ", url=f"https://t.me/ww_2_2"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝⚡", url=f"https://t.me/N_G_12"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["نادر باشا","نادر","الارنب","مبرمج","nader","NADER"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Ng_103")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["افيونا باشا","افيونا","افيونا","احمد"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ww_2_2")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["محمود باشا","العمده","العمده","محمود","mahmod","العمدده"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("FM_3omda")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["حمد باشا","حمد","الهكر","hamd","Hamd"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""**⩹⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس ar\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝒅𝒊𝒗 𝒏𝒂𝒅𝒆𝒓 ", url=f"https://t.me/Ng_103"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑  ⌝⚡", url=f"https://t.me/N_G_12"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""**⩹⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس ar\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝒅𝒊𝒗 𝒏𝒂𝒅𝒆𝒓 ", url=f"https://t.me/Ng_103"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑  ⌝⚡", url=f"https://t.me/N_G_12"),
                ],

            ]

        ),

    )



    
