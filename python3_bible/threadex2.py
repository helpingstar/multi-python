# threadex2.py
# 하위 클래스에서 run() 메서드를 재정의하여 스레드를 생성한다.
# start() 메서드를 호출하면 run() 메서드가 실행된다.

import threading, time

# Thread 클래스의 하위 클래스를 정의한다.
class MyThread(threading.Thread):
    def run(self):          # run() 메서드는 스레드가 실행할 코드를 갖는다.
        for i in range(10):
            print(f'id={self.name}-->{i} ')
            time.sleep(0)   # CPU를 양도한다.

threads = []

for i in range(2):
    th = MyThread()         # 스레드 객체를 얻고
    th.start()              # 스레드를 시작한다.
    threads.append(th)

for th in threads:
    th.join()               # 스레드 th가 종료될 때까지 기다린다.
print('Exiting')
