# Containerization ML Primer

This is a simple guide or experiment I created to learn how to containerize and serve simple ML models.


## Steps to Run and execute the project

### 1. Train the Model
```bash
python train_model.py
```

### 2. Build Docker Image
```bash
docker build -t iris-classifier .
```

### 3. Run Container
```bash
docker run -p 5000:5000 iris-classifier
```

### 4. Test the API

Health check:
```bash
curl http://localhost:5000/health
```

Make a prediction:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'
  ```

### 5. Optional: Run in detached mode
```bash
docker run -d -p 5000:5000 --name iris-api iris-classifier
```

### 6.Stop the container

```bash
docker stop iris-api
docker rm iris-api
```