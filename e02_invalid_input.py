# Geçersiz input (Invalid input,"!!!", "asdf") taramayı başlatıyor mu testi

from playwright.sync_api import sync_playwright

def test_invalid_input_triggers_warning_modal():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://s4e.io/free-security-tools")

        try:
            accept_button = page.get_by_role("button", name="Accept All")
            if accept_button.is_visible():
                accept_button.click()
        except:
            pass

       
        input_box = page.locator("input[placeholder*='example.io']").first

        invalid_inputs = ["!!!", "asdf"]

        for test_input in invalid_inputs:
            input_box.fill("")
            input_box.type(test_input)

          
            full_scan_button = page.get_by_role("button", name="Start Full Scan").first
            full_scan_button.click()

            
            modal_title = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
            assert modal_title.is_visible(), f" Modal did not appear for input: '{test_input}'"

            
            close_button = page.locator("button[aria-label='Close']").first
            if close_button.is_visible():
                close_button.click()
                page.wait_for_timeout(500)

        input(" Press Enter to close the browser...")
        browser.close()
