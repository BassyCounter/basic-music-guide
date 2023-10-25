from collections import namedtuple


def formatted_scale_degrees():
    format_string = '{scale:20} {degrees:20}'
    print(format_string.format(scale='Scale Name', degrees='Scale Degrees'))
    print('-' * 40)
    print(format_string.format(scale='Major', degrees='1 2 3 4 5 6 7'))
    print()
    print(format_string.format(scale='Major Pentatonic', degrees='1 2 3 5 6'))
    print()
    print(format_string.format(scale='Minor', degrees='1 2 \u266D3 4 5 \u266D6 \u266D7'))
    print()
    print(format_string.format(scale='Melodic Minor', degrees='1 2 \u266D3 4 5 6 7'))
    print()
    print(format_string.format(scale='Harmonic Minor', degrees='1 2 \u266D3 4 5 \u266D6 7'))
    print()
    print(format_string.format(scale='Minor Pentatonic', degrees='1 \u266D3 4 5 \u266D7'))
    print()


scales_prompt = ('Scale options:\n'
                 '  (Major)\n'
                 '  (Major Pentatonic)\n'
                 '  (Minor)\n'
                 '  (Melodic Minor)\n'
                 '  (Harmonic Minor)\n'
                 '  (Minor Pentatonic)\n'
                 '  (Scale Degrees)\n'
                 '\n'
                 'Enter scale: ')

scale_list = ['Major', 'Major Pentatonic', 'Minor', 'Melodic Minor', 'Harmonic Minor', 'Minor Pentatonic',
              'Scale Degrees']

#    Major Scale

major_steps = ('Whole', 'Whole', 'Half', 'Whole', 'Whole', 'Whole', 'Half')
simple_major_steps = ('W', 'W', 'H', 'W', 'W', 'W', 'H')
major_degrees = ('1', '2', '3', '4', '5', '6', '7')
major_scale_num = 7
major_semitones = (2, 2, 1, 2, 2, 2, 1)

major_scale_prompt = ('The Major Scale:\n'
                      '\n'
                      'The Major Scale is the most important scale within music theory.\n'
                      '\n'
                      'The formula for the Major Scale is as follows:\n'
                      '\n'
                      'Whole, Whole, Half, Whole, Whole, Whole, Half\n'
                      '\n'
                      'or for simplicity\'s sake,\n'
                      '\n'
                      'W, W, H, W, W, W, H\n'
                      '\n'
                      'The scale degrees of a major scale are pretty straightforward:\n'
                      '1, 2, 3, 4, 5, 6, 7\n'
                      '\n'
                      'The semitones BETWEEN each scale degree, which can be thought of as the amount of frets\n'
                      'shifted to or from along the fretboard of a guitar, are equal in value to steps (a whole step\n'
                      'would be 2 semitones and a half step would be 1 semitone):\n'
                      '2, 2, 1, 2, 2, 2, 1\n'
                      '\n'
                      'The number of notes within the major scale is 7 which is pretty standard for common scales.\n'
                      'One way to think of it is the amount of notes counted ascending/descending from a root within\n'
                      'the Chromatic Scale up until the octave is 12. The number of notes within the major scale (7)\n'
                      'is almost exactly half of the number of Chromatic Scale notes (12), which ideally would be 14,\n'
                      'but because B/C and E/F don\'t have any notes in between them, 2 is subtracted from the 14 (1\n'
                      'for B/C, 1 for E/F), thus leaving us with 12. Even though we only have 12 chromatic notes\n'
                      'instead of 14, it\'s still good to correlate scales of 7 notes with half of 14 because chords\n'
                      'tend to use every other note for chord building and arpeggios are essentially the same (more\n'
                      'on that elsewhere).\n'
                      '\n'
                      'Ascending and descending using the Major Scale looks like this:\n'
                      '                            (1)    (1)\n'
                      'Scale Degrees: 1 2 3 4 5 6 7 8 ==== 8 7 6 5 4 3 2 1\n'
                      '\n'
                      'Semitones:      2 2 1 2 2 2 1  ====  1 2 2 2 1 2 2\n'
                      '\n'
                      'This is the Major Scale pattern on guitar:\n'
                      '\n'
                      'E|--7|--1|---|--2|\n'
                      ' |   |   |   |   |\n'
                      'B|---|--5|---|--6|\n'
                      ' |   |   |   |   |\n'
                      'G|--2|---|--3|--4|\n'
                      ' |   |   |   |   |\n'
                      'D|--6|---|--7|--1|\n'
                      ' |   |   |   |   |\n'
                      'A|--3|--4|---|--5|\n'
                      ' |   |   |   |   |\n'
                      'E|---|--1|---|--2|\n\n')

