from dataclasses import dataclass, field
from enum import StrEnum
from hashlib import sha256
from urllib.parse import urlsplit

from playwright.sync_api import Page


@dataclass(frozen=True, slots=True)
class HtmlInput:
    title: str
    html: str = field(repr=False)
    body_sha256: str


class InputResult(StrEnum):
    DRY_RUN = 'dry_run'
    BLOCKED = 'blocked'
    INPUT_VERIFIED = 'input_verified'
    UNKNOWN = 'unknown'


def fill_blank_html_editor(page: Page, request: HtmlInput, *, dry_run: bool = True) -> InputResult:
    if dry_run:
        return InputResult.DRY_RUN
    original_url = page.url
    url = urlsplit(original_url)
    if (url.scheme != 'https' or url.netloc != 'nedamma.tistory.com'
            or url.path.rstrip('/') != '/manage/newpost'
            or not request.title.strip() or not request.html.strip()
            or sha256(request.html.encode()).hexdigest() != request.body_sha256):
        return InputResult.BLOCKED
    title = page.locator('#post-title-inp')
    editor = page.locator('#html-editor-container .CodeMirror')
    source = editor.locator('textarea')
    if (title.count() != 1 or not title.is_visible() or title.input_value().strip()
            or editor.count() != 1 or not editor.is_visible() or source.count() != 1):
        return InputResult.BLOCKED
    source.press('ControlOrMeta+A', timeout=3000)
    initial = source.input_value(timeout=3000).strip()
    if (initial not in ('', '<p data-ke-size="size16"></p>')
            or title.input_value().strip() or page.url != original_url):
        return InputResult.BLOCKED
    title.fill(request.title, timeout=3000)
    source.press('ControlOrMeta+A', timeout=3000)
    page.keyboard.insert_text(request.html)
    source.press('ControlOrMeta+A', timeout=3000)
    if (page.url != original_url or title.input_value() != request.title
            or source.input_value(timeout=3000) != request.html):
        return InputResult.UNKNOWN
    return InputResult.INPUT_VERIFIED
