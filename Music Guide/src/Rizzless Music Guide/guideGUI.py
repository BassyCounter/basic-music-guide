import os
import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import scalestuff
import modestuff
import intervalstuff
import guide


def add_to_review():
    text_box.configure(state='normal')
    if scalestuff.major_scale_prompt in text_box.get('0.0', 'end'):
        selected_topics['Major'] = 'Scales'
    elif scalestuff.major_penta_scale_prompt in text_box.get('0.0', 'end'):
        selected_topics['Major Pentatonic'] = 'Scales'
    elif scalestuff.minor_scale_prompt in text_box.get('0.0', 'end'):
        selected_topics['Minor'] = 'Scales'
    elif scalestuff.melminor_scale_prompt in text_box.get('0.0', 'end'):
        selected_topics['Melodic Minor'] = 'Scales'
    elif scalestuff.harminor_scale_prompt in text_box.get('0.0', 'end'):
        selected_topics['Harmonic Minor'] = 'Scales'
    elif scalestuff.minor_penta_scale_prompt in text_box.get('0.0', 'end'):
        selected_topics['Minor Pentatonic'] = 'Scales'
    elif scalestuff.scale_degrees_prompt in text_box.get('0.0', 'end'):
        selected_topics['Scale Degrees'] = 'Scales'
    elif modestuff.ionian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Ionian'] = 'Modes'
    elif modestuff.dorian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Dorian'] = 'Modes'
    elif modestuff.phrygian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Phrygian'] = 'Modes'
    elif modestuff.lydian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Lydian'] = 'Modes'
    elif modestuff.mixolydian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Mixolydian'] = 'Modes'
    elif modestuff.aeolian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Aeolian'] = 'Modes'
    elif modestuff.locrian_mode_prompt in text_box.get('0.0', 'end'):
        selected_topics['Locrian'] = 'Modes'
    elif intervalstuff.interval_basics in text_box.get('0.0', 'end'):
        selected_topics['Interval Basics'] = 'Intervals'
    elif intervalstuff.chord_basics in text_box.get('0.0', 'end'):
        selected_topics['Chord Basics'] = 'Intervals'
    elif intervalstuff.chord_progs in text_box.get('0.0', 'end'):
        selected_topics['Chord Progressions'] = 'Intervals'
    elif intervalstuff.arpeggio_basics in text_box.get('0.0', 'end'):
        selected_topics['Arpeggio Basics'] = 'Intervals'
    elif intervalstuff.circles_prompt in text_box.get('0.0', 'end'):
        selected_topics['Circles'] = 'More Intervals'
    elif intervalstuff.orders_prompt in text_box.get('0.0', 'end'):
        selected_topics['Orders'] = 'More Intervals'
    save_button.configure(text='Topic Staged.')
    text_box.configure(state='disabled')


def reset_save_button():
    if save_button.cget('text') == 'Topic reference staged.':
        save_button.configure(text='Stage topic reference for review file?')


def display_info(button_text):
    reset_save_button()
    text_box.configure(state='normal')
    text_box.delete('0.0', 'end')
    if button_text == 'Major':
        text_box.insert('0.0', scalestuff.major_scale_prompt)
    elif button_text == 'Major Pentatonic':
        text_box.insert('0.0', scalestuff.major_penta_scale_prompt)
    elif button_text == 'Minor':
        text_box.insert('0.0', scalestuff.minor_scale_prompt)
    elif button_text == 'Melodic Minor':
        text_box.insert('0.0', scalestuff.melminor_scale_prompt)
    elif button_text == 'Harmonic Minor':
        text_box.insert('0.0', scalestuff.harminor_scale_prompt)
    elif button_text == 'Minor Pentatonic':
        text_box.insert('0.0', scalestuff.minor_penta_scale_prompt)
    elif button_text == 'Scale Degrees':
        text_box.insert('0.0', scalestuff.scale_degrees_prompt)
    elif button_text == 'Ionian':
        text_box.insert('0.0', modestuff.ionian_mode_prompt)
    elif button_text == 'Dorian':
        text_box.insert('0.0', modestuff.dorian_mode_prompt)
    elif button_text == 'Phrygian':
        text_box.insert('0.0', modestuff.phrygian_mode_prompt)
    elif button_text == 'Lydian':
        text_box.insert('0.0', modestuff.lydian_mode_prompt)
    elif button_text == 'Mixolydian':
        text_box.insert('0.0', modestuff.mixolydian_mode_prompt)
    elif button_text == 'Aeolian':
        text_box.insert('0.0', modestuff.aeolian_mode_prompt)
    elif button_text == 'Locrian':
        text_box.insert('0.0', modestuff.locrian_mode_prompt)
    elif button_text == 'Interval Basics':
        text_box.insert('0.0', intervalstuff.interval_basics)
    elif button_text == 'Chord Basics':
        text_box.insert('0.0', intervalstuff.chord_basics)
    elif button_text == 'Chord Progressions':
        text_box.insert('0.0', intervalstuff.chord_progs)
    elif button_text == 'Arpeggio Basics':
        text_box.insert('0.0', intervalstuff.arpeggio_basics)
    elif button_text == 'Circles':
        text_box.insert('0.0', intervalstuff.circles_prompt)
    elif button_text == 'Orders':
        text_box.insert('0.0', intervalstuff.orders_prompt)
    text_box.configure(state='disabled')


