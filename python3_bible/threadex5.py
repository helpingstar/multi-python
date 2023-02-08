# threadex5.py

import threading

sem = threading.Semaphore(3)    # 세마포어 객체 생성

class RestrictedArea(threading.Thread):
    def run(self):
        for x in range(500):
            # 필요한 처리가 있으면 한다.
            sem.acquire()
            # 임계 영역 안에서 수행할 작업
            sem.release()
            # 필요한 처리가 있으면 한다.
thlist = []

# 100개의 스레드를 생성한다.
for i in range(100):
    thlist.append(RestrictedArea())

for th in thlist:
    th.start()  # 스레드를 시작한다.

for th in thlist:
    th.join()   # 스레드가 종료될 때까지 기다린다.

print('Exiting')
