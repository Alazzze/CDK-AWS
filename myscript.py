from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a virtual private cloud network (VPC)
        vpc = ec2.Vpc(self, 'MyVpc', max_azs=2, region="us-east-1")

        # Creating an EC2 instance
        instance = ec2.Instance(self, 'MyInstance',
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc,
            availability_zone='us-east-1a'  
        )

        # Creating an S3 bucket
        bucket = s3.Bucket(self, 'MyBucket',
            removal_policy=core.RemovalPolicy.DESTROY
        )

app = core.App()
MyStack(app, "MyStack")
app.synth()
