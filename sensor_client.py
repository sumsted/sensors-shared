import json
import mmap
import contextlib
import time

with open('ultrasonic_sensors.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        while True:
            m.seek(0)
            print('\nreading...')
            sensors_json = m.readline().decode("utf-8") # read from memory and convert to string
            print(sensors_json)

            try:
                sensors = json.loads(sensors_json) #convert json string to object
            except Exception as e:
                print("exception %s"% str(e))
                # could get exception if data in memory not fully formed
                # pass on this exception and keep processing using last read data

            print('front: %(front)s\nleft: %(left)s\nright: %(right)s\n' % sensors)
            time.sleep(.1)
