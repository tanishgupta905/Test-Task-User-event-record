from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime
from .models import UserActivity
from .serializers import UserActivitySerializer
from kafka import KafkaProducer
import json

try:

    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
except ValueError as e:
    print("error initiliazing Kafkaproducer")

class UserActivityView(APIView):
    def post(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserActivitySerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['event_type'] not in dict(UserActivity.EVENT_TYPES):
                return Response({'error': 'Invalid event_type.'}, status=status.HTTP_400_BAD_REQUEST)
            
            timestamp = parse_datetime(serializer.validated_data['timestamp'].isoformat())
            if not timestamp:
                return Response({'error': 'Invalid timestamp format'}, status=status.HTTP_400_BAD_REQUEST)
            
            activity = UserActivity.objects.create(
                user=user,
                event_type=serializer.validated_data['event_type'],
                timestamp=timestamp,
                metadata=serializer.validated_data.get('metadata', {})
            )

            producer.send('user-activity', {
                'username': user.username,
                'event_type': activity.event_type,
                'timestamp':activity.timestamp.isoformat(),
                'metadata': activity.metadata
            })

            return Response({'message': 'activity recorded'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
