#!/usr/bin/env python3

import os
import shlex
import subprocess
import time
import configparser
import Xlib.display


# Load the configuration file
config_file = os.path.expanduser("~/.config/hotcornered.ini")
config = configparser.ConfigParser()
config.read(config_file)


# Define the function to execute the commands
def execute_command(command):
    if command:
        command_parts = shlex.split(command)
        subprocess.Popen(command_parts, shell=True)

# Define the function to handle a mouse movement
def handle_mouse_movement():
    # Reset the timer
    global timer
    timer = time.time()


# Define the main function
def main():
    # Get the list of screens from the configuration file
    screens = config.sections()

    # Initialize the timer
    global timer
    timer = time.time()

    # Cache corner coordinates
    corners = {}
    for screen in screens:
        hot_corner_size = config.getfloat(screen, "hot_corner_size")
        corner_width = int(config.getint(screen, "width") * hot_corner_size)
        corner_height = int(config.getint(screen, "height") * hot_corner_size)
        corner_size = (corner_width, corner_height)
        screen_size = (config.getint(screen, "width"), config.getint(screen, "height"))

        corners[screen] = {
            "tl": (range(corner_size[0]), range(corner_size[1])),
            "tr": (range(screen_size[0] - corner_size[0], screen_size[0]), range(corner_size[1])),
            "bl": (range(corner_size[0]), range(screen_size[1] - corner_size[1], screen_size[1])),
            "br": (range(screen_size[0] - corner_size[0], screen_size[0]), range(screen_size[1] - corner_size[1], screen_size[1]))
        }

    # Loop indefinitely
    while True:
        # Check for mouse movement
        if time.time() - timer > 0.1:
            handle_mouse_movement()

        # Check for hot corners
        for screen in screens:
            root = Xlib.display.Display().screen().root
            pointer = root.query_pointer()

            for corner, coords in corners[screen].items():
                if pointer.root_x in coords[0] and pointer.root_y in coords[1]:
                    command_option = corner + "_command"
                    timeout_option = corner + "_timeout"
                    command = config.get(screen, command_option)
                    timeout = config.getint(screen, timeout_option)
                    time.sleep(timeout / 1000)
                    execute_command(command)
                    break


# Call the main function
if __name__ == "__main__":
    main()

