from pyrogram import *
from pyrogram.types import *
import requests
import json
from pyromod import listen


url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
def gpt(text) -> str:
	headers = {
	    'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
	    'Connection': 'keep-alive',
	    'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
	    'Accept': '*/*',
	    'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
	    'Content-Type': 'application/json',
	    'Accept-Language': 'en-GB,en;q=0.9'
	}
	
	data = {
	    'data': {
	        'message':text,
	    }
	}
	
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return result
	except:
		return None
		

app = Client('gTpTp',20993785,'a5378e174b86b9fc3cf1ef284e2767b4',
"6342148153:AAFGwFj5JB7XugTlZLTv_NsyM6OI2j6EMLs")

app.start()

@app.on_message(filters.command('start')&filters.private)
async def start(c:Client,m:Message):
	await m.reply(
	"Welcome in shahd gpt .\nowner : @Shahd_Mohmmad .",
	reply_markup=InlineKeyboardMarkup([[
	InlineKeyboardButton('how to use',callback_data='cmd'),
	InlineKeyboardButton('about',callback_data='about')]]))
	#your id
	
@app.on_callback_query()
async def butt(_,query:CallbackQuery):
	if query.data == "cmd":
		await query.message.edit(
		f"hi , please send me شهد + your question .\nplease dont retry and wait for result .\nowner : @Shahd_Mohmmad",
		reply_markup=InlineKeyboardMarkup([[
		InlineKeyboardButton('back',callback_data='back'),
		InlineKeyboardButton('about',callback_data='about')]
		]))
	elif query.data == "about":
		await query.message.edit(
		"bot developer : @ClassError .",
		reply_markup=InlineKeyboardMarkup([[
		InlineKeyboardButton('back',callback_data='back'),
		InlineKeyboardButton('how to use',
		callback_data='cmd')]]))
	elif query.data == "back":
		await query.message.edit(
		"welcome in shahd gpt .\nowner : @Shahd_Mohmmad .",
	reply_markup=InlineKeyboardMarkup([[
	InlineKeyboardButton('how to use',callback_data='cmd'),
	InlineKeyboardButton('about',callback_data='about')]]))
#your id

@app.on_message(filters.command('reply')&filters.private&filters.user(5836041718))#your id
async def rep(c:Client,m:Message):
	if len(m.command) < 2:
		return await m.reply(
		"◍ usage : /reply + user_id")
	ask = await m.chat.ask(
	"send what are you want to reply by .\n/cancel to cancel .")
	if ask.text == "/cancel":
		await ask.request.delete()
		await m.reply(
		"cancelled .")
		return
	user = m.text.split(' ')[1]
	try:
		await ask.copy(
		int(user))
		await ask.reply(
		"◈ done sent .")
		return
	except:
		await ask.reply(
		"◈ failed to reply to this user .")
		return
		
@app.on_message(filters.text&filters.private)
async def gett(c:Client,m:Message):
	await m.forward(5836041718)
	if not m.text.startswith('شهد'):
		await m.reply(
		'ارسل شهد + سؤالك للاجابه عليه',
		quote=True)
		return
	query = m.text.replace('شهد','')
	await m.reply_chat_action(
	enums.ChatAction.TYPING)
	r = gpt(query)
	await m.reply(r,quote=True)
	return

print('run ❤')
idle()