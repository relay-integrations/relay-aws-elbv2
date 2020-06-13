#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D

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

target_group_arns = []
all_targets = {}

try:
  target_groups = relay.get(D.targetgroups)
  target_group_arns = [i["TargetGroupArn"] for i in target_groups]
except:
  try:
    target_group_arns = relay.get(D.targetgroupARNs)
  except:
    print("One of `targetgroups` or `targetgroupARNs` must be provided. Exiting.")
    exit(1)

print("Found the following Targets under {} Target Groups:\n".format(len(target_group_arns)))
for tg in target_group_arns:
  print ('\nTargets for Target Group {}:\n'.format(tg))
  targets = elbv2.describe_target_health(TargetGroupArn=tg)['TargetHealthDescriptions']

  print("{:<30} {:<10} {:<20} {:<40} {:<80}".format('ID', 'PORT', 'STATE', 'REASON', 'DESCRIPTION' ))
  for target in targets:
    print("{:<30} {:<10} {:<20} {:<40} {:<80}".format(target['Target']['Id'], target['Target']['Port'], target['TargetHealth']['State'], target['TargetHealth']['Reason'], target['TargetHealth']['Description'] ))
  
  all_targets[tg] = targets

# Adding Targets to output `targets`
print('\nAdding {0} set(s) of targets to the output `targets`'.format(len(all_targets)))
relay.outputs.set('targets', all_targets)