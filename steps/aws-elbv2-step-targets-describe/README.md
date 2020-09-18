# aws-elbv2-step-targets-describe

This [AWS ELB v2](https://aws.amazon.com/elasticloadbalancing/) step container lists the ELB v2 targets given a list of target groups. 

## Example 1: Passing a list of `targetgroups` from a previous step

```yaml
steps:
# ...
- name: elbv2-describe-targets
  image: relaysh/aws-elbv2-step-targets-describe
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    targetgroups: !Output { from: elbv2-describe-target-groups, name: targetgroups}
```

## Example 2: Passing a list of `targetgroupARNs`

```yaml
steps:
# ...
- name: elbv2-describe-targets
  image: projectnebula/elbv2-describe-targets
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    targetgroupARNs: 
    - arn:aws:elasticloadbalancing:us-west-2:1800948605123:targetgroup/test1/8dd8ffd7123317
    - arn:aws:elasticloadbalancing:us-west-2:1800948605123:targetgroup/test2/8dd8ffd7123339
```

## Example Output
Example output for `targets`:
```
{
   "arn:aws:elasticloadbalancing:us-west-2:1800948605123:targetgroup/test1/8dd8ffd7123317":[
      {
         "Target":{
            "Id":"i-0d7ce1cc8568040ba",
            "Port":80
         },
         "HealthCheckPort":"80",
         "TargetHealth":{
            "State":"unhealthy",
            "Reason":"Target.Timeout",
            "Description":"Request timed out"
         }
      },
      {
         "Target":{
            "Id":"i-0dbde4b790d413e7a",
            "Port":80
         },
         "HealthCheckPort":"80",
         "TargetHealth":{
            "State":"unhealthy",
            "Reason":"Target.Timeout",
            "Description":"Request timed out"
         }
      }
   ],
   "arn:aws:elasticloadbalancing:us-west-2:1800948605123:targetgroup/test2/8dd8ffd7123339":[
      {
         "Target":{
            "Id":"i-0dbde4b790d413e7a",
            "Port":80
         },
         "HealthCheckPort":"80",
         "TargetHealth":{
            "State":"unhealthy",
            "Reason":"Target.Timeout",
            "Description":"Request timed out"
         }
      }
   ]
}
```
