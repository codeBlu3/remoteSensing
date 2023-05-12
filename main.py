import dht
import time 
import machine

d = dht.DHT22(machine.Pin(0))
def measurePrint():
    d.measure()
    print(d.humidity())
    print(d.temperature())
'''
while True: 
    measurePrint()
    time.sleep(2.5)

'''
