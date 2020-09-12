# Overview

The purpose of this lambda function is to delete tweets older than 72 hours from S3. Currently the bucket it's deleting from is set to `fedex-case` but that can be changed by modifying the bucket parameter in the `serverless.yml`.

## Prerequisites
1. `serverless` should be installed.

## Deploying
1. Deploy the function with `sudo serverless deploy`
2. Run the `cloudwatch-schedular.sh` script to add create an scheduled invoke for the function.
  - Change the target.json as well to match your lambda ARN.
