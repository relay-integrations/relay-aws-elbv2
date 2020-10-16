# aws-elbv2-step-targets-describe

This [AWS ELB v2](https://aws.amazon.com/elasticloadbalancing/) step container lists the ELB v2 targets given a list of target groups. 

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
