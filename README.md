# MIDI-to-Desmos
A simple python scipt to convert an MIDI file to a desmos graph. 

# How to use
1. Replace pathOfMidi in desmos.py to contain the path of the MIDI file then run the file
2. Open output.txt
3. Paste all of the individual note equations into a folder in desmos
4. Paste the join message into a new desmos line after the folder
5. Set the y axis to be from 329 to 659 (Currently broken, skip this step)
# Current limitations
* Note values are not accurate - will fix by converting to hz and then to desmos (currently working on)
* Program is laggy above ~250 notes
