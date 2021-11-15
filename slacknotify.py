import sys
from junitparser import JUnitXml
from slackclient import SlackClient

print ("Arguments:", sys.argv)
slackbot_id = sys.argv[1]
slackbot_token = sys.argv[2]
slackbot_channel = sys.argv[3]
junitxml_filepath = sys.argv[4]

print (slackbot_id, slackbot_token, slackbot_channel)

print("Opening junit xml file")
xml = JUnitXml.fromfile(f'/github/workspace/{junitxml_filepath}')
print(xml)
#
# for suite in xml:
#     # handle suites
#     for case in suite:
#         # handle cases
# xml.write() # Writes back to file

text_msg = "Text Message"
slack_msg = "Attachementsssssss Message"
slack = SlackClient(slackbot_token)
slack.api_call("chat.postMessage", channel=slackbot_channel, text=text_msg,
                           attachments='[{"title": "Try these - ","text": " Text "}]',
                           username=slackbot_id, icon_emoji=':robot_face:',
                           mrkdwn='true')
