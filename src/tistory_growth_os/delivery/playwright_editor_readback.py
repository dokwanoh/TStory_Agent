from dataclasses import dataclass
from hashlib import sha256
import re
from urllib.parse import urlsplit

from playwright.sync_api import Page

from ..domain.ids import PostId


@dataclass(frozen=True, slots=True)
class EditorImage:
    source_url: str
    alt: str
    filename: str | None


@dataclass(frozen=True, slots=True)
class EditorContentSnapshot:
    post_id: PostId
    title: str
    body_html: str
    body_sha256: str
    media: tuple[EditorImage, ...]


def read_editor_content(page: Page, post_id: PostId) -> EditorContentSnapshot | None:
    original_url = page.url
    parsed = urlsplit(original_url)
    if (re.fullmatch(r'[1-9][0-9]*', post_id) is None
            or parsed.scheme != 'https' or parsed.netloc != 'nedamma.tistory.com'
            or parsed.path != f'/manage/newpost/{post_id}'):
        return None
    title_input = page.locator('#post-title-inp')
    frame = page.locator('iframe#editor-tistory_ifr')
    if title_input.count() != 1 or frame.count() != 1:
        return None
    body = page.frame_locator('#editor-tistory_ifr').locator('body#tinymce[contenteditable=true]')
    if body.count() != 1:
        return None
    title = title_input.input_value(timeout=3000)
    html = body.inner_html(timeout=3000)
    if not title.strip() or not body.inner_text(timeout=3000).strip():
        return None
    images = body.locator('img')
    if images.count() != 4:
        return None
    media: list[EditorImage] = []
    for image in images.all():
        source = image.get_attribute('src', timeout=3000)
        alt = image.get_attribute('alt', timeout=3000)
        if not source or not alt or not alt.strip():
            return None
        location = urlsplit(source)
        if (location.scheme != 'https' or not location.hostname
                or location.username or location.password):
            return None
        media.append(EditorImage(source, alt, image.get_attribute('data-filename', timeout=3000)))
    if (len({item.source_url for item in media}) != 4 or page.url != original_url
            or title_input.input_value(timeout=3000) != title
            or body.inner_html(timeout=3000) != html):
        return None
    return EditorContentSnapshot(post_id, title, html, sha256(html.encode('utf-8')).hexdigest(), tuple(media))
