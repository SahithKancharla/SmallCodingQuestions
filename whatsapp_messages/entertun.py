import  pyautogui
import  time
import keyboard as k




message = """
111111111111111111111111111
1                                                  1
1                                                  1
1                 0000000000                1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                     000000                   1
1                 0000000000                1
1                                                  1
1                                                  1
1           00000              00000        1
1       000000000         000000000    1
1      00000000000     00000000000  1
1      0000000000000000000000000  1
1        000000000000000000000      1
1           00000000000000000         1
1              0000000000000             1
1                 000000000                1
1                  0000000                 1
1                   00000                   1
1                    000                    1
1                     0                     1
1                                                  1
1                                                  1
1     000000000          000000000     1
1         00000                  00000      1
1         00000                  00000      1
1         00000                  00000      1
1         00000                  00000      1
1         00000                  00000      1
1         00000                  00000      1
1         00000                  00000      1
1         000000              000000      1
1           000000          000000        1
1                0000000000000            1
1                   000000000                1
1                                                  1
111111111111111111111111111
"""
pyautogui.press("enter")
for i in message.split("\n"):

    pyautogui.typewrite(i)
    k.press_and_release("enter") 
    time.sleep(0.4)
