# Voice Assistant 🎤

A simple Python-based Voice Assistant developed as part of the **Oasis Infobyte Python Programming Internship – Task 1**.

## 📌 Project Description

This Voice Assistant listens to spoken commands through the microphone and responds using text-to-speech.

It can:
- Respond to greetings
- Tell the current time
- Tell today's date
- Search the web using Google
- Handle commands that are not understood
- Speak responses using text-to-speech

## ✨ Features

1. 🎤 Voice input using the microphone
2. 👋 Greeting response
3. 🕐 Current time
4. 📅 Current date
5. 🌐 Google web search
6. 🔊 Text-to-speech responses
7. ⚠️ Error handling for unclear commands
8. 🚪 Exit command

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

## 📋 Supported Commands

| Command | Example |
|---|---|
| Greeting | "Hello" |
| Time | "Tell me the current time" |
| Date | "What is today's date?" |
| Web Search | "Search Python programming" |
| Exit | "Exit" |

## ▶️ How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install SpeechRecognition pyttsx3 PyAudio