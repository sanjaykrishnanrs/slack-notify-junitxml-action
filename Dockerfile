# Container image that runs your code
FROM python:3

RUN pip install junitparser

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY slacknotify.py /slacknotify.py

# Code file to execute when the docker container starts up
ENTRYPOINT ["python", "slacknotify.py", $1, $2, $3, $4]