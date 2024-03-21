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

from ship_engine_python_sdk.model.tax_identifier import TaxIdentifier as TaxIdentifierSchema
from ship_engine_python_sdk.model.weight import Weight as WeightSchema
from ship_engine_python_sdk.model.shipment_status import ShipmentStatus as ShipmentStatusSchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.shipment_item import ShipmentItem as ShipmentItemSchema
from ship_engine_python_sdk.model.insurance_provider import InsuranceProvider as InsuranceProviderSchema
from ship_engine_python_sdk.model.delivery_confirmation import DeliveryConfirmation as DeliveryConfirmationSchema
from ship_engine_python_sdk.model.date_time import DateTime as DateTimeSchema
from ship_engine_python_sdk.model.service_code import ServiceCode as ServiceCodeSchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema
from ship_engine_python_sdk.model.package import Package as PackageSchema
from ship_engine_python_sdk.model.validate_address import ValidateAddress as ValidateAddressSchema
from ship_engine_python_sdk.model.advanced_shipment_options import AdvancedShipmentOptions as AdvancedShipmentOptionsSchema
from ship_engine_python_sdk.model.shipping_address import ShippingAddress as ShippingAddressSchema
from ship_engine_python_sdk.model.tag import Tag as TagSchema
from ship_engine_python_sdk.model.date import Date as DateSchema
from ship_engine_python_sdk.model.international_shipment_options_nullable import InternationalShipmentOptionsNullable as InternationalShipmentOptionsNullableSchema
from ship_engine_python_sdk.model.se_id_nullable import SeIdNullable as SeIdNullableSchema
from ship_engine_python_sdk.model.shipping_address_to import ShippingAddressTo as ShippingAddressToSchema
from ship_engine_python_sdk.model.update_shipment_request_body import UpdateShipmentRequestBody as UpdateShipmentRequestBodySchema
from ship_engine_python_sdk.model.create_and_validate_shipment import CreateAndValidateShipment as CreateAndValidateShipmentSchema
from ship_engine_python_sdk.model.order_source_name import OrderSourceName as OrderSourceNameSchema

from ship_engine_python_sdk.type.shipping_address_to import ShippingAddressTo
from ship_engine_python_sdk.type.validate_address import ValidateAddress
from ship_engine_python_sdk.type.order_source_name import OrderSourceName
from ship_engine_python_sdk.type.shipment_item import ShipmentItem
from ship_engine_python_sdk.type.date import Date
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.service_code import ServiceCode
from ship_engine_python_sdk.type.tag import Tag
from ship_engine_python_sdk.type.international_shipment_options_nullable import InternationalShipmentOptionsNullable
from ship_engine_python_sdk.type.package import Package
from ship_engine_python_sdk.type.update_shipment_request_body import UpdateShipmentRequestBody
from ship_engine_python_sdk.type.weight import Weight
from ship_engine_python_sdk.type.shipment_status import ShipmentStatus
from ship_engine_python_sdk.type.insurance_provider import InsuranceProvider
from ship_engine_python_sdk.type.se_id_nullable import SeIdNullable
from ship_engine_python_sdk.type.tax_identifier import TaxIdentifier
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.shipping_address import ShippingAddress
from ship_engine_python_sdk.type.date_time import DateTime
from ship_engine_python_sdk.type.advanced_shipment_options import AdvancedShipmentOptions
from ship_engine_python_sdk.type.create_and_validate_shipment import CreateAndValidateShipment
from ship_engine_python_sdk.type.delivery_confirmation import DeliveryConfirmation

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.tax_identifier import TaxIdentifier as TaxIdentifierPydantic
from ship_engine_python_sdk.pydantic.shipping_address import ShippingAddress as ShippingAddressPydantic
from ship_engine_python_sdk.pydantic.date_time import DateTime as DateTimePydantic
from ship_engine_python_sdk.pydantic.se_id_nullable import SeIdNullable as SeIdNullablePydantic
from ship_engine_python_sdk.pydantic.weight import Weight as WeightPydantic
from ship_engine_python_sdk.pydantic.create_and_validate_shipment import CreateAndValidateShipment as CreateAndValidateShipmentPydantic
from ship_engine_python_sdk.pydantic.validate_address import ValidateAddress as ValidateAddressPydantic
from ship_engine_python_sdk.pydantic.tag import Tag as TagPydantic
from ship_engine_python_sdk.pydantic.shipment_item import ShipmentItem as ShipmentItemPydantic
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.service_code import ServiceCode as ServiceCodePydantic
from ship_engine_python_sdk.pydantic.package import Package as PackagePydantic
from ship_engine_python_sdk.pydantic.date import Date as DatePydantic
from ship_engine_python_sdk.pydantic.insurance_provider import InsuranceProvider as InsuranceProviderPydantic
from ship_engine_python_sdk.pydantic.shipment_status import ShipmentStatus as ShipmentStatusPydantic
from ship_engine_python_sdk.pydantic.delivery_confirmation import DeliveryConfirmation as DeliveryConfirmationPydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from ship_engine_python_sdk.pydantic.order_source_name import OrderSourceName as OrderSourceNamePydantic
from ship_engine_python_sdk.pydantic.advanced_shipment_options import AdvancedShipmentOptions as AdvancedShipmentOptionsPydantic
from ship_engine_python_sdk.pydantic.shipping_address_to import ShippingAddressTo as ShippingAddressToPydantic
from ship_engine_python_sdk.pydantic.international_shipment_options_nullable import InternationalShipmentOptionsNullable as InternationalShipmentOptionsNullablePydantic
from ship_engine_python_sdk.pydantic.update_shipment_request_body import UpdateShipmentRequestBody as UpdateShipmentRequestBodyPydantic

