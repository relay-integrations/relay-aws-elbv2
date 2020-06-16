# aws-elbv2-step-load-balancers-delete

This [AWS ELB](https://aws.amazon.com/elasticloadbalancing/) step container requests that the a
set of given Elastic Loadbalancers v2 terminate immediately.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |
| `loadbalancerARNs` || array of string | The list of ELB v2 ARNs identifying the ELBs v2 to terminate. | None | True |

## Outputs 
None 

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
