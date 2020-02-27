from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

 
import logging
logging.basicConfig(level=logging.INFO)
#creating a new chatbot



#bot = ChatBot(
#	'Norman',
#
#	storage_adapter='chatterbot.storage.SQLStorageAdapter',
#	logic_adapters=[
#		'chatterbot.logic.MathematicalEvaluation',
#		'chatterbot.logic.TimeLogicAdapter',
#		'chatterbot.logic.BestMatch'
#	],
#	database_uri='sqlite:///database.db'
	#response_selection_method= get_most_frequent_response
#)

bot = ChatBot( #Creates Chat Bot
    'Charlie',
    trainer='chatterbot.trainers.ListTrainer',
    logic_adapters=[
        {
           'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

#trainerOne = ChatterBotCorpusTrainer(bot)

#trainerOne.train(
#    "chatterbot.corpus.english",
#    "chatterbot.corpus.english.greetings",
#    "chatterbot.corpus.english.conversations"
#)

trainer = ListTrainer(bot)

#Listed Training Data

trainer.train([
    'Why do people still play video games or games?',
    'Gaming puts people in a world with new possibilities',
    'Its an escape?',
    'Yes, an escape from reality',
])

trainer.train([
    'What do you want me to cook for dinner?',
    'Steak and Mashed Potatoes?',
    'Ok, anything else?',
    'Ice cream for dessert?',
    'Chocolate and Vanilla!',
])

trainer.train([
    'Whats the purpose of life?',
    'Im not sure, but I dont believe everything needs a purpose',
    'Why not?',
    'As humans we try to give everything purpose',
])

trainer.train([
    'What do you like to do?',
    'I like to read, program, and excercise, What about you?'
    'I like to play video games and make art',
    'What kind of art do you create?',
    'My art is surrealistic, I like to draw abnormal and obscure drawings.',
    'That sounds awesome.',
    'What kind of programs do you make?',
    'I program games and apps, and I really enjoy it.',
])

trainer.train([
    'Im really bored',
    'Look for something to do. Maybe read a book or play a game',
    'That is a great idea, Thank you',
    'No problem, Youre Welcome',
])

trainer.train([#make sure conversations are clear and concise and dont add any external variables like excuse me, etc.
    'Where can I find the train station?',
    'Which train station?',
    'nameOfTrainStation Station',
    'Its located in directions',
])

trainer.train([
    'Want to hang out later?',
    'Yeah, sounds good',
    'What do you want to eat?',
    'Anything, but I like tacos',
    'Ok lets eat tacos',
])

trainer.train([
    'Who are you?',
    'I am me',
    'Whats your last name?',
    'My Family name?',
    'Yes',
])

trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])
trainer.train([
    'Hi',
    'Hello',
    'Whatsup?',
    'Nothing much!',
    'Thats cool',
])

trainer.train([
    'Whats your favorite movie?',
    'I like Taxi Driver with Robert Deniro',
    'Whats your favorite food?',
    'My favorite food is French toast and Sushi',
    'Whats your favorite book',
    'I really enjoyed Meditations by Marcus Aurelius',
    'Whats your favorite flavor?',
    'My favorite flavor is Pineapple.',
    'Whats your favorite video game?',
    'My favorite video game is Dark Souls',
])

print('Ask or respond: ')

while True:
	try:
		userInput = input()
		botResponse = bot.get_response(userInput)
		#trainer.train(userInput)
		print(botResponse)

	except(KeyboardInterrupt, EOFError, SystemExit):
		break


