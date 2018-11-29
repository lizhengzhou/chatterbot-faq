from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 定义机器人
chatbot = ChatBot('Lili')

# 设置训练器
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 按自定义预料库训练
chatbot.train("./data/")

while True:
    print(chatbot.get_response(input("user:")))

