# TC-F02: "Most Used" araçlar bölümü görünür ve araç kartları içermeli
# Bu test, "En Çok Kullanılan" bölümünün sayfada göründüğünü ve en az bir araç kartı içerdiğini doğrular.

from playwright.sync_api import sync_playwright

def test_most_used_tools_section_visible():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

       
        page.goto("https://s4e.io/free-security-tools")

        # "Most used" bölümüne kaydırarak görünür olduğundan emin ol
        page.locator("text=Most used").scroll_into_view_if_needed()

        # Kontrol 1: Bölüm başlığı görünür (heading)
        assert page.locator("text=Most used").is_visible(), "'Most used' section title not found."

        # Kontrol 2: Bölümün altında en az bir araç kartı görünüyor (tool card)
        tool_cards = page.locator("section:has-text('Most used') >> div")  
        assert tool_cards.count() > 0, "No tool cards found under 'Most used' section."

        input("Press Enter to close the browser...")
        browser.close()
