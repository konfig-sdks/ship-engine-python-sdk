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

from ship_engine_python_sdk.model.partial_address import PartialAddress as PartialAddressSchema
from ship_engine_python_sdk.model.warehouse import Warehouse as WarehouseSchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema

from ship_engine_python_sdk.type.partial_address import PartialAddress
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.warehouse import Warehouse

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.warehouse import Warehouse as WarehousePydantic
from ship_engine_python_sdk.pydantic.partial_address import PartialAddress as PartialAddressPydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = WarehouseSchema


request_body_warehouse = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = WarehouseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Warehouse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Warehouse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _warehouse_mapped_args(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if warehouse_id is not None:
            _body["warehouse_id"] = warehouse_id
        if is_default is not None:
            _body["is_default"] = is_default
        if name is not None:
            _body["name"] = name
        if created_at is not None:
            _body["created_at"] = created_at
        if origin_address is not None:
            _body["origin_address"] = origin_address
        if return_address is not None:
            _body["return_address"] = return_address
        args.body = _body
        return args

    async def _awarehouse_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Warehouse
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/warehouses',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_warehouse.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _warehouse_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Warehouse
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/warehouses',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_warehouse.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class WarehouseRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def awarehouse(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._warehouse_mapped_args(
            warehouse_id=warehouse_id,
            is_default=is_default,
            name=name,
            created_at=created_at,
            origin_address=origin_address,
            return_address=return_address,
        )
        return await self._awarehouse_oapg(
            body=args.body,
            **kwargs,
        )
    
    def warehouse(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._warehouse_mapped_args(
            warehouse_id=warehouse_id,
            is_default=is_default,
            name=name,
            created_at=created_at,
            origin_address=origin_address,
            return_address=return_address,
        )
        return self._warehouse_oapg(
            body=args.body,
        )

class Warehouse(BaseApi):

    async def awarehouse(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
        validate: bool = False,
        **kwargs,
    ) -> WarehousePydantic:
        raw_response = await self.raw.awarehouse(
            warehouse_id=warehouse_id,
            is_default=is_default,
            name=name,
            created_at=created_at,
            origin_address=origin_address,
            return_address=return_address,
            **kwargs,
        )
        if validate:
            return WarehousePydantic(**raw_response.body)
        return api_client.construct_model_instance(WarehousePydantic, raw_response.body)
    
    
    def warehouse(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
        validate: bool = False,
    ) -> WarehousePydantic:
        raw_response = self.raw.warehouse(
            warehouse_id=warehouse_id,
            is_default=is_default,
            name=name,
            created_at=created_at,
            origin_address=origin_address,
            return_address=return_address,
        )
        if validate:
            return WarehousePydantic(**raw_response.body)
        return api_client.construct_model_instance(WarehousePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._warehouse_mapped_args(
            warehouse_id=warehouse_id,
            is_default=is_default,
            name=name,
            created_at=created_at,
            origin_address=origin_address,
            return_address=return_address,
        )
        return await self._awarehouse_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        warehouse_id: typing.Optional[SeId] = None,
        is_default: typing.Optional[typing.Optional[bool]] = None,
        name: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        origin_address: typing.Optional[PartialAddress] = None,
        return_address: typing.Optional[PartialAddress] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._warehouse_mapped_args(
            warehouse_id=warehouse_id,
            is_default=is_default,
            name=name,
            created_at=created_at,
            origin_address=origin_address,
            return_address=return_address,
        )
        return self._warehouse_oapg(
            body=args.body,
        )

