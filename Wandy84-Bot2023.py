import discord
from discord.ext import commands
import subprocess
import random
import requests, json
from datetime import date
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import os

def firstload():
    default_config = {
        "bot_token": 'token',
        "bot_prefix": "wb"
    }

    with open("config.json", "w") as config_file:
        json.dump(default_config, config_file, indent=4)

def config(key):
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)
        return config_data.get(key)

if not os.path.exists("config.json"):
    firstload()

if 'BOT_TOKEN' in os.environ:
    TOKEN = os.environ['BOT_TOKEN']
elif config("bot_token") is not None:
    TOKEN = config("bot_token")
else:
    print("Unknown token. Please set the BOT_TOKEN environment variable or add it to config.json")
    exit()
prefix = config("bot_prefix")
intents = discord.Intents().all()


def save_firstload():
    default = {
        "waiting_for_answer": 0,
        "letter_received": 0,
        "sticker_count": 0,
        "good_emojis": ['heart', 'heart_decoration', 'heartbeat', 'smiley', 'slight_smile', 'sunglasses', 'heart_eyes', 'star_struck', 'innocent', 'partying_face'],
        "channel_id": 857111956704198706,
        "play_words": ['lheol', 'lapy', 'nsu', 'prttey', 'ycr'],
        "playing_true": 0,
        "random_dice": ['1', '2', '3', '4', '5', '6'],
        "chosen_word": ''
    }

    with open("save.json", "w") as save_file:
        json.dump(default, save_file, indent=4)

if not os.path.exists("save.json"):
    save_firstload()

try:
    with open("save.json") as save_file:
        xp = json.load(save_file)
except json.JSONDecodeError:
    print("Error: Invalid JSON data in save.json. Initializing with default values.")
    save_firstload()
    with open("save.json") as save_file:
        xp = json.load(save_file)

def save_to_json():
    with open("save.json", "w") as save_file:
        json.dump(xp, save_file, indent=4)


client = commands.Bot(command_prefix=config("bot_prefix"), intents=intents)

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
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Duolingo Lesson (Spanish or Vanish!!)'))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def handle_help(message):
    embed=discord.Embed(title="Commands", color=0x7272f0)
    embed.add_field(name=f"{prefix} help", value="Shows this list", inline=True)
    embed.add_field(name=f"{prefix} hello", value="Says hello", inline=True)
    embed.add_field(name=f"{prefix} stickers", value="Your sticker count", inline=True)
    embed.add_field(name=f"{prefix} open letter", value="If given a letter, opens it", inline=True)
    embed.add_field(name=f"{prefix} date", value="Shows (local) date", inline=True)
    embed.add_field(name=f"{prefix} server stats", value="Shows this servers' stats", inline=True)
    embed.add_field(name=f"{prefix} play", value="Play a game!", inline=True)
    embed.add_field(name="Wandy84-Bot prefix", value="Shows this bots' prefix", inline=True)
    embed.add_field(name=f"{prefix} ping", value="Pong!", inline=True)
    embed.add_field(name=f"{prefix} weather (city)", value="Shows weather in given city", inline=True)
    embed.add_field(name=f"{prefix} roll a die", value="Rolls a die", inline=True)
    embed.add_field(name=f"{prefix} server count", value="Shows the number of servers Wandy is in", inline=True)
    embed.add_field(name=f"{prefix} wikipedia (optional: add a topic)", value="Displays random wikipedia page or chosen topic", inline=True)

    await message.channel.send(embed=embed)

async def handle_ping(message):
    embed=discord.Embed(title="Pong!", color=0x7272f0)

    await message.channel.send(embed=embed)

