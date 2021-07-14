import time 
import sys
import ibmiotf.application
import ibmiotf.device
import random
import wiotp.sdk.device


#Provide your IBM Watson Login Credentials

myConfig = { 
    "identity": {
        "orgId": "orm4ns",
        "typeId": "motors",
        "deviceId":"1271"
    },
    "auth": {
        "token": "12345678"
    }
}


def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])

    i=cmd.data['command']
    if i=='motoron':
        print("Motor is on")
    elif i=='motoroff':
        print("Motor is off")
    elif i=='lighton':
        print("Light is on")
    elif i=='lightoff':
        print("Light is off")

    
#Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    #Send Temperature,Humidity,Vibration,Current value to IBM Watson
    temperature=random.randint(30,80)
    humidity=random.randint(10,40)
    vibration=random.randint(50,100)
    current=random.randint(5,30)
    myData={'d':{'temperature' : temperature,'humidity': humidity, 'vibration':vibration, 'current':current}}
    #printing data

    print("Published Temperature = %s C" %temperature, "Humidity = %s %%" %humidity, "Vibration = %s HZ" %vibration, "Current = %s AMP" %current)
 
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()      
    
   
