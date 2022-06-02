from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_notifications as s3_notify,
)
from constructs import Construct


class CdkTutorialsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        group = iam.Group(self, "VSGroup")
        user = iam.User(self, "VSUser")
        user.add_to_group(group)
        bucket = s3.Bucket(self, 'vs-bucket')
        bucket.grant_read_write(user)
        my_lambda = _lambda.Function(
            self, "lambdaHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='lambda.handler',
            environment={'BUCKET_NAME': bucket.bucket_name}
        )
        notification = s3_notify.LambdaDestination(my_lambda)
        notification.bind(self, bucket)
        bucket.add_object_created_notification( notification, s3.NotificationKeyFilter(suffix='.jpg'))

