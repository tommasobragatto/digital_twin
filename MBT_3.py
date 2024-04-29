import json
import paho.mqtt.client as mqtt
import time

def MBT_3():
    # MQTT broker details
    broker_address = "185.131.248.7"
    broker_port = 1883
    username = "wisegrid"
    password = "wisegrid"

    # Topic to subscribe to
    topic = "MBT/MBT3/meas/full/#" #TO BE CHANGED!!!!!!!!!!!!######################

    # File to save the received JSON data
    output_file = "received_3.json" #TO BE CHANGED!!!!!!!!!!!!!!!######################

    # Waiting time in seconds
    waiting_time = 60  # Adjust this to the desired waiting time

    # Callback when a connection is established
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribe to the specified topic
        client.subscribe(topic)

    # Callback when a message is received from the subscribed topic
    def on_message(client, userdata, msg):
        print("Received message from topic {}: {}".format(msg.topic, str(msg.payload)))
        # Save the raw binary data to a file
        with open(output_file, 'wb') as file:
            file.write(msg.payload)
        print("Data saved to {}".format(output_file))    
        
    # Callback when the script is about to disconnect
    def on_disconnect(client, userdata, rc):
        print("Disconnected from the broker")
        client.loop_stop()

    # Create an MQTT client instance
    client = mqtt.Client()

    # Set the username and password for the broker
    client.username_pw_set(username, password)

    # Set callback functions
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    # Connect to the broker
    client.connect(broker_address, broker_port, 60)

    # Loop to handle network events
    client.loop_start()

    # Wait for the specified duration
    time.sleep(waiting_time)

    # Disconnect from the broker after the waiting time
    client.disconnect()
