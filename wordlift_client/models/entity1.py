# coding: utf-8

"""
    GraphQL support

    GraphQL endpoint to query Knowledge Graphs

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wordlift_client.models.properties1 import Properties1
from typing import Optional, Set
from typing_extensions import Self

class Entity1(BaseModel):
    """
    Entity
    """ # noqa: E501
    entity_id: Optional[StrictStr] = Field(default=None, description="The entity URI.", alias="entityId")
    confidence: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Confidence score representing the entity match level.")
    main_type: Optional[StrictStr] = Field(default=None, description="The main schema type for the current entity.", alias="mainType")
    types: Optional[List[StrictStr]] = Field(default=None, description="The list of schema types which the entity can be classified to.")
    label: Optional[StrictStr] = Field(default=None, description="The title of the entity.")
    description: Optional[StrictStr] = Field(default=None, description="The description about the entity.")
    images: Optional[List[StrictStr]] = Field(default=None, description="The list of entity image URIs.")
    same_as: Optional[List[StrictStr]] = Field(default=None, description="The list of entity sameas URIs.", alias="sameAs")
    properties: Optional[Properties1] = None
    synonyms: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["entityId", "confidence", "mainType", "types", "label", "description", "images", "sameAs", "properties", "synonyms"]

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
        """Create an instance of Entity1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Entity1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": obj.get("entityId"),
            "confidence": obj.get("confidence"),
            "mainType": obj.get("mainType"),
            "types": obj.get("types"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "images": obj.get("images"),
            "sameAs": obj.get("sameAs"),
            "properties": Properties1.from_dict(obj["properties"]) if obj.get("properties") is not None else None,
            "synonyms": obj.get("synonyms")
        })
        return _obj


