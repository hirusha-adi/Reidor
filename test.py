async def massspam(ctx, numberofmsges="5", everyoneyn="yes", *, messagehere="I HAD A FUCKING BONER"):
    if int(numberofmsges) <= 650:
        yes_wl = ("yes", "y", "everyone", "true")
        if everyoneyn.lower() in yes_wl:
            for channel in ctx.guild.channels:
                print(channel, "-" ,channel.id)
                try:
                    x = client.get_channel(channel.id)
                    for iteration, y in enumerate(range(int(numberofmsges))):
                        await x.send(f"@everyone @here - {messagehere}")
                        time.sleep(0.2)
                    
                except AttributeError:
                    print("Its a Category or a Voice Channel, not a text channel")
                    continue
                x = None
        else:
            for channel in ctx.guild.channels:
                print(channel, "-" ,channel.id)
                try:
                    x = client.get_channel(channel.id)
                    for iteration, y in enumerate(range(int(numberofmsges))):
                        await x.send(f"{messagehere}")
                        time.sleep(0.2)
                except AttributeError:
                    print("Its a Category or a Voice Channel, not a text channel")
                    continue
                x = None

