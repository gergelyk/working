from time import sleep
from working import working

def task_slave():
    for x in range(5):
        print(f'Slave: {x}')
        sleep(0.3)

    raise Exception('Error in slave') # __exit__ will re-raise it when master is done... or calls reraise()
        
    print('Slave is done!')

with working(task_slave) as job:
    for x in range(5):
        print(f'Master: {x}')
        sleep(1)
        job.reraise()
    
    print('Master is done!')
