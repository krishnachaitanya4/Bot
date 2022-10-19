# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:15:12 2022

@author: KRISHNA_CHAITANYA
"""

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC2024c99acc99b6368d03a115ccf9cbe0']
auth_token = os.environ['dcc39eb7786534aea3f0c0901fe0a6d6']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+917095153945',
                              to='whatsapp:+918374318214'
                          )

print(message.sid)