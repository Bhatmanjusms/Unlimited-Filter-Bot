import os
import math
import json
import time
import shutil
import heroku3
import requests

from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import Script
from plugins.helpers import humanbytes
from database.filters_mdb import filter_stats
from database.users_mdb import add_user, find_user, all_users


@trojanz.on_message(filters.command('id') & (filters.private | filters.group))
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(
            f"Your ID : `{user_id}`",
            parse_mode="md",
            quote=True
        )
    elif (chat_type == "group") or (chat_type == "supergroup"):
        user_id = message.from_user.id
        chat_id = message.chat.id
        if message.reply_to_message:
            reply_id = f"Replied User ID : `{message.reply_to_message.from_user.id}`"
        else:
            reply_id = ""
        await message.reply_text(
            f"Your ID : `{user_id}`\nThis Group ID : `{chat_id}`\n\n{reply_id}",
            parse_mode="md",
            quote=True
        )   


@trojanz.on_message(filters.command('info') & (filters.private | filters.group))
async def showinfo(client, message):
    try:
        cmd, id = message.text.split(" ", 1)
    except:
        id = False
        pass

    if id:
        if (len(id) == 10 or len(id) == 9):
            try:
                checkid = int(id)
            except:
                await message.reply_text("__Enter a valid USER ID__", quote=True, parse_mode="md")
                return
        else:
            await message.reply_text("__Enter a valid USER ID__", quote=True, parse_mode="md")
            return           

        if Config.SAVE_USER == "yes":
            name, username, dcid = await find_user(str(id))
        else:
            try:
                user = await client.get_users(int(id))
                name = str(user.first_name + (user.last_name or ""))
                username = user.username
                dcid = user.dc_id
            except:
                name = False
                pass

        if not name:
            await message.reply_text("__USER Details not found!!__", quote=True, parse_mode="md")
            return
    else:
        if message.reply_to_message:
            name = str(message.reply_to_message.from_user.first_name\
                    + (message.reply_to_message.from_user.last_name or ""))
            id = message.reply_to_message.from_user.id
            username = message.reply_to_message.from_user.username
            dcid = message.reply_to_message.from_user.dc_id
        else:
            name = str(message.from_user.first_name\
                    + (message.from_user.last_name or ""))
            id = message.from_user.id
            username = message.from_user.username
            dcid = message.from_user.dc_id
    
    if not str(username) == "None":
        user_name = f"@{username}"
    else:
        user_name = "none"

    await message.reply_text(
        f"<b>Name</b> : {name}\n\n"
        f"<b>User ID</b> : <code>{id}</code>\n\n"
        f"<b>Username</b> : {user_name}\n\n"
        f"<b>Permanant USER link</b> : <a href='tg://user?id={id}'>Click here!</a>\n\n"
        f"<b>DC ID</b> : {dcid}\n\n",
        quote=True,
        parse_mode="html"
    )


