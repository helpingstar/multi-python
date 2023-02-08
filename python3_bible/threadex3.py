# threadex3.py

import threading

g_count = 0

class MyThread(threading.Thread):
    def run(self):
        global g_count
        for i in range(10):
            lock.acquire()  # 록을 얻는다. 다른 스레드의 acquire() 메서드는 록을 얻을 수 있을 때까지 대기한다.
            g_count += 1    # 배타적으로 실행권을 얻어서 처리하고
            lock.release()  # 록을 해제한다. 만일 acquire() 메서드로 대기중인 스레드가 있으면 이들 스레드 중 하나만 대기에서 벗어난다.

lock = threading.Lock()
threads = []

for i in range(10):
    th = MyThread()         # 스레드 객체를 얻고
    th.start()              # 스레드를 시작한다.
    threads.append(th)      # 스레드 종료를 검사하기 위해 리스트에 잠시 저장한다.

for th in threads:
    th.join()
print('Exiting', g_count)
