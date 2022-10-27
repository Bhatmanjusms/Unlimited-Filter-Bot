class Script(object):

    START_MSG = """𝘏𝘦𝘭𝘭𝘰 {},🤟🏻
𝘐'𝘮 𝘢𝘯 𝘢𝘥𝘷𝘢𝘯𝘤𝘦𝘥 𝘧𝘪𝘭𝘵𝘦𝘳 𝘣𝘰𝘵 𝘸𝘩𝘪𝘤𝘩 𝘪𝘴 𝘥𝘦𝘴𝘪𝘨𝘯𝘦𝘥 𝘢𝘯𝘥 𝘣𝘶𝘪𝘭𝘵 𝘧𝘰𝘳 𝘢𝘥𝘥𝘪𝘯𝘨 𝘶𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 𝘪𝘯 𝘢𝘯𝘺 𝘨𝘳𝘰𝘶𝘱.
𝘛𝘩𝘦𝘳𝘦 𝘪𝘴 𝘯𝘰 𝘱𝘳𝘢𝘤𝘵𝘪𝘤𝘢𝘭 𝘭𝘪𝘮𝘪𝘵𝘴 𝘧𝘰𝘳 𝘮𝘺 𝘧𝘪𝘭𝘵𝘦𝘳𝘪𝘯𝘨 𝘤𝘢𝘱𝘢𝘤𝘪𝘵𝘺 🥰
𝘏𝘪𝘵 <i>/help</i> 𝘧𝘰𝘳 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴 𝘢𝘯𝘥 𝘮𝘰𝘳𝘦 𝘥𝘦𝘵𝘢𝘪𝘭𝘴..</b>
"""


    HELP_MSG = """
<i> 𝘈𝘥𝘥 𝘮𝘦 𝘢𝘴 𝘢𝘥𝘮𝘪𝘯 𝘪𝘯 𝘺𝘰𝘶𝘳 𝘨𝘳𝘰𝘶𝘱 𝘢𝘯𝘥 𝘴𝘵𝘢𝘳𝘵 𝘧𝘪𝘭𝘵𝘦𝘳𝘪𝘯𝘨 🤗 </i>

<b>🧿 Basic Commands 🧿</b>

/start - 𝘊𝘩𝘦𝘤𝘬 𝘪𝘧 𝘐'𝘮 𝘢𝘭𝘪𝘷𝘦 💀
/help - 𝘊𝘰𝘮𝘮𝘢𝘯𝘥 𝘩𝘦𝘭𝘱 🛡️
/about - 𝘚𝘰𝘮𝘦𝘵𝘩𝘪𝘯𝘨 𝘢𝘣𝘰𝘶𝘵 𝘮𝘦 🙂

<b>🛠️ Filter Commands 🛠️</b>

<code>/add name reply</code>  -  𝘈𝘥𝘥 𝘧𝘪𝘭𝘵𝘦𝘳 𝘧𝘰𝘳 𝘯𝘢𝘮𝘦

<code>/del name</code>  -  𝘋𝘦𝘭𝘦𝘵𝘦 𝘧𝘪𝘭𝘵𝘦𝘳

<code>/delall</code>  -  𝘋𝘦𝘭𝘦𝘵𝘦 𝘦𝘯𝘵𝘪𝘳𝘦 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 (𝘎𝘳𝘰𝘶𝘱 𝘖𝘸𝘯𝘦𝘳 𝘖𝘯𝘭𝘺)

<code>/viewfilters</code>  -  𝘓𝘪𝘴𝘵 𝘢𝘭𝘭 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 𝘪𝘯 𝘤𝘩𝘢𝘵

<b>🧬 Connection Commands 🧬</b>

<code>/connect groupid</code>  -  𝘊𝘰𝘯𝘯𝘦𝘤𝘵 𝘺𝘰𝘶𝘳 𝘨𝘳𝘰𝘶𝘱 𝘵𝘰 𝘮𝘺 𝘗𝘔. 𝘠𝘰𝘶 𝘤𝘢𝘯 𝘢𝘭𝘴𝘰 𝘴𝘪𝘮𝘱𝘭𝘺 𝘶𝘴𝘦,
<code>/connect</code> 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱𝘴.

<code>/connections</code>  -  𝘔𝘢𝘯𝘢𝘨𝘦 𝘺𝘰𝘶𝘳 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘪𝘰𝘯𝘴.

<b>💊 Extras 💊</b>

/status  -  𝘚𝘩𝘰𝘸𝘴 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘧 𝘺𝘰𝘶𝘳 𝘣𝘰𝘵 (𝘈𝘶𝘵𝘩 𝘜𝘴𝘦𝘳 𝘖𝘯𝘭𝘺)
/id  -  𝘚𝘩𝘰𝘸𝘴 𝘐𝘋 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯

<code>/info userid</code>  -  𝘚𝘩𝘰𝘸𝘴 𝘜𝘴𝘦𝘳 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯. 𝘜𝘴𝘦 <code>/info</code> 𝘢𝘴 𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘴𝘰𝘮𝘦 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘧𝘰𝘳 𝘵𝘩𝘦𝘪𝘳 𝘥𝘦𝘵𝘢𝘪𝘭𝘴

"""


    ABOUT_MSG = """⭕️<b>My Name : Nohara filter bot</b>

🏆<b>Creater :</b> @Imdb_updates    

🧩<b>Language :</b> <code>Python3</code>

📂<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