major_scale_contents = namedtuple('major_scale_stuff', ('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth',
                                                        'Seventh'))
major_scale_stuff = major_scale_contents(2, 2, 1, 2, 2, 2, 1)

#    Major Pentatonic

major_penta_steps = ('Whole', 'Whole', 'Whole + Half', 'Whole', 'Whole + Half')
simple_major_penta_steps = ('W', 'W', 'W+H', 'W', 'W+H')
major_penta_degrees = ('1', '2', '3', '5', '6')
major_penta_scale_num = 5
major_penta_semitones = (2, 2, 3, 2, 3)

major_penta_scale_prompt = ('The Major Pentatonic Scale:\n'
                            '\n'
                            'The Major Pentatonic Scale can be thought of as the Major Scale, but without the\n'
                            '4th and 7th scale degrees of the Major Scale. Your basic scale typically has 7 scale\n'
                            'degrees. However, with this scale being \'penta\' tonic, there are only 5 scale degrees.\n'
                            '\n'
                            'The formula for the Major Pentatonic Scale is as follows:\n'
                            '\n'
                            'Whole, Whole, Whole + Half, Whole, Whole + Half\n'
                            '\n'
                            'or for simplicity\'s sake,\n'
                            '\n'
                            'W, W, W+H, W, W+H\n'
                            '\n'
                            'The scale degrees of the Major Pentatonic Scale only differentiate from the Major\n'
                            'Scale by removing the 4th and 7th scale degrees:\n'
                            '1, 2, 3, 5, 6\n'
                            '\n'
                            'The semitones between each scale degree:\n'
                            '2, 2, 3, 2, 3\n'
                            '\n'
                            'I don\'t know a whole lot about the Major Pentatonic Scale, but from what I do, the 5\n'
                            'remaining scale degrees are the more likeable ones, the ones that most people tend to\n'
                            'use when creating music. The fourth scale degree within a normal scale can be used to\n'
                            'create a Plagal Cadence when resolving to the root in a chord progression. The fifth\n'
                            'scale degree within a normal scale can be used to create a Perfect Cadence instead,\n'
                            'which naturally has a stronger resolution than a Plagal Cadence because of that slight\n'
                            'difference in semitones (the distance is bigger). Because of that, it makes sense to\n'
                            'choose the \'Dominant\' cadence of the two, which could be why the fourth was removed\n'
                            'from the Major Pentatonic. The seventh scale degree is usually really bizarre to base\n'
                            'intervals off of, so I can see how it was also removed from the Major Pentatonic.\n'
                            '\n'
                            'Ascending and descending using the Major Pentatonic Scale looks like this:\n'
                            '                        (1)    (1)\n'
                            'Scale Degrees: 1 2 3 5 6 8 ==== 8 6 5 3 2 1\n'
                            '\n'
                            'Semitones:      2 2 3 2 3        3 2 3 2 2\n'
                            '\n'
                            'This is the Major Pentatonic Scale pattern on guitar:\n'
                            '\n'
                            'E|---|--1|---|--2|\n'
                            ' |   |   |   |   |\n'
                            'B|---|--5|---|--6|\n'
                            ' |   |   |   |   |\n'
                            'G|--2|---|--3|---|\n'
                            ' |   |   |   |   |\n'
                            'D|--6|---|---|--1|\n'
                            ' |   |   |   |   |\n'
                            'A|--3|---|---|--5|\n'
                            ' |   |   |   |   |\n'
                            'E|---|--1|---|--2|\n\n')

major_penta_scale_contents = namedtuple('major_penta_scale_stuff', ('First', 'Second', 'Third', 'Fifth', 'Sixth'))
major_penta_scale_stuff = major_penta_scale_contents(2, 2, 3, 2, 3)

#    Minor Scale (Natural Minor)

minor_steps = ('Whole', 'Half', 'Whole', 'Whole', 'Half', 'Whole', 'Whole')
simple_minor_steps = ('W', 'H', 'W', 'W', 'H', 'W', 'W')
minor_degrees = ('1', '2', '\u266D3', '4', '5', '\u266D6', '\u266D7')
minor_scale_num = 7
minor_semitones = (2, 1, 2, 2, 1, 2, 2)

