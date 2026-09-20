from contextlib import closing

from playwright.sync_api import sync_playwright

from tistory_growth_os.delivery.native_runner import wait_manager_ready


def test_manager_accessibility_heading_need_not_be_visually_displayed() -> None:
    with sync_playwright() as runtime, closing(runtime.chromium.launch(channel='chrome', chromium_sandbox=True)) as browser:
        page = browser.new_page()
        page.set_content('<h2 style="width:0;height:0;overflow:hidden">티스토리 관리센터 본문</h2><div id="mArticle"><input id="inpCheck92"></div>')
        assert not page.get_by_role('heading').is_visible()
        wait_manager_ready(page)
