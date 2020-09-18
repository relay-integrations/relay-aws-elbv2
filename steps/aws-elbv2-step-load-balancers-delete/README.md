# aws-elbv2-step-load-balancers-delete

This [AWS ELB](https://aws.amazon.com/elasticloadbalancing/) step container requests that the a
set of given Elastic Loadbalancers v2 terminate immediately.

## Example

```yaml
steps:
# ...
- name: elbv2-delete-load-balancers
  image: relaysh/aws-elbv2-step-load-balancers-delete
  spec:
    aws:
      connection: !Connection {type: aws, name: my-aws-account}
      region: us-west-2
    loadbalancerARNs:
    - arn:aws:elasticloadbalancing:us-east-1:180094860577:loadbalancer/app/kenaz-test/4e5c69e984318b23
    - arn:aws:elasticloadbalancing:us-east-1:180094860577:loadbalancer/app/kenaz-test2/008a1097171fa823
```
