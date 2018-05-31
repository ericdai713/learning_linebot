from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import *
import requests
import sys
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import pygsheets
import pytz
app = Flask(__name__)

line_bot_api = LineBotApi('XNfPf1f8R5lAlZMy49o0iVEaW0J7REURi8sQ8vpT6voY0s84f8Qwqg3rZyyXKxqXdYXjEg1NW+lBnoIB6VfPl+yKvbHO29EmujsYs9XYnaEJFnKa67fbzIGtxPGuc2fAdhMUx+ffLmT0Omb2lNg/mgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d2c493d92a8fc3a7fe31ad9552c105ec')
message = TemplateSendMessage(
	alt_text='開始玩',
	template=ButtonsTemplate(
		thumbnail_image_url='https://salemnet.vo.llnwd.net/media/cms/CW/faith/34624-start-startover-startingline.1200w.tn.jpg',
		title='選擇服務',
		text='請選擇',
		actions=[
			MessageTemplateAction(
				label='linebot建置',
				text='linebot建置',
			),
			MessageTemplateAction(
				label='爬蟲教學',
				text='爬蟲教學'
			)
		]
	)
)
tpe = pytz.timezone('Asia/Taipei')
gc = pygsheets.authorize(service_file='service_creds.json')
sh = gc.open('測驗結果')
wks = sh[0]
wks2 = sh[1]
wks3 = sh[2]
wks4 = sh[3]
wks5 = sh[4]
wks6 = sh[5]
wks7 = sh[6]
wks8 = sh[7]
wks9 = sh[8]
wks10 = sh[9]
wks11 = sh[10]
wks12 = sh[11]
wks13 = sh[12]
wks14 = sh[13]
wks15 = sh[14]
sym = sh[15]
@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'
	
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	profile = line_bot_api.get_profile(event.source.user_id)
	message3 = TemplateSendMessage(
		alt_text='爬蟲教學',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
					title='課程一',
					text='課程一',
					actions=[
						URITemplateAction(
							label='課程一影片',
							uri='http://140.115.157.83/課程一?id='+profile.display_name+'&video=課程一'
						),
						MessageTemplateAction(
							label='課程一測驗',
							text='課程一測驗'
						)
					]
				),
				CarouselColumn(
					thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
					title='課程二',
					text='課程二',
					actions=[
						URITemplateAction(
							label='課程二影片',
							uri='http://140.115.157.83/課程二?id='+profile.display_name+'&video=課程二'
						),
						MessageTemplateAction(
							label='課程二測驗',
							text='課程二測驗'
						)
					]
				),
				CarouselColumn(
					thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
					title='課程三',
					text='課程三',
					actions=[
						URITemplateAction(
							label='課程三影片',
							uri='http://140.115.157.83/課程三?id='+profile.display_name+'&video=課程三'
						),
						MessageTemplateAction(
							label='課程三測驗',
							text='課程三測驗'
						)
					]
				),
				CarouselColumn(
					thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
					title='課程四',
					text='課程四',
					actions=[
						URITemplateAction(
							label='課程四影片',
							uri='http://140.115.157.83/課程四?id='+profile.display_name+'&video=課程四'
						),
						MessageTemplateAction(
							label='課程四測驗',
							text='課程四測驗'
						)
					]
				),
				CarouselColumn(
					thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
					title='課程五',
					text='課程五',
					actions=[
						URITemplateAction(
							label='課程五影片',
							uri='http://140.115.157.83/課程五?id='+profile.display_name+'&video=課程五'
						),
						MessageTemplateAction(
							label='課程五測驗',
							text='課程五測驗'
						)
					]
				),
				CarouselColumn(
					thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
					title='課程六',
					text='課程六',
					actions=[
						URITemplateAction(
							label='課程六影片',
							uri='http://140.115.157.83/課程六?id='+profile.display_name+'&video=課程六'
						),
						MessageTemplateAction(
							label='課程六測驗',
							text='課程六測驗'
						)
					]
				)
			]
		)
	)
	response = requests.get('http://140.115.157.83/line.php?id='+profile.display_name+'&answer='+event.message.text+'&time='+datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"))
	if event.message.text == "1-1:(A)":
		cell_list = wks.find(profile.display_name)
		if not cell_list:
			wks.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C)以上皆非'),message3])
	elif event.message.text == "1-1:(B)":
		cell_list = wks.find(profile.display_name)
		if not cell_list:
			wks.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C)以上皆非'),message3])
	elif event.message.text == "1-1:(C)":
		cell_list = wks.find(profile.display_name)
		if not cell_list:
			wks.append_table(values=[profile.display_name,'','','O ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks.cell('D'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "1-2:(A)":
		cell_list = wks2.find(profile.display_name)
		if not cell_list:
			wks2.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks2.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks2.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C)以上皆是'),message3])
	elif event.message.text == "1-2:(B)":
		cell_list = wks2.find(profile.display_name)
		if not cell_list:
			wks2.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks2.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks2.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C)以上皆是'),message3])
	elif event.message.text == "1-2:(C)":
		cell_list = wks2.find(profile.display_name)
		if not cell_list:
			wks2.append_table(values=[profile.display_name,'','','O ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks2.cell('D'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks2.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "1-3:(A)":
		cell_list = wks3.find(profile.display_name)
		if not cell_list:
			wks3.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks3.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks3.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)伺服器'),message3])
	elif event.message.text == "1-3:(B)":
		cell_list = wks3.find(profile.display_name)
		if not cell_list:
			wks3.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks3.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks3.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "1-3:(C)":
		cell_list = wks3.find(profile.display_name)
		if not cell_list:
			wks3.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks3.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks3.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)伺服器'),message3])
	elif event.message.text == "1-4:(A)":
		cell_list = wks4.find(profile.display_name)
		if not cell_list:
			wks4.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks4.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks4.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)工作管理員'),message3])
	elif event.message.text == "1-4:(B)":
		cell_list = wks4.find(profile.display_name)
		if not cell_list:
			wks4.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks4.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks4.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "1-4:(C)":
		cell_list = wks4.find(profile.display_name)
		if not cell_list:
			wks4.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks4.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks4.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)工作管理員'),message3])
	elif event.message.text == "課程一測驗":
		cell_list = wks.find(profile.display_name)
		cell_list2 = wks2.find(profile.display_name)
		cell_list3 = wks3.find(profile.display_name)
		cell_list4 = wks4.find(profile.display_name)
		tmp=['','','','','','','','','','','','']
		if cell_list:
			c1 = wks.cell('B'+str(cell_list[0].row))
			tmp[0]=c1.value
			c2 = wks.cell('C'+str(cell_list[0].row))
			tmp[1]=c2.value
			c3 = wks.cell('D'+str(cell_list[0].row))
			tmp[2]=c3.value
		if cell_list2:
			c1 = wks2.cell('B'+str(cell_list2[0].row))
			tmp[3]=c1.value
			c2 = wks2.cell('C'+str(cell_list2[0].row))
			tmp[4]=c2.value
			c3 = wks2.cell('D'+str(cell_list2[0].row))
			tmp[5]=c3.value
		if cell_list3:
			c1 = wks3.cell('B'+str(cell_list3[0].row))
			tmp[6]=c1.value
			c2 = wks3.cell('C'+str(cell_list3[0].row))
			tmp[7]=c2.value
			c3 = wks3.cell('D'+str(cell_list3[0].row))
			tmp[8]=c3.value
		if cell_list4:
			c1 = wks4.cell('B'+str(cell_list4[0].row))
			tmp[9]=c1.value
			c2 = wks4.cell('C'+str(cell_list4[0].row))
			tmp[10]=c2.value
			c3 = wks4.cell('D'+str(cell_list4[0].row))
			tmp[11]=c3.value
		message4 = TemplateSendMessage(
			alt_text='課程一測驗',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程一測驗-1',
						text='資料分析的來源不包含什麼?',
						actions=[
							MessageTemplateAction(
								label=tmp[0]+'(A)資料庫',
								text='1-1:(A)'
							),
							MessageTemplateAction(
								label=tmp[1]+'(B)網頁',
								text='1-1:(B)'
							),
							MessageTemplateAction(
								label=tmp[2]+'(C)以上皆非',
								text='1-1:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程一測驗-2',
						text='資料分析可以做什麼應用?',
						actions=[
							MessageTemplateAction(
								label=tmp[3]+'(A)比價網站',
								text='1-2:(A)'
							),
							MessageTemplateAction(
								label=tmp[4]+'(B)文字探勘',
								text='1-2:(B)'
							),
							MessageTemplateAction(
								label=tmp[5]+'(C)以上皆是',
								text='1-2:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程一測驗-3',
						text='做網路爬蟲時不需要具備什麼?',
						actions=[
							MessageTemplateAction(
								label=tmp[6]+'(A)網路',
								text='1-3:(A)'
							),
							MessageTemplateAction(
								label=tmp[7]+'(B)伺服器',
								text='1-3:(B)'
							),
							MessageTemplateAction(
								label=tmp[8]+'(C)程式語言',
								text='1-3:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程一測驗-4',
						text='哪一個流程不是找出網頁Header(Get或post)的操作裡?',
						actions=[
							MessageTemplateAction(
								label=tmp[9]+'(A)重新載入此頁',
								text='1-4:(A)'
							),
							MessageTemplateAction(
								label=tmp[10]+'(B)工作管理員',
								text='1-4:(B)'
							),
							MessageTemplateAction(
								label=tmp[11]+'(C)開發人員工具',
								text='1-4:(C)'
							)
						]
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message4)
	elif event.message.text == "2-1:(A)":
		cell_list = wks5.find(profile.display_name)
		if not cell_list:
			wks5.append_table(values=[profile.display_name,'O ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks5.cell('B'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks5.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "2-1:(B)":
		cell_list = wks5.find(profile.display_name)
		if not cell_list:
			wks5.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks5.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks5.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(A)網路資源(URLs)擷取套件'),message3])
	elif event.message.text == "2-1:(C)":
		cell_list = wks5.find(profile.display_name)
		if not cell_list:
			wks5.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks5.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks5.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(A)網路資源(URLs)擷取套件'),message3])
	elif event.message.text == "2-2:(A)":
		cell_list = wks6.find(profile.display_name)
		if not cell_list:
			wks6.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks6.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks6.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)HTML剖析套件'),message3])
	elif event.message.text == "2-2:(B)":
		cell_list = wks6.find(profile.display_name)
		if not cell_list:
			wks6.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks6.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks6.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "2-2:(C)":
		cell_list = wks6.find(profile.display_name)
		if not cell_list:
			wks6.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks6.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks6.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)HTML剖析套件'),message3])
	elif event.message.text == "2-3:(A)":
		cell_list = wks7.find(profile.display_name)
		if not cell_list:
			wks7.append_table(values=[profile.display_name,'O ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks7.cell('B'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks7.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "2-3:(B)":
		cell_list = wks7.find(profile.display_name)
		if not cell_list:
			wks7.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks7.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks7.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(A)在命令提示字元安裝'),message3])
	elif event.message.text == "2-3:(C)":
		cell_list = wks7.find(profile.display_name)
		if not cell_list:
			wks7.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks7.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks7.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(A)在命令提示字元安裝'),message3])
	elif event.message.text == "課程二測驗":
		cell_list = wks5.find(profile.display_name)
		cell_list2 = wks6.find(profile.display_name)
		cell_list3 = wks7.find(profile.display_name)
		tmp=['','','','','','','','','']
		if cell_list:
			c1 = wks5.cell('B'+str(cell_list[0].row))
			tmp[0]=c1.value
			c2 = wks5.cell('C'+str(cell_list[0].row))
			tmp[1]=c2.value
			c3 = wks5.cell('D'+str(cell_list[0].row))
			tmp[2]=c3.value
		if cell_list2:
			c1 = wks6.cell('B'+str(cell_list2[0].row))
			tmp[3]=c1.value
			c2 = wks6.cell('C'+str(cell_list2[0].row))
			tmp[4]=c2.value
			c3 = wks6.cell('D'+str(cell_list2[0].row))
			tmp[5]=c3.value
		if cell_list3:
			c1 = wks7.cell('B'+str(cell_list3[0].row))
			tmp[6]=c1.value
			c2 = wks7.cell('C'+str(cell_list3[0].row))
			tmp[7]=c2.value
			c3 = wks7.cell('D'+str(cell_list3[0].row))
			tmp[8]=c3.value
		message4 = TemplateSendMessage(
			alt_text='課程二測驗',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程二測驗-1',
						text='Requests套件是做什麼的?',
						actions=[
							MessageTemplateAction(
								label=tmp[0]+'(A)網路資源(URLs)擷取套件',
								text='2-1:(A)'
							),
							MessageTemplateAction(
								label=tmp[1]+'(B)HTML剖析套件',
								text='2-1:(B)'
							),
							MessageTemplateAction(
								label=tmp[2]+'(C)網頁建置套件',
								text='2-1:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程二測驗-2',
						text='BeautifulSoup4套件是做什麼的?',
						actions=[
							MessageTemplateAction(
								label=tmp[3]+'(A)網路資源(URLs)擷取套件',
								text='2-2:(A)'
							),
							MessageTemplateAction(
								label=tmp[4]+'(B)HTML剖析套件',
								text='2-2:(B)'
							),
							MessageTemplateAction(
								label=tmp[5]+'(C)文字表格化套件',
								text='2-2:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程二測驗-3',
						text='安裝Requests套件哪個敘述是對的?',
						actions=[
							MessageTemplateAction(
								label=tmp[6]+'(A)在命令提示字元安裝',
								text='2-3:(A)'
							),
							MessageTemplateAction(
								label=tmp[7]+'(B)install'+sym.cell('C1').value+'requests',
								text='2-3:(B)'
							),
							MessageTemplateAction(
								label=tmp[8]+'(C)要進入Python環境',
								text='2-3:(C)'
							)
						]
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message4)
	elif event.message.text == "3-1:(A)":
		cell_list = wks8.find(profile.display_name)
		if not cell_list:
			wks8.append_table(values=[profile.display_name,'O ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks8.cell('B'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks8.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "3-1:(B)":
		cell_list = wks8.find(profile.display_name)
		if not cell_list:
			wks8.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks8.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks8.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(A)135'),message3])
	elif event.message.text == "3-1:(C)":
		cell_list = wks8.find(profile.display_name)
		if not cell_list:
			wks8.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks8.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks8.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(A)135'),message3])
	elif event.message.text == "課程三測驗":
		profile = line_bot_api.get_profile(event.source.user_id)
		cell_list = wks8.find(profile.display_name)
		tmp=['','','']
		if cell_list:
			c1 = wks8.cell('B'+str(cell_list[0].row))
			tmp[0]=c1.value
			c2 = wks8.cell('C'+str(cell_list[0].row))
			tmp[1]=c2.value
			c3 = wks8.cell('D'+str(cell_list[0].row))
			tmp[2]=c3.value
		message4 = TemplateSendMessage(
			alt_text='課程三測驗',
			template=ButtonsTemplate(
				thumbnail_image_url='https://i.imgur.com/7zjgsJ5.png',
				title='課程三測驗-1',
				text='如圖中程式碼，哪一個組合是對的?',
				actions=[
					MessageTemplateAction(
						label=tmp[0]+'(A)135',
						text='3-1:(A)'
					),
					MessageTemplateAction(
						label=tmp[1]+'(B)235',
						text='3-2:(B)'
					),
					MessageTemplateAction(
						label=tmp[2]+'(C)145',
						text='3-3:(C)'
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message4)
	elif event.message.text == "4-1:(A)":
		cell_list = wks9.find(profile.display_name)
		if not cell_list:
			wks9.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks9.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks9.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)print(soup.text)'),message3])
	elif event.message.text == "4-1:(B)":
		cell_list = wks9.find(profile.display_name)
		if not cell_list:
			wks9.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks9.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks9.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "4-1:(C)":
		cell_list = wks9.find(profile.display_name)
		if not cell_list:
			wks9.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks9.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)print(soup.text)'),message3])
	elif event.message.text == "4-2:(A)":
		cell_list = wks10.find(profile.display_name)
		if not cell_list:
			wks10.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks10.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks10.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)字串string'),message3])
	elif event.message.text == "4-2:(B)":
		cell_list = wks10.find(profile.display_name)
		if not cell_list:
			wks10.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks10.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks10.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "4-2:(C)":
		cell_list = wks10.find(profile.display_name)
		if not cell_list:
			wks10.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks10.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks10.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)字串string'),message3])
	elif event.message.text == "4-3:(A)":
		cell_list = wks11.find(profile.display_name)
		if not cell_list:
			wks11.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks11.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks11.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)#title'),message3])
	elif event.message.text == "4-3:(B)":
		cell_list = wks11.find(profile.display_name)
		if not cell_list:
			wks11.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks11.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks11.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "4-3:(C)":
		cell_list = wks11.find(profile.display_name)
		if not cell_list:
			wks11.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks11.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks11.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)#title'),message3])
	elif event.message.text == "4-4:(A)":
		cell_list = wks12.find(profile.display_name)
		if not cell_list:
			wks12.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks12.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks12.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C).link'),message3])
	elif event.message.text == "4-4:(B)":
		cell_list = wks12.find(profile.display_name)
		if not cell_list:
			wks12.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks12.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks12.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C).link'),message3])
	elif event.message.text == "4-4:(C)":
		cell_list = wks12.find(profile.display_name)
		if not cell_list:
			wks12.append_table(values=[profile.display_name,'','','O ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks12.cell('D'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks12.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "課程四測驗":
		cell_list = wks9.find(profile.display_name)
		cell_list2 = wks10.find(profile.display_name)
		cell_list3 = wks11.find(profile.display_name)
		cell_list4 = wks12.find(profile.display_name)
		tmp=['','','','','','','','','','','','']
		if cell_list:
			c1 = wks9.cell('B'+str(cell_list[0].row))
			tmp[0]=c1.value
			c2 = wks9.cell('C'+str(cell_list[0].row))
			tmp[1]=c2.value
			c3 = wks9.cell('D'+str(cell_list[0].row))
			tmp[2]=c3.value
		if cell_list2:
			c1 = wks10.cell('B'+str(cell_list2[0].row))
			tmp[3]=c1.value
			c2 = wks10.cell('C'+str(cell_list2[0].row))
			tmp[4]=c2.value
			c3 = wks10.cell('D'+str(cell_list2[0].row))
			tmp[5]=c3.value
		if cell_list3:
			c1 = wks11.cell('B'+str(cell_list3[0].row))
			tmp[6]=c1.value
			c2 = wks11.cell('C'+str(cell_list3[0].row))
			tmp[7]=c2.value
			c3 = wks11.cell('D'+str(cell_list3[0].row))
			tmp[8]=c3.value
		if cell_list4:
			c1 = wks12.cell('B'+str(cell_list4[0].row))
			tmp[9]=c1.value
			c2 = wks12.cell('C'+str(cell_list4[0].row))
			tmp[10]=c2.value
			c3 = wks12.cell('D'+str(cell_list4[0].row))
			tmp[11]=c3.value
		message4 = TemplateSendMessage(
			alt_text='課程四測驗',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://i.imgur.com/YzGrylJ.png',
						title='課程四測驗-1',
						text='上圖中程式碼，如何只印出文字的內容(沒有html格式)?代入print()',
						actions=[
							MessageTemplateAction(
								label=tmp[0]+'(A)soup',
								text='4-1:(A)'
							),
							MessageTemplateAction(
								label=tmp[1]+'(B)soup'+sym.cell('B1').value+'text',
								text='4-1:(B)'
							),
							MessageTemplateAction(
								label=tmp[2]+'(C)soup'+sym.cell('B1').value+'select()',
								text='4-1:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://i.imgur.com/YzGrylJ.png',
						title='課程四測驗-2',
						text='上圖中程式碼，html_sample是什麼資料類型?',
						actions=[
							MessageTemplateAction(
								label=tmp[3]+'(A)陣列array',
								text='4-2:(A)'
							),
							MessageTemplateAction(
								label=tmp[4]+'(B)字串string',
								text='4-2:(B)'
							),
							MessageTemplateAction(
								label=tmp[5]+'(C)字典dictionary',
								text='4-2:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://i.imgur.com/YzGrylJ.png',
						title='課程四測驗-3',
						text='上圖中程式碼，如何取得html的id內容?',
						actions=[
							MessageTemplateAction(
								label=tmp[6]+'(A)'+sym.cell('A1').value+'id',
								text='4-3:(A)'
							),
							MessageTemplateAction(
								label=tmp[7]+'(B)'+sym.cell('A1').value+'title',
								text='4-3:(B)'
							),
							MessageTemplateAction(
								label=tmp[8]+'(C)'+sym.cell('B1').value+'id',
								text='4-3:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://i.imgur.com/YzGrylJ.png',
						title='課程四測驗-4',
						text='上圖中程式碼，如何取得class的link內容?',
						actions=[
							MessageTemplateAction(
								label=tmp[9]+'(A)'+sym.cell('A1').value+'link',
								text='4-4:(A)'
							),
							MessageTemplateAction(
								label=tmp[10]+'(B)'+sym.cell('B1').value+'class',
								text='4-4:(B)'
							),
							MessageTemplateAction(
								label=tmp[11]+'(C)'+sym.cell('B1').value+'link',
								text='4-4:(C)'
							)
						]
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message4)
	elif event.message.text == "5-1:(A)":
		cell_list = wks13.find(profile.display_name)
		if not cell_list:
			wks13.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks13.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks13.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)InfoLite'),message3])
	elif event.message.text == "5-1:(B)":
		cell_list = wks13.find(profile.display_name)
		if not cell_list:
			wks13.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks13.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks13.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "5-1:(C)":
		cell_list = wks13.find(profile.display_name)
		if not cell_list:
			wks13.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks13.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks13.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)InfoLite'),message3])
	elif event.message.text == "課程五測驗":
		profile = line_bot_api.get_profile(event.source.user_id)
		cell_list = wks13.find(profile.display_name)
		tmp=['','','']
		if cell_list:
			c1 = wks13.cell('B'+str(cell_list[0].row))
			tmp[0]=c1.value
			c2 = wks13.cell('C'+str(cell_list[0].row))
			tmp[1]=c2.value
			c3 = wks13.cell('D'+str(cell_list[0].row))
			tmp[2]=c3.value
		message4 = TemplateSendMessage(
			alt_text='課程五測驗',
			template=ButtonsTemplate(
				thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
				title='課程五測驗-1',
				text='哪一個是爬蟲的輔助工具?',
				actions=[
					MessageTemplateAction(
						label=tmp[0]+'(A)InforLite',
						text='5-1:(A)'
					),
					MessageTemplateAction(
						label=tmp[1]+'(B)InfoLite',
						text='5-2:(B)'
					),
					MessageTemplateAction(
						label=tmp[2]+'(C)InfoWeb',
						text='5-3:(C)'
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message4)
	elif event.message.text == "6-1:(A)":
		cell_list = wks14.find(profile.display_name)
		if not cell_list:
			wks14.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks14.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks14.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)Post需要messagebody表單資料'),message3])
	elif event.message.text == "6-1:(B)":
		cell_list = wks14.find(profile.display_name)
		if not cell_list:
			wks14.append_table(values=[profile.display_name,'','O ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks14.cell('C'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks14.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "6-1:(C)":
		cell_list = wks14.find(profile.display_name)
		if not cell_list:
			wks14.append_table(values=[profile.display_name,'','','X ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks14.cell('D'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks14.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(B)Post需要messagebody表單資料'),message3])
	elif event.message.text == "6-2:(A)":
		cell_list = wks15.find(profile.display_name)
		if not cell_list:
			wks15.append_table(values=[profile.display_name,'X ','','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'1','0','0'])
		else :
			c1 = wks15.cell('B'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks15.cell('F'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C)字典dictionary'),message3])
	elif event.message.text == "2-2:(B)":
		cell_list = wks15.find(profile.display_name)
		if not cell_list:
			wks15.append_table(values=[profile.display_name,'','X ','',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','1','0'])
		else :
			c1 = wks15.cell('C'+str(cell_list[0].row))
			c1.value='X '
			c2 = wks15.cell('G'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答錯囉~答案是(C)字典dictionary'),message3])
	elif event.message.text == "6-2:(C)":
		cell_list = wks15.find(profile.display_name)
		if not cell_list:
			wks15.append_table(values=[profile.display_name,'','','O ',datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"),'0','0','1'])
		else :
			c1 = wks15.cell('D'+str(cell_list[0].row))
			c1.value='O '
			c2 = wks15.cell('H'+str(cell_list[0].row))
			c2.value=str(int(c2.value)+1)
		line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='答對了!!恭喜~'),message3])
	elif event.message.text == "課程六測驗":
		cell_list = wks14.find(profile.display_name)
		cell_list2 = wks15.find(profile.display_name)
		tmp=['','','','','','']
		if cell_list:
			c1 = wks14.cell('B'+str(cell_list[0].row))
			tmp[0]=c1.value
			c2 = wks14.cell('C'+str(cell_list[0].row))
			tmp[1]=c2.value
			c3 = wks14.cell('D'+str(cell_list[0].row))
			tmp[2]=c3.value
		if cell_list2:
			c1 = wks15.cell('B'+str(cell_list2[0].row))
			tmp[3]=c1.value
			c2 = wks15.cell('C'+str(cell_list2[0].row))
			tmp[4]=c2.value
			c3 = wks15.cell('D'+str(cell_list2[0].row))
			tmp[5]=c3.value
		message4 = TemplateSendMessage(
			alt_text='課程六測驗',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程六測驗-1',
						text='Post哪一個描述是對的?',
						actions=[
							MessageTemplateAction(
								label=tmp[0]+'(A)Post只需要傳送URL網址',
								text='6-1:(A)'
							),
							MessageTemplateAction(
								label=tmp[1]+'(B)需要表單資料',
								text='6-1:(B)'
							),
							MessageTemplateAction(
								label=tmp[2]+'(C)Post不能用於網路爬蟲',
								text='6-1:(C)'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.python.org/static/opengraph-icon-200x200.png',
						title='課程六測驗-2',
						text='Post表單資訊在python中要包裝成什麼?',
						actions=[
							MessageTemplateAction(
								label=tmp[3]+'(A)陣列array',
								text='6-2:(A)'
							),
							MessageTemplateAction(
								label=tmp[4]+'(B)字串string',
								text='6-2:(B)'
							),
							MessageTemplateAction(
								label=tmp[5]+'(C)字典dictionary',
								text='6-2:(C)'
							)
						]
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message4)
	elif event.message.text == "linebot建置":
		profile = line_bot_api.get_profile(event.source.user_id)
		message2 = TemplateSendMessage(
			alt_text='linebot建置',
			template=ButtonsTemplate(
				thumbnail_image_url='https://is3-ssl.mzstatic.com/image/thumb/Purple128/v4/a6/5c/fe/a65cfefa-5ffd-76a2-5a4b-bc4c886b8fd2/AppIcon-1x_U007emarketing-85-220-0-4.png/1200x630bb.jpg',
				title='linebot建置',
				text='請選擇',
				actions=[
					URITemplateAction(
						label='linebot申請',
						uri='http://140.115.157.83/linebot申請?id='+profile.display_name+'&video=linebot申請'
					),
					URITemplateAction(
						label='heroku部署',
						uri='http://140.115.157.83/linebot部署?id='+profile.display_name+'&video=linebot部署'
					),
					URITemplateAction(
						label='linebot建置',
						uri='http://140.115.157.83/linebot建置?id='+profile.display_name+'&video=linebot建置'
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message2)
	elif event.message.text == "爬蟲教學":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message3)
	else:
		line_bot_api.reply_message(event.reply_token, [message,TextSendMessage(text='加好友:@iqc8044p'),TextSendMessage(text='Github：https://github.com/ericdai713/learning_linebot')])

if __name__ == "__main__":
	app.run()
