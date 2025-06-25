# Android Studio Setup Guide

## Step-by-Step Instructions for Building APK

### 1. Download and Install Android Studio
- Download from: https://developer.android.com/studio
- Install with default settings
- Launch Android Studio

### 2. Set Up Android SDK
1. In Android Studio, go to **File → Settings** (or **Android Studio → Preferences** on Mac)
2. Navigate to **Appearance & Behavior → System Settings → Android SDK**
3. In the **SDK Platforms** tab, check:
   - Android 14.0 (API level 34) - recommended
   - Android 7.0 (API level 24) - minimum required
4. In the **SDK Tools** tab, ensure these are installed:
   - Android SDK Build-Tools
   - Android SDK Platform-Tools
   - Android SDK Tools
5. Click **Apply** and **OK** to download

### 3. Open the Project
1. Click **Open an existing project**
2. Navigate to and select the project root folder (the one containing `build.gradle`)
3. Click **Open**

### 4. Configure SDK Path (If Prompted)
If Android Studio asks for SDK location:
1. Go to **File → Project Structure**
2. In **SDK Location**, set the path to your Android SDK
   - Windows: Usually `C:\Users\[username]\AppData\Local\Android\Sdk`
   - Mac: Usually `~/Library/Android/sdk`
   - Linux: Usually `~/Android/Sdk`

### 5. Sync Project
1. Android Studio should automatically prompt to sync
2. If not, click **File → Sync Project with Gradle Files**
3. Wait for sync to complete (may take several minutes on first run)

### 6. Build APK
Once sync is complete:
1. Go to **Build** menu
2. Select **Build Bundle(s) / APK(s)**
3. Choose **Build APK(s)**
4. Wait for build to complete

### 7. Locate APK
1. After successful build, click **locate** in the notification
2. Or manually find it at: `app/build/outputs/apk/debug/app-debug.apk`

## Alternative: Command Line Build

If you prefer command line:

### Windows:
```cmd
gradlew.bat assembleDebug
```

### Mac/Linux:
```bash
chmod +x gradlew
./gradlew assembleDebug
```

## Troubleshooting Common Issues

### "No configured toolchains"
- Install Android Studio with default SDK
- Restart Android Studio after installation

### "SDK location not found"
- Set SDK path in File → Project Structure → SDK Location
- Ensure Android SDK is properly installed

### "Module not specified"
When Android Studio asks to select modules:
1. Select the **app** module
2. This is the main application module
3. Click **OK**

### "Gradle sync failed"
1. Check internet connection
2. Go to **File → Invalidate Caches and Restart**
3. Try **File → Sync Project with Gradle Files** again

### "Build failed - SDK not found"
1. Open **File → Project Structure**
2. Go to **SDK Location**
3. Set correct path to Android SDK
4. Click **Apply** and rebuild

## Project Structure Explanation

```
PC Remote Control/
├── app/                    ← Main Android app module
│   ├── build.gradle       ← App-level build config
│   └── src/main/          ← App source code
├── build.gradle           ← Project-level build config
├── settings.gradle        ← Project modules config
├── gradle.properties      ← Gradle settings
├── gradlew                ← Gradle wrapper (Linux/Mac)
├── gradlew.bat           ← Gradle wrapper (Windows)
└── gradle/wrapper/        ← Gradle wrapper files
```

## What Each Module Does

- **app**: The main Android application module containing all your app code
- This is the module you want to select when Android Studio asks

## Final Notes

- The APK will be in debug mode by default (for testing)
- For Play Store release, you'll need to sign the APK
- The debug APK can be installed directly on your Android device
- Make sure to enable "Install from Unknown Sources" on your device

Once you have the APK built, you can transfer it to your Android device and install it to start using your PC Remote Control app!