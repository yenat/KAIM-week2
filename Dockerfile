# Use the official Python 3.10 image as a base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of your project into the container
COPY . /app

# Switch to root user to install additional packages
USER root

# Install Jupyter and any needed packages specified in requirements.txt
RUN pip install jupyter && \
    pip install --no-cache-dir -r requirements.txt

# Install additional dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev gcc libffi-dev zlib1g-dev && \
    pip install psycopg2

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/app/notebooks"]
