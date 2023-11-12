interval_menu = ('Interval options:\n'
                 '  (Interval Basics) Lists interval basics.\n'
                 '  (Chord Basics) Shows the basics of how chords are created.\n'
                 '  (Chord Progressions) Shows how to build progressions and shows\n'
                 'some popular chord progressions.\n'
                 '  (Arpeggio Basics) Displays basic arpeggio stuff.\n'
                 '\n'
                 'Enter choice: ')

interval_list1 = ['Interval Basics', 'Chord Basics', 'Chord Progressions', 'Arpeggio Basics']

# Interval Basics

interval_basics = ('Interval Basics\n'
                   '\n'
                   'Below is a list of interval names, as well as their respective amount of\n'
                   'semitones from the root note:\n'
                   '\n'
                   'Perfect Unison: 0\n'
                   'Minor Second: 1\n'
                   'Major Second: 2\n'
                   'Minor Third: 3\n'
                   'Major Third: 4\n'
                   'Perfect Fourth: 5\n'
                   'Augmented Fourth/Diminished Fifth: 6\n'
                   'Perfect Fifth: 7\n'
                   'Minor Sixth: 8\n'
                   'Major Sixth: 9\n'
                   'Minor Seventh: 10\n'
                   'Major Seventh: 11\n'
                   'Octave: 12\n'
                   'Minor Ninth: 13\n'
                   'Major Ninth: 14\n'
                   'Minor Tenth: 15\n'
                   'Major Tenth: 16\n'
                   'Perfect Eleventh: 17\n'
                   'Augmented Eleventh/Diminished Twelfth: 18\n'
                   'Perfect Twelfth: 19\n'
                   'Minor Thirteenth: 20\n'
                   'Major Thirteenth: 21\n'
                   'Minor Fourteenth: 22\n'
                   'Major Fourteenth: 23\n'
                   '\n'
                   'Unison, Fourth, Fifth, and Octave are all considered perfect intervals, and the others after that\n'
                   'are essentially just stacked on top of the Octave\n\n')

# Chord Basics

chord_basics = ('Chord Basics:\n'
                '\n'
                'A \'chord\' is the result of playing 3 (or more) notes at once. Technically any 3 notes can\n'
                'create a chord, but they won\'t necessarily sound good or make any sense when notating/composing\n'
                'music. The creation of a chord with 3 notes, also known as a \'triad\', is achieved when you take\n'
                'the first, third, and fifth scale degrees and play those notes at once. For Major, the third is\n'
                'a normal, or \'natural\' third, but for Minor, the third gets flattened so instead of having\n'
                'a 1, 3, 5 foundation, you have 1, \u266D3, 5. For tonal music, the third scale degree makes a big\n'
                'difference in the way a chord sounds, and this is at a low-level form of chord-building, it only\n'
                'gets more complicated when you start implementing other intervals. But in general, you got Major and\n'
                'Minor chords that are created and built upon for whatever purpose is needed for the music.\n'
                '\n'
                'The primary chords of a scale are the 1, 4, and 5 scale degrees made into simple major chords.\n'
                'When it comes to frequencies, all of these are considered \'perfect\' solely because of the ratio\n'
                'they create when measuring the scale degree in comparison to all of the intervals. You don\'t\n'
                'necessarily need to know why or what makes those scale degrees perfect, but it IS important to know\n'
                'that they are like that. The 7th degree is naturally a diminished chord, and all the others are made\n'
                'into Minor chords.\n\n')

# Chord Progressions

chord_progs = ('Chord Progressions:\n'
               '\n'
               'The list below provides some common chord progressions to help with practicing improv or to serve\n'
               'as a basis for creating/composing some ideas:\n'
               '\n'
               'I-V-vi-IV\n'
               'I-IV-V-IV\n'
               'I-IV-V\n'
               'I-IV-V-V\n'
               'I-vi-IV-V\n'
               'I-ii-vi-V\n'
               'I-vi-ii-V\n'
               'I-iii-vi-V\n'
               'IV-V-IV\n'
               'I-iii-IV-vi\n'
               'I-IV-I-V\n'
               'I-I-IV-vi\n\n')

# Arpeggio Basics

arpeggio_basics = ('Arpeggio Basics:\n'
                   '\n'
                   'An arpeggio is just a chord, but each note rings out separate from each other instead of all\n'
                   'at once like in a regular chord. They are sometimes referred to as broken chords. In this version\n'
                   'of the program, no arpeggio tabs will be provided, but just know that a regular arpeggio follows\n'
                   'the 1,3,5 formula like a basic chord. All you gotta do to play a simple Major/Minor arpeggio is\n'
                   'play the corresponding scale degrees for whatever Major/Minor scale you\'re playing (1,3,5 for\n'
                   'Major; 1,\u266D3,5 for Minor).\n\n')

