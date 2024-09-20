# coding: utf-8

"""
    SEO Content Analysis API

    This API assesses the match between a URL or text content, a query, and an intent, using advanced SEO techniques.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ProjectType(str, Enum):
    """
    The project type, if applicable.
    """

    """
    allowed enum values
    """
    SMART_CONTENT = 'SMART_CONTENT'
    CONTENT_GENERATION = 'CONTENT_GENERATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProjectType from a JSON string"""
        return cls(json.loads(json_str))


