# Çıktı formatları (output) seçenekleri (PDF, CSV, HTML, video) görünebiliyor mu?

from playwright.sync_api import sync_playwright

def test_output_format_options_visible():
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

        # Her formatı sitede aramak
        for format_text in ["PDF", "CSV", "HTML", "VIDEO"]:
            format_locator = page.locator(f"text={format_text}")
            assert format_locator.first.is_visible(), f"❌ Output format '{format_text}' not visible."

        input("Press Enter to close the browser...")
        browser.close()