# More Intervals

more_intervals_menu = ('More interval options:\n'
                       '  (Circles) Shows Circle of Fifths/Fourths.\n'
                       '  (Orders) Shows Order of Sharps/Flats.\n'
                       '\n'
                       'Enter choice: ')

interval_list2 = ['Circles', 'Orders']

# Circles

circles_prompt = ('Circle of Fifths/Fourths\n'
                  '\n'
                  'The Circle of Fifths/Fourths is a very convenient way to navigate through different keys and such.\n'
                  'When practicing guitar patterns, a good way to get more comfortable with playing things in\n'
                  'different spots along the fretboard is by circling around the circle to get to the next root note\n'
                  'of a key.\n'
                  'The circle typically has C at the 12 o\'clock position because it has no sharps or flats, and then\n'
                  'goes around the circle like a clock to get to the next key that increments the number of sharps or\n'
                  'flats by one. If you go clockwise on the circle, the \'fifth\' degree of C is the next key in the\n'
                  'sequence, which is G. Taking a closer look at the key of G will reveal it has 1 sharp note within\n'
                  'the scale. On the contrary, if you were to go counter-clockwise on the circle, the next note would\n'
                  'be F. F is the \'fourth\' scale degree of C so going backwards within the circle is now a fourth,\n'
                  'instead of a fifth. That\'s the only difference between the two circles, the direction in which it\n'
                  'goes. When going counter-clockwise to F, the numbers of flats get incremented.\n'
                  'Forwards is sharps, backwards is flats. Visually, the flats are on the left side of the circle;\n'
                  'the sharps are on the right.\n'
                  '\n'
                  'The notes going clockwise are:\n'
                  'C, G, D, A, E, B, F\u266F, D\u266D, A\u266D, E\u266D, B\u266D, F\n'
                  '\n'
                  'The notes counter-clockwise are:\n'
                  'C, F, B\u266D, E\u266D, A\u266D, D\u266D, F\u266F, B, E, A, D, G\n\n')

# Orders

orders_prompt = ('Order of Sharps/Flats\n'
                 '\n'
                 'The Order of Sharps and Flats is similar to how the Circle of Fifths goes clockwise and counter-\n'
                 'clockwise. A simple way to find the number of sharps/flats of a key without having to run through\n'
                 'the circle is by using a little system that starts on F of the circle and goes clockwise for\n'
                 'the order of sharps. On paper, it goes F, C, G, D, A, E, B. A mnemonic device for this is Fat Cats\n'
                 'Go Down Alleys Eating Birds. Starting from C on the list, you would number each note incrementing\n'
                 'by 1 starting from 0, which is C because it has no sharps or flats. Once you loop around to the\n'
                 'beginning, you would just continue numbering \'til you hit 7 (the amount of notes within a scale).\n'
                 'The 7 would fall on C again, but when looping around, you also assign a sharp to the note of the\n'
                 'sequence, which for 6 and 7 is F and C. The F now becomes F\u266F having 6 sharps. C\u266F has 7,\n'
                 'or \'all\' notes sharpened. Now when you\'re looking at the note\'s number, you just include that\n'
                 'amount of characters when reading the sequence. C has none, so you would move on to the next\n'
                 'note in the sequence, which is G. Because G\'s number is 1, you read only 1 character starting from\n'
                 'the beginning of the sequence, which is F. The key of G has 1 sharp, and that sharp lands on F.\n'
                 'Please note that these exact examples only work for major keys, although could probably work in\n'
                 'minor with some tweaks.\n'
                 '                  (F\u266F)(C\u266F)\n'
                 'Order of Sharps:   F   C   G   D   A   E   B\n'
                 '                   6   0   1   2   3   4   5\n'
                 '                      (7)\n'
                 'Now for the Order of Flats, the sequence is reversed. but read the same.\n'
                 '                   \u266D   \u266D   \u266D   \u266D   \u266D\n'
                 'Order of Flats:    B   E   A   D   G   C   F\n'
                 '                   2   3   4   5   6   0   1\n'
                 '                                      (7)\n'
                 '\n'
                 'F Major has 1 flat, which is B\u266D, B\u266D Major has 2, which are B\u266D and E\u266D, etc.\n\n')
