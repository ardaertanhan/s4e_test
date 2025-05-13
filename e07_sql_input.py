# SQL tipi input yollayarak web sitesinin hata alıp almadığını kontrol etme

from playwright.sync_api import sync_playwright

def test_sql_like_input_triggers_modal_not_scan():
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

        # Target scan input field
        input_box = page.locator("input[placeholder*='example.io']").first

        sql_like_input = "' OR 1=1 --"

        input_box.fill("")
        input_box.type(sql_like_input)

        # Click "Start Full Scan"
        full_scan_button = page.get_by_role("button", name="Start Full Scan").first
        full_scan_button.click()

        # Wait for modal
        page.wait_for_selector("text=Scan Only One: Domain, Ipv4, Subdomain")
        modal_title = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
        assert modal_title.is_visible(), "Modal did not appear for SQL-like input"

        # Click "Retry" and check modal still exists
        retry_button = page.get_by_role("button", name="Retry")
        retry_button.click()

        page.wait_for_timeout(1000)
        assert modal_title.is_visible(), "Modal closed unexpectedly after SQL-like input"

        input("Press Enter to close the browser...")
        browser.close()
