# process03.py
"""
생산자와 소비자 관계 구현

생산자 : 세 개의 데이터를 1초 간격으로 생산하고 세 개는 빠르게 생산한다.
소비자 : 0.5초 간격으로 생산되는 데이터를 소비한다.

만일 소비자가 3초 이내에 생산되는 데이터가 없으면 소비자 프로세스는 종료한다.
"""

from multiprocessing import Process, Queue
from multiprocessing import queues
import time

def producer(q):
    for k in range(3):          # 천천히 생산
        q.put(k)
        print('produced', k)
        time.sleep(1)
    for k in range(3, 6):       # 빠르게 생산
        q.put(k)
        print('produced', k)

def consumer(q):
    while True:
        try:
            ele = q.get(block=True, timeout=3)
            print('consumed', ele)
            time.sleep(0.5)
        except queues.Empty:
            break
    q.close()

if __name__ == '__main__':
    q = Queue()
    con_p = Process(target=producer, args=(q,))
    con_p.start()
    producer(q)                 # 생산자는 메인 프로세스에서 실행
    con_p.join()
