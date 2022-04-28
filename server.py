#Do not touch anything unless you know what you’re doing, and you have read readme.txt!


#Configuration
radio.set_group(69) #Radio channel
voting = False #Default state

#The rest of the code is not capable of user manipulation!

answers = [0]
voters = [0]

def toggle():
    global answers, voters, voting
    if voting == False:
        answers = [0]
        voters = [0]
        voting = True
        radio.send_value("enabled", 1)
        basic.show_icon(IconNames.YES)
        pause(100)
        basic.clear_screen()
    else:
        voting = False
        basic.show_icon(IconNames.NO)
        pause(100)
        basic.clear_screen()

def show_results():
    variants = [0]
    for i in answers:
        if i not in variants:
            variants.append(i)
    for j in variants:
        if j != 0:
            basic.show_string(String.from_char_code(j))
            pause(250)
            basic.show_number(answers.count(j))
            pause(250)

def on_received_value(name, value):
    global voters,answers
    if name == "answer":
        if radio.received_packet(RadioPacketProperty.SERIAL_NUMBER) != 0:
            print(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
            print(value)
            if radio.received_packet(RadioPacketProperty.SERIAL_NUMBER) in voters:
                answers[voters.index(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))] = value
            else:
                voters.append(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
                answers.append(value)
        radio.send_value("vote_recorded", radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))

radio.on_received_value(on_received_value)
input.on_button_pressed(Button.A,toggle)
input.on_button_pressed(Button.B,show_results)