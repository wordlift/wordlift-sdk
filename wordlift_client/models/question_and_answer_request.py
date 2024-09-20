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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.webpage_properties import WebpageProperties
from typing import Optional, Set
from typing_extensions import Self

class QuestionAndAnswerRequest(BaseModel):
    """
    QuestionAndAnswerRequest
    """ # noqa: E501
    smart_content_id: Optional[StrictInt] = Field(default=None, alias="smartContentId")
    webpage_properties: Optional[WebpageProperties] = Field(default=None, alias="webpageProperties")
    __properties: ClassVar[List[str]] = ["smartContentId", "webpageProperties"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QuestionAndAnswerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of webpage_properties
        if self.webpage_properties:
            _dict['webpageProperties'] = self.webpage_properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuestionAndAnswerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "smartContentId": obj.get("smartContentId"),
            "webpageProperties": WebpageProperties.from_dict(obj["webpageProperties"]) if obj.get("webpageProperties") is not None else None
        })
        return _obj


