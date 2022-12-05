buttons = [[
            InlineKeyboardButton('💌 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 💌', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 𝐒𝐞𝐚𝐫𝐜𝐡 🔎', url='https://t.me/iPapGroup'),
            InlineKeyboardButton('⚡️ 𝐔𝐩𝐝𝐚𝐭𝐞 ⚡️', url='https://t.me/iPapkornOfficial')
            ],[
            InlineKeyboardButton('♻️ 𝐇𝐞𝐥𝐩 ♻️', callback_data='help'),
            InlineKeyboardButton('♻️ 𝐀𝐛𝐨𝐮𝐭 ♻️', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        await query.answer('Piracy Is Crime')
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('𝗠𝗮𝗻𝘂𝗲𝗹 𝗙𝗶𝗹𝘁𝗲𝗿', callback_data='manuelfilter'),
            InlineKeyboardButton('𝗔𝘂𝘁𝗼 𝗙𝗶𝗹𝘁𝗲𝗿', callback_data='autofilter'),
            InlineKeyboardButton('𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻𝘀', callback_data='coct')
        ], [
            InlineKeyboardButton('𝗘𝘅𝘁𝗿𝗮 𝗠𝗼𝗱𝗲𝘀', callback_data='GHHM'),
            InlineKeyboardButton(' 𝗢𝗪𝗡𝗘𝗥', callback_data='owner'),
            InlineKeyboardButton(' 𝗦𝗼𝗻𝗴𝘀 ', callback_data='songs')
        ], [
            InlineKeyboardButton('𝗨𝗥𝗟 𝗦𝗵𝗼𝗿𝘁', callback_data='urlshort'),
            InlineKeyboardButton('𝗬.𝗧 𝗧𝗵𝘂𝗺𝗯', callback_data='ytthumb'),
            InlineKeyboardButton('𝗬.𝗧 𝗩𝗶𝗱𝗲𝗼', callback_data='video')
        ], [
            InlineKeyboardButton('📊 𝗦𝘁𝗮𝘁𝘀 📊', callback_data='stats'),
            InlineKeyboardButton('𝗙𝗶𝗹𝗲-𝗦𝘁𝗼𝗿𝗲', callback_data='malikk')
        ], [
            InlineKeyboardButton('🏠 𝗛𝗼𝗺𝗲 🏠', callback_data='start'),
            InlineKeyboardButton('🔐 𝗖𝗹𝗼𝘀𝗲 🔐', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('♥️ 𝗦𝗼𝘂𝗿𝗰𝗲 ❤️', callback_data='source'),
            InlineKeyboardButton('🏠 𝗛𝗼𝗺𝗲 🏠', callback_data='start'),
            InlineKeyboardButton('🔐 𝗖𝗹𝗼𝘀𝗲 🔐', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "GHHM":
        buttons = [[
            InlineKeyboardButton('𝗘𝘅𝘁𝗿𝗮 𝗠𝗼𝗱𝗲𝘀', callback_data='extra'),
            InlineKeyboardButton('𝗘𝘅𝘁𝗿𝗮', callback_data='mbbumm')
        ], [
            InlineKeyboardButton('🏠 𝗛𝗼𝗺𝗲 🏠', callback_data='start'),
            InlineKeyboardButton('🔐 𝗖𝗹𝗼𝘀𝗲 🔐', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GHHN_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "urlshort":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.URLSHORT_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "malikk":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FILESTORE_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "group_rules":
        buttons = [[
            InlineKeyboardButton('💢 𝗖𝗹𝗼𝘀𝗲 💢', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GROUP_R_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "video":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VIDEO_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "songs":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SONG_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "owner":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='start'),
            InlineKeyboardButton('❗️ 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 ❗️', url='https://t.me/AkshayChand10'),
            InlineKeyboardButton('❤️ 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻 ❤️', callback_data='malik')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.OWNER_TXT,





cap = f"<b>𝐇𝐞𝐲...🖐️ {message.from_user.mention},\n\n𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐫𝐞𝐬𝐮𝐥𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 {search}\n\n📟 𝐌𝐨𝐯𝐢𝐞 𝐧𝐚𝐦𝐞:- {search}\n👩🏻‍💻 𝐑𝐞𝐪𝐮𝐞𝐬𝐭:- {message.from_user.mention}\n🚀 𝐆𝐫𝐨𝐮𝐩:- {message.chat.title}</b>"
    if imdb and imdb.get('poster'):
        try:
            hehe = await message.reply_photo(photo=imdb.get('poster'), caption=cap, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(1200)
            await hehe.delete()
            await message.delete()
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            hmm = await message.reply_photo(photo=poster, caption=cap, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(1200)
            await hmm.delete()
            await message.delete()
        except Exception as e:
            logger.exception(e)
            fek = await message.reply_photo(photo="https://graph.org/file/97235830d42b4fd4c9815.jpg", caption=cap, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(1200)
            await fek.delete()
            await msg.delete()
    else:
        fuk = await message.reply_photo(photo="https://graph.org/file/e10a1c60e0de75459435e.jpg", caption=cap, reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(1200)
        await fuk.delete()
        await msg.delete()
    if spoll:
        await msg.message.delete()

#2
pre = 'filep' if settings['file_secure'] else 'file'
    req = message.from_user.id if message.from_user else 0
    if settings["button"]:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=pre_{file.file_id}")
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=pre_{file.file_id}")
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=pre_{file.file_id}")
                ),
            ]
            for file in files
        ]

#1
settings = await get_settings(query.message.chat.id)
    nxxreq  = query.from_user.id if query.from_user else 0
    if settings['button']:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}")
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'files#{nxxreq}#{file.file_id}'
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}")
                ),
            ]
            for file in files
        ]


