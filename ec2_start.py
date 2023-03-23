# This function is used to start ec2 instances using lambda function

import boto3
region = 'us-east-1'
instances = ['i-05ce78bc5830983de' , 'i-0f52150219b4976db'] #two instance IDs
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    print('Starting instances')
    ec2.start_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))