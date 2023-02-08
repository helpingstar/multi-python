# threadex7.py
"""
크기가 10인 큐를 이용하여 10개의 소비자 스레드와 5개의 생산자 스레드가 정보를 생산하고 소비하는 생산자/소비자 문제 프로그램
threadex4.py와 동일하다. 이 방법이 더 명료하다
"""

import threading
import time
import random
from queue import Queue

NP_CONSUMER = 10                # 소비자 스레드의 수
NP_PRODUCER = NP_CONSUMER // 2  # 생산자 스레드의 수

que = Queue(10)                 # 큐 객체 생성

class Consumer(threading.Thread):
    def run(self):
        for i in range(5):
            print(que.get())
            time.sleep(0.00)

class Producer(threading.Thread):
    def run(self):
        for i in range(10):
            que.put(random.randint(0, 20))
            time.sleep(0.00)

con = []
pro = []

for i in range(NP_CONSUMER):
    con.append(Consumer())

for i in range(NP_PRODUCER):
    pro.append(Producer())

for th in con:
    th.start()

for th in pro:
    th.start()

for th in con:
    th.join()

for th in pro:
    th.join()

print('Exiting')
