import requests
import threading
from faker import Faker
url = 'https://dappsauthes.com/process.php'

fake = Faker()



threads = []

def do_thread():
    while (True):
        data = {
            'name': 'phrase',
            'recovery-phrase': 'simple scam amazing administrator twelve words secret recovery phase update restart notes',
            'submit': 'submit'
        }
        data['recovery-phrase'] = "{} {} {} {}".format(fake.bs(),fake.bs(),fake.bs(),fake.bs()) 
        # print(data['recovery-phrase'])
        response  = requests.post(url, data)
        print(response)
for x in range (0,10):
    t = threading.Thread(target=do_thread)
    t.daemon = True
    threads.append(t)

for x in range(0,10):
    threads[x].start()

for x in range(0,10):
    threads[x].join()