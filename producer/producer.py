from confluent_kafka import Producer

# Kafka configuration
config = {
    'bootstrap.servers': 'kafka-broker-1:9092',
}

def delivery_report(err, msg):
    """Delivery report callback called for each message produced."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_messages(topics, messages):
    producer = Producer(config)
    try:
        # Check topics and create messages depending on the topic
        for message in messages:
            topic = message["topic"]
            if topic not in topics:
                print(f"Invalid topic: {topic}")
                continue
            producer.produce(topic, value=message["value"].encode('utf-8'), callback=delivery_report)
            producer.flush()
    except Exception as e:
        print(f"Error producing messages: {e}")

if __name__ == "__main__":
    topics = ["univalle-ideas", "cosas-misteriosas"]
    messages = [
        {"value": "Idea 1", "topic": "univalle-ideas"},
        {"value": "Idea 2", "topic": "univalle-ideas"},
        {"value": "Idea 3", "topic": "univalle-ideas"},
        {"value": "Idea 4", "topic": "cosas-misteriosas"},
        {"value": "Hecho por Herney", "topic": "cosas-misteriosas"},
    ]
    produce_messages(topics, messages)
