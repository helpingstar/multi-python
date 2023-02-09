# process10.py
from multiprocessing.connection import Client

address = ('localhost', 6000)

def client(msg):
    conn = Client(address, authkey=b'mypassword')
    conn.send(msg)
    print(conn.recv())
    print(conn.recv_bytes())
    conn.close()

if __name__ == '__main__':
    client({'one': 1, 'two': 2})
    client((2, 3, 4))
    client(False)
