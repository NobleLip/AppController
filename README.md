```
 ▄▄▄      ██▓███  ██▓███      ▄████▄  ▒█████  ███▄    █▄▄▄█████▓██▀███  ▒█████  ██▓    ██▓   ▓█████ ██▀███  
▒████▄   ▓██░  ██▓██░  ██▒   ▒██▀ ▀█ ▒██▒  ██▒██ ▀█   █▓  ██▒ ▓▓██ ▒ ██▒██▒  ██▓██▒   ▓██▒   ▓█   ▀▓██ ▒ ██▒
▒██  ▀█▄ ▓██░ ██▓▓██░ ██▓▒   ▒▓█    ▄▒██░  ██▓██  ▀█ ██▒ ▓██░ ▒▓██ ░▄█ ▒██░  ██▒██░   ▒██░   ▒███  ▓██ ░▄█ ▒
░██▄▄▄▄██▒██▄█▓▒ ▒██▄█▓▒ ▒   ▒▓▓▄ ▄██▒██   ██▓██▒  ▐▌██░ ▓██▓ ░▒██▀▀█▄ ▒██   ██▒██░   ▒██░   ▒▓█  ▄▒██▀▀█▄  
 ▓█   ▓██▒██▒ ░  ▒██▒ ░  ░   ▒ ▓███▀ ░ ████▓▒▒██░   ▓██░ ▒██▒ ░░██▓ ▒██░ ████▓▒░██████░██████░▒████░██▓ ▒██▒
 ▒▒   ▓▒█▒▓▒░ ░  ▒▓▒░ ░  ░   ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ▒ ▒  ▒ ░░  ░ ▒▓ ░▒▓░ ▒░▒░▒░░ ▒░▓  ░ ▒░▓  ░░ ▒░ ░ ▒▓ ░▒▓░
  ▒   ▒▒ ░▒ ░    ░▒ ░          ░  ▒    ░ ▒ ▒░░ ░░   ░ ▒░   ░     ░▒ ░ ▒░ ░ ▒ ▒░░ ░ ▒  ░ ░ ▒  ░░ ░  ░ ░▒ ░ ▒░
  ░   ▒  ░░      ░░          ░       ░ ░ ░ ▒    ░   ░ ░  ░       ░░   ░░ ░ ░ ▒   ░ ░    ░ ░     ░    ░░   ░ 
      ░  ░                   ░ ░         ░ ░          ░           ░        ░ ░     ░  ░   ░  ░  ░  ░  ░     
                             ░                                                                              
```



# AppController

AppController is a small utility project designed to help you manage your time by limiting access to distracting applications and websites, such as YouTube or games. Originally created as a personal productivity tool, it was developed to run silently in the background and restrict usage of specified apps for a set amount of time each day.

> **Note:** This project was originally developed on Windows, but as of now, im using Linux/MacOs. This repository serves as a reminder and archive of past projects.



## Features

- **Customizable App Control:** Specify which applications or websites to monitor.
- **Daily Usage Limits:** Set how long each app can be used per day.
- **Silent Operation:** Runs without a visible console window.



## How to Use

1. **Edit the Configuration**

   In your script, define the apps you want to control and their daily usage limits. Example:

   ```python
   Apps = ['YouTube', 'League of Legends', 'Naruto', 'Name that Appears on the Windows TaskBar']

   # Control array: set allowed daily usage in seconds
   Cont = {
       'YouTube': 3600,  # 1 hour
       'League of Legends': 3600,  # 1 hour
       'Naruto': 1,  # 1 second (example)
       'Name that Appears on the Windows TaskBar': 1800  # 30 minutes
   }

   # Mapping app names to their executable process names
   Consola = {
       'YouTube': 'brave.exe',
       'League of Legends': 'LeagueClient.exe',
       'Naruto': 'brave.exe',
       'Name that Appears on the Windows TaskBar': 'NameOfExecutable.exe'
   }
   ```

2. **Build the Executable**

   Use [PyInstaller](https://www.pyinstaller.org/) to create a standalone executable that runs without a console window:

   ```sh
   pyinstaller --noconsole wind.py
   ```

3. **Run the Program**

   Launch the generated `.exe` file. The program will monitor and control the specified apps according to your configuration.



## Requirements

- Python 3.x
- [PyInstaller](https://www.pyinstaller.org/) (`pip install pyinstaller`)



## Disclaimer

This project was a quick experiment and is not actively maintained. Use at your own risk.



## License

This project is provided as-is for personal use and experimentation.

# Update 

I will work on this project in order to make it available for Linux and MacOs and improve every aspect that I can.
