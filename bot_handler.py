from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio
import htmlParser



#Данные для аккаунта +7 9273091197
#Получать данные для аккаунтов через БД/скрипт (?)
api_id = 24931692 # api_id
api_hash = '7acc18430237abb56186b10546ee2cd3' # api_hash
client = TelegramClient('anon', api_id, api_hash, system_version='4.16.30-vxCUSTOM')
target_chat = '@EYE9_OF6_GOD7_BOT'

#Страны, доступные для выбора в боте
countries = ['Россия', 'Украина', 'Беларусь', 'Казахстан', 'Турция', 'Мексика', 'Германия', 'Аргентина', 'Грузия'
             'Армения', 'Африка', 'Франция', 'Мальта', 'Норвегия', 'Малайзия', 'Узбекистан', 'Таджикистан',
             'Нидерланды', 'ОАЭ', 'Румыния', 'Польша', 'Испания']

socnetworks = ['Вконтакте', 'Instagram', 'Telegram', 'Пароли']

key_words = ['ФИО', 'Город', 'Имя', 'Адрес', 'ИНН', 'Адрес', 'Номер', 'VIN', 'База данных', 'СНИЛС', 'Совпадения', 'Номер', 'ОГРН', 'Арендованный хостинг', 'Кадастровый номер']

decline_words = ['ограничил', 'не удалось', 'не найдено', 'не найдены']


global API_ID
global API_HASH
global CONFIRM_CODE
global SEARCH_INFO
global SEARCH_CHOICE
global BOT_RESPONCE
global type_for_responce
global responce_full 
responce_full = False
BOT_RESPONCE = []


#Начинаем общение с ботом
async def starter(type_of_request, input_info, input_choice = 'Россия'):
    global SEARCH_INFO
    global SEARCH_CHOICE
    global type_for_responce
    SEARCH_INFO = input_info
    SEARCH_CHOICE = input_choice
    type_for_responce = type_of_request
    regular_requests = ['by_name', 'by_num', 'by_sm', 'by_car', 'by_email', 'by_cad']
    await client.send_message(target_chat, '/start')
    if any([substr in type_of_request for substr in regular_requests]):
        await client.send_message(target_chat, SEARCH_INFO)
    elif type_of_request == 'by_INN':
        await client.send_message(target_chat, '\'inn\' ' + SEARCH_INFO)
    elif type_of_request == 'by_SNILS':
        await client.send_message(target_chat, '\'snils\' ' + SEARCH_INFO)
    elif type_of_request == 'by_cpny':
        await client.send_message(target_chat, '\'company\' ' + SEARCH_INFO)
    elif type_of_request == 'by_adr':
        await client.send_message(target_chat, '\'adr\' ' + SEARCH_INFO)


#Получаем данные html ответа бота
@client.on(events.NewMessage(chats=target_chat))
async def doc_handler(event):
    from_txt = []
    if event.media:
        await event.download_media()#Можно задать конкретный путь при запуске на VM
    if any([substr in event.text for substr in key_words]):
        BOT_RESPONCE.append(event.text)
        with open ('{si}.txt'.format(si=SEARCH_INFO), 'a', encoding='utf-8') as file:
            file.write(event.text)
        try:
            htmlParser.parse_html('{si}.html'.format(si=SEARCH_INFO), '{si}.txt'.format(si=SEARCH_INFO))
            htmlParser.read_txt('{si}.txt'.format(si=SEARCH_INFO), from_txt)
            BOT_RESPONCE.extend(from_txt)
            print(BOT_RESPONCE)
            htmlParser.silentremove('{si}.html'.format(si=SEARCH_INFO))
            global responce_full
            responce_full = True
        except:
            pass
        

#Работаем с query-ответами бота, выбираем страну для поиска, проверяем, удачный ли ответ и продолжаем опрашивать бота
@client.on(events.NewMessage(chats=target_chat, pattern=r'Выберите доступные действия:'))
async def query_handler(event):
    if SEARCH_CHOICE:
        await event.message.click(countries.index(SEARCH_CHOICE)+1)


#Обработка сообщений о невозможности поиска, достижении предела запросов на день
@client.on(events.NewMessage(chats=target_chat))
async def decline_handler(event):
    async for message in client.iter_messages(entity=target_chat, limit=1):
        try:
            if any([substr in message.text for substr in decline_words]):
                BOT_RESPONCE.append(SEARCH_INFO + ' - найти информации не удалось')
            elif 'Вы слишком часто выполняете это действие' in message.text:
                await asyncio.sleep(1)
                await client.send_message(target_chat, SEARCH_INFO)
        except IndexError:
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
        await event.reply(SEARCH_INFO)


#Выбираем все соцсети при поиске по имени пользователя
@client.on(events.NewMessage(chats=target_chat))
async def socnet_handler(event):
    if 'Выберите направление поиска' in event.text:
        await event.message.click(socnetworks.index('Вконтакте'))
        await asyncio.sleep(0.1)
        await event.message.click(socnetworks.index('Instagram'))
        await asyncio.sleep(0.1)
        await event.message.click(socnetworks.index('Telegram'))    


#Выбираем дополнительную информацию в меню бота, в которых есть подобная возможность
@client.on(events.NewMessage(chats=target_chat))
async def group_handler(event):
    if 'VIN' in event.text:
        try:
            await event.click(4)
        except:
            pass
    elif 'Транзакций' in event.text or 'Арендованный хостинг' in event.text:
        try:
            await event.click(0)
        except:
            pass


async def get_responce():
    await asyncio.sleep(3)
    if type_for_responce != 'by_name':
        while not BOT_RESPONCE:
            pass
        if BOT_RESPONCE:
            return BOT_RESPONCE
    else:
        while responce_full == False:
            pass
        if responce_full == True:
            return BOT_RESPONCE


#Запускаем в работу
def start(type_of_request, input_info, input_choice = 'Россия'):
    client.loop.run_until_complete(starter(type_of_request, input_info, input_choice))

def run():
    client.loop.run_forever()

def stop():
    client.loop.stop()


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(starter('by_name', 'Антонов Вячеслав Игоревич', 'Россия'))
        client.loop.run_forever()