minor_scale_prompt = ('The Natural Minor Scale:\n'
                      '\n'
                      'The Natural Minor Scale is the basis of all minor scales.\n'
                      'The Minor scales have a sadder vibe to them as opposed to Major scales.\n'
                      'If you\'re wanting to create music that\'s a bit more dramatic and sharp, you might would\n'
                      'be inclined to use a scale that\'s Minor based. The main difference between Major and Minor is\n'
                      'that in Major, the distance from the root to the 3rd is a Major interval, whereas with Minor,\n'
                      'the distance from the root to the 3rd is a Minor interval. The root note in Natural Minor, for\n'
                      'lack of a better word, \'naturally\' creates a Minor triad when using the 1,3,5 degree formula\n'
                      'because of the flattened third.\n'
                      '\n'
                      'The formula for the Natural Minor Scale is as follows:\n'
                      '\n'
                      'Whole, Half, Whole, Whole, Half, Whole, Whole\n'
                      '\n'
                      'or for simplicity\'s sake,\n'
                      '\n'
                      'W, H, W, W, H, W, W\n'
                      '\n'
                      'The Natural Minor Scale is just like the Major Scale degrees, but with a flattened third,\n'
                      'sixth, and seventh:\n'
                      '1, 2, \u266D3, 4, 5, \u266D6, \u266D7\n'
                      '\n'
                      'The semitones between each scale degree:\n'
                      '2, 1, 2, 2, 1, 2, 2\n'
                      '\n'
                      'The 1, 4, 5 degrees of a Major or Minor scale are pretty significant in that they all are\n'
                      'considered \'Perfect\' intervals. By default, they\'re almost always natural notes, meaning\n'
                      'they are never sharp or flat. There\'s an exception to that of course, but with that in\n'
                      'mind, almost every other scale degree in Natural Minor gets flattened (except for the second\n'
                      'degree, which is also known as the \'Supertonic\'). These changes give the Minor scales their\n'
                      '\'sad\' vibe.\n'
                      '\n'
                      'Ascending and descending using the Natural Minor Scale looks like this:\n'
                      '                               (1)    (1)\n'
                      'Scale Degrees: 1 2 \u266D3 4 5 \u266D6 \u266D7 8 ==== 8 \u266D7 \u266D6 5 4 \u266D3 2 1\n'
                      '\n'
                      'Semitones:      2 1  2 2 1  2  2  ====  2  2  1 2 2  1 2\n'
                      '\n'
                      'This is the Natural Minor Scale pattern on guitar:\n'
                      '\n'
                      'E|---|--1|---|--2|-\u266D3|\n'
                      ' |   |   |   |   |   |\n'
                      'B|---|--5|-\u266D6|---|-\u266D7|\n'
                      ' |   |   |   |   |   |\n'
                      'G|--2|-\u266D3|---|--4|---|\n'
                      ' |   |   |   |   |   |\n'
                      'D|---|-\u266D7|---|--1|---|\n'
                      ' |   |   |   |   |   |\n'
                      'A|---|--4|---|--5|-\u266D6|\n'
                      ' |   |   |   |   |   |\n'
                      'E|---|--1|---|--2|-\u266D3|\n\n')

minor_scale_contents = namedtuple('minor_scale_stuff', ('First', 'Second', 'FlatThird', 'Fourth', 'Fifth', 'FlatSixth',
                                                        'FlatSeventh'))
minor_scale_stuff = minor_scale_contents(2, 1, 2, 2, 1, 2, 2)

#    Melodic Minor Scale

melminor_steps = ('Whole', 'Half', 'Whole', 'Whole', 'Whole', 'Whole', 'Half')
simple_melminor_steps = ('W', 'H', 'W', 'W', 'W', 'W', 'H')
melminor_degrees = ('1', '2', '\u266D3', '4', '5', '6', '7')
melminor_scale_num = 7
melminor_semitones = (2, 1, 2, 2, 2, 2, 1)

