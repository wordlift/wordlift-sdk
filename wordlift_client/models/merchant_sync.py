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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MerchantSync(BaseModel):
    """
    A Merchant products data synchronization.
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="The create date-time.")
    error_reason: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=500)]] = Field(default=None, description="Error that caused the synchronization to fail.")
    has_errors: Optional[StrictBool] = Field(default=None, description="Whether the sync encountered errors.")
    id: Optional[StrictInt] = Field(default=None, description="The unique id.")
    merchant_id: StrictInt = Field(description="The parent Merchant id.")
    modified_at: Optional[datetime] = Field(default=None, description="The last modified date-time.")
    products_created: Optional[StrictInt] = Field(default=None, description="The number of created products")
    products_deleted: Optional[StrictInt] = Field(default=None, description="The number of deleted products")
    products_errored: Optional[StrictInt] = Field(default=None, description="The number of errored products")
    products_skipped: Optional[StrictInt] = Field(default=None, description="The number of skipped products")
    products_total: Optional[StrictInt] = Field(default=None, description="The total number of processed products, including the skipped and errored.")
    products_unchanged: Optional[StrictInt] = Field(default=None, description="The number of products that haven't changed and therefore haven't been synced again")
    products_updated: Optional[StrictInt] = Field(default=None, description="The number of update products")
    started_at: Optional[datetime] = Field(default=None, description="The started date-time.")
    stopped_at: Optional[datetime] = Field(default=None, description="The stopped date-time.")
    __properties: ClassVar[List[str]] = ["created_at", "error_reason", "has_errors", "id", "merchant_id", "modified_at", "products_created", "products_deleted", "products_errored", "products_skipped", "products_total", "products_unchanged", "products_updated", "started_at", "stopped_at"]

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
        """Create an instance of MerchantSync from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "error_reason",
            "has_errors",
            "id",
            "merchant_id",
            "modified_at",
            "products_created",
            "products_deleted",
            "products_errored",
            "products_skipped",
            "products_total",
            "products_unchanged",
            "products_updated",
            "started_at",
            "stopped_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantSync from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "error_reason": obj.get("error_reason"),
            "has_errors": obj.get("has_errors"),
            "id": obj.get("id"),
            "merchant_id": obj.get("merchant_id"),
            "modified_at": obj.get("modified_at"),
            "products_created": obj.get("products_created"),
            "products_deleted": obj.get("products_deleted"),
            "products_errored": obj.get("products_errored"),
            "products_skipped": obj.get("products_skipped"),
            "products_total": obj.get("products_total"),
            "products_unchanged": obj.get("products_unchanged"),
            "products_updated": obj.get("products_updated"),
            "started_at": obj.get("started_at"),
            "stopped_at": obj.get("stopped_at")
        })
        return _obj


