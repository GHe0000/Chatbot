import time
import AIML.Chatbot as chatbot

def writelog(message):
    logname = './log/log' + strTime + '.txt'
    info = message + '\n'
    with open(logname, 'a') as f:
        f.write(info)

'''Main'''
now = time.time()
timeStruct = time.localtime(now) 
strTime = time.strftime('%Y-%m-%d-%H-%M-%S', timeStruct) 

print('####################')
print('Use:' + chatbot.get_name())
print('\'exit\' to exit.')

while True:
    q = input('> ')
    writelog('> ' + q)
    if q == "exit":
        print("Save Log......")
        exit()
    else:
        a = chatbot.get_response(q)
        print(a)
        writelog(a)
