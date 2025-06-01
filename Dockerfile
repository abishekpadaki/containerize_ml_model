#using python slim image
FROM python:3.9-slim

#set working directory
WORKDIR /app

#copy requirements.txt to the working directory
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy application files

COPY app.py .
COPY models/ ./models/


#expose port 5000
EXPOSE 8080

#Run the application
CMD ["python", "app.py"]