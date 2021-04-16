import discord
import subprocess
import random
import requests, json
from datetime import date

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

class WandyBotClass:
    waiting_for_answer = 0
    letter_received = 0
    # sticker_received = 0
    sticker_count = 0
    good_emojis = ['heart', 'heart_decoration' , 'heartbeat' , 'smiley' , 'slight_smile' , 'sunglasses' , 'heart_eyes' , 'star_struck' , 'innocent' , 'partying_face']
    channel_id = 819980658486542366
    nick_answer = 0
    play_words = ['lheol', 'lapy', 'nsu', 'prttey', 'ycr']
    playing_true = 0
    user_admin = 0
    user_admin_accessing_true = 0
    admin_access = 0
    user_admin_in_progress = 0
    random_dice = ['1' , '2' , '3' , '4' , '5' , '6']
    # rolling_dice = 0
    chosen_word = ''
    # guild_count = 0

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

        embed=discord.Embed(title=f"{city}"' Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def handle_hello(message):
    # tmpstr = 'Got message' + message.content
    # print(tmpstr.format(client))
    # subprocess.call('c:\Program Files (x86)\Google\Chrome\Application\chrome.exe https://aternos.org/server/')
    await message.channel.send('Hello! How are you feeling? 1. okay 2. sad 3. normal (type in a number of your choice)')
    WandyBotClass.waiting_for_answer = 1

async def handle_open_letter(message):
    if WandyBotClass.letter_received == 1:
        await message.channel.send('(You opened the letter!)  Dear {0.author}, I hope you are feeling good today! Even if you are not feeling good, you can always chat with me! :heart:    -The Wandey84-Bot Team'.format(message))
        WandyBotClass.letter_received = 0
    else:
        await message.channel.send('You do not have a letter :(')

async def handle_answers(message):
    if message.content.startswith('1'):
        await message.channel.send('Oh, I am sorry to hear that, I hope that you will feel better. Here, have a sticker: :' + random.choice(WandyBotClass.good_emojis) + ':')
        WandyBotClass.waiting_for_answer = 0
        WandyBotClass.sticker_count += 1
    if message.content.startswith('2'):
        await message.channel.send('Here, this will cheer you up. (You have received a letter! open it with wb open letter)') 
        WandyBotClass.letter_received = 1 
        WandyBotClass.waiting_for_answer = 0
    if message.content.startswith('3'):
        await message.channel.send ('Good! I hope your normal is a good thing! :) If not, have a sticker: :' + random.choice(WandyBotClass.good_emojis) + ':') 
        WandyBotClass.sticker_count += 1


async def handle_help(message):
    await message.channel.send('Commands list: wb help , wb Help link , wb hello , wb stickers , wb open letter , wb time , wb server stats , wb nick bot , wb play , Wandy84-Bot prefix , wb Ping! , wb weather (the city you want to see the weather in) , wb roll dice , wb server count. For more information about each command, run the command wb Help link')


async def handle_stickers_count(message):
    await message.channel.send('You have ' + str(WandyBotClass.sticker_count) +' sticker(s)!')



async def handle_time(message):
    today = date.today()
    await message.channel.send("Today's date: " + str(today))

async def handle_help_link(message):
    await message.channel.send('this is currently under construction, does not work :(')

async def handle_server_stats(message):
    await message.channel.send(f'server name: {message.guild.name} Total members: {message.guild.member_count}')

async def handle_nick_bot(message):
    await message.channel.send('What do you want my nick to be? (write in chat the nick)')
    WandyBotClass.nick_answer = 1

async def handle_nick_answer(message):
    # await message.author.edit(nick=message.content)
    await client.user.edit(nick=message.content)
    WandyBotClass.nick_answer = 0


async def handle_play(message):
    WandyBotClass.chosen_word = random.choice(WandyBotClass.play_words)

    await message.channel.send('Unscramble the following word: ' + WandyBotClass.chosen_word + ' type in chat the answer and see if you were correct!')
    WandyBotClass.playing_true = 1


async def handle_playing_true(message):

    if WandyBotClass.chosen_word == 'lheol':
        if message.content.startswith('hello'):
            await message.channel.send('You were correct! Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':')
            WandyBotClass.sticker_count += 1
        else:
            await message.channel.send('You were not correct :(')

    if WandyBotClass.chosen_word == 'lapy':
        if message.content.startswith('play'):
            await message.channel.send('You were correct! Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':')
            WandyBotClass.sticker_count += 1

        else:
            await message.channel.send('You were not correct :(')

    if WandyBotClass.chosen_word == 'nsu':
        if message.content.startswith('sun'):
            await message.channel.send('You were correct! Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':')
            WandyBotClass.sticker_count += 1

        else:
            await message.channel.send('You were not correct :(')
    
    
    if WandyBotClass.chosen_word == 'prttey':
        if message.content.startswith('pretty'):
            await message.channel.send('You were correct! Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':')
            WandyBotClass.sticker_count += 1
        else:
            await message.channel.send('You were not correct :(')
    
    if WandyBotClass.chosen_word == 'ycr':
        if message.content.startswith('cry'):
            await message.channel.send('You were correct! Here, have a sticker! :'+ random.choice(WandyBotClass.good_emojis) + ':')
            WandyBotClass.sticker_count += 1
        else:
            await message.channel.send('You were not correct :(')

    WandyBotClass.playing_true = 0



async def handle_prefix(message):
    await message.channel.send('The Wandy84-Bot prefix is wb! (make sure when you type wb you must write it in lowercase letters!!!) Do wb help for more commands.')



async def handle_Ping(message):
    await message.channel.send('Pong!')


async def handle_notes(message):
    if (message.author) == ('WanderingPanda84'):
    
        await message.channel.send('To use this command, you must enter a password to proceed.')
    
    else:
        return
    WandyBotClass.user_admin_in_progress = 1


async def handle_notess(message):
    if message.content.startswith('***'):
        await message.channel.send('wb nick bot needs debugging. wb Help link does not work like its supposed to yet.')
    else:
        await message.channel.send('Your password is incorrect')
    WandyBotClass.user_admin_in_progress = 0

async def handle_roll_dice(message):
    await message.channel.send('Rolling the dice...')
    await message.channel.send('The result was: ' + random.choice(WandyBotClass.random_dice) + '')
    

async def handle_server_count(message):
    await message.channel.send('Wandy84-Bot is in '+ (f' {len(client.guilds)} ') + ' servers!')
        





@client.event
async def on_member_join(member):
    channel = client.get_channel(WandyBotClass.channel_id)

    print ('Recognised that a member called ' + member.name + ' joined')
    await channel.send('Welcome ' + member.name + ' to ' + member.guild.name + ' ! We hope you will enjoy your stay!')
    member.send_message('Welcome ' + member.name + ' to ' + member.guild.name + '! We hope you will enjoy your stay!')
    if member.name == ('{0.user}'):
        await channel.send('Thank you for inviting Wandy84-Bot to your server! Wandy84-Bots prefix is wb. For a list of commands do wb help.')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(WandyBotClass.channel_id)

    print ('Recognised that member called ' + member.name + ' left')
    await channel.send('Bye ' + member.name + ', we will miss you ')
    member.send_message('Bye ' + member.name)



@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('wb hello'):
        await handle_hello(message)
        
    elif WandyBotClass.nick_answer == 1:
        await handle_nick_answer(message)

    elif WandyBotClass.waiting_for_answer == 1:
        await handle_answers(message)

    elif WandyBotClass.user_admin_in_progress == 1:
        await handle_notess(message)

    elif WandyBotClass.playing_true == 1:
        await handle_playing_true(message)

    # elif WandyBotClass.rolling_dice == 1:
    #     await handle_dice_roll_results(message)

    elif message.content.startswith('wb open letter'):
        await handle_open_letter(message)
  
    elif message.content.startswith('wb stickers'):
        await handle_stickers_count(message)

    elif message.content.startswith('wb help'):
        await handle_help(message)
    
    elif message.content.startswith('wb time'):
        await handle_time(message)

    elif message.content.startswith('wb Help link'):
        await handle_help_link(message)
    
    elif message.content.startswith('wb server stats'):
        await handle_server_stats(message)

    elif message.content.startswith('wb nick bot'):
        await handle_nick_bot(message)

    elif message.content.startswith('wb play'):
        await handle_play(message)

    elif message.content.startswith('Wandy84-Bot prefix'):
        await handle_prefix(message)

    elif message.content.startswith('wb Ping!'):
        await handle_Ping(message)

    elif message.content.startswith('wb notes'):
        await handle_notes(message)

    elif message.content.startswith('wb weather'):
        await WandyWeatherBotClass.handle_weather(message)
        city = message.content[slice(11, len(message.content))].lower()
        result = get_weather(city)
        await message.channel.send(embed=result)

    elif message.content.startswith('wb roll dice'):
        await handle_roll_dice(message)

    elif message.content.startswith('wb server count'):
        await handle_server_count(message)

    elif message.content.startswith('wb'):
        await message.channel.send('Not a command')

    elif message.content.startswith('WB'):
        await message.channel.send('Please use wb in lowercase letters if you wish to start a command.')

    elif message.content.startswith('Wb'):
        await message.channel.send('Please use wb in lowercase letters if you wish to start a command.')



client.run('ODE5ODExNTI0OTk0MTM4MTEy.YEsC-g.19S1tSyasO2Tq2tAaRnz4B9PQxU')