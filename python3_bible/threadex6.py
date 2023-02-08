# threadex6.py
"""
하나는 뭔가를 준비하는 스레드(T1)
나머지는 준비된 환경에서 실행하는 스레드
"""
import threading

eve = threading.Event()

class PrepareThread(threading.Thread):
    def run(self):
        # 뭔가를 준비하고, 준비되었음을 알린다.
        eve.set()   # 이벤트를 설정한다.
        print('ready')

class ActionThread(threading.Thread):
    def run(self):
        # 앞에서 처리할 코드가 있다면 추가한다.
        print(self.name, 'waiting..')
        # PrepareThread 객체가 준비를 마칠 때까지 기다린다.
        eve.wait()
        # 본격적인 작업은 여기에 기술한다.
        print(self.name, 'done')

thlist = []
for i in range(5):
    thlist.append(ActionThread())

for th in thlist:
    th.start()

PrepareThread().start()

for th in thlist:
    th.join()

print('Exiting')
