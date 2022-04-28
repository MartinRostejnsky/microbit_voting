# microbit_voting
A voting system for MicroBit.

###

INSTALLATION GUIDE:

1. Make sure both programs (server&client) have the same radio channel set (3rd line, "radio.set_group({channel})").
2. Install server.py to the device which you want to receive the answers.
3. Install client.py to all the devices you want to be able your voting devices.

###

CLIENT USAGE:

Use the A and B buttons to choose between the answers.
Wait for the heart icon to show up (which indicates that voting has been started by the server).
Press both (A&B) buttons at the same time to send your selected answers to the server.
You still can change your answer until the server will end the voting proccess.

###

SERVER USAGE:

Press the A button to start or end the voting proccess.
Press the B button to show the results of voting.
Ending the voting proccess before showing the results is highly recommended.

###

RADIO PROTOCOLS:

"enabled" 1 #Value sent by server to the client to signal the start of the voting proccess.
"vote_recorded" {serial_number} #Value sent by server to the client to signal the recorded vote.
"answer" {answer} #Value sent by client to server that contains the voter’s answer.

###

ADDITIONAL NOTES:

1. If you want to change anything in either server or client, do so before downloading the program to your device, and don’t touch anything you don’t understand.
2. Try not to change anything outside the configuration section.
3. Note that any wrong manipulation with the codes may cause them not to work as intended or not to work at all!
4. DO NOT EVER try to simplify the code by removing the "0"s from empty lists. (They are there because of MicroBit not supporting empty arrays.)
5. If you turn your serial number transmission off, the server won’t accept your answers!
