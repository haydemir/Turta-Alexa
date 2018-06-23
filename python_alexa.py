
import time
import paho.mqtt.client as mqtt
# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--email", required=True,
	help="E-Mail of user")
args = vars(ap.parse_args())

e_mail = args['email']

client = mqtt.Client()
import ssl

import turta_py as turta

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(e_mail)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    command = str(msg.payload).encode("utf-8").split('/')[0]

    if command == "Weather":

        client.publish(str(e_mail) + '/', 'Response/' + str(msg.payload) + '/' + str(turta.getTemp()))
    else:
	relay = str(msg.payload).encode("utf-8").split('/')[2]
	state = str(msg.payload).encode("utf-8").split('/')[3]

	if state == "off":
		turta.relayCommand(relay,0)
	else:
		turta.relayCommand(relay,1)

        client.publish(str(e_mail) + '/', 'Response/' + str(msg.payload))



client.tls_set(ca_certs="turta_mqtt_ca.crt", certfile=str(e_mail) + ".crt", keyfile=str(e_mail) + ".key", cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
client.tls_insecure_set(False)
#client.username_pw_set("sammy","sammy")
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.28.44.93", 8883, 60)
#client.subscribe("temperature", qos=0)
#client.publish("temperature", "32")

#for i in range(1,38):
#    client.publish("temperature", i)
#    time.sleep(1)
client.loop_forever()

