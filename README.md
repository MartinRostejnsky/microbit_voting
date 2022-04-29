# microbit_voting
A voting system for micro:bit.

## **INSTALLATION GUIDE:**

1. Make sure both programs (server&client) have the same radio channel set (3rd line, `radio.set_group({channel})`).
2. Install server.py to the device which you want to receive the answers.
3. Install client.py to all the devices you want to be able your voting devices.

## **CLIENT USAGE:**

1. Use the A and B buttons to choose between the answers.
2. Wait for the heart icon to show up (which indicates that voting has been started by the server).
3. Press both (A&B) buttons at the same time to send your selected answers to the server.
4. You still can change your answer until the server will end the voting proccess.

## **SERVER USAGE:**

1. Press the A button to start or end the voting proccess.
2. Press the B button to show the results of voting.
3. Ending the voting proccess before showing the results is highly recommended.

## **RADIO PROTOCOLS:**

1. `"enabled" 1` #Value sent by server to the client to signal the start of the voting proccess.
2. `"vote_recorded" {serial_number}` #Value sent by server to the client to signal the recorded vote.
3. `"answer" {answer}` #Value sent by client to server that contains the voter’s answer.

## **ADDITIONAL NOTES:**

1. If you want to change anything in either server or client, do so before downloading the program to your device, and don’t touch anything you don’t understand.
2. Try not to change anything outside the configuration section.
3. Note that any wrong manipulation with the codes may cause them not to work as intended or not to work at all!
4. DO NOT EVER try to simplify the code by removing the "0"s from empty lists. (They are there because of MicroBit not supporting empty arrays.)
5. If you turn your serial number transmission off, the server won’t accept your answers!
6. Recommended tool for installing the code is [Microsoft Makecode for micro:bit](https://makecode.microbit.org/#editor)
