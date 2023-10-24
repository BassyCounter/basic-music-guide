# todo add doc strings and comments and stuff so future you and other people don't struggle to read your spaghetti code
import scalestuff
import modestuff
import intervalstuff

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

table_of_contents_prompt = ('Concept options:\n'
                            '  (Scales) Displays Scales.\n'
                            '  (Modes) Displays Modes.\n'
                            '  (Intervals) Displays basic Interval information.\n'
                            '  (More Intervals) Displays information about Circle of Fifths/Fourths, Order of\n'
                            'Sharps/Flats, etc.\n'
                            '\n'
                            'Enter concept: ')

table_of_contents = ['Scales', 'Modes', 'Intervals', 'More Intervals']

vocab = ['Show', 'Hide', 'Print', 'Quit', 'Scales', 'Modes', 'Intervals', 'More Intervals', 'Major', 'Major Pentatonic',
         'Minor', 'Melodic Minor', 'Harmonic Minor', 'Minor Pentatonic', 'Ionian', 'Dorian', 'Phrygian', 'Lydian',
         'Mixolydian', 'Aeolian', 'Locrian', 'Interval Basics', 'Chord Basics', 'Chord Progressions', 'Arpeggio Basics',
         'Circles', 'Orders', 'Scale Degrees']  # todo Convert into dict for a 'help' command

selected_topics = {}


def validate(command):
    """

    :param command: I.e. the user_input; warns user if unrecognized.
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
    Asks user what they would like to remove from hard-coded dictionary. Warns user if it wasn't found, otherwise it
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
    Iterates through hard-coded dictionary and prints each element, otherwise it warns user if it's empty.
    :return: None
    """
    if not selected_topics:
        print('Nothin\' here.')
    else:
        for key, value in selected_topics.items():
            print(f'{key} --> {value}')


def main():  # todo split this up into smaller functions
    print("Welcome to the Rizzless Guitar Guide!\n")
    user_input = input(main_menu_prompt).strip().lower().title()

    while user_input != 'Quit':
        if user_input == 'Show':
            user_input = input(table_of_contents_prompt).strip().lower().title()
            continue
        elif user_input == 'Scales':
            user_input = input(scalestuff.scales_prompt).strip().lower().title()
            continue
        elif user_input == 'Major':
            print(scalestuff.major_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Major Pentatonic':
            print(scalestuff.major_penta_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Minor':
            print(scalestuff.minor_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Melodic Minor':
            print(scalestuff.melminor_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Harmonic Minor':
            print(scalestuff.harminor_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Minor Pentatonic':
            print(scalestuff.minor_penta_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Scale Degrees':
            scalestuff.formatted_scale_degrees()
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Modes':
            user_input = input(modestuff.modes_prompt).strip().lower().title()
            continue
        elif user_input == 'Ionian':
            print(modestuff.ionian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Dorian':
            print(modestuff.dorian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Phrygian':
            print(modestuff.phrygian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Lydian':
            print(modestuff.lydian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Mixolydian':
            print(modestuff.mixolydian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Aeolian':
            print(modestuff.aeolian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Locrian':
            print(modestuff.locrian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Intervals':
            user_input = input(intervalstuff.interval_menu).strip().lower().title()
            continue
        elif user_input == 'Interval Basics':
            print(intervalstuff.interval_basics)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'Chord Basics':
            print(intervalstuff.chord_basics)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'Chord Progressions':
            print(intervalstuff.chord_progs)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'Arpeggio Basics':
            print(intervalstuff.arpeggio_basics)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'More Intervals':
            user_input = input(intervalstuff.more_intervals_menu).strip().lower().title()
            continue
        elif user_input == 'Circles':
            print(intervalstuff.circles_prompt)
            selected_topics[user_input] = 'More Intervals'
        elif user_input == 'Orders':
            print(intervalstuff.orders_prompt)
            selected_topics[user_input] = 'More Intervals'
        elif user_input == 'Hide':
            hide_check()
        elif user_input == 'Print':
            print_check()
        else:
            validate(user_input)

        user_input = input(main_menu_prompt[26:]).strip().lower().title()


if __name__ == '__main__':
    main()

# todo create tests
