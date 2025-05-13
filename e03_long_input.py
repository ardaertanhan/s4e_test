# Sayfanın hata verip vermediğini test etmek için uzun ve garbage değerler yollama testi

from playwright.sync_api import sync_playwright

def test_long_garbage_input_is_blocked_safely():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://s4e.io/free-security-tools")

        # Accept cookies if shown
        try:
            accept_button = page.get_by_role("button", name="Accept All")
            if accept_button.is_visible():
                accept_button.click()
        except:
            pass

       
        input_box = page.locator("input[placeholder*='example.io']").first

        # Garbage karakter oluşturma
        long_input = "x" * 1500

       
        input_box.fill("")
        input_box.type(long_input)

        
        full_scan_button = page.get_by_role("button", name="Start Full Scan").first
        full_scan_button.click()

        
        modal_title = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
        assert modal_title.is_visible(), "Modal did not appear for long input — scan may have improperly triggered."

       
        close_button = page.locator("button[aria-label='Close']").first
        if close_button.is_visible():
            close_button.click()
            page.wait_for_timeout(500)

        input("Press Enter to close the browser...")
        browser.close()
