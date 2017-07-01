from base64 import b64decode
import os

import boto3
import slack
import slack.chat


ENCRYPTED = os.environ['SLACK_TOKEN']
# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per container
DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']
slack.api_token = DECRYPTED


def lambda_handler(event, context):
    slack.chat.post_message(os.environ['CHANNEL'], os.environ['MSG'], username=os.environ['USER_NAME'])
