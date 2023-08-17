import discord
from discord.ext import commands
import subprocess
import random
import requests, json
from datetime import date

TOKEN = 'token'

intents = discord.Intents().all()

client = commands.Bot(command_prefix='wb', intents=intents)

class WandyBotClass:
    waiting_for_answer = 0
    letter_received = 0
    sticker_count = 0
    good_emojis = ['heart', 'heart_decoration' , 'heartbeat' , 'smiley' , 'slight_smile' , 'sunglasses' , 'heart_eyes' , 'star_struck' , 'innocent' , 'partying_face']
    channel_id = 857111956704198706
    nick_answer = 0
    play_words = ['lheol', 'lapy', 'nsu', 'prttey', 'ycr']
    playing_true = 0
    user_admin = 0
    user_admin_accessing_true = 0
    admin_access = 0
    user_admin_in_progress = 0
    random_dice = ['1' , '2' , '3' , '4' , '5' , '6']
    chosen_word = ''


class WandyWeatherBotClass:
    @staticmethod
    async def handle_weather(message):
        print (' {0.author} is importing weather')
def get_weather(city):
    try:
        base_url = ('http://api.weatherapi.com/v1/current.json?key=56f8d9680ef24b20883144842211004')
        complete_url = base_url + "&q=" + city
        response = requests.get(complete_url) 
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed=discord.Embed(title=f"{city}"' Weather', description=f"{country}", color=0x7272f0)
        embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x7272f0)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def handle_help(message):
    embed=discord.Embed(title="Commands", color=0x7272f0)
    embed.add_field(name="wb help", value="Shows this list", inline=True)
    embed.add_field(name="wb hello", value="Says hello", inline=True)
    embed.add_field(name="wb stickers", value="Your sticker count", inline=True)
    embed.add_field(name="wb open letter", value="If given a letter, opens it", inline=True)
    embed.add_field(name="wb time", value="Shows local time", inline=True)
    embed.add_field(name="wb server stats", value="Shows this servers' stats", inline=True)
    embed.add_field(name="wb play", value="Play a game!", inline=True)
    embed.add_field(name="Wandy84-Bot prefix", value="Shows this bots' prefix", inline=True)
    embed.add_field(name="wb ping", value="Pong!", inline=True)
    embed.add_field(name="wb weather (city)", value="Shows weather in given city", inline=True)
    embed.add_field(name="wb roll a die", value="Rolls a die", inline=True)
    embed.add_field(name="wb server count", value="Shows number of members in this server", inline=True)

    await message.channel.send(embed=embed)

async def handle_ping(message):
    embed=discord.Embed(title="Pong!", color=0x7272f0)

    await message.channel.send(embed=embed)

async def handle_hello(message):
    embed=discord.Embed(title="Hello!", description="How are you feeling?", color=0x7272f0)
    embed.add_field(name="1", value="Okay", inline=True)
    embed.add_field(name="2", value="Sad", inline=True)
    embed.add_field(name="3", value="Normal", inline=True)
    embed.set_footer(text="Type in a number")

    await message.channel.send(embed=embed)
    WandyBotClass.waiting_for_answer = 1

async def handle_open_letter(message):
    if WandyBotClass.letter_received == 1:
        embed=discord.Embed(title="You opened a letter!", description='Dear {0.author}, I hope you are feeling good today! Even if you are not feeling good, you can always chat with me! :heart:    -The Wandy84-Bot Team'.format(message), color=0x7272f0)
        embed.add_field(name="Here are 5 stickers", value=':' + random.choice(WandyBotClass.good_emojis) + ': ' + ':' + random.choice(WandyBotClass.good_emojis) + ': ' + ':' + random.choice(WandyBotClass.good_emojis) + ': ' + ':' + random.choice(WandyBotClass.good_emojis) + ': ' + ':' + random.choice(WandyBotClass.good_emojis) + ':', inline=True)
        await message.channel.send(embed=embed)
        WandyBotClass.letter_received = 0
        WandyBotClass.sticker_count += 5
    else:
        embed=discord.Embed(title="You don't have a letter :(", color=0x7272f0)

        await message.channel.send(embed=embed)

