import chords as c

whole_note = 8
half_note = 4
quarter_note = 2
eight_note = 1
half_rest = 4
quarter_rest = 2
whole_rest = 8

class Mario_Underworld:
    notes = [c.C4,c.C5,c.A3,c.A4,
             c.A_sharp3,c.A_sharp4, 100,
             100,
             c.C4,c.C5,c.A3,c.A4,
             c.A_sharp3,c.A_sharp4,100,
             100,
             c.F3,c.F4,c.D3,c.D4,
             c.D_sharp3,c.D_sharp4,100,
             100,
             c.F3,c.F4,c.D3,c.D4,
             c.D_sharp3,c.D_sharp4,100,
             100,c.D_sharp4,c.C_sharp4,c.D4,
             c.C_sharp4,c.D_sharp4,
             c.D_sharp4,c.G_sharp3,
             c.G_sharp3,c.C_sharp4,
             c.C4,c.F_sharp4,c.F4,c.E3,c.A_sharp4,c.A4,
             c.G_sharp4,c.D_sharp4,c.B3,
             c.A_sharp3,c.A3,c.G_sharp3,
             100,100,100]

    beats = [quarter_note,quarter_note,quarter_note,quarter_note,
             quarter_note,quarter_note, half_rest,
             whole_rest,
             quarter_note,quarter_note,quarter_note,quarter_note,
             quarter_note,quarter_note,half_rest,
             whole_rest,
             quarter_note,quarter_note,quarter_note,quarter_note,
             quarter_note,quarter_note,half_rest,
             whole_rest,
             quarter_note,quarter_note,quarter_note,quarter_note,
             quarter_note,quarter_note, half_rest,
             half_rest, quarter_note,quarter_note,quarter_note,
             half_note,half_note,
             half_note,half_note,
             half_note,half_note,
             quarter_note,quarter_note,quarter_note,quarter_note,quarter_note,quarter_note,
             half_note,half_note,half_note,
             half_note,half_note,half_note,
             whole_rest,whole_rest,whole_rest]


class Mario_main:
    notes = [c.E6,c.E6,100,c.E6,
             100,c.C6,c.E6,100,
             c.G6,100,100,100,
             c.G5,100,100,100,
             c.C6,100,100, c.G5,
             100,100,c.E5,100,
             100,c.A5,100,c.B5,
             100,c.A_sharp5,100,c.A5,
             c.G5,c.E6,c.G6,
             c.A6,100,c.F6,c.G6,
             100,c.E6,100,c.G6,
             c.D6,c.B5,100,100]

    beats = [quarter_note,quarter_note,2,quarter_note,
             2,quarter_note,quarter_note,2,
             quarter_note,2,2,2,
             quarter_note,2,2,2,
             quarter_note,2,2,quarter_note,
             2,2,quarter_note,2,
             2,quarter_note,2,quarter_note,
             2,quarter_note,2,quarter_note,
             quarter_note,quarter_note,quarter_note,
             quarter_note,2,quarter_note,quarter_note,
             2,quarter_note,2,quarter_note,
             quarter_note,quarter_note,2,2]
