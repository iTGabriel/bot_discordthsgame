from dotenv import load_dotenv
import discord, asyncio, settings, services.bot as bot

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

    


    # EVENT//HELPER 
    if message.content.startswith('>bot'):
        await message.channel.send(embed=bot.message_help_bot(message))
    
    # Sai do Discord e fecha todas as conexões.
    if message.content.startswith('>shutdown'):
        await client.logout()
        
    # Fecha a conexões do discord.
    if message.content.startswith('>close'):
        await client.logout()


def start_server(token):
    log = open("text_main.txt", "w")
    try:
        client.run(token)
    except:
        log.write("Falha ao ligar o servidor")
        log.close()

start_server(settings.SECRET_TOKEN)


# itgabriel
# devleirbagg
