#!/bin/bash
# Script to create a GCS bucket named adk_demo_staging_bucket_34dsf

# Exit immediately if a command exits with a non-zero status
set -e

BUCKET_NAME="adk_demo_staging_bucket_34d12""

echo "Creating GCS bucket: gs://${BUCKET_NAME}..."

gcloud storage buckets create "gs://${BUCKET_NAME}"

echo "Bucket gs://${BUCKET_NAME} created successfully."
