
This project is a Django REST API to record user activity events (like page views, clicks, or form submissions). It saves the data in a database, sends it to a Kafka topic, and also includes a Kafka consumer to log the events.

---

## ✅ Features

Save user activity (event type, time, metadata) in a database
Validate user and input
Send events to Kafka for real-time processing
Kafka consumer logs events to the console
Dockerfile included for easy deployment

---

## 📦 Requirements

Python 3.10+
Docker
Kafka (you can run it using Docker or install locally)
PostgreSQL or SQLite (default)

---

### 1. Clone the Repository
bash

git clone https://github.com/tanishgupta905/Test-Task-User-event-record
cd activity-logger


Create a Virtual Environment
bash
CopyEdit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Required Packages
bash pip install -r requirements.txt

4. Run Migrations (for Database Setup)
bash :
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (For Testing)
bash
python manage.py createsuperuser
Follow the prompts to create an admin user.

6. Run the Django Server
bash
python manage.py runserver
The API is now live at: http://127.0.0.1:8000/user/<username>/activity



🧪 API Usage
Endpoint POST /user/<username>/activity

JSON Request Body
json
CopyEdit
{
  "event_type": "page_view",
  "timestamp": "2025-05-15T10:12:00Z",
  "metadata": {
    "page": "/home",
    "browser": "Chrome"
  }
}

Allowed event_type values
Sample Response
{
  "message": "activity recorded"
}


📤 Kafka Integration
1. Run Kafka with Docker
You can use this simple Kafka setup using Docker. First, create a file named kafka-docker-compose.yml with this content:
yaml
CopyEdit
version: '2'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:latest
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
Then run:
docker-compose -f kafka-docker-compose.yml up

2. Start Kafka Consumer
To read and print events from Kafka:
python manage.py consume_activities


🐳 Docker Setup (for the Django API)
1. Build Docker Image

docker build -t activity_logger .

2. Run Docker Container

docker run -p 8000:8000 activity_logger
The API will be available at: http://localhost:8000

