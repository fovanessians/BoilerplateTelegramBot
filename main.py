import os
import telebot
from telebot import types
import requests
import json
import logging
import random
from random_word import RandomWords
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from telegram.ext import filters
import sys
import time
import datetime
import re
import threading
#import asyncio
import requests
#import aiohttp
#import aiogram
#socket dependencies -------
import platform
import socket
#---------------------------

#_______________________________________________

my_secret = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(my_secret, parse_mode=None)

print('bot started....')
s = time.perf_counter()
elapsed = time.perf_counter() - s

def main():
  # Enable logging
  logging.basicConfig(
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      level=logging.INFO)
  
  logger = logging.getLogger(__name__)
  # logging

  print(logger)
  print(logger.warning)
  print(logger.critical)
  print(logger.exception)
  
  currentDateTime = datetime.datetime.now()
  print(currentDateTime)
  print(platform.node())
  print(socket.gethostname())
  print(socket.gethostbyname(socket.gethostname()))

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('0.0.0.0', 0))
  print('listening on port:', sock.getsockname()[1])

  print('----------------')
  print(socket.gethostbyname('www.replit.com'))
  print('listening on port:', sock.getsockname())
  print('----------------')

 

#___________________ ASYNC AWAIT____________________
  '''async def my_coroutine():
      await asyncio.sleep(15)
      result = datetime.datetime.now()
      print(datetime.datetime.now())
      return result 

  async def mainRoutine():
    
    await asyncio.gather( my_coroutine(),  my_coroutine(),  my_coroutine())

  # call my_async_function
  if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(mainRoutine())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
  
  for x in range(0, 1440):
      t = datetime.datetime.now()
      print(t)
      time.sleep(31)
      del t'''
#________________ASYNC AWAIT____________________
  
#_______________________________________________
  #Inline Keyboard
  @bot.message_handler(commands=['quiz'])
  def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    option1 = InlineKeyboardButton(text='option1', callback_data='option1')
    option2 = InlineKeyboardButton(text='option2', callback_data='option2')
    option3 = InlineKeyboardButton(text='option3', callback_data='option3')
    
    markup.add(option1, option2, option3)
    bot.send_message(message.chat.id, 'QUESTION', reply_markup=markup)
  
  @bot.callback_query_handler(func=InlineKeyboardButton)
  def answer(callback):
      if callback.message:
        if callback.data == 'option1':
          bot.send_message(callback.message.chat.id, 'https:// or text message')
        elif callback.data == 'option2':
          bot.send_message(callback.message.chat.id, "text based answer")
        else:
          bot.send_message(callback.message.chat.id, "text answer")
  
