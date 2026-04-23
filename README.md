# agent-engine-starter

This repository serves as a starter template and demonstration for building AI agents using the Google Agent Development Kit (ADK). 

## About the Project

The core of this repository contains a simple agent implementation located in `simple_agent/agent.py`. It showcases how to define an agent (`tool_agent`) using the `gemini-2.5-flash` model. 

The primary feature of this sample is tool usage. The agent is equipped with custom Python functions to perform basic mathematical operations:
- `add_numbers`
- `subtract_numbers`
- `multiply_numbers`
- `divide_numbers`

It is instructed to utilize these tools whenever a user asks a math-related question and to explain its logical steps for arriving at the solution. This serves as a foundational example of how to extend a language model's capabilities with external tools via the Google ADK.

## Dependencies

The project uses `uv` for dependency management (as indicated by `uv.lock`) and relies on the following key Python packages:
- `google-adk`
- `google-auth`
- `python-dotenv`

---

## Resources

Managing Deployed Agents on AgentEngine
AWS Product Mapping

**GCP vs. AWS: Core Concepts & Terminology Mapping:**

*   **Resource Hierarchy:** Google Cloud (Organization, Folders, Projects) vs. AWS (Organizations, OUs, Accounts).
*   **IAM:** Google Cloud IAM (Roles, Permissions) vs. AWS IAM (Roles, Policies).
*   **Networking:** Google Cloud VPC (Subnets, Firewall Rules) vs. AWS VPC (Subnets, Security Groups, NACLs).
*   **Regions & Zones:** Similar concepts in both clouds.

**Key GCP Services & GitHub Repo Examples:**

*   **Compute:**
    *   Google Compute Engine (VMs) ~ AWS EC2.
    *   Google Kubernetes Engine (GKE) ~ AWS EKS.
    *   Cloud Functions (Serverless) ~ AWS Lambda.
    *   GitHub: Search for repos like `GoogleCloudPlatform/compute-samples`, `GoogleCloudPlatform/kubernetes-engine-samples`, `GoogleCloudPlatform/functions-samples`.
*   **Storage:**
    *   Google Cloud Storage (Object Storage) ~ AWS S3.
    *   Cloud SQL (Managed Databases) ~ AWS RDS.
    *   Cloud Spanner (Globally Distributed DB) ~ AWS DynamoDB/Aurora (with differences).
    *   GitHub: `GoogleCloudPlatform/storage-samples`, `GoogleCloudPlatform/cloud-sql-samples`.
*   **Data & Analytics:**
    *   BigQuery (Data Warehouse) ~ AWS Redshift/Athena.
    *   Cloud Dataflow (Data Processing) ~ AWS Glue/EMR.
    *   GitHub: `GoogleCloudPlatform/bigquery-samples`, `GoogleCloudPlatform/DataflowTemplates`.
*   **AI/ML:**
    *   Vertex AI Platform (Agent Platform) ~ AWS SageMaker.
    *   GitHub: `GoogleCloudPlatform/vertex-ai-samples`.

**(10 min) Tools & Further Learning:**

*   **Cloud Console:** Quick walk-through of the UI.
*   **Cloud Shell:** Built-in command line.
*   **gcloud CLI:** Command-line tool ~ AWS CLI.
*   **Infrastructure as Code:** Cloud Deployment Manager, Terraform.
    *   GitHub: `GoogleCloudPlatform/deploymentmanager-samples`, HashiCorp's Terraform Google Provider repos.
*   **Documentation:** cloud.google.com/docs
*   **Qwiklabs:** Hands-on labs.
*   **Key GitHub Organizations:**
    *   `GoogleCloudPlatform`
    *   `GoogleCloudBuild`
    *   `googleapis` (for client libraries)