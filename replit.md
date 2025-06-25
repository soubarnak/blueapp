# PC Remote Control System

## Overview

This is a Bluetooth-based remote control system that allows users to control their computer from an Android device. The system consists of three main components: an Android application, a Python-based computer service, and a web interface for demonstration purposes. The application enables remote execution of system commands like shutdown, sleep, and lock through a secure Bluetooth Classic connection using the Serial Port Profile (SPP).

## System Architecture

The system follows a client-server architecture where:
- **Android App (Client)**: Initiates Bluetooth connections and sends commands
- **Python Service (Server)**: Runs on the target computer, listens for Bluetooth connections and executes system commands
- **Web Interface**: Provides a demonstration interface and setup instructions

### Communication Protocol
- **Transport Layer**: Bluetooth Classic (RFCOMM) using SPP profile
- **Message Format**: JSON-based command structure
- **Security**: Bluetooth pairing-based authentication

## Key Components

### Android Application
- **Technology**: Java with Android SDK
- **UI Framework**: Material Design with AppCompat
- **Bluetooth Integration**: Android Bluetooth API with SPP UUID
- **Architecture**: Single Activity with service-based Bluetooth communication
- **Key Features**:
  - Device discovery and pairing
  - Real-time connection status
  - Command transmission with feedback
  - Permission handling for Bluetooth access

### Python Computer Service
- **Technology**: Python 3.7+ with PyBluez library
- **Architecture**: Threaded server with async command processing
- **Cross-platform Support**: Windows, macOS, and Linux
- **Key Features**:
  - Bluetooth server socket management
  - JSON command parsing and validation
  - System command execution via subprocess
  - Comprehensive logging and error handling

### Web Interface
- **Technology**: HTML5, Bootstrap 5, FontAwesome
- **Purpose**: Demonstration and setup instructions
- **Architecture**: Static frontend with responsive design
- **Key Features**:
  - Modern gradient UI design
  - Setup documentation
  - Feature showcase

## Data Flow

1. **Connection Establishment**:
   - Android app scans for Bluetooth devices
   - User selects target computer
   - App initiates RFCOMM connection using SPP UUID
   - Python service accepts connection and establishes socket

2. **Command Execution**:
   - Android app sends JSON-formatted command
   - Python service receives and validates command
   - System command executed via subprocess
   - Response sent back to Android app
   - Status updated in both interfaces

3. **Error Handling**:
   - Connection failures handled gracefully
   - Invalid commands rejected with error messages
   - Automatic reconnection attempts
   - Comprehensive logging for debugging

## External Dependencies

### Android Dependencies
- Android Bluetooth API (built-in)
- AppCompat library for UI components
- Material Design components
- Required permissions: BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION

### Python Dependencies
- **PyBluez**: Bluetooth communication library
- **Flask**: Web framework (for potential web service extension)
- **Standard Library**: json, platform, subprocess, threading, logging

### System Requirements
- **Android**: API level supporting Bluetooth Classic
- **Computer**: Bluetooth adapter, Python 3.7+
- **OS Support**: Windows, macOS, Linux

## Deployment Strategy

### Development Environment
- **Platform**: Replit with Python 3.11 runtime
- **Package Management**: pip for Python dependencies
- **Build System**: Standard Python project structure

### Production Deployment
1. **Computer Service**:
   - Install Python 3.7+ and PyBluez
   - Run as system service or background process
   - Configure Bluetooth adapter and permissions

2. **Android App**:
   - Build APK using Android Studio
   - Install on target Android device
   - Grant required Bluetooth permissions

3. **Configuration**:
   - Pair Android device with computer
   - Ensure Bluetooth services are discoverable
   - Configure firewall/security settings if needed

## Changelog

- June 25, 2025: Initial setup with Android app and Python service
- June 25, 2025: Added complete build system with Gradle configuration
- June 25, 2025: Created comprehensive setup guides and build instructions
- June 25, 2025: Implemented web demonstration interface

## User Preferences

Preferred communication style: Simple, everyday language.