# Import necessary libraries

import pyttsx3  # For text-to-speech functionality
import speech_recognition as sr  # To recognize voice commands
import pywhatkit  # To play YouTube videos directly
import datetime  # To fetch the current time
import subprocess  # To open external applications (e.g., Chrome)
import webbrowser  # To open URLs in the browser
import pyjokes  # To tell jokes

# Initialize the pyttsx3 engine
engine = pyttsx3.init()  # Engine as the "voice box" of AI; allows the AI to speak
voices = engine.getProperty('voices')  # Fetch the available voices for the AI
engine.setProperty('voice', voices[1].id)  # '0' for male voice, '1' for female voice

# Recognizer object that will listen to and understand your voice
recognizer = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    engine.say(text)  # Pass the text to the engine to speak it out loud
    engine.runAndWait()  # Wait for the engine to finish speaking before continuing

# Function to process the recognized command
def process_command(command):
    command = command.lower()  # Convert the command to lowercase for easier comparison
    
    # Command to open Chrome
    if 'open chrome' in command:
        speak("Opening Chrome")  # Notify the user
        program = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Path to Chrome
        subprocess.Popen(program)  # Open Chrome using subprocess
    
    # Command to tell the current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')  # Fetch current time
        speak(f"Time is {time}")  # Read out the time
    
    # Command to play a YouTube video based on the query
    elif 'play' in command:
        speak("Playing on Youtube")  # Notify the user
        pywhatkit.playonyt(command.replace('play', '').strip())  # Play the video on YouTube
    
    # Command to open YouTube in the browser
    elif 'open youtube' in command:
        speak("Opening youtube")  # Notify the user
        webbrowser.open("http://youtube.com")  # Open YouTube URL in the browser
    
    # Command to open Notepad
    elif 'open notepad' in command:
        speak("Opening notepad")  # Notify the user
        program = "C:\\Windows\\System32\\notepad.exe"  # Path to Notepad
        subprocess.Popen(program)  # Open Notepad using subprocess
    
    # Command to tell a random joke
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()  # Get a joke from pyjokes library
        speak(joke)  # Read out the joke
    
    # Command to stop the program
    elif 'stop' in command:
        speak("Okay Byee!")  # Notify the user and end the program
        return False  # Break the loop in listen_and_process() to stop the program
    
    # If no recognized command is found
    else:
        speak("Sorry, I can't perform that action yet!") 
    return True  # Keep the loop running unless 'stop' command is given

# Function to continuously listen for commands and process them
def listen_and_process():

    with sr.Microphone() as source:  # Open microphone for listening
        print("Clearing background noises... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        print("Listening for your command...") 

        while True:  # Start a loop to continuously listen for commands
            recorded_audio = recognizer.listen(source)  # Listen for a command

            try:
                command = recognizer.recognize_google(recorded_audio)  # Convert speech to text
                print(f"You said: {command}")  # Print the recognized command for debugging
                
                if not process_command(command):  # Process the command and exit if 'stop' is said
                    break
            except Exception as e:  # In case of an error while recognizing the speech
                speak("Sorry, I couldn't understand that. Please try again.") 

# Start the continuous listening process
listen_and_process()
