import logging
from confluent_kafka import Consumer

# Set up logging
logging.basicConfig(level=logging.INFO)

# Kafka configuration
config = {
    'bootstrap.servers': 'kafka-broker-1:9092',
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest',
}

def consume_messages(topics):
    consumer = Consumer(config)
    consumer.subscribe(topics)
    logging.info(f"Subscribed to topics: {topics}")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logging.error(f"Consumer error: {msg.error()}")
                continue
            logging.info(f"Received message from {msg.topic()} at offset {msg.offset()}: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        logging.info("\nStopping consumer...")
    finally:
        consumer.close()


if __name__ == "__main__":
    topics = ["univalle-ideas", "cosas-misteriosas"]
    consume_messages(topics)
