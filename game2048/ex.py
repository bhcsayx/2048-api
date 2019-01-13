from multiprocessing import Pool
import time,os,random

def long_time_task(name):
    print('Run task %s (%s)....' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name,(end-start)))

print('Parent process %s' % (os.getpid()))
p=Pool(4)

for i in range(5):
    p.apply_async(long_time_task,args=(i,))
print('waiting all processes done')
p.close()
p.join()
print('all processes done')
