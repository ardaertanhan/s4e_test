# Bir tarama kartına tıklamak çökme veya sayfadan ayrılmaya neden olmyor mu?

from playwright.sync_api import sync_playwright

def test_click_scan_card_does_not_crash():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://s4e.io/free-security-tools")

        # OPTIONAL: Accept cookies
        try:
            accept_button = page.get_by_role("button", name="Accept All")
            if accept_button.is_visible():
                accept_button.click()
        except:
            pass

    
        latest_section = page.locator("section:has-text('Latest Tools')")
        tool_card = latest_section.locator("a").first  # first scan card

        assert tool_card.is_visible(), "❌ Scan card not visible"
        tool_card.click()

        
        page.wait_for_timeout(1000)

       
        assert "Free Security Tools" in page.title() or "S4E" in page.title(), "❌ Page crashed or redirected unexpectedly"

        input("Press Enter to close the browser...")
        browser.close()
