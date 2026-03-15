#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "No install directory provided, defaulting to $HOME/.apgman"
    INSTALL_DIR="$HOME/.apgman"
else
    INSTALL_DIR="$1"
fi

if [ ! -d "$HOME/.apgman" ]; then
    mkdir -p "$HOME/.apgman"
fi

mkdir -p "$INSTALL_DIR/builds"

if [ -f "$HOME/.apgman/install_dir" ]; then
    echo "Warning: $HOME/.apgman/install_dir already exists, overwriting..."
fi

echo "$INSTALL_DIR" > "$HOME/.apgman/install_dir"

cd "$INSTALL_DIR" || exit 1

echo "Cloning apgsearch..."
git clone https://gitlab.com/apgoucher/apgmera.git

if [ -d "apgmera" ]; then
    cd apgmera
    echo "Done!"
else
    echo "Error: apgsearch repo not found."
    exit 1
fi

exit 0