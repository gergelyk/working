from time import sleep
from working import working

def task_slave():
    for x in range(5):
        print(f'Slave: {x}')
        sleep(1)
        
    print('Slave is done!')

with working(task_slave):
    for x in range(5):
        print(f'Master: {x}')
        sleep(0.3)
        
    print('Master is done!')
