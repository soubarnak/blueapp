#!/usr/bin/env python3
"""
Computer Service for Remote Control via Bluetooth
Receives commands from Android app and executes system operations
"""

import bluetooth
import json
import platform
import subprocess
import sys
import threading
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('remote_control.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class ComputerRemoteService:
    def __init__(self):
        self.server_socket = None
        self.client_socket = None
        self.is_running = False
        self.os_type = platform.system().lower()
        logger.info(f"Service initialized for {self.os_type}")

    def setup_bluetooth_server(self):
        """Setup Bluetooth server socket"""
        try:
            # Create Bluetooth socket
            self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            
            # Bind to any available port
            self.server_socket.bind(("", bluetooth.PORT_ANY))
            
            # Listen for connections
            self.server_socket.listen(1)
            
            # Get the port number
            port = self.server_socket.getsockname()[1]
            
            # Create service UUID (same as Android app)
            uuid = "00001101-0000-1000-8000-00805F9B34FB"
            
            # Advertise service
            bluetooth.advertise_service(
                self.server_socket,
                "PC Remote Control Service",
                service_id=uuid,
                service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                profiles=[bluetooth.SERIAL_PORT_PROFILE]
            )
            
            logger.info(f"Bluetooth server started on port {port}")
            logger.info(f"Service UUID: {uuid}")
            logger.info("Waiting for connections...")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup Bluetooth server: {e}")
            return False

    def execute_system_command(self, command):
        """Execute system command based on OS"""
        try:
            command = command.strip().upper()
            logger.info(f"Executing command: {command}")
            
            if command == "SHUTDOWN":
                return self._shutdown_system()
            elif command == "SLEEP":
                return self._sleep_system()
            elif command == "LOCK":
                return self._lock_system()
            else:
                logger.warning(f"Unknown command: {command}")
                return {"status": "ERROR", "message": f"Unknown command: {command}"}
                
        except Exception as e:
            logger.error(f"Error executing command {command}: {e}")
            return {"status": "ERROR", "message": str(e)}

    def _shutdown_system(self):
        """Shutdown the computer"""
        try:
            if self.os_type == "windows":
                subprocess.run(["shutdown", "/s", "/t", "5"], check=True)
            elif self.os_type == "darwin":  # macOS
                subprocess.run(["sudo", "shutdown", "-h", "+1"], check=True)
            elif self.os_type == "linux":
                subprocess.run(["shutdown", "-h", "+1"], check=True)
            else:
                return {"status": "ERROR", "message": f"Shutdown not supported on {self.os_type}"}
            
            logger.info("Shutdown command executed successfully")
            return {"status": "SUCCESS", "message": "System will shutdown in 1 minute"}
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Shutdown command failed: {e}")
            return {"status": "ERROR", "message": "Failed to execute shutdown command"}

    def _sleep_system(self):
        """Put the computer to sleep"""
        try:
            if self.os_type == "windows":
                subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"], check=True)
            elif self.os_type == "darwin":  # macOS
                subprocess.run(["pmset", "sleepnow"], check=True)
            elif self.os_type == "linux":
                # Try systemctl first, then pm-suspend
                try:
                    subprocess.run(["systemctl", "suspend"], check=True)
                except subprocess.CalledProcessError:
                    subprocess.run(["pm-suspend"], check=True)
            else:
                return {"status": "ERROR", "message": f"Sleep not supported on {self.os_type}"}
            
            logger.info("Sleep command executed successfully")
            return {"status": "SUCCESS", "message": "System going to sleep"}
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Sleep command failed: {e}")
            return {"status": "ERROR", "message": "Failed to execute sleep command"}

    def _lock_system(self):
        """Lock the computer screen"""
        try:
            if self.os_type == "windows":
                subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"], check=True)
            elif self.os_type == "darwin":  # macOS
                subprocess.run(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"], check=True)
            elif self.os_type == "linux":
                # Try different lock commands based on desktop environment
                lock_commands = [
                    ["gnome-screensaver-command", "--lock"],
                    ["xdg-screensaver", "lock"],
                    ["dm-tool", "lock"],
                    ["loginctl", "lock-session"]
                ]
                
                success = False
                for cmd in lock_commands:
                    try:
                        subprocess.run(cmd, check=True)
                        success = True
                        break
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        continue
                
                if not success:
                    return {"status": "ERROR", "message": "No suitable lock command found"}
            else:
                return {"status": "ERROR", "message": f"Lock not supported on {self.os_type}"}
            
            logger.info("Lock command executed successfully")
            return {"status": "SUCCESS", "message": "System locked"}
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Lock command failed: {e}")
            return {"status": "ERROR", "message": "Failed to execute lock command"}

    def handle_client_connection(self, client_socket, client_info):
        """Handle client connection and commands"""
        logger.info(f"Client connected: {client_info}")
        
        try:
            while self.is_running:
                # Receive data from client
                data = client_socket.recv(1024)
                if not data:
                    break
                
                command = data.decode('utf-8').strip()
                logger.info(f"Received command from {client_info}: {command}")
                
                # Execute command
                result = self.execute_system_command(command)
                
                # Send response back to client
                response = json.dumps(result) + "\n"
                client_socket.send(response.encode('utf-8'))
                
                logger.info(f"Response sent to {client_info}: {result}")
                
        except Exception as e:
            logger.error(f"Error handling client {client_info}: {e}")
        finally:
            try:
                client_socket.close()
            except:
                pass
            logger.info(f"Client disconnected: {client_info}")

    def start_server(self):
        """Start the Bluetooth server"""
        if not self.setup_bluetooth_server():
            return False
        
        self.is_running = True
        
        try:
            while self.is_running:
                logger.info("Waiting for connection...")
                
                # Accept connection
                client_socket, client_info = self.server_socket.accept()
                
                logger.info(f"Accepted connection from {client_info}")
                
                # Handle client in separate thread
                client_thread = threading.Thread(
                    target=self.handle_client_connection,
                    args=(client_socket, client_info)
                )
                client_thread.daemon = True
                client_thread.start()
                
        except KeyboardInterrupt:
            logger.info("Server interrupted by user")
        except Exception as e:
            logger.error(f"Server error: {e}")
        finally:
            self.stop_server()

    def stop_server(self):
        """Stop the Bluetooth server"""
        self.is_running = False
        
        try:
            if self.server_socket:
                self.server_socket.close()
        except:
            pass
        
        logger.info("Server stopped")

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import bluetooth
        logger.info("PyBluez is available")
        return True
    except ImportError:
        logger.error("PyBluez is not installed. Please install it using:")
        logger.error("pip install pybluez")
        return False

def main():
    """Main function"""
    logger.info("=== PC Remote Control Service ===")
    logger.info(f"Starting service on {platform.system()} {platform.release()}")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Create and start service
    service = ComputerRemoteService()
    
    try:
        service.start_server()
    except KeyboardInterrupt:
        logger.info("Service stopped by user")
    except Exception as e:
        logger.error(f"Service error: {e}")
    finally:
        service.stop_server()

if __name__ == "__main__":
    main()
