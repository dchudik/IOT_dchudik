import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

topics = { 'move':'home/move', 'temperature':'home/temperature' }


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.wait_for_edge(14,GPIO.BOTH)

if __name__ == "__main__":

    last_state = 0
    publish.single(topics['move'], "0", hostname="192.168.1.9")

    while True:
        state = GPIO.input(14)
        if state == last_state:
            None
        if state != last_state:
            publish.single(topics['move'], state, hostname="192.168.1.9")
        last_state = state
        time.sleep(8)



    client = mqtt.Client()
    
    client.connect("192.168.1.9", 1883, 60)
    
    client.loop_forever()