scheduled_rule=fedex-case-delete-old-dev
function_name=delete-old-dates-dev-handler
statement_id=fedex-case-delete-id

aws events put-rule \
    --name $scheduled_rule \
    --schedule-expression 'rate(24 hours)'

aws lambda add-permission \
    --function-name $function_name \
    --statement-id  $statement_id \
    --action 'lambda:InvokeFunction' \
    --principal events.amazonaws.com \
    --source-arn arn:aws:events:eu-central-1:534692912862:rule/$scheduled_rule

aws events put-targets --rule $scheduled_rule --targets file://targets.json
