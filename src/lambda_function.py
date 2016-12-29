import boto3
import re
from uuid import uuid4
from datetime import datetime
from collections import namedtuple
import urllib
import logging

# setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# setup aws client outside of handler scope
s3client = boto3.client('s3')

# a regex to match the "event" nodes
r = re.compile(r'\[Event.*\]')


def lambda_handler(event, context):
    
    logger.info('received event --> {}'.format(event))
    
    for record in event['Records']:
        
        #upload hands to target bucket
        for hand in parse_hands(record['s3']):
            try:
                logger.info('(hand key) --> {}'.format(hand.key))
                s3client.put_object(Bucket='tbridgehands', Key=hand.key + '.txt', Body=hand.content)
                s3client.put_object(Bucket='tbridgehands', Key=hand.key + '.pbn', Body=hand.content)
            except Exception as e:
                logger.error('Lambda failed to upload to target bucket')
                raise e
            
            
    return 'OK'
    

def parse_hands(s3_event):
    
    try:
        # getting object key from s3 bucket.
        # need to use unquote and utf8 encoding to get around issue with non-ASCII characters in filenames 
        object_key = urllib.unquote_plus(s3_event['object']['key'].encode("utf8"))
        logger.info('(object_key) --> {}'.format(object_key))
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
            hand.key = object_key.rsplit('.', 1)[0] + '(' + str(i) + ')' + unique_stamp
            # using starting positions to split content
            hand.content = object_content[starting_positions[i]:starting_positions[i+1]]
            hands.append(hand)
    except Exception as e:
         logger.error('parse_hands failed to complete')
         raise e
    
    return hands



