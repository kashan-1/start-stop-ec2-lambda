# This function is used to stop ec2 instances using lambda function
import boto3
region = 'us-east-1'
instances = ['i-05ce78bc5830983de', 'i-0f52150219b4976db']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    print('Stopping instances')
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))