from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import sys
import io

# if 'cp65001' != sys.stdin.encoding != 'utf-8':
#     sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf8')
# if 'cp65001' != sys.stdout.encoding != 'utf-8':
#     sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# if 'cp65001' != sys.stderr.encoding != 'utf-8':
#     sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf8')

'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train(
    "./data/"
)


# Now let's get a response to a greeting
# print(chatbot.get_response('在？'))

lineCounter=1

while True:
    inputStr = input("(" + str(lineCounter) + ") user:")
    answer=chatbot.get_response(inputStr)
    print(answer)
    lineCounter += 1
