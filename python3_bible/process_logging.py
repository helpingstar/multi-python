# process_logging.py

import logging
import multiprocessing
import time

def f():
    print('doing some work..')

if __name__ == '__main__':
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(logging.INFO)

    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    n = multiprocessing.Process(name='child process', target=f)
    n.start()
