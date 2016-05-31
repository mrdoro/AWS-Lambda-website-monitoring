import boto3
import httplib
import errno
import socket
import json

def lambda_handler(event, context):
    client = boto3.client('lambda')
    websiteurl='www.sample.com' #enter your site url
    metriname='metric name' #enter metric name 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((websiteurl, 80))
    except socket.error, e:
        if 'Connection refused' in e:
            response=client.invoke(
                FunctionName='SendMetric', #paste real name of the lambda function you defined.
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 100,"MNAM": metriname}) 
            )
    else:
        c=httplib.HTTPConnection(websiteurl) #for ssl use httplib.HTTPSConnection.
    	c.request("HEAD", '')
        STAT=c.getresponse().status
        if STAT == 200 or STAT == 304:
            response=client.invoke(
                FunctionName='SendMetric', #paste real name of the lambda function.
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 200,"MNAM": metriname}) 
            )
        else:
            response=client.invoke(
                FunctionName='SendMetric',
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 50,"MNAM": metriname}) 
            )