melminor_scale_prompt = ('The Melodic Minor Scale:\n'
                         '\n'
                         'The Melodic Minor Scale is an interesting scale for sure because typically when musicians\n'
                         "use it, they use it in more ways than one. You may ask \"Well doesn't every musician use\n"
                         "scales in more ways than one anyway?\", and to that I say...\"Well, yeah...\"\n"
                         'BUT, other scales typically use the same notes and scale degrees when both ascending\n'
                         'AND descending... except for the Melodic Minor Scale... well kinda. Like I said,\n'
                         "it's an interesting scale. You can choose to descend and ascend it using the same\n"
                         'notes/scale degrees, OR you can choose to revert back to the Natural Minor Scale\n'
                         'formula when descending. Either way, the formula for the Melodic Minor Scale is\n'
                         'as follows:\n'
                         '\n'
                         'Whole, Half, Whole, Whole, Whole, Whole, Half\n'
                         '\n'
                         'or for simplicity\'s sake,\n'
                         '\n'
                         'W, H, W, W, W, W, H\n'
                         '\n'
                         'For Melodic Minor, the only scale degree that gets altered is the third:\n'
                         '1, 2, \u266D3, 4, 5, 6, 7\n'
                         '\n'
                         'The semitones between each scale degree:\n'
                         '2, 1, 2, 2, 2, 2, 1\n'
                         '\n'
                         'Idk man, somethin\' \'bout keeping everything but the third un-flat when ascending makes it\n'
                         'melodically very nice\n'
                         '\n'
                         'Ascending and descending using the Melodic Minor Scale can look like this:\n'
                         '                             (1)    (1)\n'
                         'Scale Degrees: 1 2 \u266D3 4 5 6 7 8 ==== 8 \u266D7 \u266D6 5 4 \u266D3 2 1\n'
                         '\n'
                         'Semitones:      2 1  2 2 2 2 1  ====  1  2  2 2 2  1 2\n'
                         '\n'
                         'Or this:\n'
                         '\n'
                         'Scale Degrees: 1 2 \u266D3 4 5 6 7 8 ==== 8 7 6 5 4 \u266D3 2 1\n'
                         '\n'
                         'Semitones:      2 1  2 2 2 2 1  ====  1 2 2 2 2  1 2\n'
                         '\n'
                         'This is the Melodic Minor Scale pattern on guitar:\n'
                         '\n'
                         'E|---|---|--2|-\u266D3|---|--4|\n'
                         ' |   |   |   |   |   |   |\n'
                         'B|---|---|--6|---|--7|--1|\n'
                         ' |   |   |   |   |   |   |\n'
                         'G|-\u266D3|---|--4|---|--5|---|\n'
                         ' |   |   |   |   |   |   |\n'
                         'D|---|--7|--1|---|--2|---|\n'
                         ' |   |   |   |   |   |   |\n'
                         'A|--4|---|--5|---|--6|---|\n'
                         ' |   |   |   |   |   |   |\n'
                         'E|--1|---|--2|-\u266D3|---|---|\n\n')

melminor_scale_contents = namedtuple('melminor_scale_stuff', ('First', 'Second', 'FlatThird', 'Fourth', 'Fifth',
                                                              'Sixth', 'Seventh'))
melminor_scale_stuff = melminor_scale_contents(2, 1, 2, 2, 2, 2, 1)

#    Harmonic Minor Scale

harminor_steps = ('Whole', 'Half', 'Whole', 'Whole', 'Half', 'Whole + Half', 'Half')
simple_harminor_steps = ('W', 'H', 'W', 'W', 'H', 'W+H', 'H')
harminor_degrees = ('1', '2', '\u266D3', '4', '5', '\u266D6', '7')
harminor_scale_num = 7
harminor_semitones = (2, 1, 2, 2, 1, 3, 1)

harminor_scale_prompt = ('The Harmonic Minor Scale:\n'
                         '\n'
                         'Don\'t really have much to say about this scale except it sounds super cool and it\'s used\n'
                         'in the alternate picking part of the sweep/alternate picking solo in Machine by Born of\n'
                         'Osiris (Descending, to be specific).\n'
                         '\n'
                         'The formula for the Harmonic Minor Scale is as follows:\n'
                         '\n'
                         'Whole, Half, Whole, Whole, Half, Whole + Half, Half\n'
                         '\n'
                         'or for simplicity\'s sake,\n'
                         '\n'
                         'W, H, W, W, H, W+H, H\n'
                         '\n'
                         'The scale degrees for Harmonic Minor only have the third and the sixth altered:\n'
                         '1, 2, \u266D3, 4, 5, \u266D6, 7\n'
                         '\n'
                         'The semitones between each scale degree:\n'
                         '2, 1, 2, 2, 1, 3, 1\n'
                         '\n'
                         'Harmonic Minor can be thought of as like halfway between Melodic and Natural Minor. It\'s\n'
                         'not as flat as Natural Minor, and it\'s not as un-flat as Melodic Minor.\n'
                         '\n'
                         'Ascending and descending using the Harmonic Minor Scale looks like this:\n'
                         '                              (1)    (1)\n'
                         'Scale Degrees: 1 2 \u266D3 4 5 \u266D6 7 8 ==== 8 7 \u266D6 5 4 \u266D3 2 1\n'
                         '\n'
                         'Semitones:      2 1  2 2 1  3 1        1 3  1 2 2  1 2\n'
                         '\n'
                         'This is the Harmonic Minor Scale pattern on guitar:\n'
                         '\n'
                         'E|---|---|--2|-\u266D3|---|--4|\n'
                         ' |   |   |   |   |   |   |\n'
                         'B|---|-\u266D6|---|---|--7|--1|\n'
                         ' |   |   |   |   |   |   |\n'
                         'G|-\u266D3|---|--4|---|--5|---|\n'
                         ' |   |   |   |   |   |   |\n'
                         'D|---|--7|--1|---|--2|---|\n'
                         ' |   |   |   |   |   |   |\n'
                         'A|--4|---|--5|-\u266D6|---|---|\n'
                         ' |   |   |   |   |   |   |\n'
                         'E|--1|---|--2|-\u266D3|---|---|\n\n')

