# **Rizzless Music Guide**

A simple Python project with a text-based version and a GUI created to assist the user with music theory, focusing on 
applications for guitar.

This project serves multiple purposes:
  - Assisting the user with basic information regarding music theory and how it can be applied on guitar.
  - Providing users with the option to use a simple text-based version or a GUI for learning about music theory 
concepts, depending on preference.
  - Allows the user to study/practice basic music theory concepts locally, without the need to use a browser.
  - The text-based version uses simple keywords that can be typed with one hand (if needed) to quickly search the 
available topics. This is useful if the user is holding a guitar or any other object that can restrict the use of both 
hands. Laptop users can use the trackpad with two fingers to scroll up and down to read the displayed information if 
needed (or use a mouse and scroll wheel with either hand if able). The GUI version provides full control of the music 
guide with just a mouse and scroll wheel/trackpad.
  - Allows the user to save a text file containing the topics searched, so they can come back later and reuse the 
program to study up on those topics, or find information on those topics from another source (e.g., a search engine or a
book).

## **Installation instructions**

To use this project, first you must have [Python](https://www.python.org/downloads/) installed on your computer. This 
project was created using Python 3.11, but should be usable with most Python 3.x versions. When in doubt, use Python 
3.11. You can install Python 3.11 [here](https://www.python.org/downloads/release/python-3110/). Just scroll down to the
bottom of the page and download the respective installer.

Once Python is installed, you can clone the repository by doing the following:
1. Navigate to the repository's home page and click on the green button that says "Code".
1. Find where it says "Download ZIP" to download the repo locally.

After the ZIP file has been downloaded, it is recommended to create a virtual environment so that any of the 
project's dependencies that need to be installed are completely isolated from other projects and their dependencies.
This will ensure that nothing will break, for the code of this project, as well as for code of other projects that may 
be installed in the future. You can achieve this with the following steps:
1. First, extract all of the files. You can place the extracted version of the repository wherever you wish.
2. Open the directory of the extracted repository, which should be called "rizzless-music-guide-main".
3. On Windows, right click on an open space and click the option "Open in Terminal".
4. Run the following command: ```py -m venv tutorial_env```. You can replace the ```tutorial_env``` with whatever you
would like to name the virtual environment. Wait for the command to finish before continuing.
5. Once it's complete, you should see a new directory with the name of what you chose to call it along with the other 
project files.
6. Back in Terminal, run the following command: ```tutorial_env\Scripts\activate```, again replacing ```tutorial_env```
with the virtual environment name you chose. Once the command is complete, you should now see the virtual environment's 
name within parenthesis to the left of the directory you're in. This indicates the virtual environment is active.
7. Now that the virtual environment is active, you can install the project's required dependencies by running the 
```pip install -r requirements.txt``` command.
8. Congrats! You can now navigate to "src\Rizzless Music Guide\" and run either ```guide.py``` or ```guideGUI.py``` by 
right-clicking and opening with Python!

Optionally, you can create shortcuts for either of these files and place them on your desktop or wherever else you would
like them to be. ***Please note that the virtual environment must be active for everything to run correctly.*** Every 
time the Terminal is closed with a virtual environment active, it will deactivate the virtual environment and will need 
to be reactivated. You can rerun the ```tutorial_env\Scripts\activate``` command to reactivate it (within the same 
directory as the ```tutorial_env``` folder) and leave the Terminal open in the background so the virtual environment 
stays active. If for some reason ```guide.py``` or ```guideGUI.py``` doesn't open when double-clicking the file, you 
might need to run the file from Terminal. You can do so with the following steps:
1. Navigate to the directory where ```guide.py``` and ```guideGUI.py``` reside.
2. Right click in an open space and again choose "Open in Terminal" to open a new Terminal window.
3. Type either ```python guide.py``` or ```python guideGUI.py``` and hit enter to execute the command. This should run 
the file with the first version of Python it locates on the computer.

I do realize these steps are kinda convoluted for those who may not want to have to go through all these steps just to 
try out some random code on the internet and I do intend to figure out a way to make this process a lot less complex and
easier to follow. I'm still trying to figure out the best ways to distribute Python code, whether it be packaging or
whatever other methods there are and once I find a better solution, I'll update this repo to reflect it.
