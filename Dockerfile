# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Set environment variables
ENV GRANT_SUDO='yes' \
    CHOWN_HOME=yes \
    CHOWN_HOME_OPTS=-R \
    NB_UID=1002 \
    NB_GID=1002

# Expose the port
EXPOSE 8501

# Copy the local requirements.txt file to the container at /requirements.txt
COPY /requirements.txt /

# Install system-level dependencies, upgrade pip, and install Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    ghostscript && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip setuptools wheel && \
    pip install -r /requirements.txt

# Copy the local app directory to the container at /app
COPY ./app /app

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py", "--server.baseUrlPath", "/app"]
