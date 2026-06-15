# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2026-03-13
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Ali website base methods.
"""

from alibabacloud_dypnsapi20170525.client import Client as AliClient
from alibabacloud_tea_openapi.models import Config as AliConfig
from alibabacloud_credentials.models import Config as AliCredentialConfig
from alibabacloud_credentials.client import Client as AliCredentialClient

from ..rbase import ClientBase

__all__ = (
    'ClientAli',
    'create_client_ali'
)

class ClientAli(ClientBase):
    """
    Request Ali API fetch type.
    """

def create_client_ali(key_id: str, key_secret: str) -> AliClient:
    """
    Create Ali API client.

    Parameters
    ----------
    key_id : Authorization key ID.
    key_secret: Authorization key secret.

    Returns
    -------
    Ali API client.
    """

    # Create.
    credential_config = AliCredentialConfig(
        type='access_key',
        access_key_id=key_id,
        access_key_secret=key_secret
    )
    credential_client = AliCredentialClient(credential_config)
    config = AliConfig(
        credential=credential_client,
        endpoint='dypnsapi.aliyuncs.com'
    )
    client = AliClient(config)

    return client
