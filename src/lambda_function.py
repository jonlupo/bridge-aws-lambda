import boto3
import re
from uuid import uuid4
from datetime import datetime
from collections import namedtuple

s3client = boto3.client('s3')
# a regex to match the "event" nodes
r = re.compile(r'\[Event.*\]')


def parse_hands(s3_event):
    
    object_key = s3_event['object']['key']
    starting_positions = []
    hands = []
    unique_stamp = '[' + str(datetime.now()) + ']' + str(uuid4())
    
    object_resp = s3client.get_object(Bucket='bridgehands', Key=object_key)
    object_content = object_resp['Body'].read()
    
    for matchgroup in r.finditer(object_content):
        # collecting the starting positions to 
        # write chunks to new hands 
        starting_positions.append(matchgroup.start())
    for i in range(len(starting_positions)-1):
        hand = namedtuple('hand', ['key','content'])
        # create unique key for hand (will be used as filename)
        hand.key = object_key.split('.')[0] + '(' + str(i) + ')' + unique_stamp
        # using starting positions to split content
        hand.content = object_content[starting_positions[i]:starting_positions[i+1]]
        hands.append(hand)
    
    return hands



def lambda_handler(event, context):
    
    for record in event['Records']:
        
        #upload hands to target bucket
        for hand in parse_hands(record['s3']):
            print hand.key
            s3client.put_object(Bucket='tbridgehands', Key=hand.key + '.txt', Body=hand.content)
            s3client.put_object(Bucket='tbridgehands', Key=hand.key + '.pbn', Body=hand.content)
            
    return 'OK'