# Container image that runs your code
FROM python:3

RUN pip install junitparser
RUN pip install 'slackclient<2.0.0'

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY slacknotify.py /usr/bin/slacknotify.py

RUN echo "Value of argument=$1, with name=$INPUT_SLACKBOTCHANNEL"
RUN echo "Value of argument=$4, with name=$INPUT_JUNITXML_FILEPATH"
# Code file to execute when the docker container starts up
ENTRYPOINT ["python", "/usr/bin/slacknotify.py"]
