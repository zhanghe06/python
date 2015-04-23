# encoding: utf-8
__author__ = 'zhanghe'

from Queue import Queue
import random
import threading
import time


class Producer(threading.Thread):
    """
    Producer thread
    """
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print "%s: %s is producing %d to the queue!" % (time.ctime(), self.getName(), i)
            self.data.put(i)
            time.sleep(random.randrange(10) / 5)
        print "%s: %s finished!" % (time.ctime(), self.getName())


class Consumer(threading.Thread):
    """
    Consumer thread
    """
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print "%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(), self.getName(), val)
            time.sleep(random.randrange(10))
        print "%s: %s finished!" % (time.ctime(), self.getName())


def main():
    """
    Main thread
    :return:
    """
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print 'All threads terminate!'


if __name__ == '__main__':
    main()

# 本程序是比较经典的生产者和消费者模型，运行结果：
# Fri Apr 24 00:05:42 2015: Pro. is producing 0 to the queue!
# Fri Apr 24 00:05:42 2015: Con. is consuming. 0 in the queue is consumed!
# Fri Apr 24 00:05:43 2015: Pro. is producing 1 to the queue!
# Fri Apr 24 00:05:43 2015: Con. is consuming. 1 in the queue is consumed!
# Fri Apr 24 00:05:44 2015: Pro. is producing 2 to the queue!
# Fri Apr 24 00:05:45 2015: Pro. is producing 3 to the queue!
# Fri Apr 24 00:05:46 2015: Pro. is producing 4 to the queue!
# Fri Apr 24 00:05:47 2015: Pro. finished!
# Fri Apr 24 00:05:51 2015: Con. is consuming. 2 in the queue is consumed!
# Fri Apr 24 00:05:53 2015: Con. is consuming. 3 in the queue is consumed!
# Fri Apr 24 00:05:53 2015: Con. is consuming. 4 in the queue is consumed!
# Fri Apr 24 00:06:02 2015: Con. finished!
# All threads terminate!