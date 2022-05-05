#Do not touch anything unless you know what you're doing, and you have read readme.txt!

#Configuration
radio.set_group(69) #Radio channel
radio.set_transmit_serial_number(True) #Serial number transmit, MUST BE TRUE FOR SERVER TO ACCEPT YOUR VOTE!
answer = 0 #Default answer, changes NOT recommended!
options = 4 #Number of options, HAS TO BE BIGGER THAN 0, maximal recommended number is number of letters in alphabet(26)!

#The rest of the code is not capable of user manipulation!

enabled = 0
basic.show_icon(IconNames.NO)

def on_button_pressed_a():
    global answer
    if answer == 0:
        answer = options-1
    else:
        answer -= 1
    basic.show_string(String.from_char_code(answer+65))

def on_button_pressed_b():
    global answer
    answer = (answer+1) % options
    basic.show_string(String.from_char_code(answer+65))

def on_button_pressed_ab():
    if enabled == 1:
        radio.send_value("vote", answer+1)
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    pause(100)
    basic.show_icon(IconNames.HEART)
    pause(100)
    basic.show_string(String.from_char_code(answer+65))

def on_received_value(name, value):
    global enabled
    if name == "enabled":
        enabled = value
        basic.show_icon(IconNames.HEART)
        pause(100)
        basic.show_string(String.from_char_code(answer+65))
    if name == "ack":
        print(value)

radio.on_received_value(on_received_value)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.A, on_button_pressed_a)
