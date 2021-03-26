#!/usr/bin/env python
import boto3
from relay_sdk import Interface, Dynamic as D


relay = Interface()

session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
  aws_session_token=session_token
)

elbv2 = sess.client('elbv2')

# Getting all Load Balancers
elbs = elbv2.describe_load_balancers()['LoadBalancers']
elb_arns = [i["LoadBalancerArn"] for i in elbs]

# Warn if no Load Balancers found
if (len(elb_arns)==0):
  print('No ELBs found! Exiting.')
  exit()

print('Found the following Elastic Load Balancers: \n')
print("{:<20} {:<75} {:<30} {:<30}".format('NAME', 'DNS NAME', 'SCHEME', 'VPC ID' ))
for elb in elbs:
  print("{:<20} {:<75} {:<30} {:<30}".format(elb['LoadBalancerName'], elb['DNSName'], elb['Scheme'], elb['VpcId'] ))

# Adding Load Balancers to output `loadbalancers`
print('\nAdding {0} elastic load balancer(s) to the output `loadbalancers`'.format(len(elbs)))
relay.outputs.set('loadbalancers', elbs)
