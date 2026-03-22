import os
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct


class InfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the project root (parent of infra)
        project_root = os.path.join(os.path.dirname(__file__), "..", "..")
        
        # Get the backend directory path
        backend_path = os.path.join(project_root, "backend", "functions")

        # Create first_lambda
        first_lambda = _lambda.Function(
            self,
            "FirstLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=_lambda.Code.from_asset(os.path.join(backend_path, "first_lambda")),
            function_name="first-lambda",
            timeout=Duration.seconds(30),
            memory_size=128,
        )

        # Create second_lambda
        second_lambda = _lambda.Function(
            self,
            "SecondLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=_lambda.Code.from_asset(os.path.join(backend_path, "second_lambda")),
            function_name="second-lambda",
            timeout=Duration.seconds(30),
            memory_size=128,
        )

        # Output the Lambda function ARNs
        # You can access these after deployment with:
        # aws lambda get-function --function-name first-lambda
        # aws lambda get-function --function-name second-lambda