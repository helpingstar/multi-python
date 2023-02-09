# process05.py

from multiprocessing import Process, Value, Array

def plus(v):
    for i in range(10000):
        v.value += 1
        # print(v.value)

def minus(v):
    for i in range(10000):
        v.value -= 1
        # print(v.value)

if __name__ == '__main__':
    v = Value('d', 0.0)

    p1 = Process(target=plus, args=(v,))
    p2 = Process(target=minus, args=(v,))

    p_list = [p1, p2]
    for p in p_list:
        p.start()

    for p in p_list:
        p.join()

    print(v.value)
"""
셋이 동시에 진행되며 결과는 0이 보장되지 않는다.
"""
