from collections import namedtuple

modes_prompt = ('Mode options:\n'
                '  (Ionian)\n'
                '  (Dorian)\n'
                '  (Phrygian)\n'
                '  (Lydian)\n'
                '  (Mixolydian)\n'
                '  (Aeolian)\n'
                '  (Locrian)\n'
                '\n'
                'Enter mode: ')

mode_list = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']

#    Ionian

ionian_degrees = ('1', '2', '3', '4', '5', '6', '7')
ionian_semitones = (2, 2, 1, 2, 2, 2, 1)

ionian_mode_prompt = ('Ionian Mode:\n'
                      '\n'
                      'The Ionian Mode is the most common mode of them all. This is because it\'s the mode that\n'
                      'naturally occurs when you play through a Major scale. Without knowing anything about\n'
                      'modes, it\'s pretty easy to accidentally create music within the Ionian Mode.\n'
                      'Ionian uses the first scale degree as the root note.\n'
                      '\n'
                      'The following are the Ionian degrees and semitones:\n'
                      '                       (1)    (1)\n'
                      'Degrees:  1 2 3 4 5 6 7 8 ==== 8 7 6 5 4 3 2 1\n'
                      '\n'
                      'Semitones: 2 2 1 2 2 2 1  ====  1 2 2 2 1 2 2\n'
                      '\n'
                      'This is 1 of the 3 \'Major\' scale modes and is often considered the 2nd happiest of the\n'
                      'modes, mostly because the 7th degree has a weird dissonance.\n\n')

ionian_mode_contents = namedtuple('ionian_mode_stuff', ('First', 'Second', 'Third', 'Fourth',
                                                        'Fifth', 'Sixth', 'Seventh'))
ionian_mode_stuff = ionian_mode_contents(2, 2, 1, 2, 2, 2, 1)

#    Dorian

dorian_degrees = ('1', '2', '\u266D3', '4', '5', '6', '\u266D7')
dorian_semitones = (2, 1, 2, 2, 2, 1, 2)

dorian_mode_prompt = ('Dorian Mode:\n'
                      '\n'
                      'The Dorian Mode uses the second scale degree as the root note. From what I\'ve read from\n'
                      'somewhere, it\'s similar to a natural minor scale, but it has a raised sixth instead.\n'
                      'Apparently, Simon and Garfunkel\'s "Scarborough Fair" was composed entirely in Dorian,\n'
                      'which gives it like an old, celtic vibe, but it also sounds really dreamy and chill.\n'
                      '\n'
                      'The following are the Dorian degrees and semitones:\n'
                      '                         (1)    (1)\n'
                      'Degrees:  1 2 \u266D3 4 5 6 \u266D7 8 ==== 8 \u266D7 6 5 4 \u266D3 2 1\n'
                      '\n'
                      'Semitones: 2 1  2 2 2 1  2  ====  2  1 2 2 2  1 2\n'
                      '\n'
                      'This is 1 of 4 \'minor\' scale modes and can be thought of as the happiest of the \'minor\'\n'
                      'modes.\n\n')

dorian_mode_contents = namedtuple('dorian_mode_stuff', ('First', 'Second', 'FlatThird', 'Fourth',
                                                        'Fifth', 'Sixth', 'FlatSeventh'))
dorian_mode_stuff = dorian_mode_contents(2, 1, 2, 2, 2, 1, 2)

#    Phrygian

phrygian_degrees = ('1', '\u266D2', '\u266D3', '4', '5', '\u266D6', '\u266D7')
phrygian_semitones = (1, 2, 2, 2, 1, 2, 2)

phrygian_mode_prompt = ('Phrygian Mode:\n'
                        '\n'
                        'The Phrygian Mode is similar to Dorian in how they both sound like natural minor scales,\n'
                        'but unlike Dorian, Phrygian has a lowered 2nd (as opposed to Dorian\'s raised 6th). This is\n'
                        'kind of interesting considering the Dorian scale degree being altered is the second degree\n'
                        'if you were to run through the scale backwards. The Phrygian Mode degree that gets altered\n'
                        'is also the second degree, but running through the scale normal AND it\'s lowered, not\n'
                        'raised. Not sure if that observation is important, but still a cool little thing anyway.\n'
                        '\n'
                        'The following are the Phrygian degrees and semitones:\n'
                        '                           (1)  (1)\n'
                        'Degrees:  1 \u266D2 \u266D3 4 5 \u266D6 \u266D7 8 == 8 \u266D7 \u266D6 5 4 \u266D3 \u266D2 1\n'
                        '\n'
                        'Semitones: 1  2  2 2 1  2  2  ==  2  2  1 2 2  2  1\n'
                        '\n'
                        'This is 1 of 4 \'minor\' scale modes and can be thought of as 3rd happiest of the \'minor\'\n'
                        'modes, or the 2nd \'heaviest\'.\n\n')

phrygian_mode_contents = namedtuple('phrygian_mode_stuff', ('First', 'FlatSecond', 'FlatThird',
                                                            'Fourth', 'Fifth', 'FlatSixth', 'FlatSeventh'))
phrygian_mode_stuff = phrygian_mode_contents(1, 2, 2, 2, 1, 2, 2)

#    Lydian

lydian_degrees = ('1', '2', '3', '\u266F4', '5', '6', '7')
lydian_semitones = (2, 2, 2, 1, 2, 2, 1)

