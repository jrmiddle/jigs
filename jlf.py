#!/usr/bin/env python
# Expects ~/.jira.cfg to to contain:
#
# [whistle]
# server: https://whistle.atlassian.net
# username: snoopy
# password: r3d8@r0n

try:
    from jira.client import JIRA
except ImportError as e:
    print >> sys.stderr, "Jira not found; try `pip install jira`."

import ConfigParser, os, sys

## get config

config = ConfigParser.SafeConfigParser()
files = config.read(os.path.expanduser("~/.jira.cfg"))
if len(files) == 0:
    print >> sys.stderr, "No ~/.jira.cfg found; exiting."
    sys.exit(1)

try:
    username = config.get('whistle', 'username')
    password = config.get('whistle', 'password')
    server = config.get('whistle', 'server')
except ConfigParser.NoSectionError as e:
    print >> sys.stderr, "No [whistle] section found; check your ~/.jira.cfg."
    sys.exit(2)

## initialize client
    
jira = JIRA(
    basic_auth=(username, password),
    options={'server': 'https://whistle.atlassian.net'}
)

f = jira.filter("12103")

issues =  jira.search_issues(f.jql, fields="summary,issuetype")

print ("\n".join(["* [{0}]({1}) ({2}): {3}".format(i.key, i.self, i.fields.issuetype.name, i.fields.summary) for i in issues]))