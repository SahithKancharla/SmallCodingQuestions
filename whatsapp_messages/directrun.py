# pip install pywhatkit
import pywhatkit as kit
import keyboard as k

import pyautogui
import time

# Specify the phone number (with country code) and the message
phone_number = "+919603115085"
message = "I love you bangaram"

# Send the message instantly
for i in range(1,10):
    kit.sendwhatmsg_instantly(phone_number, message)
    k.press_and_release("enter")
