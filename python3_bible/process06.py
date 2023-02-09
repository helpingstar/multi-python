# process06.py
"""
리스트와 사전, 네임스페이스의 동작을 보여주는 간단한 예
"""
from multiprocessing import Process, Manager

def f(d, l, ns):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
    ns.x *= 10
    ns.y *= 10
    ns.stack.append(1)  # 주의
    ns.stack2.append(1)
    print('ns.stack=', ns.stack)    # 결과 확인

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    ns = manager.Namespace()
    ns.x = 1
    ns.y = 2
    ns.stack = []
    ns.stack2 = manager.list()

    p = Process(target=f, args=(d, l, ns))
    p.start()
    p.join()

    print('d=', d)
    print('l=', l)
    print(f'ns.x={ns.x}, ns.y={ns.y}, ns.stack={ns.stack}, ns.stack2={ns.stack2}')
