import json

import allure
import pytest
from allure_commons.types import AttachmentType


def log_api(result):
    allure.attach(
        body=f"Method: {result.request.method}\nURL: {result.request.url}",
        name="Request info",
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=f'Status code: {result.status_code}',
        name='Response status code',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=result.text,
        name='Response',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )