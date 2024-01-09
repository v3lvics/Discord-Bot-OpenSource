import discord
from discord.ext import commands
from discord import app_commands
bot = commands.Bot(command_prefix=("?"),intents=discord.Intents.all())
import time

@bot.event
async def on_ready():
    print("Bot Online")

@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user_id, *, reason="***<:tickno:1126629983209664527> User didn't provide a reason.***"):
    try:
        user = await bot.fetch_user(user_id)
        if user is None:
            raise discord.NotFound
        await ctx.guild.ban(user, reason=reason)
        ban = discord.Embed(
            color=discord.Colour.green(),
            title=f"**<:tickyes:1126630082262335488> Banned** {user.name}!",
            description=f"**Reason:** {reason}\n**By:** {ctx.author.mention} ",
        )   
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)
    except discord.NotFound:
        await ctx.channel.send("<:tickno:1126629983209664527> User not found or not a member of any mutual guild.")

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="***<:tickno:1126629983209664527> User didnt provde reason.***"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f" **<:tickyes:1126630082262335488> Kicked** {user.name}!", description=f"**Reason:** {reason}\n**By:** {ctx.author.mention}",color=discord.Color.green())
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, user_id, *, reason="***<:tickno:1126629983209664527> User didn't provide a reason.***"):
    try:
        await ctx.message.delete()
        user = await bot.fetch_user(user_id)
        if user is None:
            raise discord.NotFound
        await ctx.guild.unban(user, reason=reason)
        unban = discord.Embed(
            title=f" **<:tickyes:1126630082262335488> Unbanned** {user.name}!",
            description=f"**Reason:** {reason}\n**By:** {ctx.author.mention}",
        )
        await ctx.channel.send(embed=unban)
        await user.send(embed=unban)
    except discord.NotFound:
        await ctx.channel.send("<:tickno:1126629983209664527> User not found / not a member of any mutual guild.")

@commands.has_permissions(administrator=True)
@bot.command()
async def cleanraid(ctx,*, name="No name given."):
    raid_embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Raid Cleanup",
        description="Preparing mass channel delete of " + name
    )
    
    await ctx.send(embed = raid_embed)
    await ctx.message.delete()
    for channel in bot.get_all_channels():
        if channel.name == name:
            await channel.delete()

    raid_done = discord.Embed(
        color=discord.Colour.green(),
        title="Raid Cleanup",
        description="<:tickyes:1126630082262335488> Succesfully cleaned up all channels named: " + name
    )
    time.sleep(2)
    await ctx.send(embed = raid_done)



@bot.command()
async def baninfo(ctx):
    username = ctx.message.author.name
    print(username + " used baninf")
    ban_embed = discord.Embed(
        title="Ban Command",
        description="The `ban` command is used to ban a user from the server.",
        color=discord.Color.dark_gray()
    )
    ban_embed.add_field(
        name="Usage",
        value="`?ban <user_id> [reason]`",
        inline=False
    )
    ban_embed.add_field(
        name="Permissions Required",
        value="`Ban Members`",  	
        inline=False
    )
    await ctx.send(embed=ban_embed)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="sayhi")
async def dosmh(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.name} i see you used a command.")



@bot.command()
async def cmds(ctx):
    cmds_embed = discord.Embed(
        title="Command List",
        description="Commands that are currently supported. [MIGHT GET OUTDATED]\n Permission(s) required to use: None",
        color=discord.Color.dark_blue()
    )
    cmds_embed.add_field(
        name="Ban",
        value="?ban <user_id> [reason]\n ?unban <user_id> [reason]\n ?baninfo\n Permission(s) required to use: Ban Members",
        inline=False
    )
    cmds_embed.add_field(
        name="Kick",
        value="?kick <user_id> [reason]\n Permission(s) required to use: Kick Members",  	
        inline=False
    )
    cmds_embed.add_field(
        name="Raid Cleanup",
        value="?cleanraid [Spammed channles / name]\n Permission(s) required to use: Administrator",  	
        inline=False
    )
    cmds_embed.add_field(
        name="Ping",
        value="?ping\n Permission(s) required to use: None",  	
        inline=False
    )

    cmds_embed.add_field(
        name="Shutdown",
        value="?shutdown\n [Bot owner only]",  	
        inline=False
    )
    cmds_embed.add_field(
        name="Add Role",
        value="?add [user id] [Role Name]\n Permission(s) required to use: Manage Roles \n [RoLe NAME MUST INCLUDE CAPPED LETTERS]",  	
        inline=False
    )
    cmds_embed.add_field(
        name="Remove Role",
        value="?remove [user id] [Role Name]\n Permission(s) required to use: Manage Roles \n [RoLe NAME MUST INCLUDE CAPPED LETTERS]",  	
        inline=False
    )
    await ctx.send(embed = cmds_embed)

@commands.has_permissions(manage_roles=True)
@bot.command()
async def add(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    add_embed = discord.Embed(
        title="<:tickyes:1126630082262335488> Added role.", 
        description="Succesfully gave user role.",
        color=discord.Color.dark_blue()
    )
    add_embed.add_field(
        name="Role Granted.",
        value=f"Role Granted: " + role.mention,
        inline=False
    )
    await ctx.send(embed=add_embed)

@commands.has_permissions(manage_roles=True)
@bot.command()
async def remove(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    add_embed = discord.Embed(
        title="<:tickyes:1126630082262335488> Removed Role.",
        description="Succesfully removed user role.",
        color=discord.Color.dark_green()
    )
    add_embed.add_field(
        name="Role Removed.",
        value=f"Role Removed: " + role.mention,
        inline=False
    )
    await ctx.send(embed=add_embed)

@bot.command(aliases=["whois"])
async def getinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    
    userAvatar = member.display_avatar
    embed = discord.Embed(title=f"User Information:", description="", color=0xffff00)
    embed.set_thumbnail(url=userAvatar.url)

    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="User ID:", value=member.id,inline=False)
    embed.add_field(name="Display Name:", value=member.display_name,inline=False)

    embed.add_field(name="Account creation:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
    embed.add_field(name="Member joined:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)

    embed.add_field(name="User Roles:", value="".join([role.mention for role in roles]),inline=False)
    await ctx.send(embed=embed)

@commands.has_guild_permissions(manage_messages=True)
@bot.command
async def purge(ctx,am):
    await ctx.channel.purge(limit = int(am) +1)

    finish = discord.Embed(
        title="<:tickyes:1126630082262335488> Operation successful.", 
        description="Successfully purged " + am +" messages.",
        colour=discord.Colour.dark_green()
    )

    msg = await ctx.send(finish)

@bot.command()
async def ping(ctx):
        await ctx.send("Pong!")




# RICH PRESENCE

# DISCORD NEW UPDATE FOR SCRIPTING EMBEDS USE THIS WHEN SENDING:
# await ctx.send(embed = your_embed)
# role grant = await.user.add_roles(role) / include *role* in ctx

# BOT TOKEN DO NOT SHARE / BOT ABUSE RISK AND EXPLOIT
bot.run('YourBotToken')
