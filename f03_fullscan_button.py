# ✅ TC-F03: Full Scan button triggers scan input modal

from playwright.sync_api import sync_playwright

def test_full_scan_button_opens_modal():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        
        page.goto("https://s4e.io/free-security-tools")

        # Cookie pop-up ile ilgilenme
        try:
            accept_button = page.get_by_role("button", name="Accept All")
            if accept_button.is_visible():
                accept_button.click()
        except:
            pass  

        #  "Start Full Scan" butonunu bul ve tıkla
        full_scan_button = page.get_by_role("button", name="Start Full Scan").first
        assert full_scan_button.is_visible(), "Full Scan button not visible"
        full_scan_button.click()

        # Modal ve başlığı kontrol et
        modal_title = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
        assert modal_title.is_visible(), "Modal did not appear after clicking Full Scan"

        input("Press Enter to close the browser...")
        browser.close()
