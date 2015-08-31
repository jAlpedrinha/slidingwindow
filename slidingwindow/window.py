from multiprocessing import Queue, Pool
import sys, os


def callback_wrapper(queue,callback,task):
    def new_func(*args,**kwargs):
        print "will put args in queue",task
        callback(task)
        queue.put(task)
    return new_func


class SlidingWindow(object):
    def __init__(self, size, target, tasks, log_folder=None,task_finished=None):
        self.size = size
        self.task_finished = task_finished
        self.target = target
        self.tasks = tasks
        self.log_folder = log_folder
        self.queue = Queue()
        process_names = Queue()
        for i in range(size):
            process_names.put(i)
        self.pool = Pool(self.size, self.initializer, [process_names])
        for i in range(self.size):
            self.queue.put(None)

    def initializer(self,queue):
        if self.log_folder:
            id_ = queue.get()
            sys.stderr = open('{}/worker_{}.stderr.log'.format(self.log_folder, id_),'a')
            sys.stdout = open('{}/worker_{}.stdout.log'.format(self.log_folder, id_),'a')

    def start(self):
        for task in self.tasks:
            self.queue.get(block=True)
            try:
                self.pool.apply_async(self.target,task, callback=callback_wrapper(self.queue, self.task_finished, task))
            except Exception as e:
                print e

        for i in range(self.size):
            self.queue.get(block=True)
            
