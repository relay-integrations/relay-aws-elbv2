#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D


relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
)

elbv2 = sess.client('elbv2')


elb_arns = [] # List of Load Balancers to look for target groups under
all_target_groups = [] # List of target groups by ELB
get_all = False # Get all groups if no ELBs are specified

try:
  loadbalancers = relay.get(D.loadbalancers)
  elb_arns = [i["LoadBalancerArn"] for i in loadbalancers]
except:
  try:
    elb_arns = relay.get(D.loadbalancerARNs)
  except:
    get_all = True # If no ELBs are specified, get all Target Groups.

if get_all:
  print("Found the following Target Groups:\n")
  target_groups = elbv2.describe_target_groups()['TargetGroups']
  print("{:<20} {:<20} {:<20} {:<20}".format('NAME', 'PROTOCOL', 'PORT', 'VPC ID' ))
  for group in target_groups:
    print("{:<20} {:<20} {:<20} {:<20}".format(group['TargetGroupName'], group['Protocol'], group['Port'], group['VpcId'] ))
    all_target_groups.append(group)
  
else:
  print ("Found the following Target Groups under {} ELBv2 Load Balancers:\n".format(len(elb_arns)))
  for arn in elb_arns: 
    print('\nTarget Groups for ELBv2 {}:\n'.format(arn))
    target_groups = elbv2.describe_target_groups(LoadBalancerArn=arn)['TargetGroups']
    
    print("{:<20} {:<20} {:<20} {:<20}".format('NAME', 'PROTOCOL', 'PORT', 'VPC ID' ))
    for group in target_groups:
      print("{:<20} {:<20} {:<20} {:<20}".format(group['TargetGroupName'], group['Protocol'], group['Port'], group['VpcId'] ))
      all_target_groups.append(group)

# Adding Target Groups to output `targetgroups`
print('\nAdding {0} target group(s) to the output `targetgroups`'.format(len(all_target_groups)))
relay.outputs.set('targetgroups', all_target_groups)

