from dotenv import load_dotenv
import discord, asyncio, settings,  services.bot as bot

client = discord.Client()

@client.event
async def on_ready():
    print(f'\n---------------------------------\n')
    print(f'Chatbot discord elaborado por: itgabriel\n')
    for channel in client.guilds:
        print(f'Servidor id: {channel.id}')
        print(f'Servidor utilizador: {channel.name}')
        print(f'Quantidade de usuários: {channel.member_count}')
    print(f'\n---------------------------------\n')


# Evento responsável por monitorar as mensagens que é recebida no servidor
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    # Com base na quantidade de players, faz a separação de 1x1.
    if message.content.startswith('>formar-partida'):
        import time, random
        await message.channel.send(f"```- Bem vindo ao sistema de campeonato -```")
        time.sleep(2.0)
        await message.channel.send(f"```- Elaborado por Gabriel Gustavo // vulgo GG -```")
        time.sleep(2.0)
        await message.channel.send(f"```- Inicializando o sistema de campeonato para {message.content} -```")
        time.sleep(1.0)
        await message.channel.send("```- Informe a quantidades de participantes - ```")
        qtd_players = await client.wait_for('message')
        try:
            jogadores = []
            for jogador in range(int(qtd_players.content)):
                time.sleep(1.0)
                await message.channel.send(f"```Digite o nome do {jogador + 1}º player```")
                nome_jogador = await client.wait_for('message')
                jogadores.append(nome_jogador.content)
            
            random.shuffle(jogadores)

            versus = []
            contador = 1
            versus_quadro = "```TABELA DE JOGOS\n"

            for jogador in range(len(jogadores)):

                if len(versus) < 2:
                    if int((jogador + 1)) <= len(jogadores):
                        versus.append(jogadores[jogador])

                if len(versus) == 2:
                    versus_quadro += f'\n{contador}º - {versus[0]} VS {versus[1]}'
                    versus.pop()
                    versus.pop()
                    contador += 1

            await message.channel.send( (versus_quadro+'```') )
            if bool(versus):
                await message.channel.send(f'```Jogador em espera/sem versus(que sobrou) -> {versus[0]}```')

        except:
            await message.channel.send(f'```Falha em realizar a separação de partidas/contra.```')

    

    # EVENT// 
    if message.content.startswith('>bot'):
        await message.channel.send(embed=bot.message_help_bot(message))
    # if message.channel.name == "canal-texto-teste":
    #     for channel in message.guild.channels:
    #         if channel.name == "teste-de-comandos":
    #            print(channel)
    #            print(channel.id)
    #            channel_anuncio = client.get_channel(channel.id)
    #            print(channel_anuncio)
    #            channel_anuncio.send("Noticias funfou")
    # EVENT// 
    # if message.content.startswith('>aviso'):
    #     await message.channel.send(f'`Avisos em manutenção`')
    # EVENT// 
    # if message.content.startswith('>clear'):
    #     await message.channel.send(f'`Limpeza/clear em manutenção`')
    #     # total_messages = message.fetch_message(message.channel.id)
    #     # print(total_messages)
    #     # await message.channel.bulkDelete()
    #     # print(client.get_channel(message.channel.id))
    # EVENT// 
    # if message.content.startswith('>ping'):
    #     await message.channel.send(f'`Pong {message.author.name}`')
    # EVENT// 
    # if message.content.startswith('>gif'):
    #     await message.channel.send(f'`Gif do servidor:`')
    #     await message.channel.send(f'https://media.giphy.com/media/1C8bHHJturSx2/giphy.gif')
    # EVENT// 
    # # No canal que foi dado o comando, deleta tudo e também o canal.
    # if message.content.startswith('>deletechannel'):
    #     await message.channel.delete()



# Eventos de ingressão do usuário
# @client.event
# async def on_member_join(member):
#     channel_bemvindo = client.get_channel(member.guild.channels[3].id)
#     await channel_bemvindo.send(bot.message_welcome_bot(member))
    
# @client.event
# async def on_message_delete(message):
#     await message.channel.send(f"Mensagme excluida: {message.author}")


client.run(settings.SECRET_TOKEN)


# itgabriel
# devleirbagg
