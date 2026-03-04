import subprocess
import time

# --- CONFIGURATION ---
TARGET_NUMBER = "1690"
ITERATIONS = 100

# COORDINATES: 
# Use 'Pointer Location' in Developer Options to find these for your specific phone:
TEXT_BOX_X = 500   # Middle of the "Type a message" area
TEXT_BOX_Y = 2100  # Bottom area where the text box usually is

# These coordinates are for the "Send" button for Galaxy Note S21. Adjust as needed.
SEND_BUTTON_X = 1000
SEND_BUTTON_Y = 2215

def run_adb(command):
    subprocess.run(f"adb shell {command}", shell=True)

def main():
    print("Launching SMS App...")
    run_adb(f"am start -a android.intent.action.SENDTO -d sms:{TARGET_NUMBER}")
    time.sleep(1) # Wait for app to open

    print(f"Starting SMS sequence for {ITERATIONS} messages...")
    # --- START TIMER ---
    start_time = time.time()
    for i in range(1, ITERATIONS + 1):
        # Clear input text
        run_adb("input text ''")

        print(f"Processing SMS {i}...")

        # STEP 1: Click the text box to ensure focus
        # Without this, 'input text' often fails
        run_adb(f"input tap {TEXT_BOX_X} {TEXT_BOX_Y}")
        time.sleep(0.5)

        # STEP 2: Type the message
        message = f"Test0{i}"
        run_adb(f"input text {message}")

        # Press back to hide keyboard (if needed)
        run_adb("input keyevent 4") 

        # STEP 3: Click Send
        run_adb(f"input tap {SEND_BUTTON_X} {SEND_BUTTON_Y}")
        time.sleep(0.5)
        run_adb(f"input tap {SEND_BUTTON_X} {SEND_BUTTON_Y}")
    
    # STEP 4: Force close app
    run_adb("am force-stop com.google.android.apps.messaging")

    # --- END TIMER & CALCULATION ---
    end_time = time.time()
    total_duration = end_time - start_time
    
    print("-" * 30)
    print(f"Finished {ITERATIONS} messages.")
    print(f"Total Execution Time: {total_duration:.2f} seconds")
    print("-" * 30)

if __name__ == "__main__":
    main()