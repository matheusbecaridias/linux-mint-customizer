I'll retrieve the full file content and create comprehensive instructions for those commands.# Display Brightness Control Instructions

Here's a clear instruction guide for the commands in your file:

## Overview
These commands adjust display brightness on Linux systems using `xrandr`, the X11 display configuration tool. This is useful for Linux Mint and other X11-based desktop environments.

## Step-by-Step Instructions

### 1. **List Connected Displays**
```bash
xrandr | grep " connected"
```
**Purpose:** Identify all connected displays and their names (like VGA-1, HDMI-1, DP-1, etc.)

**Output Example:**
```
VGA-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 510mm x 287mm
HDMI-1 connected (normal left inverted right x axis y axis) 0mm x 0mm
```

### 2. **Adjust Display Brightness**
```bash
xrandr --output VGA-1 --brightness 0.6
```
**Purpose:** Set the brightness of the VGA-1 display to 60%

**Parameters:**
- `--output VGA-1` — Specify which display to adjust (replace with your display name from step 1)
- `--brightness 0.6` — Set brightness level (ranges from 0.0 to 1.0, where 1.0 is 100%)

## Usage Guide

1. **Find your display name:**
   ```bash
   xrandr | grep " connected"
   ```
   Note the output name (e.g., `VGA-1`, `HDMI-1`, `eDP-1`)

2. **Adjust brightness** by replacing `VGA-1` with your display and `0.6` with your desired level:
   ```bash
   xrandr --output HDMI-1 --brightness 0.8  # 80% brightness
   ```

## Brightness Values Reference
- `0.5` = 50% (dimmer)
- `0.75` = 75% (medium)
- `1.0` = 100% (full brightness)

## Tips
- Changes are temporary and reset on reboot
- For permanent changes, add the command to your startup script or autostart applications
- Works for all connected displays; adjust each separately if needed