#____________________________________________________________

  @bot.message_handler(commands=['start', 'hello'])
  def send_welcome(message):
    bot.reply_to(message, "start & hello")



  
  '''@bot.message_handler(commands=['time'])
  def send_time(message):
    timeDateStr = 'Day: ' + str(timeDateDict['Day']) + " " + 'Time: ' + str(timeDateDict['Hour']) + ':' + str(timeDateDict['Minute']) + ' : ' + str(timeDateDict['Seconds']) 
    bot.reply_to(message, timeDateStr)'''
    
  
  
  @bot.message_handler(commands=['func1'])
  def func1(message):
    # waits for answer
    randomNum = 0
    randomNum = round(random.uniform(0, 3))
    time.sleep(32.2)
      
    if randomNum <= 1:
      newStr = "rand answer1"      
    elif randomNum == 2:
      newStr = "rand answer2"           
    else:
      newStr = "rand answer3"
  
    #print(randomInherit.run())
    bot.reply_to(message, newStr)
  
  
  @bot.message_handler(commands=["command"])
  def command(message):
    bot.reply_to(message, "text")
  
  
  @bot.message_handler(commands=["command2"])
  def command2(message):
    bot.reply_to(message, "answer")
  
  
  @bot.message_handler(commands=["command3"])
  def command3(message):
    bot.reply_to(message, "answer")
  
  
  @bot.message_handler(commands=["command4"])
  def command4(message):
    bot.reply_to(message,
                 "answer")
  
  
  @bot.message_handler(commands=["command5"])
  def command5(message):
    bot.send_message(
        message.chat.id,
        "{name} blah blah blah".format(name=message.from_user.first_name))
  
  
  @bot.message_handler(commands=["photo_command6"])
  def photo(message):
    bot.send_message(
        message.chat.id,
        "https://..... "
    )
  
  
  @bot.message_handler(commands=["photo_command7"])
  def photo2(message):
    bot.send_message(message.chat.id, "https://....."
    )

  @bot.message_handler(commands=["yourinfo"])
  def yourinfo(message):
    user_info = message.from_user
    print(user_info)
    print(type(user_info))
    print(message.from_user.id)
    print(message.from_user.username)
    #print(message.reply_to_message)
    print('____________')
    bot.get_chat_member(message.chat.id, message.from_user.id)
    infoFromCommand = bot.get_chat_member(message.chat.id, message.from_user.id)
    bot.send_message(message.chat.id, infoFromCommand)

  @bot.message_handler(commands=["callout"])
  def callout(message):
    user_info = message.from_user
    print(user_info)
    print(type(user_info))
    print(message.from_user.id)
    print(message.from_user.username)
    #print(message.reply_to_message)
    print('____________')
    print(message.reply_to_message.from_user.username)
    print(message.reply_to_message.from_user.id)
    print("___________________________")
    print(message.reply_to_message.from_user)
    name = message.reply_to_message.from_user.username
    #bot.get_chat_member(message.chat.id, message.from_user.id)
    bot.send_message(message.chat.id, "text " + name + " text")


  
  @bot.message_handler(commands=["judge"])
  def judge(message):
    response_API = requests.get('https://API rand quotes or chat initiation. FIND FREE APIS ON THE WEB')
    print(response_API.status_code)
    judgeVar = response_API.text
    user_id = message.reply_to_message.from_user.id
    try:
      user_name = message.reply_to_message.from_user.username
    except Exception as e:
      print('NoneType not allowed, must reply to a message', str(e))
      user_name = 'assign exception name'        
    print(user_name)
    if user_name == 'not allowed to judge this username':
      bot.send_message(message.chat.id, "You are not welcome to judge me")
    elif user_name != 'assign exception name':
      bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> {judgeVar}", "HTML")
    else:
      bot.send_message(message.chat.id, 'text')
  

  @bot.message_handler(commands=["chance"])
  def chance(message):
    percent = str(round(random.uniform(0, 1) * 100))
    bot.send_message(message.chat.id, "There is a " + percent + "%" + " " + message.text)

  @bot.message_handler(commands=["chat_member_count"])
  def chat_member_count(message):
    getComm = bot.get_chat_member_count(message.chat.id)
    bot.send_message(message.chat.id, 'member count is {a} text'.format(a=getComm))

  @bot.message_handler(commands=["eraser"])
  def unpin(message):
    bot.unpin_all_chat_messages(message.chat.id, "erased pins")

  
  @bot.message_handler(commands=["follower"])
  def follower(message):
    response_API = requests.get('https://FREE APIS FOR FOLLOWERS RESPOND TO POSTS')
    print(response_API.status_code)
    data = response_API.text
    #print(data)
    #parse_json = json.loads(data)
    bot.reply_to(message, data)
  
  
  @bot.message_handler(commands=["random2"])
  def random2(message):
    response_API = requests.get(
        'https://API')
    print(response_API.status_code)
    array = json.loads(response_API.text)
    #print(array)
    #print(array['object'])
    #data = response_API.text
    #print(data)
    #parse_json = json.loads(data)
    word = message.text
    scramble = list(word)
    #print(scramble)
    random.shuffle(scramble)
    newphrase = ''.join(scramble)
    #print(newphrase)
    r = RandomWords()
    word_rand = r.get_random_word()
    word_rand2 = r.get_random_word()
  
    bot.reply_to(
        message, newphrase[:5] + "  " + word_rand + "  " + newphrase[5:10] +
        "  " + array['object'] + " " + word_rand2 + " " + ": my friend ")

  
  
  @bot.message_handler(commands=["dart"])
  def dart(message):
    bot.send_dice(message.chat.id, "🎯")
  
  
  @bot.message_handler(commands=["dice"])
  def dice(message):
    bot.send_dice(message.chat.id)
  
  @bot.message_handler(commands=["ball"])
  def ball(message):
    bot.send_dice(message.chat.id, '⚽')

  @bot.message_handler(commands=["bowl"])
  def bowl(message):
    bot.send_dice(message.chat.id, '🎳')

  @bot.message_handler(commands=["slot"])
  def slot(message):
    bot.send_dice(message.chat.id, '🎰')

  @bot.message_handler(commands=["poll"])
  def poll(message):
    bot.send_poll(message.chat.id, "question?", ["answer1", "answer1", "answer1", "answer1"], 30)

  @bot.message_handler(commands=["poll2"])
  def poll2(message):
    bot.send_poll(message.chat.id, "questione?", ["answer1", "answer1", "answer1", "answer1", "answer1", "answer1"], 30)
  
  @bot.message_handler(commands=["reply_command1"])
  def reply_command1(message):
    bot.reply_to(message,
                 "response")
 

