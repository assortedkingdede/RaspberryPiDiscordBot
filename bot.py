import random
import discord
from discord.ext import commands
import DiscordUtils

#Shoutout to the dumbass who made this program who has uploaded the bot token multiple times

#Shoutouts to the people who made Bonzi Buddy for causing over twenty years of terror on the internet. 

TOKEN = 'INSERT TOKEN HERE'

description = '''Bonzi Buddy Stealer of Memes'''
bot = commands.Bot(command_prefix='?', description=description)

defaultRole = 'level 1'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for guild in bot.guilds:
        print(guild.name)
        print(guild.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="Bonzification"))
    
@bot.event
async def on_command_error(ctx, error):
    user = ctx.message.author
    await ctx.send(f"An error occured: {str(error)}")
    print(ctx.message.author)

#@bot.event
#async def on_member_join(member):
    #channel = discord.utils.get(member.guild.channels, name="general")
    #embed = discord.Embed(title = "

@bot.command()
async def hello(ctx):
    """Says world"""
    user = ctx.message.author
    await ctx.send("world")
    print(ctx.message.author)

@bot.command()
async def add(ctx, left : int, right : int):
    """Addition"""
    user = ctx.message.author
    await ctx.send(left + right)
    print(ctx.message.author)

@bot.command()
async def subtract(ctx, left : int, right : int):
    """Subtraction"""
    user = ctx.message.author
    await ctx.send(left - right)
    print(ctx.message.author)
    
@bot.command()
async def multiply(ctx, left : int, right : int):
    """Multiplication"""
    user = ctx.message.author
    await ctx.send(left * right)
    print(ctx.message.author)
    
@bot.command()
async def divide(ctx, left : int, right : int):
    """Division"""
    user = ctx.message.author
    await ctx.send(left / right)
    print(ctx.message.author)
    
"""Add a for loop to call more than one joke"""                           
@bot.command()
async def joke(ctx, arg):
    """Unfunny Joke"""
    user = ctx.message.author
    print(ctx.message.author)
    if arg = 1
        await ctx.send(random.choice(jokes))
    elif arg = 2
        await ctx.send(random.choice(jokes))
        await ctx.send(random.choice(jokes))
    
    
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
                          
@bot.command
async def help(ctx):
    await ctx.send("""Commands:
    !help: Shows this command
    !hello: Says World
    !add: Adds two numbers.
    !subtract: Subtracts on number from another
    !multiply:
    !divide:
    
    
    
jokes = ["What do you call a Cow that can\'t give milk? An utter faliure!",
         "What do Donkeys send out near Christmas? Mule tide greetings!",
         "Who earns a living by driving his customers away? A Taxi Driver!",
         "What question can never be answered by yes? Are you asleep?",
         "Why do they call HTML hyper text? Too much Java!",
         "When is the best time to got to bed? When the bed won\'t come to you!",
         "Why did the scientist install a knocker on his door? To win the No-bel prize!",
         "Who earns a living by driving their customers away? A taxi driver!"]

gifs =["https://media.discordapp.net/attachments/817586768827121666/836011336437727262/image0.gif",
        "https://tenor.com/view/jontron-just-let-me-die-flex-tape-im-too-perfect-let-me-die-gif-13374794",
        "https://tenor.com/view/tf2-spy-spy-tf2-gentlemen-gif-18144778"]

bot.run(TOKEN)

if __name__ == "__main__":
    run()
