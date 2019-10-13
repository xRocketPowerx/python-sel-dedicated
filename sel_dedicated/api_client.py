# coding: utf-8
"""
    Seido User REST API client
"""

from __future__ import absolute_import

from sel_dedicated_client.api_client import ApiClient as _Base


class ApiClient(_Base):
    """Wrapper for Generic API client for OpenAPI client library builds.

    """

    def call_api(self, *args, **kwargs):
        auth_settings = kwargs.pop("auth_settings", None)
        if auth_settings is None or not auth_settings:
            auth_settings = ["X_Token_Auth"]
        else:
            if "X_Token_Auth" not in auth_settings:
                auth_settings.append("X_Token_Auth")

        return super().call_api(auth_settings=auth_settings, *args, **kwargs)
