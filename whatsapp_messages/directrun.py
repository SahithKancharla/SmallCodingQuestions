# pip install pywhatkit
import pywhatkit as kit
import keyboard as k

import pyautogui
import time

# Specify the phone number (with country code) and the message
phone_number = "+918247253455"
message = [
    "111111111111111111111111111",
    "1_________________________1",
    "1_________________________1",
    "1_______¶¶¶¶¶¶¶¶¶¶________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_________¶¶¶¶¶¶__________1",
    "1_______¶¶¶¶¶¶¶¶¶¶________1",
    "1_________________________1",
    "1_________________________1",
    "1____¶¶¶¶¶_______¶¶¶¶¶____1",
    "1__¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶___1",
    "1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶__1",
    "1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶__1",
    "1__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___1",
    "1___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____1",
    "1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____1",
    "1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1",
    "1_______¶¶¶¶¶¶¶¶¶¶¶_______1",
    "1________¶¶¶¶¶¶¶¶¶________1",
    "1_________¶¶¶¶¶¶¶_________1",
    "1__________¶¶¶¶¶__________1",
    "1___________¶¶¶___________1",
    "1____________¶____________1",
    "1_________________________1",
    "1_________________________1",
    "1_¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶_1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶_________¶¶¶¶¶___1",
    "1___¶¶¶¶¶¶_______¶¶¶¶¶¶___1",
    "1____¶¶¶¶¶¶_____¶¶¶¶¶_____1",
    "1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1",
    "1________¶¶¶¶¶¶¶¶¶________1",
    "1_________________________1",
    "111111111111111111111111111",
    ]

# Send the message instantly
for i in message:
    # print(i)
    kit.sendwhatmsg_instantly(phone_number, i)
    time.sleep(2)
    k.press_and_release("enter")
