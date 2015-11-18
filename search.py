#!/usr/bin/env python

from otrs.client import GenericTicketConnector
from otrs.objects import Ticket, Article, DynamicField, Attachment

import yaml
config = yaml.safe_load(open("config.yml"))

server_uri = config['server']
webservice_name = 'GenericTicketConnector'
client = GenericTicketConnector(server_uri, webservice_name)

# user session
client.user_session_register(config['username'], config['password'])

# returns all tickets in queue Support
tickets = client.ticket_search(
    Queues = 'Support Queue',
    From = '{{term}}',
    To = '{{term}}',
    Cc = '{{term}}',
    Subject = '{{term}}',
    Body = '{{term}}',
    ContentSearch = 'OR',
    FullTextIndex = 1
)

print tickets
