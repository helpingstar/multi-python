# threadex1.py
# Thread 클래스의 하위 클래스를 정의하지 않고 스레드를 생성한다.
# Thread 클래스의 생성자에 함수와 인수를 넘겨 스레드를 생성한다.

import threading, time

# 스레드로 실행할 함수를 정의한다.
def myThread(id):
    for i in range(10):
        print(f'{id} --> {i}')
        time.sleep(0)   # CPU를 양도한다.


threads = []            # 스레드 객체를 저장할 리스트를 생성한다.
for i in range(2):      # 스레드 두 개를 생성한다.
    th = threading.Thread(target = myThread, args = (i,))
    th.start()          # 스레드를 실행한다.
    threads.append(th)  # 스레드 객체를 리스트에 저장한다.

for th in threads:
    th.join()           # 스레드가 종료될 때까지 대기한다.
print('Existing')

"""
join()에 시간 정보를 넘기면 지정된 초 동안 프로세스 종료를 대기한다.

th.isAlive()는 스레드가 종료되었는지 확인한다.
"""
