#!/bin/bash
# Test build script

# Find Java installation
JAVA_PATH=$(ls /nix/store/*openjdk*/bin/java | head -1)
if [ -n "$JAVA_PATH" ]; then
    export JAVA_HOME=$(dirname $(dirname $JAVA_PATH))
    echo "Using Java: $JAVA_HOME"
else
    echo "Java not found"
    exit 1
fi

# Clean and build
echo "Cleaning project..."
./gradlew clean

echo "Building debug APK..."
./gradlew assembleDebug

echo "Build complete!"
ls -la app/build/outputs/apk/debug/ 2>/dev/null || echo "APK not found - check build logs"