harminor_scale_contents = namedtuple('harminor_scale_stuff', ('First', 'Second', 'FlatThird', 'Fourth', 'Fifth',
                                                              'FlatSixth', 'Seventh'))
harminor_scale_stuff = harminor_scale_contents(2, 1, 2, 2, 1, 3, 1)

#    Minor Pentatonic Scale

minor_penta_steps = ('Whole + Half', 'Whole', 'Whole', 'Whole + Half', 'Whole')
simple_minor_penta_steps = ('W+H', 'W', 'W', 'W+H', 'W')
minor_penta_degrees = ('1', '\u266D3', '4', '5', '\u266D7')
minor_penta_scale_num = 5
minor_penta_semitones = (3, 2, 2, 3, 2)

minor_penta_scale_prompt = ('The Minor Pentatonic Scale:\n'
                            '\n'
                            'Similar to how the Major Pentatonic removes two scale degrees, the Minor Pentatonic\n'
                            "removes the 2nd and 6th scale degrees, leaving 5 notes, or 'penta-tonics'.\n"
                            '\n'
                            'The formula for the Minor Pentatonic Scale is as follows:\n'
                            '\n'
                            'Whole + Half, Whole, Whole, Whole + Half, Whole\n'
                            '\n'
                            'or for simplicity\'s sake,\n'
                            '\n'
                            'W+H, W, W, W+H, W\n'
                            '\n'
                            'The scale degrees for the Minor Pentatonic Scale follow the scale degrees from Natural\n'
                            'Minor, but remove the 2nd and 6th scale degrees:\n'
                            '\n'
                            '1, \u266D3, 4, 5, \u266D7\n'
                            '\n'
                            'The semitones between each scale degree:\n'
                            '\n'
                            '3, 2, 2, 3, 2\n'
                            '\n'
                            'Minor Pentatonic is a chill little guitar warmup when you got nothin\' else in mind to\n'
                            'play.\n'
                            '\n'
                            'Ascending and descending using the Minor Pentatonic Scale looks like this:\n'
                            '                          (1)    (1)\n'
                            'Scale Degrees: 1 \u266D3 4 5 \u266D7 8 ==== 8 \u266D7 5 4 \u266D3 1\n'
                            '\n'
                            'Semitones:      3  2 2 3  2        2  3 2 2  3\n'
                            '\n'
                            'This is the Minor Pentatonic Scale pattern on guitar:\n'
                            '\n'
                            'E|--1|---|---|-\u266D3|\n'
                            ' |   |   |   |   |\n'
                            'B|--5|---|---|-\u266D7|\n'
                            ' |   |   |   |   |\n'
                            'G|-\u266D3|---|--4|---|\n'
                            ' |   |   |   |   |\n'
                            'D|-\u266D7|---|--1|---|\n'
                            ' |   |   |   |   |\n'
                            'A|--4|---|--5|---|\n'
                            ' |   |   |   |   |\n'
                            'E|--1|---|---|-\u266D3|\n\n')

minor_penta_scale_contents = namedtuple('minor_penta_scale_stuff', ('First', 'FlatThird', 'Fourth', 'Fifth',
                                                                    'FlatSeventh'))
minor_penta_scale_stuff = minor_penta_scale_contents(3, 2, 2, 3, 2)
