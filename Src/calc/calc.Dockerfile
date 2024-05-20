# Use Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir streamlit requests

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the app when the container starts
CMD ["streamlit", "run", "calculator.py", "--server.port=8501", "--server.address=0.0.0.0"]
