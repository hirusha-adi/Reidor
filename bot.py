# ALL IMPORTS
# --------------------------
import discord, json, asyncio, string
import time, os, platform, datetime, random
from discord.ext import commands

from keep_alive import keep_alive
from intstallerm import INSTALL_ALL
# try:
#     INSTALL_ALL()
# except:
#     pass


# MAIN VERIABLES
# --------------------------
# token = os.environ['TOKEN']
token = "YOUR TOKEN HERE"
botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["bot-prefix"]
bot_creator_name = botconfigdata["bot-creator-name"]
bot_name = botconfigdata["bot-name"]
bot_author_icon = botconfigdata["author-icon"]


# CREATING THE BOT
# --------------------------
client = commands.Bot(command_prefix = bot_prefix)
client.remove_command('help')


# ONLY THESE USERS ARE ABLE TO USE THE BOT COMMANDS
# --------------------------
able_users = (
    837958948995989514, # Key
    584662127470575616, # Me
    384159667275825152, # Shado
    650641006248591401, # Lemons
    709299771415986227, # Mikey
    763756846074167326 # Busters
) 


# --------------------------


# NOW THE BOT IS READY
# --------------------------
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print(f"Discord.py API Version: {discord.__version__}")
    print(f"Python VersionW: {platform.python_version()}")
    print("The bot is ready to be used!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))


loading_msg = discord.Embed(title="Processing", color=0x5600f5)
loading_msg.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
loading_msg.set_thumbnail(url="https://cdn.discordapp.com/attachments/866002022464487444/866011073513652234/waiting-icon-gif-1_1.gif")
loading_msg.add_field(name="PLEASE WAIT", value="`PLEASE WAIT WHILE THE COMMAND IS BEEN COMPLETED`", inline=False)
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
    loading_sent = await ctx.send(embed=loading_msg)

    if int(numberofmsges) <= 650:
        yes_wl = ("yes", "y", "everyone", "true")
        if everyoneyn.lower() in yes_wl:
            for iteration, x in enumerate(range(int(numberofmsges))):
                await ctx.send(f"@everyone @here - {messagehere}")
                await asyncio.sleep(0.3)
        else:
            for iteration, x in enumerate(range(int(numberofmsges))):
                await ctx.send(f"{messagehere}")
                await asyncio.sleep(0.4)
        
        await loading_sent.delete()
    else:
        embed=discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/878570620999319562/pngaaa.com-3484527.png")
        embed.add_field(name="Error:", value="Please enter a value below 650", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await loading_sent.delete()
        await ctx.send(embed=embed)


# THE MASS SPAM COMMAND
# Spam to all the channels in one server
# --------------------------
@client.command(aliases=["ms", "masspam", "maspam", "mspam", "masss"])
async def massspam(ctx, numberofmsges="5", everyoneyn="yes", *, messagehere="I HAD A FUCKING BONER"):
    
    # The number of messages should be below or equal 650
    if int(numberofmsges) <= 350:

        # If it should @everyone or no
        yes_wl = ("yes", "y", "everyone", "true")
        if everyoneyn.lower() in yes_wl:

            # Every channel in the server ( this includes all Voice Channels, Text Channels and Categories )
            for channel in ctx.guild.channels:
                print(channel, "-" ,channel.id)

                # This is for the above given reason ( this includes all Voice Channels, Text Channels and Categories )
                try:
                    # This will get the discord channel for the channel.id
                    x = client.get_channel(channel.id)

                    # The normal spam command
                    for iteration, y in enumerate(range(int(numberofmsges))):
                        await x.send(f"@everyone @here - {messagehere}")
                        await asyncio.sleep(0.4)
                    
                except AttributeError:
                    print("Its a Category or a Voice Channel, not a text channel")
                    continue
                x = None

        else:
            # Every channel in the server ( this includes all Voice Channels, Text Channels and Categories )
            for channel in ctx.guild.channels:
                print(channel, "-" ,channel.id)

                # This is for the above given reason ( this includes all Voice Channels, Text Channels and Categories )
                try:
                    # This will get the discord channel for the channel.id
                    x = client.get_channel(channel.id)

                    # The normal spam command
                    for iteration, y in enumerate(range(int(numberofmsges))):
                        await x.send(f"{messagehere}")
                        time.sleep(0.2)
                    
                except AttributeError:
                    print("Its a Category or a Voice Channel, not a text channel")
                    continue
                x = None

    else:
        embed=discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/878570620999319562/pngaaa.com-3484527.png")
        embed.add_field(name="Error:", value="Please enter a value below 350", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)




# MASS CHANNEL
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# THE MASS CHANNEL COMMAND - UNSAFE
# --------------------------
@client.command(aliases=["mc", "masschanel", "masschanal", "masschanelunsafe"])
async def masschannel(ctx, numberofchannels="5", *, channelname="gg-niglet"):
    if int(numberofchannels) <= 100:
        
        newchannelname = str(channelname).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace("<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")
        
        for iteration, chnls in enumerate(range(int(numberofchannels))):
            print(chnls, iteration)
            await ctx.guild.create_text_channel(f'{iteration}{newchannelname}')

    else:
        embed=discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/878594081951981568/Channel_A_Logo_transparent.png")
        embed.add_field(name="Error:", value="Please enter a value below 45", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)


# THE MASS CHANNEL COMMAND - SAFE
# --------------------------
@client.command(aliases=["mcs", "mc-s", "mc_s", "safemasschannel"])
async def masschannelsafe(ctx, numberofchannels="5", *, channelname="gg-niglet"):
    if int(numberofchannels) <= 45:
        
        newchannelname = str(channelname).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace("<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")
        
        for iteration, chnls in enumerate(range(int(numberofchannels))):
            print(chnls, iteration)
            await asyncio.sleep(1)
            await ctx.guild.create_text_channel(f'{iteration}{newchannelname}')

    else:
        embed=discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/878594081951981568/Channel_A_Logo_transparent.png")
        embed.add_field(name="Error:", value="Please enter a value below 60", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)




# MASS ROLE
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# THE MASS ROLE COMMAND - UNSAFE
# --------------------------
@client.command(aliases=["mr", "mrunsfae", "massroleunsafe"])
async def massrole(ctx, numberofroles="5", *, rolenamelol="Moderator"):
    if int(numberofroles) <= 150:

        # The permissions of this role is of a Moderator 
        role_perms = discord.Permissions(add_reactions=True, administrator=False, attach_files=True, ban_members=False, change_nickname=True, connect=True, create_instant_invite=True, deafen_members=False, embed_links=True, external_emojis=True, kick_members=False, manage_channels=False, manage_emojis=False, manage_guild=False, manage_messages=False, manage_nicknames=False, manage_permissions=False, manage_roles=False, manage_webhooks=False, mention_everyone=False, move_members=False, mute_members=False, priority_speaker=True, view_guild_insights=True,  view_channel=True,  view_audit_log=False, use_voice_activation=True, use_slash_commands=True, use_external_emojis=True, stream=True, speak=True, send_tts_messages=False, send_messages=True, request_to_speak=True, read_messages=True, read_message_history=True)

        newrolenamelol = str(rolenamelol).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace("<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")
        
        # Creating the coles with a number infront of it, so there won't be the same name repeatedly
        for iteration, chnls in enumerate(range(int(numberofroles))):

            if rolenamelol == "random":
                # This will give it a random name
                newrolenamelol = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

            print(iteration, chnls)
            try:
                await ctx.guild.create_role(name=f"{iteration}{newrolenamelol}", permissions=role_perms)
            except:
                pass
    else:
        embed=discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/878594081951981568/Channel_A_Logo_transparent.png")
        embed.add_field(name="Error:", value="Please enter a value below 150", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)

# THE MASS ROLE COMMAND - SAFE
# --------------------------
@client.command(aliases=["mrs", "mrsafe", "safemassrole"])
async def massrolesafe(ctx, numberofroles="5", *, rolenamelol="Moderator"):
    if int(numberofroles) <= 45:

        # The permissions of this role is of a Moderator 
        role_perms = discord.Permissions(add_reactions=True, administrator=False, attach_files=True, ban_members=False, change_nickname=True, connect=True, create_instant_invite=True, deafen_members=False, embed_links=True, external_emojis=True, kick_members=False, manage_channels=False, manage_emojis=False, manage_guild=False, manage_messages=False, manage_nicknames=False, manage_permissions=False, manage_roles=False, manage_webhooks=False, mention_everyone=False, move_members=False, mute_members=False, priority_speaker=True, view_guild_insights=True,  view_channel=True,  view_audit_log=False, use_voice_activation=True, use_slash_commands=True, use_external_emojis=True, stream=True, speak=True, send_tts_messages=False, send_messages=True, request_to_speak=True, read_messages=True, read_message_history=True)

        newrolenamelol = str(rolenamelol).replace(" ", "-").replace("[", "x").replace("]", "x").replace(":", "x").replace("<", "x").replace(">", "x").replace("?", "x").replace("/", "x").replace("{", "x").replace("}", "x")

        # Creating the roles with a number infront of it, so there won't be the same name repeatedly
        for iteration, chnls in enumerate(range(int(numberofroles))):
            if rolenamelol == "random":
                # This will give it a random name
                newrolenamelol = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

            print(iteration, chnls)
            await asyncio.sleep(1)
            try:
                await ctx.guild.create_role(name=f"{iteration}{newrolenamelol}", permissions=role_perms)
            except:
                pass
    else:
        embed=discord.Embed(title="AN ERROR HAS OCCURED!!", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/878594081951981568/Channel_A_Logo_transparent.png")
        embed.add_field(name="Error:", value="Please enter a value below 40", inline=True)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)



# HELP
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

@client.command(aliases=["Help", "how", "howtouse", "h"])
async def help(ctx, *, subcmnd="all"):
    # ALL COMMAND NAME LIST WITH ALIASES
    # --------------------------
    spam_unsafe_wl = ("spam", "s", "spamunsafe", "spamnotsafe", "unsafespam", "notsafespam", "sunsafe")
    mass_spam_wl = ("massspam", "ms", "masspam", "maspam", "mspam", "masss")

    masschannel_unsafe_wl = ("masschannel", "mc", "masschanel", "masschanal", "masschanel", "masschanelunsafe")
    masschannel_safe_wl = ("masschannelsafe", "mcs", "mc-s", "mc_s", "safemasschannel")

    massrole_unsafe_wl = ("massrole", "mr", "mrunsfae", "massroleunsafe")
    massrole_safe_wl = ("massrolesafe", "mrs", "mrsafe", "safemassrole")

    if subcmnd in spam_unsafe_wl:
        embed=discord.Embed(title="Help for Spam", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:", value=f"{str(spam_unsafe_wl)}", inline=False)
        embed.add_field(name="Usage:", value=f"`{bot_prefix}s [number_of_messages] [everyone_mention_yes_or_no] [message_to_spam] `", inline=False)
        embed.add_field(name="Description", value="This will only spam messages in the given channel, maximum number_of_messages possible is 650, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)
            
    elif subcmnd in mass_spam_wl:
        embed=discord.Embed(title="Help for Mass Spam", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:", value=f"{str(mass_spam_wl)}", inline=False)
        embed.add_field(name="Usage:", value=f"`{bot_prefix}ms [number_of_messages] [everyone_mention_yes_or_no] [message_to_spam] `", inline=False)
        embed.add_field(name="Description", value="This will spam in every channel of every server the bot has been joined to, maximum number_of_messages possible is 350, default is 5, so its 5 messages for every channel one by one", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)
    
    elif subcmnd in masschannel_unsafe_wl:
        embed=discord.Embed(title="Help for Mass Channel Creating - Unsafe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(name="Usage:", value=f"`{bot_prefix}mc [number_of_channels_to_create] [channel_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates channels in the server upto the specified amount with the given name continuously, maximum number_of_channels_to_create is 100, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)
    
    elif subcmnd in masschannel_safe_wl:
        embed=discord.Embed(title="Help for Mass Channel Creating - Safe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(name="Usage:", value=f"`{bot_prefix}mcs [number_of_channels_to_create] [channel_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates channels in the server upto the specified amount with the given name with a time interval, maximum number_of_channels_to_create is 45, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)
    
    elif subcmnd in massrole_unsafe_wl:
        embed=discord.Embed(title="Help for Mass Role Creating - Unsafe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(name="Usage:", value=f"`{bot_prefix}mr [number_of_roles_to_create] [role_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates roles in the server upto the specified amount with the given name continuously, maximum number_of_roles_to_create is 150, default is 5", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)
    
    elif subcmnd in massrole_safe_wl:
        embed=discord.Embed(title="Help for Mass Role Creating - Safe", color=0x00d9ff)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        embed.add_field(name="Usage:", value=f"`{bot_prefix}mr [number_of_roles_to_create] [role_name] `", inline=False)
        embed.add_field(name="Description", value="This command creates roles in the server upto the specified amount with the given name with a time interval, maximum number_of_roles_to_create is 45, default is 5. Mentioning the [role_name] as 'random' will create roles with random names", inline=False)
        embed.set_footer(text=f"Bot created by {bot_creator_name}")
        await ctx.send(embed=embed)




# THE BOT WILL ONLY ACCEPT COMMANDS FROM able_users
# --------------------------
@client.event
async def on_message(message):
    if client.user == message.author:
        return
    
    if message.author.id in able_users:

        if message.content.lower().startswith(f"{bot_prefix}help"):
            try:
                subcmnd = str(message.content).split(" ")[1]
            except:
                subcmnd = "spam"

        #     if subcmnd in spam_unsafe_wl:
        #         embed=discord.Embed(title="Help for Spam", color=0x00d9ff)
        #         embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        #         embed.add_field(name="Other names:", value=f"{str(spam_unsafe_wl)}", inline=False)
        #         embed.add_field(name="Usage:", value=f"`{bot_prefix}s [number_of_messages] [everyone_mention_yes_or_no] [message_to_spam] `", inline=False)
        #         embed.add_field(name="Description", value="This will only spam messages in the given channel, maximum number_of_messages possible is 650, default is 5", inline=False)
        #         embed.set_footer(text=f"Bot created by {bot_creator_name}")
        #         await message.channel.send(embed=embed)
            
        #     elif subcmnd in mass_spam_wl:
        #         embed=discord.Embed(title="Help for Mass Spam", color=0x00d9ff)
        #         embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        #         embed.add_field(name="Other names:", value=f"{str(mass_spam_wl)}", inline=False)
        #         embed.add_field(name="Usage:", value=f"`{bot_prefix}ms [number_of_messages] [everyone_mention_yes_or_no] [message_to_spam] `", inline=False)
        #         embed.add_field(name="Description", value="This will spam in every channel of every server the bot has been joined to, maximum number_of_messages possible is 350, default is 5, so its 5 messages for every channel one by one", inline=False)
        #         embed.set_footer(text=f"Bot created by {bot_creator_name}")
        #         await message.channel.send(embed=embed)
            
        #     elif subcmnd in masschannel_unsafe_wl:
        #         embed=discord.Embed(title="Help for Mass Channel Creating - Unsafe", color=0x00d9ff)
        #         embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        #         embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        #         embed.add_field(name="Usage:", value=f"`{bot_prefix}mc [number_of_channels_to_create] [channel_name] `", inline=False)
        #         embed.add_field(name="Description", value="This command creates channels in the server upto the specified amount with the given name continuously, maximum number_of_channels_to_create is 100, default is 5", inline=False)
        #         embed.set_footer(text=f"Bot created by {bot_creator_name}")
        #         await message.channel.send(embed=embed)
            
        #     elif subcmnd in masschannel_safe_wl:
        #         embed=discord.Embed(title="Help for Mass Channel Creating - Safe", color=0x00d9ff)
        #         embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        #         embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        #         embed.add_field(name="Usage:", value=f"`{bot_prefix}mcs [number_of_channels_to_create] [channel_name] `", inline=False)
        #         embed.add_field(name="Description", value="This command creates channels in the server upto the specified amount with the given name with a time interval, maximum number_of_channels_to_create is 45, default is 5", inline=False)
        #         embed.set_footer(text=f"Bot created by {bot_creator_name}")
        #         await message.channel.send(embed=embed)
            
        #     elif subcmnd in massrole_unsafe_wl:
        #         embed=discord.Embed(title="Help for Mass Role Creating - Unsafe", color=0x00d9ff)
        #         embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        #         embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        #         embed.add_field(name="Usage:", value=f"`{bot_prefix}mr [number_of_roles_to_create] [role_name] `", inline=False)
        #         embed.add_field(name="Description", value="This command creates roles in the server upto the specified amount with the given name continuously, maximum number_of_roles_to_create is 150, default is 5", inline=False)
        #         embed.set_footer(text=f"Bot created by {bot_creator_name}")
        #         await message.channel.send(embed=embed)
            
        #     elif subcmnd in massrole_safe_wl:
        #         embed=discord.Embed(title="Help for Mass Role Creating - Safe", color=0x00d9ff)
        #         embed.set_author(name=f"{bot_name}", icon_url=f"{bot_author_icon}")
        #         embed.add_field(name="Other names:", value=f"{str(masschannel_unsafe_wl)}", inline=False)
        #         embed.add_field(name="Usage:", value=f"`{bot_prefix}mr [number_of_roles_to_create] [role_name] `", inline=False)
        #         embed.add_field(name="Description", value="This command creates roles in the server upto the specified amount with the given name with a time interval, maximum number_of_roles_to_create is 45, default is 5. Mentioning the [role_name] as 'random' will create roles with random names", inline=False)
        #         embed.set_footer(text=f"Bot created by {bot_creator_name}")
        #         await message.channel.send(embed=embed)


        await client.process_commands(message)
    




keep_alive()

client.run(token)











