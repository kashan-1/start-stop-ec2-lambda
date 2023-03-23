# start-stop-ec2-lambda
This repository contains code on how to start and stop ec2 instances using Lambda function and cloudwatch

## Steps
These all steps are performed on `AWS` 
1. First create policy by going -> `IAM` -> `create policy` \
add `ec2_start_stop_policy.json` file script \
next -> `tag` -> `add policy name` -> `Create policy`

2. Goto `Roles` -> `Create Role` -> click `AWS Service` radio button -> usecase `Lambda` click Next
In permissions section click on previously created `Policy`
Enter `Role Name` and click `Create Role`

3. Goto AWS Lambda and add these two python file seprately

4. Goto CloudWatch -> events -> Rules -> Create Rule\
Event Source -> Schedule -> Cron Expression -> Lambda function -> select lambda function
configure details -> create rule
