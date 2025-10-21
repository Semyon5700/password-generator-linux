#!/bin/bash

# Password Generator Installer
# Author: Semyon5700
# License: GPL-3.0

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root: sudo ./install.sh"
    exit 1
fi

APP_NAME="password-generator"
INSTALL_DIR="/opt/$APP_NAME"
BIN_PATH="/usr/local/bin/$APP_NAME"

echo "Creating installation directory..."
mkdir -p "$INSTALL_DIR"

echo "Copying program files..."
cp password_generator.py "$INSTALL_DIR/"
if [ -d "icons" ]; then
    cp -r icons "$INSTALL_DIR/"
else
    echo "Icons folder not found, continuing without icons"
fi

echo "Creating executable file..."
cat > "$BIN_PATH" << EOF
#!/bin/bash
cd $INSTALL_DIR
exec python3 password_generator.py
EOF

chmod +x "$BIN_PATH"
chmod +x "$INSTALL_DIR/password_generator.py"

echo "Creating menu file..."
cat > "/usr/share/applications/$APP_NAME.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Password Generator
Comment=Simple secure password generator
Exec=$BIN_PATH
Icon=password-generator
Categories=Utility;Security;
Terminal=false
StartupNotify=true
Keywords=password;generator;security;
EOF

echo "Installation completed!"
echo "Program installed in: $INSTALL_DIR"
echo "Executable: $BIN_PATH"
