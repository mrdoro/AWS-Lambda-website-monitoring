import boto3

def send_function(event, context):
#some names can be customized 
    valu=event['VAL']
    mname=event['MNAM']
    d=boto3.client('cloudwatch')
    d.put_metric_data(Namespace='WebStatus',
        MetricData=[
            {
            'MetricName': mname,
            'Dimensions': [
                {
                'Name': 'Status',
                'Value': 'WebsiteStatusCode'
                },
            ],
            'Value': valu,
            },
        ]
    )
