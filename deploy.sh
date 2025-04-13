#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Set the path to your service account key file
export GOOGLE_APPLICATION_CREDENTIALS="key.json"

# Authenticate with Google Cloud using the service account
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

# Set your project ID
gcloud config set project $GCP_PROJECT_ID

# Set default region for Cloud Run (optional)
gcloud config set run/region $GCP_REGION

gcloud auth configure-docker $GCP_REGION-docker.pkg.dev --quiet

# Variables
PROJECT_ID=$GCP_PROJECT_ID
LOCATION=$GCP_REGION
REPOSITORY=$GCP_GCR_REPO
IMAGE=$GCP_GCR_IMAGE
TAG=$GCP_GCR_TAG

IMAGE_NAME=$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
IMAGE_URI=$IMAGE_NAME:$TAG

# Build Docker image
docker build --platform linux/amd64 -t $IMAGE_URI .

# Push the Docker image to Google Artifact Registry
docker push $IMAGE_URI

# Deploy to Cloud Run
gcloud run deploy $GCP_GCR_IMAGE \
  --image=$IMAGE_URI \
  --platform=managed \
  --region=$GCP_REGION \
  --allow-unauthenticated \
  --memory=2G \
  --cpu=2
  