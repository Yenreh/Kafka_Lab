from confluent_kafka import Consumer

# Kafka configuration
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest',  # Start reading from the beginning
}

def consume_messages(topic):
    consumer = Consumer(config)
    consumer.subscribe([topic])
    print(f"Subscribed to topic: {topic}")
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nStopping consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    topic_name = "univalle-ideas"  # Replace with your topic
    consume_messages(topic_name)
