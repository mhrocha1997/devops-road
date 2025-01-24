import time
from kafka import KafkaConsumer
import os

KAFKA_BROKER = os.getenv('KAFKA_BROKER_LIST', 'localhost:9092')
TOPIC_NAME = os.getenv('TOPIC_NAME', 'example-topic')
GROUP_ID = os.getenv('GROUP_ID', 'example-group')

def main():
    print(f"Connecting to Kafka broker: {KAFKA_BROKER}")
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BROKER,
        group_id=GROUP_ID,
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    print(f"Subscribed to topic: {TOPIC_NAME}")
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")
        time.sleep(30) 
        print("Message processed.")

if __name__ == "__main__":
    main()
