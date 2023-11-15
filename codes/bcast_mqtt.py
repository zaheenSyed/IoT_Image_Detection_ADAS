import time
import paho.mqtt.client as mqtt


def bcast(msg):
    
    client = mqtt.Client("rpi_client2") #this name should be unique
    client.connect('127.0.0.1',1883)
    # start a new thread
    client.loop_start()
    
    try:
        msg =str(msg)
        pubMsg = client.publish(
            topic='rpi/broadcast',
            payload=msg.encode('utf-8'),
            qos=0,
        )
        pubMsg.wait_for_publish()
        time.sleep(1)
    except Exception as e:
        print(e)
    return