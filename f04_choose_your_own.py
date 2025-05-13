# "Choose your own" bölümü mevcut ve kullanılabilir mi?

from playwright.sync_api import sync_playwright

def test_choose_your_own_scans_section():
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

        
        choose_section = page.locator("section:has-text('choose your own')")
        assert choose_section.is_visible(), "❌ 'Choose your own' section not found."

   
        scan_buttons = choose_section.locator("button")
        assert scan_buttons.count() > 0, "❌ No scan buttons found in 'Choose your own' section."

        
        scan_buttons.first.hover()

        input("Press Enter to close the browser...")
        browser.close()
