from aws_cdk import App, Stack, CfnOutput
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3

class MyStack(Stack):

    def __init__(self, scope, id, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Створення віртуальної приватної хмарної мережі (VPC)
        vpc = ec2.Vpc(self, 'MyVpc', max_azs=2)

        # Створення EC2 інстансу
        instance = ec2.Instance(self, 'MyInstance',
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc
        )

        # Створення S3 бакету
        bucket = s3.Bucket(self, 'MyBucket')

        # Виведення інформації про IP адресу інстансу
        CfnOutput(self, 'InstancePublicIp', value=instance.instance_public_ip)

app = App()
MyStack(app, "MyStack")
app.synth()
