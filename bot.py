import random
import discord
from discord.ext import commands

TOKEN = 'ODAxNDk4NzA0MzgwMjk3MjI3.YAhj1g.nHVNCgql1remOKmwuaY_sSD-R8g'

description = '''Bonzi Buddy Stealer of Memes'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="Waluigi for Atari 2600"))
    
@bot.event
async def on_command_error(ctx, error):
    user = ctx.message.author
    await ctx.send(f"An error occured: {str(error)}")
    print(ctx.message.author)

#role = "Citizen" # Role to be autoroled when user joins

#@client.event
#async def on_member_join(member): 
    #rank = discord.utils.get(member.guild.roles, name=role) #Bot get guild(server) roles
    #await member.add_roles(rank)
    #print(f"{member} was given the {rank} role.")

@bot.command()
async def hello(ctx):
    """Says world"""
    user = ctx.message.author
    await ctx.send("world")
    print(ctx.message.author)

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    user = ctx.message.author
    await ctx.send(left + right)
    print(ctx.message.author)
    
@bot.command()
async def joke(ctx):
    """Unfunny Joke"""
    user = ctx.message.author
    await ctx.send(random.choice(jokes)) 
    print(ctx.message.author)
    
@bot.command()
async def sayuser(ctx):
    """get user name"""
    user = ctx.message.author
    await ctx.send("mention: " + user.mention + " name: " + user.name)
    print(ctx.message.author)

@bot.command()
async def mario(ctx):
    """RUN"""
    user = ctx.message.author
    await ctx.send("https://cdn.discordapp.com/attachments/731930062777221171/794807999096684584/video0_67.mp4")
    print(ctx.message.author)
    
@bot.command()
async def betaGif(ctx):
    """NULL"""
    user = ctx.message.author
    await ctx.send(random.choice(gifs))
    print(ctx.message.author)
    
#@bot.command()
#async def gif(ctx):
    #ctx.send(file=discord.File('squidward.gif'))
    
jokes = ["What do you call a Cow that can\'t give milk? An utter faliure!",
         "What do Donkeys send out near Christmas? Mule tide greetings!",
         "Who earns a living by driving his customers away? A Taxi Driver!",
         "What question can never be answered by yes? Are you asleep?",
         "Why do they call HTML hyper text? Too much Java!",
         "When is the best time to got to bed? When the bed won\'t come to you!"]
gifs = ["https://media.discordapp.net/attachments/817586768827121666/836011336437727262/image0.gif"]

bot.run(TOKEN)

if __name__ == "__main__":
    run()


