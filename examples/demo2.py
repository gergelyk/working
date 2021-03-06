from time import sleep
from working import working

def task_slave():
    for x in range(5):
        print(f'Slave: {x}')
        sleep(1)
        
    print('Slave is done!')

with working(task_slave) as job:
    for x in range(5):
        print(f'Master: {x}')
        sleep(0.3)
        
    job.join() # master waits for slave to finish
        
    print('Master is done!')
