import discord 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidores são:{os.linesep} 1 - Não desrespeitar os membros{os.linesep} 2 - Regra importante 2 ')
        elif message.content == '?nivel':
            await message.author.send('Nível 1')

    async def on_member_join(self, member):
        guild =  member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name} '
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('My token goes here')

