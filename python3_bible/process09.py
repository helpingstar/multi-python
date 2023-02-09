# process09.py
"""
서버측 코드, 소켓 객체를 생성하고 외부로부터 접속을 기다린다.
접속 후에는 연결 객체를 통해 send(), send_bytes() 메서드 등으로 파이썬 객체를 보낼 수 있고,
recv(), recv_bytes() 메서드 등으로 보내진 파이썬 객체를 받을 수 있다.
"""
from multiprocessing.connection import Listener

address = ('localhost', 6000)

def server():
    listener = Listener(address, authkey=b'mypassword')
    print('listening..')
    from_client = True
    while from_client:
        conn = listener.accept()
        print('connection accepted from', listener.last_accepted)

        conn.send([1, 2, 3, 4])
        conn.send_bytes(b'hello')
        from_client = conn.recv()
        print(from_client)

        conn.close()
    listener.close()

if __name__ == '__main__':
    server()
