import time
class TrafficLight:
    __color = 'red'

    def running(self):
        n = 0
        while n != 3:
            TrafficLight.__color = 'red'
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'yellow'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'green'
            print(TrafficLight.__color)
            time.sleep(4)
            n += 1

t = TrafficLight
t.running('')