async def handle_answers(message):
    if message.content.startswith('1'):
        embed=discord.Embed(title="Okay is better than nothing!", description='Here, have a sticker: :' + random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

        await message.channel.send(embed=embed)

        WandyBotClass.waiting_for_answer = 0
        WandyBotClass.sticker_count += 1

    if message.content.startswith('2'):
        embed=discord.Embed(title="Here, this will cheer you up.", description="(You have received a letter! open it with wb open letter)", color=0x7272f0)

        await message.channel.send(embed=embed)

        WandyBotClass.letter_received = 1 
        WandyBotClass.waiting_for_answer = 0

    if message.content.startswith('3'):
        embed=discord.Embed(title="Good! I hope your normal is a good thing!", description='Here, have a sticker: :' + random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

        await message.channel.send(embed=embed)

        WandyBotClass.sticker_count += 1
        WandyBotClass.waiting_for_answer = 0

async def handle_stickers_count(message):
    embed=discord.Embed(title="Your Stickers", description='You have ' + str(WandyBotClass.sticker_count) +' sticker(s)!', color=0x7272f0)

    await message.channel.send(embed=embed)


async def handle_play(message):
    WandyBotClass.chosen_word = random.choice(WandyBotClass.play_words)

    embed=discord.Embed(title="Unscramble the following word:", description=WandyBotClass.chosen_word, color=0x7272f0)
    embed.set_footer(text="Type the answer and see if you were correct!")

    await message.channel.send(embed=embed)

    await message.channel.send('Unscramble the following word: ' + WandyBotClass.chosen_word + ' type in chat the answer and see if you were correct!')
    WandyBotClass.playing_true = 1


async def handle_playing_true(message):

    if WandyBotClass.chosen_word == 'lheol':
        if message.content.startswith('hello'):
            embed=discord.Embed(title="You were correct!", description='Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

            await message.channel.send(embed=embed)
            WandyBotClass.sticker_count += 1
        else:
            embed=discord.Embed(title="You weren't correct :(", color=0x7272f0)

            await message.channel.send(embed=embed)


    if WandyBotClass.chosen_word == 'lapy':
        if message.content.startswith('play'):
            embed=discord.Embed(title="You were correct!", description='Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

            await message.channel.send(embed=embed)
            WandyBotClass.sticker_count += 1
        else:
            embed=discord.Embed(title="You weren't correct :(", color=0x7272f0)

            await message.channel.send(embed=embed)


    if WandyBotClass.chosen_word == 'nsu':
        if message.content.startswith('sun'):
            await message.channel.send('You were correct! Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':')
            WandyBotClass.sticker_count += 1
        else:
            embed=discord.Embed(title="You weren't correct :(", color=0x7272f0)

            await message.channel.send(embed=embed)
    
    
    if WandyBotClass.chosen_word == 'prttey':
        if message.content.startswith('pretty'):
            embed=discord.Embed(title="You were correct!", description='Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

            await message.channel.send(embed=embed)
            WandyBotClass.sticker_count += 1
        else:
            embed=discord.Embed(title="You weren't correct :(", color=0x7272f0)

            await message.channel.send(embed=embed)


    if WandyBotClass.chosen_word == 'ycr':
        if message.content.startswith('cry'):
            embed=discord.Embed(title="You were correct!", description='Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

            await message.channel.send(embed=embed)
            WandyBotClass.sticker_count += 1
        else:
            embed=discord.Embed(title="You weren't correct :(", color=0x7272f0)

            await message.channel.send(embed=embed)

    WandyBotClass.playing_true = 0


async def handle_roll_dice(message):
    embed=discord.Embed(title="Rolling the die...", description='The result was: ' + random.choice(WandyBotClass.random_dice) + '', color=0x7272f0)

    await message.channel.send(embed=embed)


async def handle_server_count(message):
    embed=discord.Embed(title='Wandy84-Bot is in'+ (f' {len(client.guilds)} ') + 'servers!', color=0x7272f0)

    await message.channel.send(embed=embed)


async def handle_server_stats(message):
    embed=discord.Embed(title=f'Server name: {message.guild.name} Total members: {message.guild.member_count}', color=0x7272f0)

    await message.channel.send(embed=embed)


async def handle_time(message):
    today = date.today()
    embed=discord.Embed(title="Today's date: " + str(today), color=0x7272f0)

    await message.channel.send(embed=embed)


async def handle_prefix(message):
    embed=discord.Embed(title="The Wandy84-Bot prefix is wb. Type wb help for a command list.", color=0x7272f0)

    await message.channel.send(embed=embed)


@client.event
async def on_member_join(member):
    channel = client.get_guild(789869494709256214).get_channel(WandyBotClass.channel_id)

    print ('Recognised that a member called ' + member.name + ' joined')
    await channel.send('Welcome @' + member.name + ' to ' + member.guild.name + ' ! We hope you will enjoy your stay!')
    if member.name == ('{0.user}'):
        await channel.send('Thank you for inviting Wandy84-Bot to your server! Wandy84-Bots prefix is wb. For a list of commands do wb help.')

@client.event
async def on_member_remove(member):
    channel = client.get_guild(789875655290388530).get_channel(WandyBotClass.channel_id)

    print ('Recognised that member called ' + member.name + ' left')
    await channel.send('Bye ' + member.name + ', we will miss you ')


@client.event
async def on_message(message):
    print(message.author, message.content, message.channel.id)

    if message.author == client.user:
        return

    elif message.content.startswith('wb help'):
        await handle_help(message)

    elif message.content.startswith('wb hello'):
        await handle_hello(message)

    elif WandyBotClass.waiting_for_answer == 1:
        await handle_answers(message)

    elif WandyBotClass.playing_true == 1:
        await handle_playing_true(message)

    elif message.content.startswith('wb open letter'):
        await handle_open_letter(message)
  
    elif message.content.startswith('wb stickers'):
        await handle_stickers_count(message)

    elif message.content.startswith('wb ping'):
        await handle_ping(message)

    elif message.content.startswith('wb play'):
        await handle_play(message)

    elif message.content.startswith('wb roll a die'):
        await handle_roll_dice(message)

    elif message.content.startswith('wb server count'):
        await handle_server_count(message)

    elif message.content.startswith('wb server stats'):
        await handle_server_stats(message)
    
    elif message.content.startswith('wb weather'):
        await WandyWeatherBotClass.handle_weather(message)
        city = message.content[slice(11, len(message.content))].lower()
        result = get_weather(city)
        await message.channel.send(embed=result)
    
    elif message.content.startswith('wb time'):
        await handle_time(message)

    elif message.content.startswith('Wandy84-Bot prefix'):
        await handle_prefix(message)

    elif message.content.startswith('wb'):
        embed=discord.Embed(title="Not a command, to see commands use wb help.", color=0x7272f0)
        await message.channel.send(embed=embed)

    elif message.content.startswith('wB'):
        embed=discord.Embed(title="Please use wb in lowercase letters if you wish to start a command.", color=0x7272f0)
        await message.channel.send(embed=embed)

    elif message.content.startswith('WB'):
        embed=discord.Embed(title="Please use wb in lowercase letters if you wish to start a command.", color=0x7272f0)
        await message.channel.send(embed=embed)

    elif message.content.startswith('Wb'):
        embed=discord.Embed(title="Please use wb in lowercase letters if you wish to start a command.", color=0x7272f0)
        await message.channel.send(embed=embed)

client.run(TOKEN)
