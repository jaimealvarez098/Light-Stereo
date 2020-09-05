import time
import board
import digitalio
import pulseio
import Songs as s
import Songs2 as s2

#initializing RGBLED, piezo buzzers and button pins
red = digitalio.DigitalInOut(board.D8)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.D9)
green.direction = digitalio.Direction.OUTPUT
blue = digitalio.DigitalInOut(board.D10)
blue.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.D2)
button.direction =  digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
button2 = digitalio.DigitalInOut(board.D13)
button2.direction =  digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN
button3 = digitalio.DigitalInOut(board.D4)
button3.direction =  digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN
button4 = digitalio.DigitalInOut(board.D5)
button4.direction =  digitalio.Direction.INPUT
button4.pull = digitalio.Pull.DOWN
button5 = digitalio.DigitalInOut(board.D6)
button5.direction =  digitalio.Direction.INPUT
button5.pull = digitalio.Pull.DOWN
button6 = digitalio.DigitalInOut(board.D7)
button6.direction =  digitalio.Direction.INPUT
button6.pull = digitalio.Pull.DOWN
buzzer = pulseio.PWMOut(board.D3,variable_frequency = True)

#captures frequency of each note/cord

#Linkin Park - In Then End: divide by 4
#Jingle Bells: Divide by 8
#Mario songs: Divide by 11
time_duration = 0
while True:
    #if button 3 is pressed, play Linkin park
    if button3.value == True:
        while time_duration < len(s.LinkinPark_InTheEnd.notes):
            buzzer.duty_cycle = 2**15
            beat_duration = s.LinkinPark_InTheEnd.beats[time_duration]/4
            #play buzzer
            buzzer.frequency = s.LinkinPark_InTheEnd.notes[time_duration]
            
            #if button1 is pressed, pause the music
            if button.value == True:
                while True:
                    red.value = False
                    blue.value = False
                    green.value = False
                    buzzer.duty_cycle = 0
                    #if button2 is pressed, unpause the song
                    if button2.value == True: break

            #display LEDs
            else:
                if buzzer.frequency == 100:
                    buzzer.duty_cycle = 0
                    time.sleep(beat_duration)
                #Jingle Bells = 170
                #Linkin Park = 500
                elif buzzer.frequency < 350:
                    red.value = True
                    time.sleep(beat_duration)
                    red.value = False
                #Jingle Bells 170 and 600
                elif buzzer.frequency >= 350 and buzzer.frequency < 850:
                    green.value = True
                    time.sleep(beat_duration)
                    green.value = False
                else:
                    blue.value = True
                    time.sleep(beat_duration)
                    blue.value = False
                buzzer.duty_cycle = 0
                time_duration+=1

    elif button4.value == True:
        while time_duration < len(s.JingleBells.notes):
            buzzer.duty_cycle = 2**15
            beat_duration = s.JingleBells.beats[time_duration]/8
            #play buzzer
            buzzer.frequency = s.JingleBells.notes[time_duration]

            if button.value == True:
                while True:
                    red.value = False
                    blue.value = False
                    green.value = False
                    buzzer.duty_cycle = 0
                    if button2.value == True: break

            #display LEDs
            else:
                if buzzer.frequency == 100:
                    time.sleep(beat_duration)
                    buzzer.duty_cycle = 0
                #Jingle Bells = 170
                #Linkin Park = 500
                elif buzzer.frequency < 250:
                    red.value = True
                    time.sleep(beat_duration)
                    red.value = False
                #Jingle Bells 170 and 600
                elif buzzer.frequency >= 350 and buzzer.frequency < 850:
                    green.value = True
                    time.sleep(beat_duration)
                    green.value = False
                else:
                    blue.value = True
                    time.sleep(beat_duration)
                    blue.value = False
                buzzer.duty_cycle = 0
                time_duration+=1

    elif button5.value == True:
        while time_duration < len(s2.Mario_main.notes):
            buzzer.duty_cycle = 2**15
            beat_duration = s2.Mario_main.beats[time_duration]/12
            #play buzzer
            buzzer.frequency = s2.Mario_main.notes[time_duration]

            if button.value == True:
                while True:
                    red.value = False
                    blue.value = False
                    green.value = False
                    buzzer.duty_cycle = 0
                    if button2.value == True: break

            #display LEDs
            else:
                if buzzer.frequency == 100:
                    buzzer.duty_cycle = 0
                    time.sleep(beat_duration)
                #Jingle Bells = 170
                #Linkin Park = 500
                elif buzzer.frequency < 350:
                    red.value = True
                    time.sleep(beat_duration)
                    red.value = False
                #Jingle Bells 170 and 600
                elif buzzer.frequency >= 350 and buzzer.frequency < 800:
                    green.value = True
                    time.sleep(beat_duration)
                    green.value = False
                else:
                    blue.value = True
                    time.sleep(beat_duration)
                    blue.value = False
                buzzer.duty_cycle = 0
                time_duration+=1


    elif button6.value == True:
        while time_duration < len(s2.Mario_Underworld.notes):
            buzzer.duty_cycle = 2**15
            beat_duration = s2.Mario_Underworld.beats[time_duration]/11
            #play buzzer
            buzzer.frequency = s2.Mario_Underworld.notes[time_duration]

            if button.value == True:
                while True:
                    red.value = False
                    blue.value = False
                    green.value = False
                    buzzer.duty_cycle = 0
                    if button2.value == True: break

            #display LEDs
            else:
                if buzzer.frequency == 100:
                    buzzer.duty_cycle = 0
                    time.sleep(beat_duration)
                #Jingle Bells = 170
                #Linkin Park = 500
                elif buzzer.frequency < 350 and buzzer.frequency >250:
                    red.value = True
                    time.sleep(beat_duration)
                    red.value = False
                #Jingle Bells 170 and 600
                elif buzzer.frequency >= 350 and buzzer.frequency < 850:
                    green.value = True
                    time.sleep(beat_duration)
                    green.value = False
                else:
                    blue.value = True
                    time.sleep(beat_duration)
                    blue.value = False
                time_duration+=1
                buzzer.duty_cycle = 0

    time_duration = 0
