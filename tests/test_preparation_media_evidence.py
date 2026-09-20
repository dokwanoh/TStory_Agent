from pathlib import Path

import pytest

from tistory_growth_os.preparation.contracts import PreparationError
from tistory_growth_os.preparation.media_evidence import native_generation_evidence


SESSION = '01a0c105-e3f3-7231-b726-d0dd1281fb5a'


def test_native_generation_requires_same_session_fresh_outputs(tmp_path: Path) -> None:
    folder = tmp_path / 'generated_images' / SESSION
    folder.mkdir(parents=True)
    image = folder / 'exec-9425f8a4-4ed8-4f5b-aeae-4f96e96cbaf1.png'
    _ = image.write_bytes(b'\x89PNG\r\n\x1a\n' + b'x' * 2000)
    proof = native_generation_evidence(tmp_path, SESSION, 0, 1)
    assert image.name in proof and SESSION in proof
    with pytest.raises(PreparationError, match='generation_tool_evidence_required'):
        _ = native_generation_evidence(tmp_path, SESSION, image.stat().st_mtime + 1, 1)
    with pytest.raises(PreparationError, match='generation_tool_evidence_required'):
        _ = native_generation_evidence(tmp_path, SESSION, 0, 4)


def test_native_generation_rejects_symlink_and_untrusted_identity(tmp_path: Path) -> None:
    with pytest.raises(PreparationError, match='generation_tool_evidence_required'):
        _ = native_generation_evidence(tmp_path, '../elsewhere', 0, 1)
    folder = tmp_path / 'generated_images' / SESSION
    folder.mkdir(parents=True)
    image = tmp_path / 'outside.png'
    _ = image.write_bytes(b'\x89PNG\r\n\x1a\n' + b'x' * 2000)
    (folder / 'exec-9425f8a4-4ed8-4f5b-aeae-4f96e96cbaf1.png').symlink_to(image)
    with pytest.raises(PreparationError, match='generation_tool_evidence_required'):
        _ = native_generation_evidence(tmp_path, SESSION, 0, 1)
