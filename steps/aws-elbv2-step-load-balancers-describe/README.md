# aws-elbv2-step-load-balancers-describe

This [AWS ELB v2](https://aws.amazon.com/elasticloadbalancing/) step container lists the ELB v2 load balancers
in an AWS account and region.

## Example Output 

Example output for `loadbalancers`:
```
[
   {
      "LoadBalancerArn":"arn:aws:elasticloadbalancing:us-west-2:180094860577:loadbalancer/app/test1/ad652aa6a13aasdfa",
      "DNSName":"my-elb.us-east-1.elb.amazonaws.com",
      "CanonicalHostedZoneId":"Z35SXDOTRQ72343",
      "CreatedTime":datetime.datetime(2020,4,24,17,25,47,120000,"tzinfo=tzlocal())",
      "LoadBalancerName":"test1",
      "Scheme":"internet-facing",
      "VpcId":"vpc-98b2a6112",
      "State":{
         "Code":"active"
      },
      "Type":"application",
      "AvailabilityZones":[
         {
            "ZoneName":"us-east-1a",
            "SubnetId":"subnet-4efd21823",
            "LoadBalancerAddresses":[

            ]
         },
         {
            "ZoneName":"us-east-1c",
            "SubnetId":"subnet-b0be61204",
            "LoadBalancerAddresses":[

            ]
         }
      ],
      "SecurityGroups":[
         "sg-601c1209"
      ],
      "IpAddressType":"ipv4"
   }
]
```
