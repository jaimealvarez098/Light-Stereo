import chords as c
all_notes = [c.C1,c.C_sharp1,c.D1,c.D_sharp1,c.E1,c.F1,c.F_sharp1,c.G1,c.G_sharp1,c.A1,c.A_sharp1,c.B1,
    c.C2,c.C_sharp2,c.D2,c.D_sharp2,c.E2,c.F2,c.F_sharp2,c.G2,c.G_sharp2,c.A2,c.A_sharp2,c.B2,
    c.C3,c.C_sharp3,c.D3,c.D_sharp3,c.E3,c.F3,c.F_sharp3,c.G3,c.G_sharp3,c.A3,c.A_sharp3,c.B3,
    c.C4,c.C_sharp4,c.D4,c.D_sharp4,c.E4,c.F4,c.F_sharp4,c.G4,c.G_sharp4,c.A4,c.A_sharp4,c.B4,
    c.C5,c.C_sharp5,c.D5,c.D_sharp5,c.E5,c.F5,c.F_sharp5,c.G5,c.G_sharp5,c.A5,c.A_sharp5,c.B5,
    c.C6,c.C_sharp6,c.D6,c.D_sharp6,c.E6,c.F6,c.F_sharp6,c.G6,c.G_sharp6,c.A6,c.A_sharp6,c.B6,100]
#determining what kind of note is being played to check
#how long we have to play the note for
whole_note = 8
half_note = 4
quarter_note = 2
eight_note = 1
half_rest = 4
quarter_rest = 2
whole_rest = 8
eight_break = 1

#Linkin Park: In The End
class LinkinPark_InTheEnd:
    #The song
    notes = [c.D5,c.A5,c.A5,c.F5,
            c.E5,c.E5,c.E5,c.E5,c.F6,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,c.E5,c.E5,c.E5,c.F6,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,c.E5,c.E5,c.E5,c.F6,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,100,c.A5,c.A5,c.A_sharp5,
            c.E4,
            c.A4,c.F4,
            c.E4,
            c.D4,c.A4,c.F4,c.A_sharp4,
            c.E4,
            c.A4,c.F4,
            c.E4,
            c.D4,c.A4,c.A4,c.A4,c.B4,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,c.E5,c.E5,c.E5,c.F6,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,c.E5,c.E5,c.E5,c.F6,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,c.E5,c.E5,c.E5,c.F6,
            c.D5,c.A5,c.A5,c.F5,
            c.E5,100,c.A5,c.C5,c.D5,
            c.E4,c.E5,c.E5,c.C5,c.C5,
            c.C5,c.C4,c.D5,c.E5,
            c.E4,
            c.D5,c.E5,c.D5,c.E5,c.F4,c.E4,
            c.F4,c.F4,c.F5,c.C5,c.D5]

    beats = [quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note, quarter_note, quarter_note, eight_note, eight_note,
        quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note, quarter_note, quarter_note, eight_note, eight_note,
        quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note, quarter_note, quarter_note, eight_note, eight_note,
        quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note,1, eight_note, quarter_note, quarter_note,
        whole_note,
        half_note, quarter_note,
        whole_note,
        half_note, quarter_note, eight_note, eight_note,
        whole_note,
        half_note, quarter_note,
        whole_note,
        quarter_note,eight_note,quarter_note,eight_note,eight_note,
        quarter_note,quarter_note,quarter_note,quarter_note,
        quarter_note, quarter_note, quarter_note, eight_note, eight_note,
        quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note, quarter_note, quarter_note, eight_note, eight_note,
        quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note, quarter_note, quarter_note, eight_note, eight_note,
        quarter_note, quarter_note, quarter_note, quarter_note,
        quarter_note,1,eight_note,quarter_note,quarter_note,
        quarter_note,eight_note,eight_note,eight_note,eight_note,
        half_note,eight_note,eight_note,eight_note,eight_note,
        quarter_note,
        eight_note,eight_note,eight_note,eight_note,eight_note,eight_note,
        eight_note,eight_note,eight_note,quarter_note,quarter_note]#43

class JingleBells:
    notes = [c.E3,c.E3,c.E3,
             c.E3,c.E3,c.E3,
             c.E3,c.C5,c.D4,c.E3,
             c.E3,
             c.F4,c.F4,c.F4,c.F4,
             c.F4,c.E3,c.E3,c.E3,c.E3,
             c.E3,c.D2,c.D4,c.E3,
             c.D2,c.G5,
             c.E3,c.E3,c.E3,
             c.E3,c.E3,c.E3,
             c.E3,c.C5,c.D2,c.D2,
             c.E3,
             c.F4,c.F4,c.F4,c.F4,
             c.F4,c.E3,c.E3,c.E3,c.E3,
             c.G5,c.G5,c.F4,c.D2,
             c.C3,
             c.G6,c.E6,c.D6,c.G6,
             c.G6,c.G6,c.G6,
             c.G6,c.E5,c.D5,c.C5,
             c.A2,
             c.A3,c.F4,c.E4,c.D5,
             c.B2,
             c.G5,c.G5,c.F4,c.D4,
             c.E2,
             c.G6,c.E6,c.D6,c.G6,
             c.G6,c.G6,c.G6,
             c.G6,c.E5,c.D5,c.C5,
             c.A2,
             c.A3,c.F4,c.E4,c.D5,
             c.G3,c.G3,c.G3,c.G3,c.G3,
             c.A3,c.G4,c.F4,c.D5,
             c.C3]

    beats = [2,2,4,2,2,4,2,2,3,1,8,2,2,3,1,2,2,2,1,1,2,2,2,2,4,4,2,2,4,2,2,4, #32
            2,2,3,1,8,2,2,3,1,2,2,2,1,1,2,2,2,2,8,2,2,2,2,6,1,1,2,2,2,2,8,2,2,2,2, #35
            8,2,2,2,2,8,2,2,2,2,6,1,1,2,2,2,2,8,2,2,2,2,2,2,2,1,1,2,2,2,2,8] #27
