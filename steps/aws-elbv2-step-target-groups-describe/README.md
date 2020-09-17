# aws-elbv2-step-target-groups-describe

This [AWS ELB v2](https://aws.amazon.com/elasticloadbalancing/) step container lists the ELB v2 target groups in a provided region.

If no load balancers are specified, all target groups in the account will be output.

## Example 1: Get all Target Groups

```yaml
steps:
# ...
- name: elbv2-describe-target-groups
  image: relaysh/aws-elbv2-step-target-groups-describe
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
```

## Example 2: Passing a list of `loadbalancers` from a previous step

```yaml
steps:
# ...
- name: elbv2-describe-target-groups
  image: projectnebula/elbv2-describe-target-groups
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    loadbalancers: !Output {from: describe-ELBv2-load-balancers, name: loadbalancers}
```

## Example 3: Passing a list of `loadbalancerARNs`
```yaml
steps:
# ...
- name: elbv2-describe-target-groups
  image: projectnebula/elbv2-describe-target-groups
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    loadbalancerARNs:
    - arn:aws:elasticloadbalancing:us-east-1:180094860577:loadbalancer/app/test1/ad652aa6a13aa6da
```

## Example Output
Example output for `targetgroups`:
```
[
   {
      "TargetGroupArn":"arn:aws:elasticloadbalancing:us-west-2:1800948605123:targetgroup/test1/8dd8ffd71233172b3",
      "TargetGroupName":"target_group1",
      "Protocol":"HTTP",
      "Port":80,
      "VpcId":"vpc-98b21611",
      "HealthCheckProtocol":"HTTP",
      "HealthCheckPort":"traffic-port",
      "HealthCheckEnabled":True,
      "HealthCheckIntervalSeconds":30,
      "HealthCheckTimeoutSeconds":5,
      "HealthyThresholdCount":5,
      "UnhealthyThresholdCount":2,
      "HealthCheckPath":"/",
      "Matcher":{
         "HttpCode":"200"
      },
      "LoadBalancerArns":[
         "arn:aws:elasticloadbalancing:us-east-1:1800948605123:loadbalancer/app/test1/ad652aa6a13a123da"
      ],
      "TargetType":"instance"
   }
]
```
