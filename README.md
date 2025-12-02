# python-rpi-screen-br-control

A simple Python CLI tool to control the power and brightness of the official Raspberry Pi 7" Touchscreen.

## Prerequisites

* Python 3
* [rpi_backlight](https://github.com/linusg/rpi-backlight) library

## Installation

1.  **Install the dependency:**
    ```bash
    pip install rpi_backlight
    ```

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Klarulor/python-rpi-screen-br-control.git](https://github.com/Klarulor/python-rpi-screen-br-control.git)
    cd python-rpi-screen-br-control
    ```

## Usage

You can run the script via the command line to toggle power or set specific brightness levels.

### Toggle Power

**Turn the screen ON:**
```bash
python main.py true
```

**Turn the screen OFF:**
```bash
python main.py false

```
**Set Brightness**
To change the brightness, provide an integer value (usually between 0 and 100, or 0 and 255 depending on your specific hardware configuration).
Example (Set brightness to 50):
```bash
python main.py 50
```

### Troubleshooting
Permission Denied? If you get a permission error, you may need to add your user to the video group or set up udev rules. Please refer to the rpi_backlight documentation for instructions on how to run this without sudo.
