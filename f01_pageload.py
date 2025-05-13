from playwright.sync_api import sync_playwright

def test_page_loads_successfully():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://s4e.io/free-security-tools")

        # Fonksiyonel test: Başlık ve ana başlık mevcut olmalı (title, main heading)
        title = page.title()
        assert "Free Security Tools" in title or "S4E" in title
        assert page.locator("text=Online Free Security Tools").is_visible()

        input("Press Enter to close the browser...")
        browser.close()