class Time:
  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute

def goodNight():
  for x in range(0, 1440):
    time.sleep(31)
    updateTimeObj = datetime.datetime.now()
    night = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (night.hour == 3 and night.minute == 3):
      bot.send_message(-1001369983015, "Good Night!")
    time.sleep(31)
    del night
    if x==1440:
      del x

def morning():
  for x in range(0, 1440):
    time.sleep(31)
    updateTimeObj = datetime.datetime.now()
    morning = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (morning.hour == 12 and morning.minute == 15):
      bot.send_message(-1001369983015, "Good Morning!")
    time.sleep(31)
    del morning
    if x==1440:
      del x

def test():
  for x in range(0, 1440):
    time.sleep(25)
    updateTimeObj = datetime.datetime.now()
    test = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (test.minute == 56):
      bot.send_message(-681387171, 'test')
    #print(test.minute)
    time.sleep(31)
    del test
    if x==1440:
      del x

def afternoon():
  for x in range(0, 1440):
    #time.sleep(29)
    updateTimeObj = datetime.datetime.now()
    afternoon = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (afternoon.hour == 19 and afternoon.minute == 25):
      bot.send_message(-1001369983015, "Good afternoon")
    time.sleep(29)
    del afternoon
    if x==1440:
      del x

#question language modeler
def question():
  @bot.message_handler(regexp = r"^(//)([a-z0-9]*\s*)*\?")
  def question_me(message):
    ranMsgNumQ = random.randint(0, 9)
    #print(ranMsgNum)
    if ranMsgNumQ == 1:
      #bot.reply_to(message, message.text) echo function
      bot.reply_to(message, "msg1'")
    elif ranMsgNumQ == 2:
      bot.reply_to(message, "msg2")
    elif ranMsgNumQ == 3:
      bot.reply_to(message, "msg3")
    elif ranMsgNumQ == 4:
      bot.reply_to(message, "msg4")
    elif ranMsgNumQ == 5:
      bot.reply_to(message, "msg5")
    elif ranMsgNumQ == 6:
      bot.reply_to(message, "msg6")
    elif ranMsgNumQ == 7:
      bot.reply_to(message, "msg7")
    elif ranMsgNumQ == 8:
      bot.reply_to(message, "msg8")
    elif ranMsgNumQ == 9:
      bot.reply_to(message, "msg9")
    
