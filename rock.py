from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import discord
import asyncio

import logging
import codecs

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = ChatBot('Test', 
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
	database='Rockeira',
	logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
	database_uri='URI MONGODB'
	)

# If you do not use MongoDB:
#bot = ChatBot('Test') 

#bot.train('chatterbot.corpus.portuguese')

client = discord.Client()

#bot.set_trainer(ListTrainer)
#train = codecs.open('basico.txt', 'r', 'utf-8')
#conv = train.readlines()
#bot.train(conv)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	counter = 0
	if message.content.startswith('reboot-navi'):
		exit()

	#while True:
	if message.author != client.user: 
		if counter > 10:
			await asyncio.sleep(10)
			counter = 0

		quest = message.content
		print('>>> Human:', quest)
		response = bot.get_response(quest)
	if float(response.confidence) > 0.5:
		print('>>> Bot:', response)
		await client.send_message(message.channel, str(response))
		counter += 1
	else:
		pass

client.run('YOUR DISCORD TOKEN')