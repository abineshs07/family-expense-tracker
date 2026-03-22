#!/usr/bin/env python3
import os
import aws_cdk as cdk
from infra.infra_stack import InfraStack

app = cdk.App()

# Get region from environment, default to us-east-1
region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

InfraStack(
    app,
    "InfraStack",
    # Use environment variables from AWS CLI or GitHub Actions
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=region
    ),
)

app.synth()