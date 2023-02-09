# process07.py
"""
Pool 함수를 이용해 네 개의 프로세스 풀을 만들고, 각 프로세스가 비동기적으로 각자의 연산(f)을 수행한다.
CPU에 4개의 코어가 있다면 4개의 프로세스가 각 코어에서 실행되고 결과가 출력된다.
즉 실행시간은 하나의 프로세스가 한 작업을 수행한 시간과 거의 같다.

apply_async() 메서드는 풀에서 하나의 작업 프로세스를 선택해 작업을 수행하고는 ApplyResult 객체를 즉시 반환한다(r1, r2, r3, r4).
연산이 종료되었는지는 r1.ready() 메서드로 파악할 수 있다.
r1.get(timeout=2)는 2초 이내에 결과가 나타나지 않으면 TimeoutError 예외를 발생시킨다.
r1.get()는 결과가 나타날 때까지 기다린다.
apply() 메서드는 풀에서 하나의 작업 프로세스를 선택해 작업을 수행하고 결과가 나타날 때까지 기다린다.
map() 메서드는 풀에서 모든 작업 프로세스를 선택해 작업을 수행하고 결과가 나타날 때까지 기다린다.(병렬형)
"""
from multiprocessing import Pool

def f(x):
    for k in range(10**7):
        pass
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool:     # start 4 worker processes
        r1 = pool.apply_async(f, (10,))
        r2 = pool.apply_async(f, (20,))
        r3 = pool.apply_async(f, (30,))
        r4 = pool.apply_async(f, (40,))

        print(r1.get(timeout=2))
        print(r2.get(timeout=2))
        print(r3.get(timeout=2))
        print(r4.get(timeout=2))
