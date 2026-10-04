import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Create recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please try again.")
        return ""

    except sr.RequestError:
        speak("Sorry, the speech recognition service is unavailable.")
        return ""


def main():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        # Tell the current time
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        # Tell today's date
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")

        # Respond to hello
        elif "hello" in command:
            speak("Hello! Nice to talk to you.")

        # Search the web
        elif command.startswith("search "):
            topic = command[7:].strip()

            if topic:
                speak(f"Searching for {topic}.")
                search_url = (
                    "https://www.google.com/search?q="
                    + topic.replace(" ", "+")
                )
                webbrowser.open(search_url)
            else:
                speak("Please tell me what you want to search for.")

        # Exit the assistant
        elif command in ["exit", "quit", "stop", "goodbye"]:
            speak("Goodbye!")
            break

        # Unknown command
        else:
            speak("I did not understand that command. Please try again.")


if __name__ == "__main__":
    main()