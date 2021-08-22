import os, time

from discord import client
import bot
import selfbot
    
    
def ENTIRE_PROGRAM():
    print(""" 
    ██████████████████████████████████
    █▄─▄▄▀█▄─▄▄─█▄─▄█▄─▄▄▀█─▄▄─█▄─▄▄▀█
    ██─▄─▄██─▄█▀██─███─██─█─██─██─▄─▄█
    ▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀

            [1] Start Bot
            [2] Start Self Bot
            [99] Exit
    """)
    mainchoice = input("+ Please select an option: ")

    if mainchoice == "1":
        os.system("cls")
        bot.keep_alive()
        bot.client.run(bot.token)
    
    elif mainchoice == "2":
        os.system("cls")
        selfbot.keep_alive()
        selfbot.client.run(selfbot.token)

    
    else:
        os.system("cls")
        print("- COMMAND YOU ENTERED IS NOT RECOGNIZED")
        time.sleep(3.5)
        exit()


ENTIRE_PROGRAM()


