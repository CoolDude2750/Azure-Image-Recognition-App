from io import BytesIO

import pytest
from fastapi import HTTPException
from starlette.datastructures import UploadFile

from src.api import _format_result, _read_image


class DummyResult:
    caption = None
    tags = {"values": [{"name": "cat", "confidence": 0.956}]}
    objects = {"values": [{"tags": [{"name": "cat", "confidence": 0.923}]}]}


@pytest.mark.anyio
async def test_read_image_rejects_unsupported_content_type():
    file = UploadFile(BytesIO(b"not-an-image"), filename="notes.txt", headers={"content-type": "text/plain"})

    with pytest.raises(HTTPException) as error:
        await _read_image(file)

    assert error.value.status_code == 415


@pytest.mark.anyio
async def test_read_image_rejects_empty_upload():
    file = UploadFile(BytesIO(b""), filename="empty.png", headers={"content-type": "image/png"})

    with pytest.raises(HTTPException) as error:
        await _read_image(file)

    assert error.value.status_code == 400


def test_format_result_normalizes_confidences_and_values():
    assert _format_result(DummyResult()) == {
        "caption": None,
        "caption_confidence": None,
        "tags": [{"name": "cat", "confidence": 0.96}],
        "objects": [{"name": "cat", "confidence": 0.92}],
    }