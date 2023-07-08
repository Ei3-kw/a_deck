import discord
import 

async def send_msg(msg, user_msg, is_private):
    try:
        response = ...
        await msg.author.send(response) if is_private else await msg.channel.send(response)
    except Exception as e:
        print(e)

def run():
    TOKEN = 'MTEyNzIxMzI5OTc0MjgxMDIwMg.GBUVXk.XOLHwySJkRL3ZfM1fZuccoScfklyF0RBpHOKEE'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is launched... Target locked. Roger that target lock. Fire at will. ')

    @client.event
    async def on_msg(msg):
        if msg.author == client.user:
            return

        user = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

        if user_msg[0] == '!':
            await send_msg(msg, user_msg[1:], is_private=True)
        else:
            await send_msg(msg, user_msg, is_private=False)

    client.run(TOKEN)