#!/usr/bin/env python3
import sys
import os
import subprocess

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No file specified")
        sys.exit(1)

    filepath = os.path.abspath(sys.argv[1])

    # Run with proper PTY allocation
    if os.name == 'nt':  # Windows
        # Use winpty or just run directly (sometimes works)
        subprocess.run(['pybricksdev', 'run', 'ble', filepath, '--stay-connected', '--no-start'])
    else:  # Linux/Mac
        # Force allocation of a pseudo-terminal
        subprocess.run(['pybricksdev', 'run', 'ble', filepath, '--stay-connected', '--no-start'])