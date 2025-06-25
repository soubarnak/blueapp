# Quick APK Build Guide

## The Module Selection Issue

When Android Studio asks "Select modules to include in configuration", simply:

1. **Select the "app" module** - this is your main Android application
2. Click **OK**

The "app" module contains all your Android app code and is the only module you need to build the APK.

## Step-by-Step Solution

### 1. Open Project in Android Studio
- File → Open → Select this project folder
- Wait for indexing to complete

### 2. When Asked About Modules
- Check **app** module only
- Click **OK**

### 3. Sync Project
- Should happen automatically
- If not: File → Sync Project with Gradle Files

### 4. Build APK
- Build → Build Bundle(s) / APK(s) → Build APK(s)
- Select **app** module if prompted again
- Wait for build to complete

### 5. Find Your APK
- Look in: `app/build/outputs/apk/debug/app-debug.apk`
- Or click "locate" in the build notification

## Alternative: Command Line Build

If Android Studio is giving you trouble:

```bash
# Make executable (Mac/Linux)
chmod +x gradlew

# Build APK
./gradlew assembleDebug

# On Windows use:
gradlew.bat assembleDebug
```

## What Each File Does

- **app/** = Your Android app code (this is the module to select)
- **build.gradle** = Build configuration  
- **gradlew** = Build script

## Troubleshooting

**"No modules found"**: 
- Make sure you opened the root project folder (not the app folder)
- The folder should contain `build.gradle` and `settings.gradle`

**"Gradle sync failed"**:
- Check internet connection
- File → Invalidate Caches and Restart

**"SDK not found"**:
- File → Project Structure → SDK Location
- Set path to your Android SDK

Your APK will be a debug version ready for testing on your Android device!