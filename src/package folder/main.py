import scalestuff
import modestuff
import intervalstuff


def invalidate(command):
    """
    Displays text specific to why the command was invalid.
    :param command: I.e. the user_input
    :return: None
    """
    if command == '':
        print('Enter any command from below to continue.')
    elif command not in vocab:
        print('Unknown, please check for misspelling.')


def hide_check():
    """
    Warns user if the container is empty and carries on, otherwise it calls hide().
    :return: None
    """
    if not selected_topics:
        print('No topics are available for review.')
    elif selected_topics:
        hide()


def hide():
    """
    Asks user what they would like to remove from standard dictionary. Warns user if key wasn't found, otherwise it
    deletes it.
    :return: None
    """
    topic = input('Enter topic you wish to remove from topic review: ').strip().lower().title()
    if topic in selected_topics:
        del selected_topics[topic]
    else:
        print('Topic is either misspelled or has not been searched for.')


def print_check():
    """
    Iterates through standard dictionary and prints each key and corresponding value.
    :return: None
    """
    if not selected_topics:
        print('Nothin\' here.')
    else:
        for topic, parent_topic in selected_topics.items():
            print(f'{topic} --> {parent_topic}')


def core_script_logic(command):
    """
    Executes relevant logic native to script (nothing required externally).
    :param command: I.e. the user_input
    :return: None
    """
    if command == 'Show':
        for topic, info in table_of_contents.items():
            print(display_topic_str.format(col1=topic, col2=info['descr']))
    elif command == 'Hide':
        hide_check()
    elif command == 'Print':
        print_check()


def display_matches(command):
    """
    Displays all relevant topics related to the command that are found within table_of_contents.
    :param command: I.e. the user_input
    :return:None
    """
    for topic, info in table_of_contents.items():
        if info['Parent Topic'] == command:
            print(display_topic_str.format(col1=topic, col2=info['descr']))


def fetch_topic_info(command):
    """
    Displays the relevant topic information from the imported modules and stores the search within a basic dictionary
    using information from table_of_contents.
    :param command: I.e. the user_input
    :return: None
    """
    if command == 'Major':
        print(scalestuff.major_scale_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Major Pentatonic':
        print(scalestuff.major_penta_scale_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Minor':
        print(scalestuff.minor_scale_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Melodic Minor':
        print(scalestuff.melminor_scale_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Harmonic Minor':
        print(scalestuff.harminor_scale_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Minor Pentatonic':
        print(scalestuff.minor_penta_scale_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Scale Degrees':
        scalestuff.formatted_scale_degrees()
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Ionian':
        print(modestuff.ionian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Dorian':
        print(modestuff.dorian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Phrygian':
        print(modestuff.phrygian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Lydian':
        print(modestuff.lydian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Mixolydian':
        print(modestuff.mixolydian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Aeolian':
        print(modestuff.aeolian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Locrian':
        print(modestuff.locrian_mode_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Interval Basics':
        print(intervalstuff.interval_basics)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Chord Basics':
        print(intervalstuff.chord_basics)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Chord Progressions':
        print(intervalstuff.chord_progs)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Arpeggio Basics':
        print(intervalstuff.arpeggio_basics)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Circles':
        print(intervalstuff.circles_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']
    elif command == 'Orders':
        print(intervalstuff.orders_prompt)
        selected_topics[command] = table_of_contents[command]['Parent Topic']


def gather_vocab():
    for key in table_of_contents.keys():
        vocab.append(key)
    for key, item in table_of_contents.items():
        if item['Parent Topic'] not in vocab:
            vocab.append(item['Parent Topic'])
    for core_command in core_script_commands:
        vocab.append(core_command)


def main():
    print("Welcome to the Rizzless Guitar Guide!\n")
    user_input = input(main_menu_prompt).strip().lower().title()

    while user_input != 'Quit':
        if user_input in core_script_commands:
            core_script_logic(user_input)
        elif user_input in ['Scales', 'Modes', 'Intervals', 'More Intervals']:
            display_matches(user_input)
        elif user_input in table_of_contents.keys():
            fetch_topic_info(user_input)
        else:
            invalidate(user_input)

        user_input = input(main_menu_prompt[26:]).strip().lower().title()


main_menu_prompt = ('Main Menu\n'
                    'Program options:\n'
                    '  (Show) Displays concepts.\n'
                    '  (Hide) Removes concept from final review.\n'
                    'Good to do for accidental searches.\n'
                    '  (Print) Prints list that documents what the user\n'
                    'has searched to review areas of focus for practice.\n'
                    '  (Quit) Terminates program.\n'
                    '\n'
                    'Enter input: ')

main_menu_options = ['Show', 'Hide', 'Print', 'Quit']

table_of_contents = {
    'Major': {'descr': 'Shows Major scale info.',
              'Parent Topic': 'Scales'
              },
    'Major Pentatonic': {'descr': 'Shows Major Pentatonic scale info.',
                         'Parent Topic': 'Scales'
                         },
    'Minor': {'descr': 'Shows Minor scale info.',
              'Parent Topic': 'Scales'
              },
    'Melodic Minor': {'descr': 'Shows Melodic Minor scale info.',
                      'Parent Topic': 'Scales'
                      },
    'Harmonic Minor': {'descr': 'Shows Harmonic Minor scale info.',
                       'Parent Topic': 'Scales'
                       },
    'Minor Pentatonic': {'descr': 'Shows Minor Pentatonic scale info.',
                         'Parent Topic': 'Scales'
                         },
    'Scale Degrees': {'descr': 'Shows the scale degrees for all scales listed.',
                      'Parent Topic': 'Scales'
                      },
    'Ionian': {'descr': 'Shows information for the Ionian mode.',
               'Parent Topic': 'Modes'
               },
    'Dorian': {'descr': 'Shows information for the Dorian mode.',
               'Parent Topic': 'Modes'
               },
    'Phrygian': {'descr': 'Shows information for the Phrygian mode.',
                 'Parent Topic': 'Modes'
                 },
    'Lydian': {'descr': 'Shows information for the Lydian mode.',
               'Parent Topic': 'Modes'
               },
    'Mixolydian': {'descr': 'Shows information for the Mixolydian mode.',
                   'Parent Topic': 'Modes'
                   },
    'Aeolian': {'descr': 'Shows information for the Aeolian mode.',
                'Parent Topic': 'Modes'
                },
    'Locrian': {'descr': 'Shows information for the Locrian mode.',
                'Parent Topic': 'Modes'
                },
    'Interval Basics': {'descr': 'Shows information about interval names and their semitones.',
                        'Parent Topic': 'Intervals'
                        },
    'Chord Basics': {'descr': 'Shows the basic fundamentals of how chords are made.',
                     'Parent Topic': 'Intervals'
                     },
    'Chord Progressions': {'descr': 'Shows common chord progressions.',
                           'Parent Topic': 'Intervals'
                           },
    'Arpeggio Basics': {'descr': 'Shows information about the basics of arpeggios.',
                        'Parent Topic': 'Intervals'
                        },
    'Circles': {'descr': 'Shows information about the Circle of Fifths and the Circle of Fourths.',
                'Parent Topic': 'More Intervals'
                },
    'Orders': {'descr': 'Shows information about the Orders of Sharps and the Order of Flats.',
               'Parent Topic': 'More Intervals'
               }
}
display_topic_str = '{col1:24}{col2:120}'
core_script_commands = ['Show', 'Hide', 'Print']
vocab = []
selected_topics = {}

if __name__ == '__main__':
    gather_vocab()
    main()

# todo create tests
