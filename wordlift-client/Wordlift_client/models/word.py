# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Word(BaseModel):
    """
    A Word bias.
    """ # noqa: E501
    bias: StrictInt = Field(description="The bias.")
    cluster: Annotated[str, Field(strict=True, max_length=1000)] = Field(description="The cluster of the word.")
    content_generation_id: StrictInt = Field(description="The content generation id.")
    created_at: Optional[datetime] = Field(default=None, description="The create date-time.")
    id: Optional[StrictInt] = Field(default=None, description="The unique id.")
    modified_at: Optional[datetime] = Field(default=None, description="The last modified date-time.")
    token_id: Annotated[str, Field(strict=True, max_length=1000)] = Field(description="The token id for the word.")
    word: Annotated[str, Field(strict=True, max_length=1000)] = Field(description="The actual word.")
    __properties: ClassVar[List[str]] = ["bias", "cluster", "content_generation_id", "created_at", "id", "modified_at", "token_id", "word"]

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
        """Create an instance of Word from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "content_generation_id",
            "created_at",
            "id",
            "modified_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Word from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bias": obj.get("bias"),
            "cluster": obj.get("cluster"),
            "content_generation_id": obj.get("content_generation_id"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "modified_at": obj.get("modified_at"),
            "token_id": obj.get("token_id"),
            "word": obj.get("word")
        })
        return _obj


