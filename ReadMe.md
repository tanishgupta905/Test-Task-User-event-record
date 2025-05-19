# 📊 User Activity Logger API

A Django REST API to record user activity events such as page views, clicks, and form submissions.

This system:
- Stores event data in a database
- Sends events to a Kafka topic
- Logs events using a Kafka consumer
- Can be containerized with Docker

---

## ✅ Features

- Save user activity (event type, time, metadata) in a database
- Input validation and user verification
- Kafka producer for real-time event forwarding
- Kafka consumer logs events to the console
- Dockerfile included for deployment

---

## 📦 Requirements

- Python 3.10+
- Docker (for optional containerization)
- Kafka (via Docker or local install)
- PostgreSQL or SQLite (default)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/tanishgupta905/Test-Task-User-event-record
cd activity-logger
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin Access)

```bash
python manage.py createsuperuser
```

### 6. Run the Django Development Server

```bash
python manage.py runserver
```

The API will be available at:  
👉 `http://127.0.0.1:8000/user/<username>/activity`

---

## 🧪 API Usage

### Endpoint

```
POST /user/<username>/activity
```

### JSON Request Body

```json
{
  "event_type": "page_view",
  "timestamp": "2025-05-15T10:12:00Z",
  "metadata": {
    "page": "/home",
    "browser": "Chrome"
  }
}
```

### Allowed `event_type` values

- `page_view`
- `click`
- `form_submission`

### Sample Response

```json
{
  "message": "activity recorded"
}
```

---

## 📤 Kafka Integration

### 1. Run Kafka via Docker

Create a file named `kafka-docker-compose.yml` with the following content:

```yaml
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
```

Start Kafka using:

```bash
docker-compose -f kafka-docker-compose.yml up
```

### 2. Start Kafka Consumer

To consume and log events from Kafka:

```bash
python manage.py consume_activities
```

---

## 🐳 Docker Setup for Django API

### 1. Build the Docker Image

```bash
docker build -t activity_logger .
```

### 2. Run the Docker Container

```bash
docker run -p 8000:8000 activity_logger
```

API will be accessible at:  
👉 `http://localhost:8000`

---

## 📝 Notes

- You can switch from SQLite to PostgreSQL in `settings.py`
- Make sure Kafka is running **before** posting events or starting the consumer
- Test the API using tools like Postman, curl, or httpie

---

## 👤 Author

**Tanish Gupta**  
GitHub: [@tanishgupta905](https://github.com/tanishgupta905)

---

## 🤝 Contributions

Pull requests and suggestions are welcome!
