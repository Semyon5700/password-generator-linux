#!/bin/bash

# Password Generator Uninstaller
# Author: Semyon5700
# License: GPL-3.0

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root: sudo ./uninstall.sh"
    exit 1
fi

APP_NAME="password-generator"
INSTALL_DIR="/opt/$APP_NAME"
BIN_PATH="/usr/local/bin/$APP_NAME"

echo "Removing program..."
rm -rf "$INSTALL_DIR"

echo "Removing executable file..."
rm -f "$BIN_PATH"

echo "Removing menu file..."
rm -f "/usr/share/applications/$APP_NAME.desktop"

echo "Updating desktop database..."
update-desktop-database /usr/share/applications/

echo "Uninstallation completed!"
