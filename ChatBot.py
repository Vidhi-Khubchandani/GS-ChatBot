from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot("GS-ChatBot")
trainer = ChatterBotCorpusTrainer(chatBot)

trainer.train("data\\data.yml")

print("Hi, I am Chitti the robot")

while True:
    query = input(">>>")
    print(chatBot.get_response(Statement(text=query, search_text=query)))
