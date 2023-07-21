# joke-serverless-app

A Python-based serverless app using AWS Lambda that fetches data from a JokeAPI, processes the data, stores it in Google Cloud Firestore, and returns the data as a response.

# Tech Stack

- Docker
- AWS Lambda
- AWS ECR (In Production)
- Python 3.8
- Google Cloud Firestore

## Run the app locally inside Docker

- Since this function uses Google Cloud Firestore, you will need to authenticate this function with Google Cloud using a service account key. Create a service account, download the JSON key file, rename it to `service_account_key.json`, and put it in the root of this repo.

- Build and run the app
```
docker-compose up -d --build
```
- Test the app
```
curl -XPOST "http://localhost:3001/2015-03-31/functions/function/invocations" -d '{"category": "Any", "language": "en"}'
```
