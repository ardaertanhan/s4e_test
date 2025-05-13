# Bu test, giriş boşsa modalın açık kalmasını sağlamayı test epmektedir (empty input)

from playwright.sync_api import sync_playwright

def test_empty_input_does_not_trigger_scan():
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
        input_box.fill("")

   
        full_scan_button = page.get_by_role("button", name="Start Full Scan").first
        full_scan_button.click()

        
        page.wait_for_selector("text=Scan Only One: Domain, Ipv4, Subdomain")
        modal_title = page.locator("text=Scan Only One: Domain, Ipv4, Subdomain")
        assert modal_title.is_visible(), "Modal did not appear."

        
        retry_button = page.get_by_role("button", name="Retry")
        retry_button.click()

        
        page.wait_for_timeout(1000)
        assert modal_title.is_visible(), "Modal closed unexpectedly after empty input."

        input("Press Enter to close the browser...")
        browser.close()
