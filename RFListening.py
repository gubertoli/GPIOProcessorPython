from datetime import datetime
import matplotlib.pyplot as pyplot
from GPIOProcessor import GPIOProcessor
import time

RECEIVED_SIGNAL = [[], []]
MAX_DURATION = 5 

if __name__ == '__main__':
    GP = GPIOProcessor()
    x = GP.getPin23()
    x.setDirection("in")
    cumulative_time = 0
    beginning_time = datetime.now()
    print '**Started recording**'
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        data = x.getValue()
        data = int(data.replace('\n',''))
        RECEIVED_SIGNAL[1].append(data)
        cumulative_time = time_delta.seconds
    print '**Ended Recording**'
    print len(RECEIVED_SIGNAL[0]), 'samples recorded'
    x.out()
    
    GP.cleanup()
    
    print '**Processing Results**'

    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds/1000000.0

    print '**Plotting results**'

    pyplot.plot(RECEIVED_SIGNAL[0],RECEIVED_SIGNAL[1])
    pyplot.axis([0, MAX_DURATION, -1, 2])
    pyplot.show()
