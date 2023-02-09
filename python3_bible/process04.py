# process04.py
"""
메인 프로세스 쓰기(p) : O, 읽기(q) : X
멀티 프로세스 쓰기(p) : X, 읽기(q) : O
"""
from multiprocessing import Process, Pipe

def reader(pipe):
    p, q = pipe
    p.close()   # 파이프 입력은 사용하지 않으므로 닫는다.
    while True:
        try:
            msg = q.recv()  # 파이프에서 데이터 항목을 읽는다.
            print(msg)
        except EOFError:
            break

def writer(p):
    for i in range(0, 1000):
        p.send(i)

if __name__ == '__main__':
    p, q = Pipe()
    reader_p = Process(target=reader, args=((p, q),))
    reader_p.start()    # 읽기 프로세스를 시작한다.

    q.close()           # 파이프 출력은 사용하지 않으므로 닫는다.
    writer(p)           # 메인 프로세스에서 항목을 생산한다.
    p.close()           # 데이터 생산이 끝났으므로 파이프를 닫는다.
    reader_p.join()
