import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

class AutoClick(threading.Thread):
    def __init__(self, delay, button):
        super(AutoClick, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    
    def start_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.running = False
    
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


if __name__ == "__main__":
    delay = 0.01
    button = Button.left
    start_and_stop_key = KeyCode(char='s')
    exit_key = KeyCode(char=27)

    mouse = Controller()
    main_thread = AutoClick(delay, button)
    main_thread.start()

    def on_key_press(key):
        if key == start_and_stop_key:
            if main_thread.running:
                main_thread.stop_clicking()
            else:
                main_thread.start_clicking()
        elif key == exit_key:
            main_thread.exit()
            listener.stop()

    with Listener(on_press=on_key_press) as listener:
        listener.join()