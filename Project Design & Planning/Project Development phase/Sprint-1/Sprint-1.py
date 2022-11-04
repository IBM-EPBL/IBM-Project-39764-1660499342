import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "b31tni",
        "typeId": "print1",
        "deviceId":"printid"
    },
    "auth": {
        "token": "z?7tcRfcekcO08R6f2"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    o2=random.randint(0,100)
    othergas=random.randint(0,100)
    limit=50
    if(othergas > limit):
        print("Alert the gas is leaked")
    else:
        pass
    myData={'oxygen':o2, 'other gas':othergas}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
