# coding: utf-8

"""
    Middleware

    Knowledge Graph data management.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Account(BaseModel):
    """
    Account
    """ # noqa: E501
    analytics_client_factory: Optional[StrictStr] = None
    analyzer_id: Optional[StrictInt] = Field(default=None, alias="analyzerId")
    botify_project: Optional[StrictStr] = None
    botify_token: Optional[StrictStr] = None
    botify_username: Optional[StrictStr] = None
    collection: Optional[StrictStr] = Field(default='entity', description="The collection hosing the Knowledge Graph.")
    country: Optional[StrictStr] = None
    dataset_id: Optional[StrictStr] = Field(default=None, alias="datasetId")
    dataset_uri: Optional[StrictStr] = Field(default=None, alias="datasetUri")
    domain_uri: Optional[StrictStr] = Field(default=None, alias="domainUri")
    google_search_console_site_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    indexed: Optional[StrictBool] = None
    is_wordpress: Optional[StrictBool] = None
    key: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    ng_dataset_id: Optional[StrictStr] = Field(default=None, alias="ngDatasetId")
    resolved_url: Optional[StrictStr] = Field(default=None, alias="resolvedUrl")
    subscription_id: Optional[StrictInt] = Field(default=None, alias="subscriptionId")
    url: Optional[StrictStr] = None
    wp_admin: Optional[StrictStr] = Field(default=None, alias="wpAdmin")
    wp_json: Optional[StrictStr] = Field(default=None, alias="wpJson")
    wp_include_exclude_default: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["analytics_client_factory", "analyzerId", "botify_project", "botify_token", "botify_username", "collection", "country", "datasetId", "datasetUri", "domainUri", "google_search_console_site_url", "id", "indexed", "is_wordpress", "key", "language", "ngDatasetId", "resolvedUrl", "subscriptionId", "url", "wpAdmin", "wpJson", "wp_include_exclude_default"]

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
        """Create an instance of Account from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analytics_client_factory": obj.get("analytics_client_factory"),
            "analyzerId": obj.get("analyzerId"),
            "botify_project": obj.get("botify_project"),
            "botify_token": obj.get("botify_token"),
            "botify_username": obj.get("botify_username"),
            "collection": obj.get("collection") if obj.get("collection") is not None else 'entity',
            "country": obj.get("country"),
            "datasetId": obj.get("datasetId"),
            "datasetUri": obj.get("datasetUri"),
            "domainUri": obj.get("domainUri"),
            "google_search_console_site_url": obj.get("google_search_console_site_url"),
            "id": obj.get("id"),
            "indexed": obj.get("indexed"),
            "is_wordpress": obj.get("is_wordpress"),
            "key": obj.get("key"),
            "language": obj.get("language"),
            "ngDatasetId": obj.get("ngDatasetId"),
            "resolvedUrl": obj.get("resolvedUrl"),
            "subscriptionId": obj.get("subscriptionId"),
            "url": obj.get("url"),
            "wpAdmin": obj.get("wpAdmin"),
            "wpJson": obj.get("wpJson"),
            "wp_include_exclude_default": obj.get("wp_include_exclude_default")
        })
        return _obj


