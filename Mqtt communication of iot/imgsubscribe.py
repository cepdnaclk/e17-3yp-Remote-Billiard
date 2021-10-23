import time 
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import uuid
import base64
import json
def resignal (self,dontcare,data):
	print("\nRecieving data from AWS IoT core\n")
	print("\nTopic: "+ data.topic)
	#print("Data: ", (data.payload))
	#print(type(data.payload))
	data1 = json.loads(data.payload)
	#f = open('receive.jpg','w')
	#f.write(data.payload)
	#f.close()
	print("\nSenders ID: "+data1["client_ID"])
	bytes = data1["image1"].encode('utf-8')
	with open('recieved.png', 'wb') as file_to_save:
		decoded_image_data = base64.standard_b64decode(bytes)
		file_to_save.write(decoded_image_data)
		print("Image received")


myMQTTClient = AWSIoTMQTTClient(str(uuid.uuid1()))
myMQTTClient.configureEndpoint("alses9dufe5nu-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("certificates/root.pem", "certificates/private.pem.key", "certificates/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

myMQTTClient.subscribe("billiard/device1",1,resignal)

while True:
    time.sleep(5)