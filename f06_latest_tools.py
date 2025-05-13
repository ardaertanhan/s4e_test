# "Latest Tools" görülür mü ve an az bir tool card içeriyor mu?

from playwright.sync_api import sync_playwright

def test_latest_tools_section_is_loaded():
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

       
        section = page.locator("section:has-text('Latest Tools')")
        assert section.is_visible(), "❌ 'Latest Tools' section is not visible."

        
        tool_cards = section.locator("a")  
        assert tool_cards.count() > 0, "❌ No tools found in the 'Latest Tools' section."

        input(" Press Enter to close the browser...")
        browser.close()
