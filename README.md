# Doorbell Dash
wi-fi 'doorbell' that takes a photo of the button presser, and texts your phone when pressed. Uses a reprogrammed Amazon Dash Button and a Raspberry Pi with pi-camera.

## Installation
* $ pip3 install scapy-python3
* $ pip install twilio
* $ pip install pyimgur

## Usage
* You must run script as root user / SUDO

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Setup Twilio Account
* To receive SMS notifications, you need to sign up for Twilio
* Signup for a free Twilio account
* As part of the signup process, you need to verify a phone number. Use the cell phone number that you want to send messages to.
* After you verify your phone number, Twilio will assign you an account phone number to use that is in the same area code as the number you verified. This is the phone number that will be sending MMS messages on your behalf.
* Click get started, then Go to Your Account.
* When you login to your account, you will see an Account SID and Auth Token field. Click on the lock icon in front of the Auth Token field to reveal the value. Make note of these two values. You will need them for the Python code.

## Twilio Notes
* Twilio makes sending SMS / MMS messages simple by managing the connections with all of the different mobile providers for you. Software developers can use a simple Python API / SDK to request that a message be sent and the Twilio service takes care of the rest.
* Twilio service prepends “Sent from a Twilio Trial account” to trial account messages.
* the service is free as long as you are sending 250 messages or less per month.

## Credits
* Nick Chemsak

## License
[MIT License] (https://github.com/nchemsak/doorbell_dash_angularJS/blob/master/LICENSE)


