import aiml
import os

sessionId = 12345

os.chdir("./AIML/Corpus")

bot = aiml.Kernel()
if os.path.isfile('bot_brain.brn'):
    bot.bootstrap(brainFile = 'bot_brain.brn')
else:
    bot.bootstrap(learnFiles = 'startup.xml', commands = 'Chatbot')
    bot.saveBrain("bot_brain.brn")

def get_response(message_in):
    return bot.respond(message_in, sessionId)

def get_name():
    os.chdir("../..")
    return 'AIML_ChatBot'
