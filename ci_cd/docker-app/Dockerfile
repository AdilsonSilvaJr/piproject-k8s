FROM python:3.8-slim

# Install Streamlit
RUN pip install streamlit

# Copy your application code to the container
COPY app/src /app

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "/app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
