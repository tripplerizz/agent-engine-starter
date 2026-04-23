import os
import vertexai
from vertexai.preview import reasoning_engines
from vertexai import agent_engines
from simple_agent.agent import root_agent

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = "us-central1"
STAGING_BUCKET = "adk_demo_staging_bucket_3412"
DEV_USER = os.getenv("DEV_USER")
DISPLAY_NAME = "simple_agent_" + DEV_USER

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

adk_app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

remote_app = agent_engines.create(
    agent_engine=adk_app,
    extra_packages=["./simple_agent"],
    requirements=["google-cloud-aiplatform[adk,agent_engines]"],
    display_name=DISPLAY_NAME,
    gcs_dir_name= DEV_USER + "_" + str(uuid.uuid4())
)

print(f"Deployed! Resource name: {remote_app.resource_name}")
