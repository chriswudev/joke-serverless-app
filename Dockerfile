FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Copy lambda function code and install requirements
COPY . .

# Install the function's dependencies using file requirements.txt
# from the project folder.
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
ADD . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service account key JSON file to the container
COPY service_account_key.json /app/

# Set the environment variable for authentication
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/service_account_key.json

# Set the entry point for the Lambda function
CMD ["app.fetch_jokes"]
