# xbox-rumble-test

This project provides a Python script, `xbox_rumble.py`, to test rumble functionality on an Xbox 360/ Xbox One controller.

## What It Does

The script connects to an Xbox controller, enabling rumble (vibration) tests. Choose from:
- **Custom rumble test** - Set intensity and duration.
- **Quick test** - Preset rumble at 75% intensity for 2 seconds.
- **Stop rumble** - Instantly stop ongoing rumble.

## Setup and Requirements

1. **Python 3.6 or newer** is required.
2. Install the `pygame` library:

    ```bash
    pip install pygame
    ```
3. **SDL2** - Handles low-level I/O for controllers through Pygame. Pre-installed with Pygame, but install separately if needed.

    ### On Ubuntu:
    ```bash
    sudo apt install libsdl2-dev
    ```

## How to Use It

1. **Clone the Repository**

    ```bash
    git clone https://github.com/1ramihamada/xbox-rumble-test.git
    cd xbox-rumble-test
    ```

2. **Run the Script**

    Connect an Xbox controller and run:
    ```bash
    python3 xbox_rumble.py
    ```

3. **Menu Options**

    - **1: Custom Rumble Test** - Set intensity (0-100%) and duration.
    - **2: Quick Test** - Rumbles both motors at 75% intensity for 2 seconds.
    - **3: Stop Rumble** - Stops any active rumble effect.
    - **q: Quit** - Exits the program.

### Example Usage

Run a quick test by selecting **2** from the menu. For custom settings, select **1** and follow prompts.

## Troubleshooting

- **Controller not detected**: Check connection.
- **Permissions** (Linux): If access issues occur, try `sudo`.

## License

MIT License - open-source project.
