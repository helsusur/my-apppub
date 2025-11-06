import subprocess
import os
import sys

# The Public Google Drive Folder URL
# IMPORTANT: This link must be set to "Anyone with the link can view" in Google Drive.
GOOGLE_DRIVE_URL = "https://drive.google.com/drive/folders/1oQAhts89LuWBECml1AcvoklepL_DkAWZ?usp=sharing"

# --- 1. Define Browser Launch Command ---

def launch_app_mode(url, browser_name):
    """Launches the given URL in the specified browser's App Mode."""
    
    if browser_name == "chrome":
        # Common locations for Chrome executable
        paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
        
    elif browser_name == "edge":
        # Common locations for Edge executable
        paths = [
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        ]
        
    else:
        return False # Unsupported browser name

    browser_path = next((p for p in paths if os.path.exists(p)), None)

    if browser_path:
        # The '--app=' argument is the key: it creates the dedicated, executable-like window
        command = [browser_path, f"--app={url}"]
        
        # Launch non-blocking and hide console
        subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
        return True
    return False

# --- 2. Execute the Launch ---

if __name__ == "__main__":
    
    # Priority 1: Try Google Chrome (Best compatibility with Google Drive)
    if launch_app_mode(GOOGLE_DRIVE_URL, "chrome"):
        # print("Launched in Chrome App Mode.") # Suppressed by --windowed flag
        sys.exit()
        
    # Priority 2: Try Microsoft Edge (Good fallback on Windows)
    elif launch_app_mode(GOOGLE_DRIVE_URL, "edge"):
        # print("Launched in Edge App Mode.") # Suppressed by --windowed flag
        sys.exit()

    # Fallback to default system browser
    else:
        # This will open in their default full browser if App Mode executables aren't found
        import webbrowser
        webbrowser.open(GOOGLE_DRIVE_URL)