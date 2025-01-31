import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
from threading import Thread
import cmd

# Initialize the recognizer 
r = sr.Recognizer()
listening = False

def record_text():
    global listening
    while listening:
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)  

                # Listens for user's input
                print("Listening...")
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                print("You said: " + MyText)
                
                output_text(MyText)
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError as e:
            print("Unknown error occurred: {0}".format(e))

def output_text(text):
    with open("output_text.txt", "a") as f:
        f.write(text)
        f.write("\n")

def start_listening():
    global listening
    listening = True
    thread = Thread(target=record_text)
    thread.start()

def stop_listening():
    global listening
    listening = False

# Set up the GUI
root = tk.Tk()
root.title("Speech to Text")

# Use ttk for modern widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

start_button = ttk.Button(frame, text="Start Listening", command=start_listening, style="TButton")
start_button.pack(pady=10, fill=tk.X)

stop_button = ttk.Button(frame, text="Stop Listening", command=stop_listening, style="TButton")
stop_button.pack(pady=10, fill=tk.X)

class SpeechToTextCmd(cmd.Cmd):
    prompt = '> '
    intro = "Welcome to the Speech to Text command line. Type 'start' to start listening and 'stop' to stop listening."

    def do_start(self, arg):
        "Start listening"
        start_listening()
        print("Started listening...")

    def do_stop(self, arg):
        "Stop listening"
        stop_listening()
        print("Stopped listening...")

    def do_exit(self, arg):
        "Exit the command line interface"
        print("Exiting...")
        return True

if __name__ == "__main__":
    # Start the GUI in a separate thread
    gui_thread = Thread(target=root.mainloop)
    gui_thread.start()

    # Start the command line interface
    SpeechToTextCmd().cmdloop()