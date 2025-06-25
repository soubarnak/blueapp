# PC Remote Control

A Bluetooth-based remote control system that allows you to control your computer from an Android device. Perform system operations like shutdown, sleep, and lock remotely via a secure Bluetooth connection.

## Features

- **Bluetooth Connectivity**: Secure Bluetooth Classic connection using SPP profile
- **System Control**: Remote shutdown, sleep, and lock commands
- **Cross-Platform**: Supports Windows, macOS, and Linux
- **Android App**: Intuitive Material Design interface
- **Real-time Feedback**: Status updates and error handling
- **Secure Commands**: Validated command execution with proper error handling

## Components

### Android Application
- Java-based Android app with Material Design UI
- Bluetooth device discovery and pairing
- Secure command transmission
- Real-time connection status
- Background operation support

### Computer Service
- Python service with PyBluez for Bluetooth communication
- Cross-platform system command execution
- JSON-based message protocol
- Comprehensive logging
- Error handling and validation

### Web Interface
- Bootstrap-based demonstration interface
- Setup instructions and feature overview
- Status monitoring (demonstration only)

## Setup Instructions

### Computer Setup

1. **Install Python 3.7+**
   ```bash
   # Check Python version
   python --version
   