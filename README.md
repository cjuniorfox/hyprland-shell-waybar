# Hyprland Waybar Customization

This project provides a set of customizations for Waybar to enhance the user experience when using it with Hyprland. It integrates several tools to provide a seamless and efficient workflow.

## Features

- **Custom Menu**: Quick access to applications and commands using Rofi.
- **Clock**: Displays the current time and date with a tooltip calendar.
- **Disk Usage**: Monitor disk usage.
- **Memory and CPU Usage**: Keep track of system performance.
- **Dunst Notifications**: Manage notifications with Dunst.
- **Keyboard Layout Switcher**: Easily switch between keyboard layouts.
- **System Updates**: Check for system updates.
- **Audio Output Selector**: Quickly switch between audio outputs.
- **Shutdown Menu**: Access shutdown, reboot, and logout options.

## Tools Used

- `checkupdate`: Checks for system updates.
- `rofi-shutdown-menu`: Provides a shutdown menu using Rofi.
- `rofi-audio-output-selector`: Allows switching between audio outputs using Rofi.
- `hyprland-keyboard-changer`: Changes keyboard layouts for Hyprland.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hyprland-waybar-customization.git
    cd hyprland-waybar-customization
    ```

2. **Copy the configuration files:**
    ```bash
    cp -r .config/waybar ~/.config/waybar
    ```

3. **Install the required tools:**
    Ensure you have the following tools installed:
    - `checkupdate`
    - `rofi`
    - `dunst`
    - `hyprland`
    - `hyprctl`

4. **Configure Waybar:**
    Edit the Waybar configuration files as needed to match your system setup.

## Configuration

### Waybar Configuration

The main configuration file is located at `~/.config/waybar/config`. It includes custom modules and settings for Waybar.

### Custom Scripts

Custom scripts are located in `~/.config/waybar/scripts`. These scripts handle various functionalities such as checking updates, switching keyboard layouts, and managing notifications.

### Example Configuration

Here is an example of the Waybar configuration:

```json
{
    "layer": "top",
    "height": 32,
    "spacing": 6,
    "include": [
        "/etc/xdg/waybar/modules.json",
        "~/.config/waybar/quick-launcher.json",
        "~/.config/waybar/modules-left.json"
    ],
    "modules-center": ["hyprland/workspaces"],
    "modules-right": [
        "idle_inhibitor",
        "disk",
        "memory",
        "cpu",
        "custom/dunst",
        "custom/block_keybind",
        "custom/hyprland_keyboard",
        "custom/updates",
        "pulseaudio",
        "battery",
        "clock",
        "tray",
        "custom/shutdown"
    ]
}
```

## Usage

- **Menu**: Click on the menu icon to open the Rofi menu.
- **Clock**: Click on the clock to switch between time and = - date formats.
- **Disk**, Memory, and CPU: Monitor system performance.
- **Notifications**: Scroll the mouse wheel to show notifications.
- **Keyboard Layout**: Click to change the keyboard layout.
- **System Updates**: Click to check for updates.
- **Audio Output**: Click to switch audio outputs.
- **Shutdown**: Click to open the shutdown menu.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Waybar
- Hyprland
- Rofi
- Dunst

Enjoy your enhanced Waybar experience with Hyprland!