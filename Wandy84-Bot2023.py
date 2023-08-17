import discord
from discord.ext import commands
import random

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
    # rolling_dice = 0
    chosen_word = ''
    # guild_count = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def handle_ping(message):
    await message.channel.send('Pong!')

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
        WandyBotClass.waiting_for_answer = 0

async def handle_stickers_count(message):
    await message.channel.send('You have ' + str(WandyBotClass.sticker_count) +' sticker(s)!')

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

async def handle_roll_dice(message):
    await message.channel.send('Rolling the dice...')
    await message.channel.send('The result was: ' + random.choice(WandyBotClass.random_dice) + '')

async def handle_server_count(message):
    await message.channel.send('Wandy84-Bot is in '+ (f' {len(client.guilds)} ') + ' servers!')

async def handle_server_stats(message):
    await message.channel.send(f'server name: {message.guild.name} Total members: {message.guild.member_count}')

@client.event
async def on_message(message):
    print(message.author, message.content, message.channel.id)

    if message.author == client.user:
        return

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

    elif message.content.startswith('wb'):
        await message.channel.send('Not a command, to see commands use wb help')

    elif message.content.startswith('wB'):
        await message.channel.send('Please use wb in lowercase letters if you wish to start a command.')

    elif message.content.startswith('WB'):
        await message.channel.send('Please use wb in lowercase letters if you wish to start a command.')

    elif message.content.startswith('Wb'):
        await message.channel.send('Please use wb in lowercase letters if you wish to start a command.')

client.run(TOKEN)
