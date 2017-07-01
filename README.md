## AWS IOT Slack Button

An AWS lambda handler that sends a slack message when [the AWS IoT button](https://aws.amazon.com/iotbutton/) is pressed.

### How to use

1. Install packages: `. install.sh`
1. Package python codes into a zip file: `. package.sh`
1. Setup [AWS Lambda](http://docs.aws.amazon.com/iot/latest/developerguide/iot-button-lambda.html) for the AWS IoT button.
1. Upload package.zip file to AWS Lambda.
1. Set AWS Lambda environment variables:
```
SLACK_TOKEN ... an encrypted slack token using KMS.
CHANNEL ... a name of slack channel to where you want to send a message, e.g. "#test".
MSG ... a message you want to send when button is pressed.
USER_NAME ... a user name you want to set as a sender.
```
