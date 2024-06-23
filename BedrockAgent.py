import string
import random
import boto3
from dotenv import load_dotenv
import os

load_dotenv()



class BedrockAgent:
    def __init__(self):
        self.reset_session()

    def invoke(self, text: str) -> str:
        # Initialize a session using Amazon Bedrock
        print(os.getenv('AWS_ACCESS_KEY_ID'))
        session = boto3.Session(
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name='us-east-1'
        )

        # Initialize Bedrock client
        bedrock_client = session.client('bedrock-agent-runtime')

        # Invoke the Bedrock agent
        response = bedrock_client.invoke_agent(
            agentAliasId='QZEDAWGXTI',
            agentId='ZIDEKNGDFI',
            inputText=text,
            sessionId=self.sessionId
        )

        res = ''.join([ event['chunk']['bytes'].decode('utf-8') for event in response['completion'] ])
        return res

    def reset_session(self) -> None:
        self.sessionId = ''.join(random.choices(string.ascii_letters, k=10))
