from __future__ import print_function

def lambda_handler(event, context):
    for record in event['Records']:
        print('EventID: ' + record['eventID'])
        print('EventName: ' + record['eventName'])
    print('Successfully processed %s records.' % str(len(event['Records'])))
