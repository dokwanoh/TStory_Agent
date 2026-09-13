from contextlib import closing
from datetime import datetime

import pytest
from playwright.sync_api import Route, sync_playwright

from tistory_growth_os.delivery.playwright_publish_settings import read_publish_settings
from tistory_growth_os.delivery.playwright_manager import ManagerVisibility
from tistory_growth_os.domain.ids import PostId


def panel_html() -> str:
    return '''<div role="dialog" class="editor_layer"><legend>발행정보 입력폼</legend>
    <strong class="tit_publish">시험 제목</strong>
    <input type="radio" name="basicSet" value="20" checked>
    <input type="radio" name="basicSet" value="15">
    <input type="radio" name="basicSet" value="0">
    <dl id="home_subject"><button><i class="mce-txt">스포츠일반</i></button></dl>
    <button class="btn_date on">2030-01-01 12:00</button>
    <button class="btn_date">현재</button><button class="btn_date">예약</button>
    <input id="urlPublish" value="fixture-post"></div>'''


@pytest.mark.parametrize('case', ['valid', 'origin', 'wrong_id', 'unsafe_id', 'missing',
                                 'duplicate', 'date', 'current', 'reservation', 'visibility',
                                 'home', 'slug', 'hidden'])
def test_saved_panel_reads_only_unambiguous_observed_settings(case: str) -> None:
    html = panel_html()
    variants = {
        'missing': '', 'duplicate': html + html,
        'date': html.replace('2030-01-01', '2030-99-99'),
        'current': html.replace('2030-01-01 12:00', '현재'),
        'reservation': html.replace('2030-01-01 12:00', '예약'),
        'visibility': html.replace('value="20"', 'value="99"'),
        'home': html.replace('id="home_subject"', 'id="other"'),
        'slug': html.replace('fixture-post', '../manage'),
        'hidden': html.replace('role="dialog"', 'role="dialog" hidden'),
    }
    requests: list[str] = []

    def serve(route: Route) -> None:
        requests.append(route.request.method)
        route.fulfill(content_type='text/html; charset=utf-8', body=variants.get(case, html))

    with sync_playwright() as p, closing(p.chromium.launch(channel='chrome', chromium_sandbox=True)) as browser:
        page = browser.new_page(service_workers='block')
        page.route('**/*', serve)
        origin = 'https://example.test' if case == 'origin' else 'https://nedamma.tistory.com'
        page.goto(origin + '/manage/newpost/79')
        identity = {'wrong_id': '80', 'unsafe_id': '79/../80'}.get(case, '79')
        result = read_publish_settings(page, PostId(identity))
        if case == 'valid':
            assert result is not None
            assert result.post_id == PostId('79')
            assert result.title == '시험 제목'
            assert result.visibility is ManagerVisibility.PUBLIC
            assert result.home_topic == '스포츠일반'
            assert result.existing_at == datetime.fromisoformat('2030-01-01T12:00:00+09:00')
            assert result.slug == 'fixture-post'
        else:
            assert result is None
        assert requests == ['GET']
