import time
import AIML.ChatBot as chatbot

def init():
    
    chatbot.init()

    print('####################')
    print('Use: ' + chatbot.get_name())
    print('\'exit\' to exit.')

    timeStruct = time.localtime(time.time())
    strTime = time.strftime('%Y-%m-%d-%H-%M-%S', timeStruct)
    
    global logname
    logname = './log/log' + strTime + '.txt'
    with open(logname, 'a') as f:
        f.write('Use: ' + chatbot.get_name())

def writelog(message):
    info = message + '\n'
    with open(logname, 'a') as f:
        f.write(info)

'''Main'''
init()
while True:
    q = input('> ')
    writelog('> ' + q)
    if q == "exit":
        print("Exit......")
        exit()
    else:
        a = chatbot.get_response(q)
        print(a)
        writelog(a)
