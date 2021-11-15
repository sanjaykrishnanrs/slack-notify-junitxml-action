# Container image that runs your code
FROM python:3

RUN pip install junitparser
RUN pip install 'slackclient<2.0.0'

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY slacknotify.py /slacknotify.py

RUN ls

# Code file to execute when the docker container starts up
ENTRYPOINT ["python", "slacknotify.py"]
