# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from Wordlift_client.models.page_website_search import PageWebsiteSearch

from Wordlift_client.api_client import ApiClient, RequestSerialized
from Wordlift_client.api_response import ApiResponse
from Wordlift_client.rest import RESTResponseType


class GoogleSearchConsoleSearchesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def list_website_search1(
        self,
        since: Annotated[StrictStr, Field(description="The start date, inclusive, in yyyy-MM-dd format.")],
        until: Annotated[StrictStr, Field(description="The end date, inclusive, in yyyy-MM-dd format.")],
        dimensions: Annotated[List[StrictStr], Field(description="The dimensions, e.g. `query`, `page`. Must repeat for each dimension.")],
        cursor: Annotated[Optional[StrictStr], Field(description="The cursor")] = None,
        data_state: Annotated[Optional[StrictStr], Field(description="If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=25000, strict=True)]], Field(description="The maximum number of results")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PageWebsiteSearch:
        """List Website Search data

        List the Website Search performance data

        :param since: The start date, inclusive, in yyyy-MM-dd format. (required)
        :type since: str
        :param until: The end date, inclusive, in yyyy-MM-dd format. (required)
        :type until: str
        :param dimensions: The dimensions, e.g. `query`, `page`. Must repeat for each dimension. (required)
        :type dimensions: List[str]
        :param cursor: The cursor
        :type cursor: str
        :param data_state: If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data.
        :type data_state: str
        :param limit: The maximum number of results
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_website_search1_serialize(
            since=since,
            until=until,
            dimensions=dimensions,
            cursor=cursor,
            data_state=data_state,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PageWebsiteSearch",
            '401': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def list_website_search1_with_http_info(
        self,
        since: Annotated[StrictStr, Field(description="The start date, inclusive, in yyyy-MM-dd format.")],
        until: Annotated[StrictStr, Field(description="The end date, inclusive, in yyyy-MM-dd format.")],
        dimensions: Annotated[List[StrictStr], Field(description="The dimensions, e.g. `query`, `page`. Must repeat for each dimension.")],
        cursor: Annotated[Optional[StrictStr], Field(description="The cursor")] = None,
        data_state: Annotated[Optional[StrictStr], Field(description="If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=25000, strict=True)]], Field(description="The maximum number of results")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PageWebsiteSearch]:
        """List Website Search data

        List the Website Search performance data

        :param since: The start date, inclusive, in yyyy-MM-dd format. (required)
        :type since: str
        :param until: The end date, inclusive, in yyyy-MM-dd format. (required)
        :type until: str
        :param dimensions: The dimensions, e.g. `query`, `page`. Must repeat for each dimension. (required)
        :type dimensions: List[str]
        :param cursor: The cursor
        :type cursor: str
        :param data_state: If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data.
        :type data_state: str
        :param limit: The maximum number of results
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_website_search1_serialize(
            since=since,
            until=until,
            dimensions=dimensions,
            cursor=cursor,
            data_state=data_state,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PageWebsiteSearch",
            '401': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def list_website_search1_without_preload_content(
        self,
        since: Annotated[StrictStr, Field(description="The start date, inclusive, in yyyy-MM-dd format.")],
        until: Annotated[StrictStr, Field(description="The end date, inclusive, in yyyy-MM-dd format.")],
        dimensions: Annotated[List[StrictStr], Field(description="The dimensions, e.g. `query`, `page`. Must repeat for each dimension.")],
        cursor: Annotated[Optional[StrictStr], Field(description="The cursor")] = None,
        data_state: Annotated[Optional[StrictStr], Field(description="If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=25000, strict=True)]], Field(description="The maximum number of results")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List Website Search data

        List the Website Search performance data

        :param since: The start date, inclusive, in yyyy-MM-dd format. (required)
        :type since: str
        :param until: The end date, inclusive, in yyyy-MM-dd format. (required)
        :type until: str
        :param dimensions: The dimensions, e.g. `query`, `page`. Must repeat for each dimension. (required)
        :type dimensions: List[str]
        :param cursor: The cursor
        :type cursor: str
        :param data_state: If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data.
        :type data_state: str
        :param limit: The maximum number of results
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_website_search1_serialize(
            since=since,
            until=until,
            dimensions=dimensions,
            cursor=cursor,
            data_state=data_state,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PageWebsiteSearch",
            '401': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_website_search1_serialize(
        self,
        since,
        until,
        dimensions,
        cursor,
        data_state,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'dimensions': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if cursor is not None:
            
            _query_params.append(('cursor', cursor))
            
        if since is not None:
            
            _query_params.append(('since', since))
            
        if until is not None:
            
            _query_params.append(('until', until))
            
        if dimensions is not None:
            
            _query_params.append(('dimensions', dimensions))
            
        if data_state is not None:
            
            _query_params.append(('data_state', data_state))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/accounts/me/google/searches',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


