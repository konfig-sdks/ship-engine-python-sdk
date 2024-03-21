# coding: utf-8

"""
    ShipEngine API

    ShipEngine's easy-to-use REST API lets you manage all of your shipping needs without worrying about the complexities of different carrier APIs and protocols. We handle all the heavy lifting so you can focus on providing a first-class shipping experience for your customers at the best possible prices.  Each of ShipEngine's features can be used by itself or in conjunction with each other to build powerful shipping functionality into your application or service.  ## Getting Started If you're new to REST APIs then be sure to read our [introduction to REST](https://www.shipengine.com/docs/rest/) to understand the basics.  Learn how to [authenticate yourself to ShipEngine](https://www.shipengine.com/docs/auth/), and then use our [sandbox environment](https://www.shipengine.com/docs/sandbox/) to kick the tires and get familiar with our API. If you run into any problems, then be sure to check the [error handling guide](https://www.shipengine.com/docs/errors/) for tips.  Here are some step-by-step **tutorials** to get you started:    - [Learn how to create your first shipping label](https://www.shipengine.com/docs/labels/create-a-label/)   - [Calculate shipping costs and compare rates across carriers](https://www.shipengine.com/docs/rates/)   - [Track packages on-demand or in real time](https://www.shipengine.com/docs/tracking/)   - [Validate mailing addresses anywhere on Earth](https://www.shipengine.com/docs/addresses/validation/)   ## Shipping Labels for Every Major Carrier ShipEngine makes it easy to [create shipping labels for any carrier](https://www.shipengine.com/docs/labels/create-a-label/) and [download them](https://www.shipengine.com/docs/labels/downloading/) in a [variety of file formats](https://www.shipengine.com/docs/labels/formats/). You can even customize labels with your own [messages](https://www.shipengine.com/docs/labels/messages/) and [images](https://www.shipengine.com/docs/labels/branding/).   ## Real-Time Package Tracking With ShipEngine you can [get the current status of a package](https://www.shipengine.com/docs/tracking/) or [subscribe to real-time tracking updates](https://www.shipengine.com/docs/tracking/webhooks/) via webhooks. You can also create [custimized tracking pages](https://www.shipengine.com/docs/tracking/branded-tracking-page/) with your own branding so your customers will always know where their package is.   ## Compare Shipping Costs Across Carriers Make sure you ship as cost-effectively as possible by [comparing rates across carriers](https://www.shipengine.com/docs/rates/get-shipment-rates/) using the ShipEngine Rates API. Or if you don't know the full shipment details yet, then you can [get rate estimates](https://www.shipengine.com/docs/rates/estimate/) with limited address info.   ## Worldwide Address Validation ShipEngine supports [address validation](https://www.shipengine.com/docs/addresses/validation/) for virtually [every country on Earth](https://www.shipengine.com/docs/addresses/validation/countries/), including the United States, Canada, Great Britain, Australia, Germany, France, Norway, Spain, Sweden, Israel, Italy, and over 160 others. 

    The version of the OpenAPI document: 1.1.202403202303
    Contact: sales@shipengine.com
    Created by: https://www.shipengine.com/contact/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from ship_engine_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from ship_engine_python_sdk.api_response import AsyncGeneratorResponse
from ship_engine_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ship_engine_python_sdk import schemas  # noqa: F401

from ship_engine_python_sdk.model.shipment_status import ShipmentStatus as ShipmentStatusSchema
from ship_engine_python_sdk.model.shipments_sort_by import ShipmentsSortBy as ShipmentsSortBySchema
from ship_engine_python_sdk.model.list_shipments_response_body import ListShipmentsResponseBody as ListShipmentsResponseBodySchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.sort_dir import SortDir as SortDirSchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema

from ship_engine_python_sdk.type.shipments_sort_by import ShipmentsSortBy
from ship_engine_python_sdk.type.sort_dir import SortDir
from ship_engine_python_sdk.type.shipment_status import ShipmentStatus
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.list_shipments_response_body import ListShipmentsResponseBody

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.shipments_sort_by import ShipmentsSortBy as ShipmentsSortByPydantic
from ship_engine_python_sdk.pydantic.shipment_status import ShipmentStatus as ShipmentStatusPydantic
from ship_engine_python_sdk.pydantic.sort_dir import SortDir as SortDirPydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from ship_engine_python_sdk.pydantic.list_shipments_response_body import ListShipmentsResponseBody as ListShipmentsResponseBodyPydantic

# Query params
ShipmentStatusSchema = ShipmentStatusSchema
BatchIdSchema = schemas.Schema


class TagSchema(
    schemas.StrSchema
):
    pass
CreatedAtStartSchema = schemas.DateTimeSchema
CreatedAtEndSchema = schemas.DateTimeSchema
ModifiedAtStartSchema = schemas.DateTimeSchema
ModifiedAtEndSchema = schemas.DateTimeSchema


class PageSchema(
    schemas.Int32Schema
):
    pass


class PageSizeSchema(
    schemas.Int32Schema
):
    pass
SalesOrderIdSchema = schemas.StrSchema
SortDirSchema = SortDirSchema
SortBySchema = ShipmentsSortBySchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'shipment_status': typing.Union[ShipmentStatusSchema, ],
        'batch_id': typing.Union[BatchIdSchema, ],
        'tag': typing.Union[TagSchema, str, ],
        'created_at_start': typing.Union[CreatedAtStartSchema, str, datetime, ],
        'created_at_end': typing.Union[CreatedAtEndSchema, str, datetime, ],
        'modified_at_start': typing.Union[ModifiedAtStartSchema, str, datetime, ],
        'modified_at_end': typing.Union[ModifiedAtEndSchema, str, datetime, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'sales_order_id': typing.Union[SalesOrderIdSchema, str, ],
        'sort_dir': typing.Union[SortDirSchema, ],
        'sort_by': typing.Union[SortBySchema, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_shipment_status = api_client.QueryParameter(
    name="shipment_status",
    style=api_client.ParameterStyle.FORM,
    schema=ShipmentStatusSchema,
    explode=True,
)
request_query_batch_id = api_client.QueryParameter(
    name="batch_id",
    style=api_client.ParameterStyle.FORM,
    schema=SeIdSchema,
    explode=True,
)
request_query_tag = api_client.QueryParameter(
    name="tag",
    style=api_client.ParameterStyle.FORM,
    schema=TagSchema,
    explode=True,
)
request_query_created_at_start = api_client.QueryParameter(
    name="created_at_start",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtStartSchema,
    explode=True,
)
request_query_created_at_end = api_client.QueryParameter(
    name="created_at_end",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtEndSchema,
    explode=True,
)
request_query_modified_at_start = api_client.QueryParameter(
    name="modified_at_start",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtStartSchema,
    explode=True,
)
request_query_modified_at_end = api_client.QueryParameter(
    name="modified_at_end",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtEndSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_sales_order_id = api_client.QueryParameter(
    name="sales_order_id",
    style=api_client.ParameterStyle.FORM,
    schema=SalesOrderIdSchema,
    explode=True,
)
request_query_sort_dir = api_client.QueryParameter(
    name="sort_dir",
    style=api_client.ParameterStyle.FORM,
    schema=SortDirSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=ShipmentsSortBySchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ListShipmentsResponseBodySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ListShipmentsResponseBody


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ListShipmentsResponseBody


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _shipments_mapped_args(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if shipment_status is not None:
            _query_params["shipment_status"] = shipment_status
        if batch_id is not None:
            _query_params["batch_id"] = batch_id
        if tag is not None:
            _query_params["tag"] = tag
        if created_at_start is not None:
            _query_params["created_at_start"] = created_at_start
        if created_at_end is not None:
            _query_params["created_at_end"] = created_at_end
        if modified_at_start is not None:
            _query_params["modified_at_start"] = modified_at_start
        if modified_at_end is not None:
            _query_params["modified_at_end"] = modified_at_end
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["page_size"] = page_size
        if sales_order_id is not None:
            _query_params["sales_order_id"] = sales_order_id
        if sort_dir is not None:
            _query_params["sort_dir"] = sort_dir
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        args.query = _query_params
        return args

    async def _ashipments_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List Shipments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_shipment_status,
            request_query_batch_id,
            request_query_tag,
            request_query_created_at_start,
            request_query_created_at_end,
            request_query_modified_at_start,
            request_query_modified_at_end,
            request_query_page,
            request_query_page_size,
            request_query_sales_order_id,
            request_query_sort_dir,
            request_query_sort_by,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/shipments',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _shipments_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List Shipments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_shipment_status,
            request_query_batch_id,
            request_query_tag,
            request_query_created_at_start,
            request_query_created_at_end,
            request_query_modified_at_start,
            request_query_modified_at_end,
            request_query_page,
            request_query_page_size,
            request_query_sales_order_id,
            request_query_sort_dir,
            request_query_sort_by,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/shipments',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ShipmentsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ashipments(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._shipments_mapped_args(
            shipment_status=shipment_status,
            batch_id=batch_id,
            tag=tag,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            modified_at_start=modified_at_start,
            modified_at_end=modified_at_end,
            page=page,
            page_size=page_size,
            sales_order_id=sales_order_id,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return await self._ashipments_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def shipments(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._shipments_mapped_args(
            shipment_status=shipment_status,
            batch_id=batch_id,
            tag=tag,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            modified_at_start=modified_at_start,
            modified_at_end=modified_at_end,
            page=page,
            page_size=page_size,
            sales_order_id=sales_order_id,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return self._shipments_oapg(
            query_params=args.query,
        )

class Shipments(BaseApi):

    async def ashipments(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
        validate: bool = False,
        **kwargs,
    ) -> ListShipmentsResponseBodyPydantic:
        raw_response = await self.raw.ashipments(
            shipment_status=shipment_status,
            batch_id=batch_id,
            tag=tag,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            modified_at_start=modified_at_start,
            modified_at_end=modified_at_end,
            page=page,
            page_size=page_size,
            sales_order_id=sales_order_id,
            sort_dir=sort_dir,
            sort_by=sort_by,
            **kwargs,
        )
        if validate:
            return ListShipmentsResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(ListShipmentsResponseBodyPydantic, raw_response.body)
    
    
    def shipments(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
        validate: bool = False,
    ) -> ListShipmentsResponseBodyPydantic:
        raw_response = self.raw.shipments(
            shipment_status=shipment_status,
            batch_id=batch_id,
            tag=tag,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            modified_at_start=modified_at_start,
            modified_at_end=modified_at_end,
            page=page,
            page_size=page_size,
            sales_order_id=sales_order_id,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        if validate:
            return ListShipmentsResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(ListShipmentsResponseBodyPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._shipments_mapped_args(
            shipment_status=shipment_status,
            batch_id=batch_id,
            tag=tag,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            modified_at_start=modified_at_start,
            modified_at_end=modified_at_end,
            page=page,
            page_size=page_size,
            sales_order_id=sales_order_id,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return await self._ashipments_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        batch_id: typing.Optional[SeId] = None,
        tag: typing.Optional[str] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        modified_at_start: typing.Optional[datetime] = None,
        modified_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sales_order_id: typing.Optional[str] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[ShipmentsSortBy] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._shipments_mapped_args(
            shipment_status=shipment_status,
            batch_id=batch_id,
            tag=tag,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            modified_at_start=modified_at_start,
            modified_at_end=modified_at_end,
            page=page,
            page_size=page_size,
            sales_order_id=sales_order_id,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return self._shipments_oapg(
            query_params=args.query,
        )

