# Jarvis Voice Assistant

## Overview
Jarvis is a voice-activated assistant built using Python. It utilizes various libraries to perform tasks such as web browsing, playing music, fetching weather information, and providing news updates. The assistant can recognize voice commands and respond accordingly, making it a versatile tool for users.

## Features
- **Voice Recognition**: Uses the `speech_recognition` library to understand user commands.
- **Text-to-Speech**: Implements `pyttsx3` for vocal responses.
- **Web Browsing**: Opens various websites based on user commands.
- **Music Playback**: Plays specific songs from YouTube.
- **Weather Information**: Fetches and speaks the current weather for a specified city.
- **News Updates**: Retrieves and reads out the latest news headlines.

## Requirements
- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `requests`
  - `google.generativeai`
  - `gradio`
  - `python-dotenv`
  
You can install the required libraries using pip:


## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a `.env` file in the root directory and add your API keys:
   ```
   weatherapi=YOUR_WEATHER_API_KEY
   newsapi=YOUR_NEWS_API_KEY
   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Start the application, and it will initialize the Jarvis assistant.
- Speak commands starting with "Jarvis" to activate the assistant.
- You can ask for the weather, play music, or open websites by saying the appropriate command.

## Example Commands
- "Jarvis, open Google"
- "Jarvis, play perfect"
- "Jarvis, what's the weather in Delhi?"
- "Jarvis, tell me the news"

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the developers of the libraries used in this project.
- Special thanks to the OpenWeatherMap and NewsAPI for providing weather and news data.
