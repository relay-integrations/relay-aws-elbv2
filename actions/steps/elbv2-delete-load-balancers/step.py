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

to_terminate = relay.get(D.loadbalancerARNs)

if (len(to_terminate) == 0):
  print('No load balancers found to terminate. Exiting.')
  exit()


# Terminate ELBs 
print('ELBs to terminate: {0}'.format(to_terminate))
for t in to_terminate:
    print('\nTerminating ELB: {0}'.format(t))
    elbv2.delete_load_balancer(LoadBalancerArn=t)