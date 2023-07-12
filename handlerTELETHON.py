from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio
from numba import njit
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#Данные для аккаунта +7 9273091197
#Получать данные для аккаунтов через БД/скрипт (?)
api_id = 24931692 
api_hash = '7acc18430237abb56186b10546ee2cd3'
client = TelegramClient('anon', api_id, api_hash, system_version='4.16.30-vxCUSTOM')
target_chat = '@eyeofgodrbot'

#Страны, доступные для выбора в боте
countries = ['Россия', 'Украина', 'Беларусь', 'Казахстан', 'Турция', 'Мексика', 'Германия', 'Аргентина', 'Грузия'
             'Армения', 'Африка', 'Франция', 'Мальта', 'Норвегия', 'Малайзия', 'Узбекистан', 'Таджикистан',
             'Нидерланды', 'ОАЭ', 'Румыния', 'Польша', 'Испания']


#Пример данных для поиска, потом подгружать с БД/запроса (?)
keys_search = ['Антонов Вячеслав Олегович', 'Антонов Георгий Олегович'] # 'Сидоров Вячеслав Олегович', 
               #'Куприн Вячеслав Александрович']
#['Антонов Вячеслав Олегович'] 

#Ведем подсчет запросов к боту
action_count = 0


#Начинаем общение с ботом
async def starter():
    await client.send_message(target_chat, '/start')


#Получаем ответ на /start
@client.on(events.NewMessage(chats=target_chat, pattern=r'Добро пожаловать!'))
async def greet_handler(event):
    await event.reply(keys_search[action_count])


#Получаем данные html ответа бота
@client.on(events.NewMessage(chats=target_chat, pattern=keys_search[action_count]))
async def doc_handler(event):
    global action_count
    if event.message.document:
        await event.message.download_media()#Можно задать конкретный путь при запуске на VM
    

#Работаем с query-ответами бота, выбираем страну для посика, проверяем, удачный ли ответ и продолжаем опрашивать бота
@njit
@client.on(events.NewMessage(chats=target_chat, pattern=r'Выберите доступные действия:'))
async def query_handler(event):
    global action_count
    await event.message.click(countries.index('Россия')+1)
    await asyncio.sleep(1e-3) #Информацию от бота при неудаче не выходит поймать в event, 
#потому приходится немного ждать и просматривать историю сообщений (бот правит/удаляет сообщения при неудаче)
    async for message in client.iter_messages(entity=target_chat, limit=2):
        try:
            if 'ограничил' in message.text or 'не удалось' in message.text:
                #Позже отправлять в БД (?) соответствующее неудачному запросу сообщение
                action_count += 1
                await client.send_message(target_chat, keys_search[action_count])
            elif keys_search[action_count] in message.text:
                action_count += 1
                await client.send_message(target_chat, keys_search[action_count])
        except IndexError:
            #Это означает, кончились ФИО для опроса бота
            pass
        if 'заблокирована' in message.text:
            #Это означает, что исчерпаны запросы для конкретного аккаунта telegram на сегодня
            return


#Вступаем в чат при соответствующем требовании
@client.on(events.NewMessage(chats=target_chat))
async def group_handler(event):
    if 'Обязательным условием' in event.text:
        link = event.buttons[0][0].url
        await client(JoinChannelRequest(link))
        await asyncio.sleep(0.001)
        await event.click(1)


#Получаем ответ на подпику на группу
@client.on(events.NewMessage(chats=target_chat))
async def greet_handler(event):
    if 'Вы можете прислать боту запросы в следующем формате:' in event.text:
        await event.reply(keys_search[action_count])




#Запускаем в работу
with client:
    client.loop.run_until_complete(starter())
    client.loop.run_forever()