# process02.py

from multiprocessing import Process
import os

class MyProcess(Process):
    def __init__(self, n, m):
        Process.__init__(self)
        self.n = n
        self.m = m

    def run(self):
        print('pid=', os.getpid(), 'id(m)=', id(self.m))
        for i in range(self.n):
            print(f'id={os.getpid()} --> {i}')
            for k in range(self.m):     # 시간을 보내기 위한 코드
                pass

if __name__ == '__main__':
    p_list = []                     # 프로세스 객체를 저장할 리스트
    for i in range(2):              # 프로세스 객체 두 개를 생성한다.
        p = MyProcess(5, 100000)
        p.start()                   # 프로세스를 실행한다.
        p_list.append(p)            # 프로세스 객체를 리스트에 추가한다.

    for p in p_list:
        p.join()                    # 프로세스가 종료될 때까지 대기한다.

    print('Exiting')
