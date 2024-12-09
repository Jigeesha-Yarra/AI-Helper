# Voice Assistant Project

This project is a simple **voice assistant** built using Python. It can perform various tasks such as opening applications (e.g., Chrome, Notepad), telling the time, playing YouTube videos, and telling jokes, all through voice commands. The assistant uses **speech recognition** to understand the commands and **text-to-speech** to respond back.

## Features

- **Voice Commands**: The assistant listens to voice commands and executes tasks.
- **Opening Applications**: It can open programs like Google Chrome, Notepad, etc.
- **Current Time**: It can tell the current time on command.
- **YouTube Video Playback**: It can play YouTube videos based on user requests.
- **Telling Jokes**: It can tell random jokes.
- **Stop Command**: The assistant stops listening when the "stop" command is given.

## Requirements

- Python 3.x
- `pyttsx3`: Text-to-speech conversion library
- `speech_recognition`: Library for speech recognition
- `pywhatkit`: For playing YouTube videos
- `datetime`: For fetching the current time
- `subprocess`: To open applications (Chrome, Notepad, etc.)
- `webbrowser`: To open URLs (like YouTube)
- `pyjokes`: To get a random joke

You can install the required libraries using `pip`:

```bash
pip install pyttsx3 speech_recognition pywhatkit pyjokes
