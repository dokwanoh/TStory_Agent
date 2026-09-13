from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
import re
from urllib.parse import urlsplit

from playwright.sync_api import Page

from ..domain.ids import PostId
from .reservation_readback import KST


class ManagerVisibility(StrEnum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'


@dataclass(frozen=True, slots=True)
class ManagerPostSummary:
    post_id: PostId
    display_title: str
    url: str
    category: str
    listed_at: datetime
    visibility: ManagerVisibility


def read_manager_post(page: Page, post_id: PostId) -> ManagerPostSummary | None:
    original_url = page.url
    parsed = urlsplit(original_url)
    if parsed.scheme != 'https' or parsed.netloc != 'nedamma.tistory.com' or parsed.path.rstrip('/') != '/manage/posts':
        return None
    if re.fullmatch(r'[1-9][0-9]*', post_id) is None:
        return None
    if page.get_by_role('heading', name='티스토리 관리센터 본문', exact=True).count() != 1:
        return None
    checkbox = page.locator(f'#inpCheck{post_id}')
    if checkbox.count() != 1:
        return None
    row = checkbox.locator('xpath=ancestor::li[1]')
    title = row.locator('a.link_cont')
    category = row.locator('.txt_cate')
    date = row.locator('.txt_info:not(.txt_ellip)')
    setting = row.locator('.btn_opt > .txt_ellip')
    if any(item.count() != 1 for item in (row, title, category, date, setting)):
        return None
    display_title = title.inner_text(timeout=3000).strip()
    target_url = title.get_attribute('href', timeout=3000)
    if not display_title or target_url is None:
        return None
    target = urlsplit(target_url)
    if (target.scheme != 'https' or target.netloc != 'nedamma.tistory.com'
            or target.query or target.fragment or target.path in ('', '/')
            or target.path.startswith('/manage')):
        return None
    stamp = date.inner_text(timeout=3000).strip()
    if re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', stamp) is None:
        return None
    try:
        listed_at = datetime.strptime(stamp, '%Y-%m-%d %H:%M').replace(tzinfo=KST)
    except ValueError:
        return None
    visibility = {'공개': ManagerVisibility.PUBLIC, '비공개': ManagerVisibility.PRIVATE,
                  '보호': ManagerVisibility.PROTECTED}.get(setting.inner_text(timeout=3000).strip())
    category_text = category.inner_text(timeout=3000).strip()
    if visibility is None or page.url != original_url:
        return None
    return ManagerPostSummary(post_id, display_title, target_url, category_text, listed_at, visibility)
