import json
botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["bot-prefix"]
bot_creator_name = botconfigdata["bot-creator-name"]
bot_name = botconfigdata["bot-name"]
bot_author_icon = botconfigdata["author-icon"]
bot_sm_wt = botconfigdata["safe-modes-wait-time"] # bot safe mode what time

botsmwt = float(bot_sm_wt)

print(botsmwt)
print(type(botsmwt))