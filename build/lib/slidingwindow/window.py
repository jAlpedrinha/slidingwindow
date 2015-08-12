from multiprocessing import Queue, Pool


def callback_wrapper(queue):
	def new_func(*args,**kwargs):
		queue.put(None)
	return new_func


class SlidingWindow(object):
	def __init__(self, size, target, tasks):
		self.size = 5
		self.target = target
		self.tasks = tasks
		self.queue = Queue()
		self.pool = Pool(processes = self.size)
		for i in range(self.size):
			self.queue.put(None)

	def start(self):
		for task in self.tasks:
			self.queue.get(block=True)
			self.pool.apply_async(self.target,task, callback=callback_wrapper(self.queue))

		for i in range(self.size):
			self.queue.get(block=True)
			
