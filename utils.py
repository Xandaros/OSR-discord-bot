from config import roles_dict
import discord
from config import *

async def add_role(ctx, role_name):
    role_dict = roles_dict[role_name]
    if str(ctx.message.channel) not in role_dict['allowed_channels']:
        message = "Please " + ctx.message.author.mention + ", use the appropriate channels for this command: "
        message += ' '.join(role_dict['allowed_channels'])
        await ctx.send(message)
        return

    role = role_dict["role"]
    if role in ctx.message.author.roles:
        await ctx.send("Hey, " + ctx.message.author.mention + " is still " +
                       role_dict["verbose"] + ".")
    else:
        await ctx.message.author.add_roles(role)
        await ctx.send("Hey, " + ctx.message.author.mention + " is " + role_dict["verbose"] + ".")

def user_info_message(user, infos):
    message = '**' + user.name + '**'
    info = infos.get(str(user.id))
    if info is not None:
        kgs_username = info.get('kgs_username')
        kgs_rank = info.get('kgs_rank')
        ogs_username = info.get('ogs_username')
        ogs_rank = info.get('ogs_rank')
        servers = []
        if kgs_username is not None or ogs_username is not None:
            message += ':'
            if ogs_username is not None:
                servers.append(' OGS | ' + ogs_username + ' (' + ogs_rank + ')')
            if kgs_username is not None:
                servers.append(' KGS | ' + kgs_username + ' (' + kgs_rank + ')')
        message += ' - '.join(servers)
    message += '\n'
    return message

def user_rank(user, infos):
    message = ''
    info = infos.get(str(user.id))
    if info is not None:
        kgs_rank = info.get('kgs_rank')
        ogs_rank = info.get('ogs_rank')
        servers = []
        if kgs_rank is not None or ogs_rank is not None:
            if ogs_rank is not None:
                servers.append('OGS: ' + ogs_rank + ')')
            if kgs_rank is not None:
                servers.append('KGS: ' + kgs_rank + ')')
        message += ' - '.join(servers)
        message = '({0})'.format(message)
    return message

def get_user(username, bot):
    role = discord.utils.get(bot.get_guild(guild_id).roles, id=287489624014585866)
    if username[0] == "#":
        user = discord.utils.get(role.members, discriminator=str(username[1:]))
    else:
        user = discord.utils.get(role.members, display_name=username)
    if user is None:
        user = discord.utils.get(role.members, name=username)
    return user
