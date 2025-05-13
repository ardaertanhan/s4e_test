#  Geçersiz input verme, modali kapatma, hızlıca resubmit etme fonksiyonel testi

from playwright.sync_api import sync_playwright

def test_modal_close_and_resubmit_does_not_crash():
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
        invalid_input = "asdf"

        # İlk submission
        input_box.fill("")
        input_box.type(invalid_input)
        full_scan_button = page.get_by_role("button", name="Start Full Scan").first
        full_scan_button.click()

        # Modali bekleme
        modal_title = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
        page.wait_for_selector("text=Scan Only One: Domain, Ipv4, Subdomain")
        assert modal_title.is_visible(), "Modal didn't appear on first submission"

        
        page.wait_for_timeout(500)
        modal_close_button = page.locator("div[role='dialog'] button").first
        assert modal_close_button.is_visible(), "Modal close button not visible"
        modal_close_button.click()

        page.wait_for_timeout(500)

        # Re-submit 
        input_box.fill("")
        input_box.type(invalid_input)
        full_scan_button.click()

        modal_title_again = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
        assert modal_title_again.is_visible(), "Modal didn't reappear after quick second submit"

        input("Press Enter to close the browser...")
        browser.close()