def on_closing():
    msg = CTkMessagebox(app,
                        title='Save to file?',
                        message='Would you like to save your topic references to a file? Doing so will overwrite any '
                                'references currently within file.',
                        icon='question',
                        option_1='Cancel',
                        option_2='No',
                        option_3='Yes')
    response = msg.get()

    if response == 'Yes':
        if selected_topics:  # We want to save only if selected topics has stuff (True)
            with open(txt_path, 'wt') as file:
                for key, value in selected_topics.items():
                    file.write(f'{key} --> {value}\n')
        app.destroy()
    if response == 'No':
        app.destroy()


def save_file():
    if selected_topics:  # We want to save only if selected topics has stuff (True)
        with open(txt_path, 'wt') as file:
            for key, value in selected_topics.items():
                file.write(f'{key} --> {value}\n')


def save_warning():
    msg = CTkMessagebox(title='Warning',
                        message='Saving will overwrite any references currently within file, would you like to '
                                'continue?',
                        icon='warning',
                        option_1='Cancel',
                        option_2='Yes')
    response = msg.get()

    if response == 'Yes':
        save_file()


def text_box_fonts():
    # fixme try to figure out a way to make the new window not hide behind the main one
    fonts = ['Consolas', 'Lucida Console', 'Courier New', 'Terminal', 'MS Gothic', 'NSimSun']

    settings_window = ctk.CTkToplevel(app)
    settings_window.minsize(55, 200)
    settings_window.title('Font Options')

    combo_box = ctk.CTkComboBox(settings_window,
                                values=fonts,
                                command=set_font)
    combo_box.pack(padx=10, pady=10)


def set_font(choice):
    text_box.configure(font=(choice, 14))


selected_topics = {}

# File directory
home_directory = os.path.expanduser('~')
documents_directory = os.path.join(home_directory, 'Documents')
txt_file = 'Music Guide Topic References.txt'
txt_path = os.path.join(documents_directory, txt_file)

# App colors
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('dark-blue')

# App configuration
app = ctk.CTk()
app.title('Rizzless Music Guide')
app.geometry(f'{1200}x{650}')
# app.iconbitmap()

menu_bar = tk.Menu(app)

file_menu = tk.Menu(menu_bar,
                    tearoff=0)
file_menu.add_command(label='Save',
                      command=save_warning)
file_menu.add_separator()
# Create submenu within file menu
settings_menu = tk.Menu(file_menu, tearoff=0)
settings_menu.add_command(label='Change Topic Display Font', command=text_box_fonts)
file_menu.add_cascade(label='Settings', menu=settings_menu)
file_menu.add_separator()
file_menu.add_command(label='Exit',
                      command=on_closing)
file_menu.add_command(label='Force Exit',
                      command=exit)
menu_bar.add_cascade(menu=file_menu,
                     label='File')
app.config(menu=menu_bar)

# Define widgets
text_box = ctk.CTkTextbox(app,
                          font=('Terminal', 14),
                          state='normal')  # Set to normal by default, switches to disabled after displaying info
scrollable_frame = ctk.CTkScrollableFrame(app,
                                          width=25,
                                          label_text='Topics:',
                                          label_font=('Arial', 18))
# Iterate over table_of_contents keys to append topic button to scrollable_frame
for topic in guide.table_of_contents.keys():
    item = ctk.CTkButton(scrollable_frame,
                         text=topic,
                         font=('Arial', 14),
                         command=lambda t=topic: display_info(t))
    item.pack(pady=5)
save_button = ctk.CTkButton(app,
                            text='Stage topic reference for review file?',
                            command=add_to_review)

# Define grid
app.columnconfigure((0, 1, 2, 3, 4), weight=1)
app.rowconfigure((0, 1, 2, 3), weight=1)

# Place widgets
text_box.grid(row=0, column=0, rowspan=4, columnspan=4, sticky='nwse', padx=20, pady=20)
scrollable_frame.grid(row=0, column=4, rowspan=3, sticky='nwse', pady=20)
save_button.grid(row=3, column=4, sticky='n')

if __name__ == '__main__':
    app.protocol('WM_DELETE_WINDOW', on_closing)
    app.mainloop()
