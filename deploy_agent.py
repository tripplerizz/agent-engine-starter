import os
import vertexai
from vertexai.preview import reasoning_engines
from vertexai import agent_engines
from simple_agent.agent import root_agent

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")
DISPLAY_NAME = os.getenv("DISPLAY_NAME")
DEV_USER = os.getenv("DEV_USER")

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
    gcs_dir_name= DEV_USER + str(uuid.uuid4())
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
)

print(f"Deployed! Resource name: {remote_app.resource_name}")