#emphatic language modeler
def screaming():
  @bot.message_handler(regexp = r"^(//)([A-Z0-9]*\s*)*(!$)")
  def all_caps(message):
    ranMsgNumCaps = random.randint(0, 10)
    #print(ranMsgNum)
    if ranMsgNumCaps == 1:
      #bot.reply_to(message, message.text) echo function
      bot.reply_to(message, "caps1")
    elif ranMsgNumCaps == 2:
      bot.reply_to(message, "caps2")
    elif ranMsgNumCaps == 3:
      bot.reply_to(message, "caps3")
    elif ranMsgNumCaps == 4:
      bot.reply_to(message, "caps4")
    elif ranMsgNumCaps == 5:
      bot.reply_to(message, "caps5")
    elif ranMsgNumCaps == 6:
      bot.reply_to(message, "caps6")
    elif ranMsgNumCaps == 7:
      bot.reply_to(message, "caps7")
    elif ranMsgNumCaps == 8:
      bot.reply_to(message, "caps8")
    elif ranMsgNumCaps == 9:
      bot.reply_to(message, "caps9")
    elif ranMsgNumCaps == 10:
      bot.reply_to(message, "caps10")

#standard response modeler
def bresponse():
  @bot.message_handler(regexp=r'^(//)([a-z0-9]*\s*)*(\.$)')
  def respond_statement(message):
    ranMsgNum = random.randint(0, 24)
    #print(ranMsgNum)
    if ranMsgNum == 1:
      #bot.reply_to(message, message.text) echo function
      bot.reply_to(message, "a1")
    elif ranMsgNum == 2:
      bot.reply_to(message, "a2")
    elif ranMsgNum == 3:
      bot.reply_to(message, "a3")
    elif ranMsgNum == 4:
      bot.reply_to(message, "a4")
    elif ranMsgNum == 5:
      bot.reply_to(message, "a5")
    elif ranMsgNum == 6:
      bot.reply_to(message, "a6")
    elif ranMsgNum == 7:
      bot.reply_to(message, "a7")
    elif ranMsgNum == 8:
      bot.reply_to(message, "a8")
    elif ranMsgNum == 9:
      bot.reply_to(message, "a9")
    elif ranMsgNum == 10:
      bot.reply_to(message, "a10")
    elif ranMsgNum == 11:
      bot.reply_to(message, "a11")
    elif ranMsgNum == 12:
      bot.reply_to(message, "a12")
    elif ranMsgNum == 13:
      bot.reply_to(message, "a13")
    elif ranMsgNum == 14:
      bot.reply_to(message, "a14")
    elif ranMsgNum == 15:
      bot.reply_to(message, "a15")
    elif ranMsgNum == 16:
      bot.reply_to(message, "a16")
    elif ranMsgNum == 17:
      bot.reply_to(message, "a17")
    elif ranMsgNum == 18:
      bot.reply_to(message, "a18")
    elif ranMsgNum == 19:
      bot.reply_to(message, "a19")
    elif ranMsgNum == 20:
      bot.reply_to(message, "a20")
    elif ranMsgNum == 21:
      bot.reply_to(message, "a21")
    elif ranMsgNum == 22:
      bot.reply_to(message, "a22")
    elif ranMsgNum == 23:
      bot.reply_to(message, "a23")
    elif ranMsgNum == 24:
      bot.reply_to(message, "a23")
   

# creating thread
t1 = threading.Thread(target=main)
t2 = threading.Thread(target=goodNight)
t3 = threading.Thread(target=morning)
t4 = threading.Thread(target=test)
t5 = threading.Thread(target=afternoon)
t6 = threading.Thread(target=question)
t7 = threading.Thread(target=screaming)
t8 = threading.Thread(target=bresponse)  

  
# starting thread 1
t1.start()
# starting thread 2
t2.start()
# starting thread 3
t3.start()
# starting thread 4
t4.start()
# starting thread 5
t5.start()
# starting thread 6
t6.start()
# starting thread 7
t7.start()
# starting thread 8  
t8.start()

#sychronous switch (not needed unless sequential operations required)
# wait until thread 1 is completely executed
#t1.join()
# wait until thread 2 is completely executed
#t2.join()
# wait until thread 3 is completely executed
#t3.join()


#asyncio.run(bot.polling()) - not implementing async funcitonality
bot.infinity_polling()
