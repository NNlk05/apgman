#!/usr/bin/env bash

RULE=$1
SYMM=$2
ARGS=$3

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

if [ -z "$RULE" ]; then
    echo "No rule provided, defaulting to 'b3s23'"
    RULE="b3s23"
fi
if [ -z "$SYMM" ]; then
    echo "No symmetry provided, defaulting to 'C1'"
    SYMM="C1"
fi


INSTALL_DIR=$($SCRIPT_DIR/apgman-util-get-install-dir.sh)

cd "$INSTALL_DIR/builds" || exit 1

echo "Running apgsearch with rule $RULE and symmetry $SYMM..."

./apgluxe-$RULE-$SYMM $ARGS

exit 0