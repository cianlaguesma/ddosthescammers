import requests
import threading
import sys
from faker import Faker
url = 'https://dappsauthes.com/process.php'

faker = Faker()


threads = []

def do_thread():
    while (True):
        data = {
            'name': 'phrase',
            'recovery-phrase': 'simple scam amazing administrator twelve words secret recovery phase update restart notes',
            'submit': 'submit'
        }
        fakeWords = faker.words(12)
        listToStr = ' '.join([str(elem) for elem in fakeWords])
        data['recovery-phrase'] = listToStr
        # print(data['recovery-phrase'])
        response  = requests.post(url, data)
        print(response)
# do_thread()
for x in range (0,10):
    t = threading.Thread(target=do_thread)
    t.daemon = True
    threads.append(t)

for x in range(0,10):
    threads[x].start()

for x in range(0,10):
    threads[x].join()
