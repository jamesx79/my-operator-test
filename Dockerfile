FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the operator code
COPY operator.py .

# Make the operator executable
RUN chmod +x operator.py

# Run the operator
CMD ["python", "-u", "operator.py"]
