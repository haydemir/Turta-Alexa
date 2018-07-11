
import time
import paho.mqtt.client as mqtt
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--email", required=True,
	help="E-Mail of user")
args = vars(ap.parse_args())

e_mail = args['email']

client = mqtt.Client()
import ssl


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(e_mail)

def on_message(client, userdata, msg):
    command = str(msg.payload).encode("utf-8").split('/')[0]

    if command == "Weather":

        print("Weather command received. 35 degree responded")
        client.publish(str(e_mail) + '/', 'Response/' + str(msg.payload) + '/' + str(35))
    else:
	relay = str(msg.payload).encode("utf-8").split('/')[2]
	state = str(msg.payload).encode("utf-8").split('/')[3]

	if state == "off":
		print("Relay " + relay + " is OFF")
	else:
		print("Relay " + relay + " is ON")

        client.publish(str(e_mail) + '/', 'Response/' + str(msg.payload))



client.tls_set(ca_certs="turta_mqtt_ca.crt", certfile=str(e_mail) + ".crt", keyfile=str(e_mail) + ".key", cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
client.tls_insecure_set(False)
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.28.44.93", 8883, 60)

client.loop_forever()
