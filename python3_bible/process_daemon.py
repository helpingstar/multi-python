# process_daemon.py

from multiprocessing import current_process, Process
import logging
import multiprocessing
import time

def daemon():
    p = current_process()
    print('Starting:', p.name, p.pid)
    time.sleep(5)
    print('Exiting :', p.name, p.pid)

def non_daemon():
    p = current_process()
    print('Starting:', p.name, p.pid)
    print('Exiting :', p.name, p.pid)

if __name__ == '__main__':
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(logging.INFO)
    p = current_process()
    print('Starting:', p.name, p.pid)

    d = Process(name='daemon', target=daemon, daemon=True)
    n = Process(name='non-daemon', target=non_daemon)

    d.start()
    time.sleep(1)
    n.start()
