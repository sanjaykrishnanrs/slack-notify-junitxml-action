# slack-notify-junitxml-action
Github actions to notify the test result from junitxml file to any slack channel

There is a demo in youtube of this plugin: - https://youtu.be/KhZ1TdRjTy0

## What does this github action do ?
Be it any type of tests - unit/integration/api in any language - java/python, you can generate **[JUNITXML](https://llg.cubic.org/docs/junit/)** easily as all languages provide this out of box. <br>
For example if you are using pytest (python), then you can generate junitxml report like this: <br>
```pytest <test> --junitxml=<reportname>```

So, a junitxml report with a slackbot can use this github action to post crisp & clear message conveying the test result.
Test result status follows jenkins convention
* **Passed** &emsp;&emsp; All tests have passed
* **Unstable** &emsp;&nbsp;&nbsp;Few tests have not passed
* **Failure** &emsp;&emsp;&nbsp;&nbsp;No tests have passed
  
## Slack Message examples
![Slack message](images/slack-message-examples.png)

  
## Usage


```
name: Notify in Slack Channels
on: workflow_dispatch
jobs:
  notify-slack:
    runs-on: ubuntu-latest
    name: A job to notify in slack with my github actions
    environment: Slackbot Notification
    steps:
      - uses: actions/checkout@v2
      - name: Notify Slack Test Result
        uses: sanjaykrishnanrs/slack-notify-junitxml-action@0.1.12-alpha
        with:
          title: API Tests
          slackbotid: ${{ secrets.SLACKBOTID }}
          slackbottoken: ${{ secrets.SLACKBOTTOKEN }}
          slackchannel: '${{ secrets.SLACKCHANNEL }}'
          junitxml_filepath: junitreport.xml
```

# Pre-requisite
A slackbot configured in slack and added as an app to the channel where the message has to be sent. <br>
Read more - https://slack.com/intl/en-in/help/articles/115005265703-Create-a-bot-for-your-workspace
# License

The scripts and documentation in this project are released under the [MIT License](LICENSE)

# Contributions

Contributions are welcome! Create a branch or Fork the repo - Start doing !
