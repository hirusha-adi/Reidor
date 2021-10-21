import os
import time
import bot


def ENTIRE_PROGRAM():
    os.system("cls")
    print(""" 
    ██████████████████████████████████
    █▄─▄▄▀█▄─▄▄─█▄─▄█▄─▄▄▀█─▄▄─█▄─▄▄▀█
    ██─▄─▄██─▄█▀██─███─██─█─██─██─▄─▄█
    ▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀
            Discord Bot v1.0

            [1] Start Bot
            [99] Exit
    """)
    mainchoice = input("+ Please select an option: ")

    if mainchoice == "1":
        os.system("cls")
        bot.keep_alive()
        bot.client.run(bot.token)

    elif mainchoice == "2":
        os.system("cls")
        print("""

        █████████████████████████████████████████
        █─▄▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█▄─▄█─▄─▄─█─▄▄▄▄█
        █─███▀██─▄─▄██─▄█▀██─██─██─████─███▄▄▄▄─█
        ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀

                    Requested by Key
             Made by @hirusha-adi (github)
       link: https://github.com/hirusha-adi/Reidor
                
                    [1] Main Menu
                    [99] Exit

        """)
        subinp = input("+ Please select an option: ")
        if subinp == "99":
            exit()
        else:
            ENTIRE_PROGRAM()

    else:
        os.system("cls")
        print("- COMMAND YOU ENTERED IS NOT RECOGNIZED")
        time.sleep(3.5)
        exit()


ENTIRE_PROGRAM()
