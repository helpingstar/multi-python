# process01.py

from multiprocessing import Process
import os

# 프로세스로 실행할 함수를 정의한다.
def f(n, m):
    print('pid=', os.getpid(), 'id(m)=', id(m))
    for i in range(n):
        print(f'id={os.getpid()} --> {i}')
        for k in range(m):    # 시간을 보내기 위한 코드
            pass


if __name__ == '__main__':
    p_list = []         # 프로세스 객체를 저장할 리스트
    m = 100000
    for i in range(2):  # 프로세스 객체 두 개를 생성한다.
        p = Process(target=f, args=(5, m))
        p.start()           # 프로세스를 실행한다.
        p_list.append(p)    # 프로세스 객체를 리스트에 추가한다.

    for p in p_list:
        p.join()            # 프로세스가 종료될 때까지 대기한다.
    print('Exiting')

"""
`Process` 클래스가 프로세스를 생성하기 위하여 내부에서는 `fork()` 함수를 사용한다.
따라서 새로운 프로세스 객체를 생성할 때 전달되는 인수들은 전체가 복사되어 전달된다.
위의 예에서 두 프로세스로 전달된 값 100,000은 프로세스마다 다른 객체이다.
"""