@trojanz.on_message((filters.private | filters.group) & filters.command('status'))
async def bot_status(client,message):
    if str(message.from_user.id) not in Config.AUTH_USERS:
        return

    chats, filters = await filter_stats()

    if Config.SAVE_USER == "yes":
        users = await all_users()
        userstats = f"> __**{users} 𝘶𝘴𝘦𝘳𝘴 𝘩𝘢𝘷𝘦 𝘪𝘯𝘵𝘦𝘳𝘢𝘤𝘵𝘦𝘥 𝘸𝘪𝘵𝘩 𝘺𝘰𝘶𝘳 𝘣𝘰𝘵**__\n\n"
    else:
        userstats = ""

    if Config.HEROKU_API_KEY:
        try:
            server = heroku3.from_key(Config.HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {Config.HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)
                quota_details = f"""
**🔮 𝘏𝘦𝘳𝘰𝘬𝘶 𝘢𝘤𝘤𝘰𝘶𝘯𝘵 𝘴𝘵𝘢𝘵𝘶𝘴🔮 **

• __𝘠𝘰𝘶 𝘩𝘢𝘷𝘦 **{total} 𝘩𝘰𝘶𝘳𝘴** 𝘰𝘧 𝘧𝘳𝘦𝘦 𝘥𝘺𝘯𝘰 𝘲𝘶𝘰𝘵𝘢 𝘢𝘷𝘢𝘪𝘭𝘢𝘣𝘭𝘦 𝘦𝘢𝘤𝘩 𝘮𝘰𝘯𝘵𝘩.__

• __𝘋𝘺𝘯𝘰 𝘩𝘰𝘶𝘳𝘴 𝘶𝘴𝘦𝘥 𝘵𝘩𝘪𝘴 𝘮𝘰𝘯𝘵𝘩__ ;
        - **{used} 𝘩𝘰𝘶𝘳𝘴**  ( {usedperc}% )

• __𝘋𝘺𝘯𝘰 𝘩𝘰𝘶𝘳𝘴 𝘳𝘦𝘮𝘢𝘪𝘯𝘪𝘯𝘨 𝘵𝘩𝘪𝘴 𝘮𝘰𝘯𝘵𝘩__ ;
        - **{hours} 𝘩𝘰𝘶𝘳𝘴**  ( {leftperc}% )
        - **𝘈𝘱𝘱𝘳𝘰𝘹𝘪𝘮𝘢𝘵𝘦𝘭𝘺 {days} 𝘥𝘢𝘺𝘴**
"""
            else:
                quota_details = ""
        except:
            print("Check your Heroku API key")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - Config.BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**🗃️ 𝘋𝘪𝘴𝘤 𝘥𝘦𝘵𝘢𝘪𝘭𝘴 🗃️**\n\n" \
            f"> 𝘜𝘚𝘌𝘋  :  {used} / {total}\n" \
            f"> 𝘍𝘙𝘌𝘌  :  {free}\n\n"
    except:
        disk = ""
    await message.reply_text(
        "**🗞️ 𝘊𝘶𝘳𝘳𝘦𝘯𝘵 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘧 𝘺𝘰𝘶𝘳 𝘣𝘰𝘵 🗞️**\n\n"
        f"• __**{filters}** 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 𝘢𝘤𝘳𝘰𝘴𝘴 **{chats}** 𝘤𝘩𝘢𝘵𝘴__\n\n"
        f"{userstats}"
        f"• __𝘉𝘰𝘵 𝘶𝘱𝘵𝘪𝘮𝘦__ : **{uptime}**\n\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode="md"
    )


@trojanz.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=Script.START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝘓𝘦𝘵’𝘴 𝘳𝘰𝘭𝘭", url=f'http://t.me/?startgroup=true')
                    ],[
                    InlineKeyboardButton("❓ 𝘏𝘦𝘭𝘱 ❓", callback_data="help_data")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )
    if Config.SAVE_USER == "yes":
        try:
            await add_user(
                str(message.from_user.id),
                str(message.from_user.username),
                str(message.from_user.first_name + " " + (message.from_user.last_name or "")),
                str(message.from_user.dc_id)
            )
        except:
            pass


@trojanz.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️‍🔥 𝘈𝘣𝘰𝘶𝘵 𝘮𝘦", callback_data="about_data"),
                    InlineKeyboardButton("🤖 𝘉𝘰𝘵 𝘤𝘩𝘢𝘯𝘯𝘦𝘭", url="https://t.me/filmyfunda_movies")
                ],
                [
                    InlineKeyboardButton("🔙 𝘉𝘢𝘤𝘬", callback_data="start_data"),
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command('about') & filters.private)
async def about(client, message):
    await message.reply_text(
        text=Script.ABOUT_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘚𝘰𝘶𝘳𝘤𝘦 𝘤𝘰𝘥𝘦", url="https://t.me/filmyfunda_movies")
                ],
                [
                    InlineKeyboardButton("🔙 𝘉𝘢𝘤𝘬", callback_data="help_data"),
                    InlineKeyboardButton("❌ 𝘊𝘭𝘰𝘴𝘦", callback_data="close_data"),
                ]                
            ]
        ),
        reply_to_message_id=message.message_id
    )
