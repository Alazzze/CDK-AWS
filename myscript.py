from aws_cdk import App, Stack, CfnOutput
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3

class MyStack(Stack):

    def __init__(self, scope, id, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a virtual private cloud network (VPC)
        vpc = ec2.Vpc(self, 'MyVpc', max_azs=2)

        # Creating an EC2 instance
        instance = ec2.Instance(self, 'MyInstance',
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc
        )

        # Creating an S3 bucket
        bucket = s3.Bucket(self, 'MyBucket')

        # Output information about the IP address of the instance
        CfnOutput(self, 'InstancePublicIp', value=instance.instance_public_ip)

app = App()
MyStack(app, "MyStack")
app.synth()