async def handle_hello(message):
    embed=discord.Embed(title="Hello!", description="How are you feeling?", color=0x7272f0)
    embed.add_field(name="1", value="Great", inline=True)
    embed.add_field(name="2", value="Sad", inline=True)
    embed.add_field(name="3", value="Okay", inline=True)
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
        embed=discord.Embed(title="Yay!", description='Here, have a sticker: :' + random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

        await message.channel.send(embed=embed)

        WandyBotClass.waiting_for_answer = 0
        WandyBotClass.sticker_count += 1

    if message.content.startswith('2'):
        embed=discord.Embed(title="Here, this will cheer you up.", description=f"(You have received a letter! open it with {prefix} open letter)", color=0x7272f0)

        await message.channel.send(embed=embed)

        WandyBotClass.letter_received = 1 
        WandyBotClass.waiting_for_answer = 0

    if message.content.startswith('3'):
        embed=discord.Embed(title="Nice! I hope your normal is good!", description='Here, have a sticker: :' + random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)

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
            embed=discord.Embed(title="You were correct!", description='Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':', color=0x7272f0)
            
            await message.channel.send(embed=embed)
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


async def handle_date(message):
    today = date.today()
    embed=discord.Embed(title="Today's date: " + str(today), color=0x7272f0)

    await message.channel.send(embed=embed)


async def handle_prefix(message):
    embed=discord.Embed(title=f"The Wandy84-Bot prefix is {prefix}. Type {prefix} help for a command list.", color=0x7272f0)

    await message.channel.send(embed=embed)

async def handle_wikipedia(message, topic=None):
    if topic:
        query = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        response = requests.get(query)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string
            first_section = soup.find('div', {'class': 'mw-parser-output'}).find('p')
            
            text_content = ""
            while first_section and first_section.name != 'h2':
                text_content += first_section.get_text() + "\n"
                first_section = first_section.find_next_sibling()
            
            image_url = None
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                image_tag = infobox.find('img')
                if image_tag:
                    image_url = "https:" + image_tag['src']

            embed = discord.Embed(title=title, url=response.url, description=text_content[:2000], color=0x7272f0)
            if image_url:
                embed.set_image(url=image_url)
            embed.add_field(name=f"Open Wikipedia for more info", value="Some Wikipedia pages are older than others, so some topics may have errors or won't display correctly", inline=True)
            await message.channel.send(embed=embed)
            return
        
    query = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(query)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        first_section = soup.find('div', {'class': 'mw-parser-output'}).find('p')
        
        text_content = ""
        while first_section and first_section.name != 'h2':
            text_content += first_section.get_text() + "\n"
            first_section = first_section.find_next_sibling()
        
        image_url = None
        infobox = soup.find('table', {'class': 'infobox'})
        if infobox:
            image_tag = infobox.find('img')
            if image_tag:
                image_url = "https:" + image_tag['src']

        embed = discord.Embed(title=title, url=response.url, description=text_content[:2000], color=0x7272f0)
        if image_url:
            embed.set_image(url=image_url)
        embed.add_field(name="Open Wikipedia for more info", value="Some Wikipedia pages are older than others, so some topics may have errors or won't display correctly", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to fetch random Wikipedia article", color=0x7272f0)
        await message.channel.send(embed=embed)



@client.event
async def on_member_join(member):
    channel = client.get_guild(789869494709256214).get_channel(WandyBotClass.channel_id)

    print ('Recognised that a member called ' + member.name + ' joined')
    await channel.send('Welcome @' + member.name + ' to ' + member.guild.name + ' ! We hope you will enjoy your stay!')
    if member.name == ('{0.user}'):
        await channel.send(f'Thank you for inviting Wandy84-Bot to your server! Wandy84-Bots prefix is {prefix}. For a list of commands do {prefix} help.')

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

    elif message.content.startswith(f'{prefix} help'):
        await handle_help(message)

    elif message.content.startswith(f'{prefix} hello'):
        await handle_hello(message)

    elif WandyBotClass.waiting_for_answer == 1:
        await handle_answers(message)

    elif WandyBotClass.playing_true == 1:
        await handle_playing_true(message)

    elif message.content.startswith(f'{prefix} open letter'):
        await handle_open_letter(message)
  
    elif message.content.startswith(f'{prefix} stickers'):
        await handle_stickers_count(message)

    elif message.content.startswith(f'{prefix} ping'):
        await handle_ping(message)

    elif message.content.startswith(f'{prefix} play'):
        await handle_play(message)

    elif message.content.startswith(f'{prefix} roll a die'):
        await handle_roll_dice(message)

    elif message.content.startswith(f'{prefix} server count'):
        await handle_server_count(message)

    elif message.content.startswith(f'{prefix} server stats'):
        await handle_server_stats(message)
    
    elif message.content.startswith(f'{prefix} weather'):
        await WandyWeatherBotClass.handle_weather(message)
        city = message.content[slice(11, len(message.content))].lower()
        result = get_weather(city)
        await message.channel.send(embed=result)
    
    elif message.content.startswith(f'{prefix} date'):
        await handle_date(message)

    elif message.content.startswith('Wandy84-Bot prefix'):
        await handle_prefix(message)

    elif message.content.startswith(f'{prefix} wikipedia'):
        parts = message.content.split(' ', 2)
        
        if len(parts) == 2:
            await handle_wikipedia(message)
        elif len(parts) == 3:
            await handle_wikipedia(message, parts[2])

    elif message.content.startswith(prefix):
        embed=discord.Embed(title=f"Not a command, to see commands use {prefix} help.", color=0x7272f0)
        await message.channel.send(embed=embed)

try: 
    client.run(TOKEN)
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
