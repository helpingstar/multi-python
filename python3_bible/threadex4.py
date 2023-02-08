# threadex4.py
"""
생산자/소비자 문제
생산자는 정보를 생산하여 버퍼에 보관하고, 소비자는 생산된 정보를 가져간다.
소비자는 생산된 정보가 있을 경우에만 정보를 가져가고, 정보가 없으면 대기한다.
"""
import threading, time
import random

NP_CONSUMER = 10                # 소비자 프로세스의 수
NP_PRODUCER = NP_CONSUMER // 2  # 생산자 프로세스의 수

buffer = []                     # 공유 버퍼
cv = threading.Condition()      # 조건 변수 생성

# 소비자
class Consumer(threading.Thread):
    def run(self):
        for x in range(5):      # 한 소비자는 5개의 정보를 소비한다.
            cv.acquire()
            while len(buffer) < 1:  # 정보가 없으면
                print('waiting..')
                cv.wait()           # 대기한다.
            print(buffer.pop(0))    # 정보를 소비한다.
            cv.release()
            time.sleep(0.01)        # 잠시 대기한다.

# 생산자
class Producer(threading.Thread):
    def run(self):
        for x in range(10):
            cv.acquire()
            buffer.append(random.randrange(0, 20))  # 정보를 생산한다.
            cv.notify()             # 대기 중인 소비자에게 알린다.
            cv.release()
            time.sleep(0.02)        # 잠시 대기한다.

con = []    # 소비자 스레드 리스트
pro = []    # 생산자 스레드 리스트

for i in range(NP_CONSUMER):
    con.append(Consumer())  # 소비자 스레드 생성

for i in range(NP_PRODUCER):
    pro.append(Producer())  # 생산자 스레드 생성

for th in con:
    th.start()            # 소비자 스레드를 먼저 시작한다.

for th in pro:
    th.start()          # 생산자 스레드를 시작한다.

for th in con:
    th.join()           # 소비자 스레드가 종료될 때까지 대기한다.

for th in pro:
    th.join()           # 생산자 스레드가 종료될 때까지 대기한다.

print('Exiting')
