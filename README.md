# Dawia Assistant

Dawia is a personal assistant that integrates with Mistral's API to generate responses, it can also do various tasks like controlling IoT devices, launching applications, and organizing files. Dawia can be interacted with through text or speech prompts.

![demo_gif](https://github.com/thevorgx/projects_assets/blob/master/Dawia_readme_assets/demo.gif)

[watch Dawia's demo video here](https://www.youtube.com/watch?v=DV3MVqj8Ig4)

## Current Features

- **Voice Assistant**: Interact with Dawia through text or speech prompts.
- **API Model Selection**: Choose from different Mistral models to chape the assistant's response.
- **Voice Configuration**: Customize Dawia's voice output using different voice options.
- **Google Authentication**: Login using your Google account to access Dawia.
- **Search Engine Integration**: Search Google or YouTube directly via commands.
- **Program LauncherControl**: Open or launch applications.
- **Device Control**: Control IoT devices (like lights).
- **File Organization**: Automatically organize files in directories with a simple command.
- **Chat History**: Save load, delete chat history for user-specific interactions.

## Project Structure

```bash
├── assets/                         # -> Contains images and icons for Dawia's UI
│   ├── img   
│   ├── user_img
├── chat_db/                        # -> Contains user chat history management file
│   ├── local_db_manager.py         # -> Saves and loads chat history()
├── config_utility/                 # -> Contains configuration utility file
│   ├── config_manager.py           # -> Loads and saves configurations            
├── source/                         # -> Main back end source code files
│   ├── response_manager.py         # -> Handles Mistral AI API interactions, and response streaming 
│   ├── voice_manager.py            # -> Handles speech prompting, tts(text to speech), and stt(speech to text)
│   ├── tools_manager.py            # -> Utility functions (image processing, launching apps, etc.)
│   ├── dir_manager.py              # -> Manages file organization feature
│   ├── search_engine_manager.py    # -> Search Google or YouTube usng user prompt
│   └── device_manager.py           # -> Handles device management like toggling lights
├── google_credentials.json         # -> Google authentication credentials for login feature
├── README.md                       # -> Project documentation
├── config.json                     # -> Configuration file storing default user values
└── app.py                          # -> Main entry point for Dawia's web application
```
## Project Architecture

![architecture](https://github.com/thevorgx/projects_assets/blob/master/Dawia_readme_assets/diag.webp)

## Prerequisites

- **Python 3.12+**
- **Streamlit** for web application development
- **Google API credentials** for authentication

### Required Python Libraries

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

### Libraries
- `mistralai`: For interacting with the Mistral API.
- `edge_tts`: For text-to-speech conversion.
- `speech_recognition`: For speech-to-text conversion.
- `playsound`: For playing generated audio files.
- `streamlit`: Main web application framework.
- `streamlit_image_select`: For image selection.
- `streamlit_google_auth`: Google authentication integration.
- `concurrent.futures`: For handling asynchronous tasks.
- `pickle`: For handling user/chat history.
- `json`: For handling JSON data(user config).
- `os`: For interacting with the operating system.
- `Pathlib`: For handling file paths.
- `chutil`: For handling file operations.
- `subprocess`: For launching applications.
- `wxPython`: for directory path selection without interacting with streamlit mainloop.
- `base64`: For image encoding.
- `yeelight`: For controlling Yeelight devices.
- `webbrowser`: For opening URLs.
- `time`: For pauses between each yeld for response stream to the user.


## Configuration

- **config.json**: The configuration file contains the initial settings for the assistant, such as the API model, Dawia's voice model, toggle voice response ON/OFF, and user avatar.
- **google_credentials.json**: Required for enabling Google authentication.

## Running the Project

1. **Clone the repository**:

   ```bash
   git clone https://github.com/thevorgx/Dawia_virtual_assistant
   cd dawia-assistant
   ```

2. **Set up virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment**:

   Ensure you have the `google_credentials.json` file in the root directory.

5. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```
   or
      ```bash
   python -m streamlit run app.py
   ```

6. **Access the app**:

   Visit `http://localhost:8501` in your browser.

## Usage

Once you have the app running:

1. **Login**: Use your Google account to authenticate.
2. **Configure API Key**: Paste your Mistral API key in the provided field in the sidebar.
3. **Interact**: You can either type messages or use the microphone button to send speech commands.
4. **Configure settings**: In the sidebar, customize Dawia's settings, such as API model, voice options, and your user avatar.

## Contribution
This project was done as a part of ALX software engineering program(back-end), the development of Dawia will continue to improve and add more features. the idea behind the making of Dawia, is to creat a personal assistant that can be used to automate tasks and control your home devices using text or voice commands.

This project is open source, and it will always be, If you have any ideas or suggestions, feel free to open an issue or submit a pull request.
