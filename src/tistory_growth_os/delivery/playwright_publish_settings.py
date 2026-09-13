from dataclasses import dataclass
from datetime import datetime
import re
from urllib.parse import urlsplit

from playwright.sync_api import Page

from ..domain.ids import PostId
from .playwright_manager import ManagerVisibility
from .reservation_readback import KST


@dataclass(frozen=True, slots=True)
class PublishSettingsSnapshot:
    post_id: PostId
    title: str
    visibility: ManagerVisibility
    home_topic: str
    existing_at: datetime
    slug: str


def read_publish_settings(page: Page, post_id: PostId) -> PublishSettingsSnapshot | None:
    original_url = page.url
    parsed = urlsplit(original_url)
    if (re.fullmatch(r'[1-9][0-9]*', post_id) is None
            or parsed.scheme != 'https' or parsed.netloc != 'nedamma.tistory.com'
            or parsed.path != f'/manage/newpost/{post_id}'):
        return None
    panel = page.get_by_role('dialog').filter(has=page.locator('legend').filter(has_text='발행정보 입력폼'))
    if panel.count() != 1 or not panel.is_visible():
        return None
    title = panel.locator('.tit_publish')
    home = panel.locator('#home_subject button .mce-txt')
    date = panel.locator('.btn_date.on')
    selected = panel.locator('input[name=basicSet]:checked')
    slug_input = panel.locator('#urlPublish')
    if any(item.count() != 1 for item in (title, home, date, selected, slug_input)):
        return None
    stamp = date.inner_text(timeout=3000).strip()
    if re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', stamp) is None:
        return None
    try:
        existing_at = datetime.strptime(stamp, '%Y-%m-%d %H:%M').replace(tzinfo=KST)
    except ValueError:
        return None
    visibility = {'20': ManagerVisibility.PUBLIC, '15': ManagerVisibility.PROTECTED,
                  '0': ManagerVisibility.PRIVATE}.get(selected.input_value(timeout=3000))
    title_text = title.inner_text(timeout=3000).strip()
    home_text = home.inner_text(timeout=3000).strip()
    slug = slug_input.input_value(timeout=3000)
    if (visibility is None or not title_text or not home_text or not slug.strip()
            or any(character in slug for character in '/?#%\\') or slug in ('.', '..')
            or page.url != original_url):
        return None
    return PublishSettingsSnapshot(post_id, title_text, visibility, home_text, existing_at, slug)
