#Equation is capped at 259 individual lines

import mido
mid = mido.MidiFile('Super Mario 64 - Medley.mid', clip=True)
alph = "abcdefghijklmnopqrstuvwz"

    
#Each note is an array with the following format: [note, start time (in ticks), duration]
notes = []
#Duration of a tick in milliseconds
tick_duration = 50000/ mid.ticks_per_beat
#Current time of note
currentNoteTime = 0
#Loop through mid and find notes
for i, track in enumerate(mid.tracks):
    for msg in track:
        note = False
        if type(msg) == mido.MetaMessage: #Contains tempo - deal with later
            pass
        try:
            msg.velocity
            note = True
        except AttributeError:
            #Not a note, do nothing
            pass
        if note == False:
            pass
        elif msg.type == 'set_tempo':
            tick_duration = msg.tempo / mid.ticks_per_beat
        elif msg.velocity != 0:
            #Create new note entry - [note, start time, ID, IDnum] - does not include duration as it is unknown at this point
            currentNoteTime += msg.time
            if len(notes) > 0:
                #Find the correct letter for the note from the previous note
                positionInStringOfLastLetter = alph.find(notes[-1][2])
                if positionInStringOfLastLetter == 23:
                    #Last letter was z, reset to a
                    letter = 'a'
                else:
                    #Increment letter by 1
                    letter = alph[positionInStringOfLastLetter + 1]
                for i in reversed(notes):
                    if i[2] == letter:
                        #Found a note with the same letter, increment ID
                        correctID = i[3] + 1
                        break
                else:
                    #No note with that letter found, add new note
                    correctID = 0
                    pass
                notes.append([msg.note, currentNoteTime, letter, correctID])
            else:
                
                notes.append([msg.note, currentNoteTime, 'a', 0])
        else: 
            # Note off event
            # Find the correct note in notes and add duration to it - [note, start time, ID, IDnum], duration
            currentNoteTime += msg.time
            for i in reversed(notes):
                if i[0] == msg.note:
                    #calculate duration of note
                    i.append(currentNoteTime - i[1])
                    break
            
print(notes)
factorToDivide = 6
# Create equations for each note
joinMessageFactory = []
for j in notes:
    if j[3] == 0:
        joinMessageFactory.append([j[2]])
        equation = "{} = {}\\left\\".format(j[2], round((j[0] / factorToDivide), 2)) + "{0<x<" + str(j[4] / 500) + "\\right\\}"
    else:
        joinMessageFactory.append([j[2], str(j[3])])
        equation = str(j[2]) + "_{" + str(j[3])+ "} = " + str(round((j[0] / factorToDivide), 2)) + "\\left\\{0<x<" + str(j[4] / 500) + "\\right\\}"
    with open("output.txt", "a") as output:
        output.write(equation + "\n")
# Create equation to join all the notes together
joinMessage = "join("
for i in joinMessageFactory:
    if len(i) == 1:
        joinMessage += i[0] + ","
    else:
        joinMessage += i[0] + "_{" +  i[1] + "},"
joinMessage += ")"
print(joinMessage)
            
    
