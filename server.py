#Do not touch anything unless you know what you're doing, and you have read readme.txt!

#Configuration
radio.set_group(69) #Radio channel
voting = False #Default state

#The rest of the code is not capable of user manipulation!

answers: any = []
voters: any = []

def toggle():
    global answers, voters, voting
    if voting == False:
        answers = []
        voters = []
        voting = True
        radio.send_value("enabled", 1)
        basic.show_icon(IconNames.YES)
        pause(100)
        basic.clear_screen()
    else:
        radio.send_value("enabled", 0)
        voting = False
        basic.show_icon(IconNames.NO)
        pause(100)
        basic.clear_screen()

def show_results():
    variants: any = []
    for i in answers:
        if i not in variants:
            variants.append(i)
    for j in variants:
        basic.show_string(String.from_char_code(j+65))
        pause(250)
        basic.show_number(answers.count(j))
        pause(250)

def on_received_value(name, value):
    global voters,answers
    if name == "vote":
        if voting == True:
            if radio.received_packet(RadioPacketProperty.SERIAL_NUMBER) != 0:
                print(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
                print(value)
                if radio.received_packet(RadioPacketProperty.SERIAL_NUMBER) in voters:
                    answers[voters.index(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))] = value
                else:
                    voters.append(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
                    answers.append(value)
            radio.send_value("ack", radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
            music.play_tone(Note.C, music.beat(1))

radio.on_received_value(on_received_value)
input.on_button_pressed(Button.A,toggle)
input.on_button_pressed(Button.B,show_results)
