from datetime import datetime
import discord

intents = discord.Intents.all()
intents.members = True


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client(intents=intents)

prefix = "!"


@client.event
async def on_member_join(member):
    await member.send(f'''Welcome to the server{member.mention}''')
    for channel in member.server.channels:
        await channel.send


@client.event
async def on_member_update(before, after):
    status = f'''{before.name} ||{before.raw_status}|| status was changed to ||{after.raw_status}|| at {datetime.now().strftime("%H:%M:%S")}'''
    with open("status.txt", "a") as status_file:
        status_file.write(f"\n{status}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    id = client.get_guild(875028803464863784)
    print(f"""By: {message.author} || Message: {message.content} || at {datetime.now().strftime("%H:%M")}""")
    channels = ["general"]
    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            if message.author.id == 690162584589959188:
                await message.channel.send("Mvj is lawda")
            else:
                await message.channel.send(f"Hello {message.author.mention}")
        elif message.content == "!users":
            await message.channel.send(f'''Total members: {id.member_count}''')

    
# This will log the messages 
@client.event
async def on_message(message, pf=prefix):
    with open('logs.txt', "a") as logs_file:
        logs_file.write(f"""By: {message.author} || Message: {message.content} || at {datetime.now().strftime("%H:%M")}\n""")
        logs_file.close()
    
    if message.content == "!get":
        with open("status.txt", "rb") as file:
            await message.channel.send(file=discord.File(file, "status_log.txt"))

    if message.content == "!textlogs":
        with open("logs.txt", "rb") as file:
            await message.channel.send(file=discord.File(file, "status_log.txt"))


client.run(token)
# making a change
# adding a second comment
# 3d comment
# yes yes yes

if True:
    pass
