# process08.py
from multiprocessing import Pool

"""
Pool 함수를 이용해 네 개의 프로세스 풀을 만들고, 각 프로세스가 비동기적으로 각자의 연산(f)을 수행한다.
4개의 프로세스 풀에서 사용 가능한 프로세스에 차례로 f함수를 수행할 것을 요청한다.

map_async() 메서드는 map() 함수와 같으나 결과 객체를 즉시 반환한다.
ready() 메서드를 통해 연산이 끝났는지 알 수 있으며 get() 메서드를 통해서 결과를 얻어낸다.
"""

def f(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool:     # start 4 worker processes
        print(pool.map(f, range(10)))   # prints "[0, 1, 4,..., 81]"