lydian_mode_prompt = ('Lydian Mode:\n'
                      '\n'
                      'The Lydian Mode can be described as an \'almost\' Major scale that has a raised 4th. Which is\n'
                      'fitting considering that Lydian is the 4th mode. So just remember \'Lydian, 4th mode: Raised\n'
                      '4th\'.\n'
                      '\n'
                      'The following are the Lydian degrees and semitones:\n'
                      '                        (1)    (1)\n'
                      'Degrees:  1 2 3 \u266F4 5 6 7 8 ==== 8 7 6 5 \u266F4 3 2 1\n'
                      '\n'
                      'Semitones: 2 2 2  1 2 2 1  ====  1 2 2 1  2 2 2\n'
                      '\n'
                      'This is 1 of the 3 \'Major\' scale modes and is often considered THE happiest of the modes\n'
                      'because the 4th degree gets augmented into a regular 5th Major degree, which gives it a sense\n'
                      'of urgency and kind of a whimsical vibe.\n\n')

lydian_mode_contents = namedtuple('lydian_mode_stuff', ('First', 'Second', 'Third', 'SharpFourth',
                                                        'Fifth', 'Sixth', 'Seventh'))
lydian_mode_stuff = lydian_mode_contents(2, 2, 2, 1, 2, 2, 1)

#    Mixolydian

mixolydian_degrees = ('1', '2', '3', '4', '5', '6', '\u266D7')
mixolydian_semitones = (2, 2, 1, 2, 2, 1, 2)

mixolydian_mode_prompt = ('Mixolydian Mode:\n'
                          '\n'
                          'It\'s Major-sounding like Lydian, except it has a lowered 7th. In fact, it\'s literally\n'
                          'a Major scale but \u266D7. The flattened 7 gets rid of the dissonance that\'s often\n'
                          'created when using a normal 7th.\n'
                          'The flat 7 can give it a \'bluesy\' sound.\n'
                          '\n'
                          'The following are the Mixolydian degrees and semitones:\n'
                          '                        (1)    (1)\n'
                          'Degrees:  1 2 3 4 5 6 \u266D7 8 ==== 8 \u266D7 6 5 4 3 2 1\n'
                          '\n'
                          'Semitones: 2 2 1 2 2 1  2  ====  2  1 2 2 1 2 2\n'
                          '\n'
                          'This is 1 of the 3 \'Major\' scale modes and is often considered the 3rd happiest mode\n'
                          'because of that smoothed out 7th degree.\n\n')

mixolydian_mode_contents = namedtuple('mixolydian_mode_stuff', ('First', 'Second', 'Third', 'Fourth',
                                                                'Fifth', 'Sixth', 'FlatSeventh'))
mixolydian_mode_stuff = mixolydian_mode_contents(2, 2, 1, 2, 2, 1, 2)

#    Aeolian

aeolian_degrees = ('1', '2', '\u266D3', '4', '5', '\u266D6', '\u266D7')
aeolian_semitones = (2, 1, 2, 2, 1, 2, 2)

aeolian_mode_prompt = ('Aeolian Mode:\n'
                       '\n'
                       'Aeolian is a pretty swell fella, it\'s actually the exact notes you play when you\'re\n'
                       'switching to the relative minor scale of the Major scale you\'re working with.\n'
                       '\n'
                       'The following are the Aeolian degrees and semitones:\n'
                       '                          (1)    (1)\n'
                       'Degrees:  1 2 \u266D3 4 5 \u266D6 \u266D7 8 ==== 8 \u266D7 \u266D6 5 4 \u266D3 2 1\n'
                       '\n'
                       'Semitones: 2 1  2 2 1  2  2  ====  2  2  1 2 2  1 2\n'
                       '\n'
                       'This is 1 of the 4 \'minor\' modes and is identical to Natural Minor. Aeolian can be\n'
                       'thought of as the 2nd happiest of the \'minor\' modes (similar to how Ionian is the 2nd\n'
                       'happiest of the \'Major\' modes).\n\n')

aeolian_mode_contents = namedtuple('aeolian_mode_stuff', ('First', 'Second', 'FlatThird', 'Fourth',
                                                          'Fifth', 'FlatSixth', 'FlatSeventh'))
aeolian_mode_stuff = aeolian_mode_contents(2, 1, 2, 2, 1, 2, 2)

#    Locrian

locrian_degrees = ('1', '\u266D2', '\u266D3', '4', '\u266D5', '\u266D6', '\u266D7')
locrian_semitones = (1, 2, 2, 1, 2, 2, 2)

locrian_mode_prompt = ('Locrian Mode:\n'
                       '\n'
                       'Locrian is wack. Don\'t use Locrian. It\'s the only mode with a diminished 5th.\n'
                       '\n'
                       'The following are the Locrian degrees and semitones:\n'
                       '                            (1)\n'
                       'Degrees:  1 \u266D2 \u266D3 4 \u266D5 \u266D6 \u266D7 8\n'
                       '\n'
                       'Semitones: 1  2  2 1  2  2  2\n'
                       '\n'
                       'The darkest mode. 1 of the 4 \'minor\' modes. The relationship from the root to the now\n'
                       'diminished fifth makes it not at all ideal to use in tonal music, since the fifth should stay\n'
                       'natural or \'perfect\' for the use of a strong cadence. A flattened fifth already completely\n'
                       'removes the strongest possible cadence.\n\n')

locrian_mode_contents = namedtuple('locrian_mode_stuff', ('First', 'FlatSecond', 'FlatThird',
                                                          'Fourth', 'FlatFifth', 'FlatSixth', 'FlatSeventh'))
locrian_mode_stuff = locrian_mode_contents(1, 2, 2, 1, 2, 2, 2)
