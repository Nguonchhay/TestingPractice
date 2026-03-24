from patchright.sync_api import sync_playwright
import random
import time

def generate_redeem_code(length=8):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(charset) for _ in range(length))

def run_redeem_attempt(playwright, user_id, server_id):
    # Use context manager for the browser to ensure it closes properly every time
    # Pathing: Use r"" for Windows paths to avoid 'unicodeescape' errors
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=r"C:\playwright_profile", 
        channel="chrome",
        headless=False,
        no_viewport=False, # Set False to allow mobile emulation
        viewport={"width": 390, "height": 844},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    )

    # Use the first page created by persistent context instead of creating a new one every time
    page = browser.pages[0] if browser.pages else browser.new_page()
    code = generate_redeem_code()
    print(f"\n--- Retry Redeem Code: {code} ---")

    try:
        page.goto("https://aomlbb.play.cellcard.com.kh", wait_until="networkidle", timeout=60000)
        
        # 1. Clear and Fill IDs (Force clearing in case persistent context remembered old values)
        user_field = page.locator('input[placeholder*="User ID"]')
        server_field = page.locator('input[placeholder*="Server ID"]')
        
        user_field.wait_for(state="visible")
        user_field.fill("") # Clear first
        user_field.type(user_id, delay=50)
        
        server_field.fill("")
        server_field.type(server_id, delay=50)
        
        # 2. Click "Check" button
        check_btn = page.locator('button:has-text("Check"), button:has-text("ពិនិត្យ")')
        check_btn.scroll_into_view_if_needed()
        check_btn.click() # Using click() is often more stable in Chrome than tap()
        
        # Wait for the account nickname to appear (verifies the check worked)
        page.wait_for_timeout(1000)

        # 3. Handle the Redeem Code input
        # Use a more flexible selector for the placeholder changes you mentioned
        code_input = page.locator('input[placeholder*="Redeem" i], input[placeholder*="code" i]')
        code_input.wait_for(state="visible")
        code_input.click()
        
        # Clear any existing code
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        
        # Human-like typing
        page.keyboard.type(code, delay=random.randint(50, 150))

        # 4. Confirm Button
        confirm_btn = page.locator('button:has-text("Confirm"), button:has-text("បញ្ជាក់")')
        confirm_btn.click()
        page.wait_for_timeout(1000)

    except Exception as e:
        print(f"Error during attempt: {e}")
    finally:
        # Close the context so the next loop starts with a fresh window
        browser.close()

# Main Loop
USER_ID = "2100310736"
SERVER_ID = "17263"

with sync_playwright() as playwright:
    # 1. Start the timer
    start_time = time.time()
    test_count = 15
    for i in range(test_count):
        print(f"Starting Round {i+1}...")
        run_redeem_attempt(playwright, USER_ID, SERVER_ID)
        
        wait = random.uniform(1, 3)
        print(f"Waiting {wait:.2f}s before next browser launch...")
        time.sleep(wait)
    
    # 2. End the timer
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution Time: {duration:.2f} seconds for retry {test_count} times")