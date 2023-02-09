# process05.py

from multiprocessing import Process, Value, Array

def change(v, a):
    v.value = 3.14
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    v = Value('d', 0.0)
    a = Array('i', range(5))

    p = Process(target=change, args=(v, a))
    p.start()
    p.join()

    print(v.value)      # 3.14
    print(a[:])         # [-0, -1, -2, -3, -4]
