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

from ship_engine_python_sdk.model.label_status import LabelStatus as LabelStatusSchema
from ship_engine_python_sdk.model.paged_list_response_body import PagedListResponseBody as PagedListResponseBodySchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.service_code import ServiceCode as ServiceCodeSchema
from ship_engine_python_sdk.model.sort_dir import SortDir as SortDirSchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema

from ship_engine_python_sdk.type.sort_dir import SortDir
from ship_engine_python_sdk.type.paged_list_response_body import PagedListResponseBody
from ship_engine_python_sdk.type.service_code import ServiceCode
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.label_status import LabelStatus

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.service_code import ServiceCode as ServiceCodePydantic
from ship_engine_python_sdk.pydantic.sort_dir import SortDir as SortDirPydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from ship_engine_python_sdk.pydantic.label_status import LabelStatus as LabelStatusPydantic
from ship_engine_python_sdk.pydantic.paged_list_response_body import PagedListResponseBody as PagedListResponseBodyPydantic

# Query params
LabelStatusSchema = LabelStatusSchema
ServiceCodeSchema = schemas.Schema
CarrierIdSchema = schemas.Schema


class TrackingNumberSchema(
    schemas.StrSchema
):
    pass
BatchIdSchema = schemas.Schema
RateIdSchema = schemas.Schema
ShipmentIdSchema = schemas.Schema
WarehouseIdSchema = schemas.Schema
CreatedAtStartSchema = schemas.DateTimeSchema
CreatedAtEndSchema = schemas.DateTimeSchema


class PageSchema(
    schemas.Int32Schema
):
    pass


class PageSizeSchema(
    schemas.Int32Schema
):
    pass
SortDirSchema = SortDirSchema


class SortBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def MODIFIED_AT(cls):
        return cls("modified_at")
    
    @schemas.classproperty
    def CREATED_AT(cls):
        return cls("created_at")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'label_status': typing.Union[LabelStatusSchema, ],
        'service_code': typing.Union[ServiceCodeSchema, ],
        'carrier_id': typing.Union[CarrierIdSchema, ],
        'tracking_number': typing.Union[TrackingNumberSchema, str, ],
        'batch_id': typing.Union[BatchIdSchema, ],
        'rate_id': typing.Union[RateIdSchema, ],
        'shipment_id': typing.Union[ShipmentIdSchema, ],
        'warehouse_id': typing.Union[WarehouseIdSchema, ],
        'created_at_start': typing.Union[CreatedAtStartSchema, str, datetime, ],
        'created_at_end': typing.Union[CreatedAtEndSchema, str, datetime, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'sort_dir': typing.Union[SortDirSchema, ],
        'sort_by': typing.Union[SortBySchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_label_status = api_client.QueryParameter(
    name="label_status",
    style=api_client.ParameterStyle.FORM,
    schema=LabelStatusSchema,
    explode=True,
)
request_query_service_code = api_client.QueryParameter(
    name="service_code",
    style=api_client.ParameterStyle.FORM,
    schema=ServiceCodeSchema,
    explode=True,
)
request_query_carrier_id = api_client.QueryParameter(
    name="carrier_id",
    style=api_client.ParameterStyle.FORM,
    schema=SeIdSchema,
    explode=True,
)
request_query_tracking_number = api_client.QueryParameter(
    name="tracking_number",
    style=api_client.ParameterStyle.FORM,
    schema=TrackingNumberSchema,
    explode=True,
)
request_query_batch_id = api_client.QueryParameter(
    name="batch_id",
    style=api_client.ParameterStyle.FORM,
    schema=SeIdSchema,
    explode=True,
)
request_query_rate_id = api_client.QueryParameter(
    name="rate_id",
    style=api_client.ParameterStyle.FORM,
    schema=SeIdSchema,
    explode=True,
)
request_query_shipment_id = api_client.QueryParameter(
    name="shipment_id",
    style=api_client.ParameterStyle.FORM,
    schema=SeIdSchema,
    explode=True,
)
request_query_warehouse_id = api_client.QueryParameter(
    name="warehouse_id",
    style=api_client.ParameterStyle.FORM,
    schema=SeIdSchema,
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
request_query_sort_dir = api_client.QueryParameter(
    name="sort_dir",
    style=api_client.ParameterStyle.FORM,
    schema=SortDirSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PagedListResponseBodySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PagedListResponseBody


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PagedListResponseBody


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

    def _labels_mapped_args(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if label_status is not None:
            _query_params["label_status"] = label_status
        if service_code is not None:
            _query_params["service_code"] = service_code
        if carrier_id is not None:
            _query_params["carrier_id"] = carrier_id
        if tracking_number is not None:
            _query_params["tracking_number"] = tracking_number
        if batch_id is not None:
            _query_params["batch_id"] = batch_id
        if rate_id is not None:
            _query_params["rate_id"] = rate_id
        if shipment_id is not None:
            _query_params["shipment_id"] = shipment_id
        if warehouse_id is not None:
            _query_params["warehouse_id"] = warehouse_id
        if created_at_start is not None:
            _query_params["created_at_start"] = created_at_start
        if created_at_end is not None:
            _query_params["created_at_end"] = created_at_end
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["page_size"] = page_size
        if sort_dir is not None:
            _query_params["sort_dir"] = sort_dir
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        args.query = _query_params
        return args

    async def _alabels_oapg(
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
        List labels
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_label_status,
            request_query_service_code,
            request_query_carrier_id,
            request_query_tracking_number,
            request_query_batch_id,
            request_query_rate_id,
            request_query_shipment_id,
            request_query_warehouse_id,
            request_query_created_at_start,
            request_query_created_at_end,
            request_query_page,
            request_query_page_size,
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
            path_template='/v1/labels',
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


    def _labels_oapg(
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
        List labels
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_label_status,
            request_query_service_code,
            request_query_carrier_id,
            request_query_tracking_number,
            request_query_batch_id,
            request_query_rate_id,
            request_query_shipment_id,
            request_query_warehouse_id,
            request_query_created_at_start,
            request_query_created_at_end,
            request_query_page,
            request_query_page_size,
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
            path_template='/v1/labels',
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


class LabelsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alabels(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._labels_mapped_args(
            label_status=label_status,
            service_code=service_code,
            carrier_id=carrier_id,
            tracking_number=tracking_number,
            batch_id=batch_id,
            rate_id=rate_id,
            shipment_id=shipment_id,
            warehouse_id=warehouse_id,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            page_size=page_size,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return await self._alabels_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def labels(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._labels_mapped_args(
            label_status=label_status,
            service_code=service_code,
            carrier_id=carrier_id,
            tracking_number=tracking_number,
            batch_id=batch_id,
            rate_id=rate_id,
            shipment_id=shipment_id,
            warehouse_id=warehouse_id,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            page_size=page_size,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return self._labels_oapg(
            query_params=args.query,
        )

class Labels(BaseApi):

    async def alabels(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PagedListResponseBodyPydantic:
        raw_response = await self.raw.alabels(
            label_status=label_status,
            service_code=service_code,
            carrier_id=carrier_id,
            tracking_number=tracking_number,
            batch_id=batch_id,
            rate_id=rate_id,
            shipment_id=shipment_id,
            warehouse_id=warehouse_id,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            page_size=page_size,
            sort_dir=sort_dir,
            sort_by=sort_by,
            **kwargs,
        )
        if validate:
            return PagedListResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(PagedListResponseBodyPydantic, raw_response.body)
    
    
    def labels(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PagedListResponseBodyPydantic:
        raw_response = self.raw.labels(
            label_status=label_status,
            service_code=service_code,
            carrier_id=carrier_id,
            tracking_number=tracking_number,
            batch_id=batch_id,
            rate_id=rate_id,
            shipment_id=shipment_id,
            warehouse_id=warehouse_id,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            page_size=page_size,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        if validate:
            return PagedListResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(PagedListResponseBodyPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._labels_mapped_args(
            label_status=label_status,
            service_code=service_code,
            carrier_id=carrier_id,
            tracking_number=tracking_number,
            batch_id=batch_id,
            rate_id=rate_id,
            shipment_id=shipment_id,
            warehouse_id=warehouse_id,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            page_size=page_size,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return await self._alabels_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        label_status: typing.Optional[LabelStatus] = None,
        service_code: typing.Optional[ServiceCode] = None,
        carrier_id: typing.Optional[SeId] = None,
        tracking_number: typing.Optional[str] = None,
        batch_id: typing.Optional[SeId] = None,
        rate_id: typing.Optional[SeId] = None,
        shipment_id: typing.Optional[SeId] = None,
        warehouse_id: typing.Optional[SeId] = None,
        created_at_start: typing.Optional[datetime] = None,
        created_at_end: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_dir: typing.Optional[SortDir] = None,
        sort_by: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._labels_mapped_args(
            label_status=label_status,
            service_code=service_code,
            carrier_id=carrier_id,
            tracking_number=tracking_number,
            batch_id=batch_id,
            rate_id=rate_id,
            shipment_id=shipment_id,
            warehouse_id=warehouse_id,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            page_size=page_size,
            sort_dir=sort_dir,
            sort_by=sort_by,
        )
        return self._labels_oapg(
            query_params=args.query,
        )

