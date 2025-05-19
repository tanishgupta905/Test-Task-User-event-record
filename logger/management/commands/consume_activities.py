from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
import json

class Command(BaseCommand):
    help = 'Consume user activity events from Kafka and log them.'

    def handle(self, *args, **kwargs):
        consumer = KafkaConsumer(
            'user-activity',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='user-activity-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

        self.stdout.write(self.style.SUCCESS('Starting Kafka consumer...'))
        for message in consumer:
            self.stdout.write(f"Consumed event: {message.value}")
