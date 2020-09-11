import discord

# def message_welcome_bot(member):
#     return str(f'Olá {member.mention}\n'
#     + f'Bem vindo ao servidor **{member.guild.name}**\n'
#     + f'Não se esqueça de ler nossas')
    # + f'Não se esqueça de ler nossas <#{member.guild.channels[5].id}>')
    


def message_help_bot(message):
    embedCard = discord.Embed(description="Precisa de ajuda ? Utilize algum dos comandos abaixo para que eu possa lhe auxiliar.", color=000000000)
    embedCard.set_author(name=f"{message.author.display_name}", icon_url=message.author.avatar_url)
    embedCard.add_field(name=">formar-partida", value="Com base na quantidade de players, faz a separação de 1x1", inline=False)
    # embedCard.add_field(name=">clear", value="Limpa o histórico de conversa.(Necessário permissão de ADM/Moderador)", inline=False)
    # embedCard.add_field(name=">ping", value="Brinque de ping-pong!", inline=True)
    # embedCard.add_field(name=">gif", value="Um gif aleatório!", inline=True)
    embedCard.set_footer(text=f"Command owner: {message.author.display_name}", icon_url=message.author.avatar_url)
    return embedCard