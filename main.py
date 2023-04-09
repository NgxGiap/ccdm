import discum_berus
import time #import lib time
import multiprocessing
import json #extr json lib
import random
import re
import os
import sys
try:
  from tkinter import messagebox
  use_terminal=False
except:
  use_terminal=True
once=False
wbm=[12,16] #random wait time range between 2 message
update = 0
class bot:
  owoid=408785106942164992 #user id of the owo bot

  with open('settings.json') as file:
    data = json.load(file)
    token = data["token"]
    channel = data["channel"]
  if token == "def":
    token = input("please enter your dc token for once: ")
    data["token"] = token
    update = 1
  if channel == "def":
    channel = input("please enter the id of the channel: ")
    data["channel"] = channel
    update = 1

  if update:
    with open("settings.json", "w") as file:
      json.dump(data, file)
  commands=[
    "Owo h",
    "Owo h",
  "Owo",
    "Owo b",
    ]
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    if os.name == "nt":
      purple = ''
      okblue = ''
      okcyan = ''
      okgreen = ''
      warning = ''
      fail = ''
      reset = ''
      bold = ''
      underline = ''
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
def report_error(content):
  if use_terminal:
    print(at(), content)
  else:
    messagebox.showerror("Warning BOT", content)
client=discum_berus.Client(token=bot.token, log=False)
def issuechecker():
  msgs=client.getMessages(str(bot.channel), num=10)
  msgs=json.loads(msgs.text)
  owodes=0
  for msgone in msgs:
    if msgone['author']['id']==str(bot.owoid):
      owodes=owodes+1
      msgonec=msgone['content']
      if ":warning: | Berus Please complete your captcha to verify that you are human! (1/5)" in str(msgonec):
          return "exit"
      if ":warning: | Berus Please complete your captcha to verify that you are human! (2/5)" in str(msgonec):
          return "exit"
      if ":warning: | Berus Please complete your captcha to verify that you are human! (3/5)" in str(msgonec):
          return "exit"
      if ":warning: | Berus Please complete your captcha to verify that you are human! (4/5)" in str(msgonec):
          return "exit"
      if ":warning: | Berus Please complete your captcha to verify that you are human! (5/5)" in str(msgonec):
          return "exit"
      if ":warning:" in str(msgonec):
          return "exit"
      if "Please DM me" in str(msgonec):
          return "exit"
      if "http://verify.owobot.com" in str(msgonec):
          return "exit"
      if "(1/5)" in str(msgonec):
          return "exit"
      if "(2/5)" in str(msgonec):
          return "exit"
      if "(3/5)" in str(msgonec):
          return "exit"
      if "(4/5)" in str(msgonec):
          return "exit"
      if "(5/5)" in str(msgonec):
          return "exit"
      if 'banned' in msgonec:
          print(f'{at()}{bot.color.fail} !!! [BANNED] !!! {bot.color.reset} your account have been banned from owo bot ')
          return "exit"
      if ' Please complete your captcha to verify that you are human!' in msgonec:
          print(f'{at()}{bot.color.warning} !! [CAPTCHA] !! {bot.color.reset} CAPTCHA   ACTION REQUİRED {msgonec[-6:]}')
          return "exit"
  if not owodes:
    return "exit"
def security():
        if issuechecker() == "exit":
          report_error("Ban-security triggered, answer the captcha or DM Berus#1878")
          sys.exit()
def runner():
  if issuechecker() == "exit":
          return security()
  else:
        global wbm
        command=random.choice(bot.commands)
        command2=random.choice(bot.commands)
        client.typingAction(str(bot.channel))
        client.sendMessage(str(bot.channel), command)
        print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} {command}")
        if not command2==command:
          client.typingAction(str(bot.channel))
          time.sleep(1)
          client.sendMessage(str(bot.channel), command2)
          print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} {command2}")
        time.sleep(random.randint(wbm[0],wbm[1]))
def owopray():
  client.sendMessage(str(bot.channel), "owo pray")
  print(f"{at()}{bot.color.okgreen} [SENT] {bot.color.reset} owo pray")
def loopie():
  if issuechecker() == "exit":
    return security()
  else:
    x=True
    pray = 0
    main=time.time()
    while x:
        runner()
        if time.time() - pray > random.randint(300, 500):
          security()
          owopray()
          pray=time.time()
      
        if time.time() - main > random.randint(1000, 1800):
          time.sleep(random.randint(150, 300))
          security ()
          main=time.time()
@client.gateway.command
def userinfo(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = client.gateway.session.user
        print("Logged in as {}#{} - Code & Develop By Berus".format(user['username'], user['discriminator']))
@client.gateway.command
def defination1(resp):
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol=multiprocessing.Process(target=loopie)
      lol.run()
#print(bot.token)
client.gateway.run()