from . import path

# Path params
ShipmentIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'shipment_id': typing.Union[SeIdSchema, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_shipment_id = api_client.PathParameter(
    name="shipment_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateShipmentRequestBodySchema


request_body_update_shipment_request_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = CreateAndValidateShipmentSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CreateAndValidateShipment


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CreateAndValidateShipment


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

    def _shipment_0_mapped_args(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if shipment_id is not None:
            _body["shipment_id"] = shipment_id
        if carrier_id is not None:
            _body["carrier_id"] = carrier_id
        if service_code is not None:
            _body["service_code"] = service_code
        if external_order_id is not None:
            _body["external_order_id"] = external_order_id
        if items is not None:
            _body["items"] = items
        if tax_identifiers is not None:
            _body["tax_identifiers"] = tax_identifiers
        if external_shipment_id is not None:
            _body["external_shipment_id"] = external_shipment_id
        if shipment_number is not None:
            _body["shipment_number"] = shipment_number
        if ship_date is not None:
            _body["ship_date"] = ship_date
        if created_at is not None:
            _body["created_at"] = created_at
        if modified_at is not None:
            _body["modified_at"] = modified_at
        if shipment_status is not None:
            _body["shipment_status"] = shipment_status
        if ship_to is not None:
            _body["ship_to"] = ship_to
        if ship_from is not None:
            _body["ship_from"] = ship_from
        if warehouse_id is not None:
            _body["warehouse_id"] = warehouse_id
        if return_to is not None:
            _body["return_to"] = return_to
        if is_return is not None:
            _body["is_return"] = is_return
        if confirmation is not None:
            _body["confirmation"] = confirmation
        if customs is not None:
            _body["customs"] = customs
        if advanced_options is not None:
            _body["advanced_options"] = advanced_options
        if insurance_provider is not None:
            _body["insurance_provider"] = insurance_provider
        if order_source_code is not None:
            _body["order_source_code"] = order_source_code
        if packages is not None:
            _body["packages"] = packages
        if total_weight is not None:
            _body["total_weight"] = total_weight
        if comparison_rate_type is not None:
            _body["comparison_rate_type"] = comparison_rate_type
        if validate_address is not None:
            _body["validate_address"] = validate_address
        args.body = _body
        if shipment_id is not None:
            _path_params["shipment_id"] = shipment_id
        args.path = _path_params
        return args

    async def _ashipment_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update Shipment By ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_shipment_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/v1/shipments/{shipment_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_shipment_request_body.serialize(body, content_type)
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


    def _shipment_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update Shipment By ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_shipment_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/v1/shipments/{shipment_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_shipment_request_body.serialize(body, content_type)
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


class Shipment0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ashipment_0(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._shipment_0_mapped_args(
            ship_to=ship_to,
            ship_from=ship_from,
            shipment_id=shipment_id,
            tags=tags,
            shipment_id=shipment_id,
            carrier_id=carrier_id,
            service_code=service_code,
            external_order_id=external_order_id,
            items=items,
            tax_identifiers=tax_identifiers,
            external_shipment_id=external_shipment_id,
            shipment_number=shipment_number,
            ship_date=ship_date,
            created_at=created_at,
            modified_at=modified_at,
            shipment_status=shipment_status,
            warehouse_id=warehouse_id,
            return_to=return_to,
            is_return=is_return,
            confirmation=confirmation,
            customs=customs,
            advanced_options=advanced_options,
            insurance_provider=insurance_provider,
            order_source_code=order_source_code,
            packages=packages,
            total_weight=total_weight,
            comparison_rate_type=comparison_rate_type,
            validate_address=validate_address,
        )
        return await self._ashipment_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def shipment_0(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._shipment_0_mapped_args(
            ship_to=ship_to,
            ship_from=ship_from,
            shipment_id=shipment_id,
            tags=tags,
            shipment_id=shipment_id,
            carrier_id=carrier_id,
            service_code=service_code,
            external_order_id=external_order_id,
            items=items,
            tax_identifiers=tax_identifiers,
            external_shipment_id=external_shipment_id,
            shipment_number=shipment_number,
            ship_date=ship_date,
            created_at=created_at,
            modified_at=modified_at,
            shipment_status=shipment_status,
            warehouse_id=warehouse_id,
            return_to=return_to,
            is_return=is_return,
            confirmation=confirmation,
            customs=customs,
            advanced_options=advanced_options,
            insurance_provider=insurance_provider,
            order_source_code=order_source_code,
            packages=packages,
            total_weight=total_weight,
            comparison_rate_type=comparison_rate_type,
            validate_address=validate_address,
        )
        return self._shipment_0_oapg(
            body=args.body,
            path_params=args.path,
        )

class Shipment0(BaseApi):

    async def ashipment_0(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateAndValidateShipmentPydantic:
        raw_response = await self.raw.ashipment_0(
            ship_to=ship_to,
            ship_from=ship_from,
            shipment_id=shipment_id,
            tags=tags,
            shipment_id=shipment_id,
            carrier_id=carrier_id,
            service_code=service_code,
            external_order_id=external_order_id,
            items=items,
            tax_identifiers=tax_identifiers,
            external_shipment_id=external_shipment_id,
            shipment_number=shipment_number,
            ship_date=ship_date,
            created_at=created_at,
            modified_at=modified_at,
            shipment_status=shipment_status,
            warehouse_id=warehouse_id,
            return_to=return_to,
            is_return=is_return,
            confirmation=confirmation,
            customs=customs,
            advanced_options=advanced_options,
            insurance_provider=insurance_provider,
            order_source_code=order_source_code,
            packages=packages,
            total_weight=total_weight,
            comparison_rate_type=comparison_rate_type,
            validate_address=validate_address,
            **kwargs,
        )
        if validate:
            return RootModel[CreateAndValidateShipmentPydantic](raw_response.body).root
        return api_client.construct_model_instance(CreateAndValidateShipmentPydantic, raw_response.body)
    
    
    def shipment_0(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        validate: bool = False,
    ) -> CreateAndValidateShipmentPydantic:
        raw_response = self.raw.shipment_0(
            ship_to=ship_to,
            ship_from=ship_from,
            shipment_id=shipment_id,
            tags=tags,
            shipment_id=shipment_id,
            carrier_id=carrier_id,
            service_code=service_code,
            external_order_id=external_order_id,
            items=items,
            tax_identifiers=tax_identifiers,
            external_shipment_id=external_shipment_id,
            shipment_number=shipment_number,
            ship_date=ship_date,
            created_at=created_at,
            modified_at=modified_at,
            shipment_status=shipment_status,
            warehouse_id=warehouse_id,
            return_to=return_to,
            is_return=is_return,
            confirmation=confirmation,
            customs=customs,
            advanced_options=advanced_options,
            insurance_provider=insurance_provider,
            order_source_code=order_source_code,
            packages=packages,
            total_weight=total_weight,
            comparison_rate_type=comparison_rate_type,
            validate_address=validate_address,
        )
        if validate:
            return RootModel[CreateAndValidateShipmentPydantic](raw_response.body).root
        return api_client.construct_model_instance(CreateAndValidateShipmentPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._shipment_0_mapped_args(
            ship_to=ship_to,
            ship_from=ship_from,
            shipment_id=shipment_id,
            tags=tags,
            shipment_id=shipment_id,
            carrier_id=carrier_id,
            service_code=service_code,
            external_order_id=external_order_id,
            items=items,
            tax_identifiers=tax_identifiers,
            external_shipment_id=external_shipment_id,
            shipment_number=shipment_number,
            ship_date=ship_date,
            created_at=created_at,
            modified_at=modified_at,
            shipment_status=shipment_status,
            warehouse_id=warehouse_id,
            return_to=return_to,
            is_return=is_return,
            confirmation=confirmation,
            customs=customs,
            advanced_options=advanced_options,
            insurance_provider=insurance_provider,
            order_source_code=order_source_code,
            packages=packages,
            total_weight=total_weight,
            comparison_rate_type=comparison_rate_type,
            validate_address=validate_address,
        )
        return await self._ashipment_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        ship_to: ShippingAddressTo,
        ship_from: ShippingAddress,
        shipment_id: SeId,
        tags: typing.Optional[typing.List[Tag]] = None,
        shipment_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        external_order_id: typing.Optional[typing.Optional[str]] = None,
        items: typing.Optional[typing.List[ShipmentItem]] = None,
        tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = None,
        external_shipment_id: typing.Optional[typing.Optional[str]] = None,
        shipment_number: typing.Optional[typing.Optional[str]] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        modified_at: typing.Optional[DateTime] = None,
        shipment_status: typing.Optional[ShipmentStatus] = None,
        warehouse_id: typing.Optional[SeIdNullable] = None,
        return_to: typing.Optional[ShippingAddress] = None,
        is_return: typing.Optional[typing.Optional[bool]] = None,
        confirmation: typing.Optional[DeliveryConfirmation] = None,
        customs: typing.Optional[InternationalShipmentOptionsNullable] = None,
        advanced_options: typing.Optional[AdvancedShipmentOptions] = None,
        insurance_provider: typing.Optional[InsuranceProvider] = None,
        order_source_code: typing.Optional[OrderSourceName] = None,
        packages: typing.Optional[typing.List[Package]] = None,
        total_weight: typing.Optional[Weight] = None,
        comparison_rate_type: typing.Optional[typing.Optional[str]] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._shipment_0_mapped_args(
            ship_to=ship_to,
            ship_from=ship_from,
            shipment_id=shipment_id,
            tags=tags,
            shipment_id=shipment_id,
            carrier_id=carrier_id,
            service_code=service_code,
            external_order_id=external_order_id,
            items=items,
            tax_identifiers=tax_identifiers,
            external_shipment_id=external_shipment_id,
            shipment_number=shipment_number,
            ship_date=ship_date,
            created_at=created_at,
            modified_at=modified_at,
            shipment_status=shipment_status,
            warehouse_id=warehouse_id,
            return_to=return_to,
            is_return=is_return,
            confirmation=confirmation,
            customs=customs,
            advanced_options=advanced_options,
            insurance_provider=insurance_provider,
            order_source_code=order_source_code,
            packages=packages,
            total_weight=total_weight,
            comparison_rate_type=comparison_rate_type,
            validate_address=validate_address,
        )
        return self._shipment_0_oapg(
            body=args.body,
            path_params=args.path,
        )

