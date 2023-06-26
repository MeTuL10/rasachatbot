from kafka import KafkaProducer

# Define server with port
bootstrap_servers = ['pkc-7prvp.centralindia.azure.confluent.cloud:9092']

# Define topic name where the message will publish
topicName = 'topic_0'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# Publish text in defined topic
producer.send(topicName, b'Hello from kafka...')

# Print message
print("Message Sent")