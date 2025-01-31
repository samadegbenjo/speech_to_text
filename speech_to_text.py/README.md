# Speech to Text

This is a Python program that listens to speech and transcribes it into a text file. It provides both a graphical user interface (GUI) and a command-line interface (CLI) for ease of use.

## Features

- Start and stop listening using GUI buttons.
- Start and stop listening using terminal commands.
- Transcribes speech to `output_text.txt` file.

## Requirements

- Python 3.x
- `speech_recognition` library
- `tkinter` library (comes with Python standard library)
- `pyaudio` library (for microphone input)

## Installation

1. Install the required libraries:
    ```sh
    pip install SpeechRecognition pyaudio
    ```

2. Clone this repository or download the [speech_to_text.py](http://_vscodecontentref_/0) file.

## Usage

### Graphical User Interface (GUI)

1. Run the program:
    ```sh
    python speech_to_text.py
    ```

2. Use the "Start Listening" and "Stop Listening" buttons to control the transcription.

### Command-Line Interface (CLI)

1. Run the program:
    ```sh
    python speech_to_text.py
    ```

2. Use the following commands in the terminal:
    - [start](http://_vscodecontentref_/1): Start listening and transcribing.
    - `stop`: Stop listening and transcribing.
    - `exit`: Exit the command-line interface.

## File Structure

- [speech_to_text.py](http://_vscodecontentref_/2): The main program file.
- [output_text.txt](http://_vscodecontentref_/3): The file where transcribed text is saved.

## Example

1. Start the program:
    ```sh
    python speech_to_text.py
    ```

2. In the terminal, type [start](http://_vscodecontentref_/4) to begin listening and `stop` to stop listening.

3. The transcribed text will be saved in [output_text.txt](http://_vscodecontentref_/5).

## Troubleshooting

- Ensure your microphone is working and not muted.
- Ensure you have a stable internet connection for the Google Speech Recognition API.
- If you encounter errors, check the terminal for detailed error messages.

## License

This project is licensed under the MIT License.