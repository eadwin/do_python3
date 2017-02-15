#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager


#发送任务的队列：
task_queue = queue.Queue()

#接收结果的队列：
result_queue = queue.Queue()


# QueueManager inherited BaseManager
class QueueManager(BaseManager):
    pass


#regist Queue
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

#绑定端口5000，设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
#get Queue object from net

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,100)
    print('Put task %d...' % n)
    task.put(n)


print('Try 2 get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)


manager.shutdown()
print('master exit.')