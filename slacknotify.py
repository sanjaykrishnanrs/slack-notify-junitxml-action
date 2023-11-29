import sys
from junitparser import JUnitXml
from slackclient import SlackClient


def get_slack_message(xml):
    total = 0
    duration = 0
    failures = 0
    skipped = 0

    for suite in xml:
        duration = duration + suite.time
        failures = failures + suite.failures
        skipped = skipped + suite.skipped
        total = total + suite.tests

    passed = total - failures
    duration = str(round(duration / 60)) + ' min' if duration >= 60 else str(duration) + ' sec'

    if not passed:
        status = "Failure"
        color = '#F21410'
    elif failures:
        status = "Unstable"
        color = '#FFA500'
    else:
        status = "Passed"
        color = '#228B22'


    lst_slack_msg = []
    slack_msg = {}
    text_msg = ""
    slack_msg['title'] = f'{title} - {status} [{duration}]'
    slack_msg['text'] = f'Total: `{total}` | Passed: `{passed}` | Failed: `{failures}` | Skipped: `{skipped}`'
    slack_msg['color'] = color
    lst_slack_msg.append(slack_msg)



    return lst_slack_msg, text_msg


title = sys.argv[1]
slackbot_id = sys.argv[2]
slackbot_token = sys.argv[3]
slackbot_channel = sys.argv[4]
junitxml_filepath = sys.argv[5]

print("Opening junit xml file")
xml = JUnitXml.fromfile(f'{junitxml_filepath}')
attach, text_msg = get_slack_message(xml)
slack = SlackClient(slackbot_token)
response = slack.api_call("chat.postMessage", channel=slackbot_channel, text=text_msg,
                           attachments=attach,
                           username=slackbot_id, icon_emoji=':robot_face:',
                           mrkdwn='true')
print("Response from Slack:", response)

