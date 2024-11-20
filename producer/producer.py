from confluent_kafka import Producer

# Kafka configuration
config = {
    'bootstrap.servers': 'localhost:9092',
}

def delivery_report(err, msg):
    """Delivery report callback called for each message produced."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_messages(topic):
    producer = Producer(config)
    try:
        for i in range(10):  # Producing 10 messages as a demo
            value = f"Test message {i}"
            producer.produce(topic, value.encode('utf-8'), callback=delivery_report)
            producer.flush()  # Ensure all messages are sent
        print("All messages produced!")
    except Exception as e:
        print(f"Error producing messages: {e}")

if __name__ == "__main__":
    topic_name = "univalle-ideas"  # Replace with your topic
    produce_messages(topic_name)
