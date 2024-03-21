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

from ship_engine_python_sdk.model.tracking_status import TrackingStatus as TrackingStatusSchema
from ship_engine_python_sdk.model.carrier_code import CarrierCode as CarrierCodeSchema
from ship_engine_python_sdk.model.package_code import PackageCode as PackageCodeSchema
from ship_engine_python_sdk.model.optional_link_nullable import OptionalLinkNullable as OptionalLinkNullableSchema
from ship_engine_python_sdk.model.label_download import LabelDownload as LabelDownloadSchema
from ship_engine_python_sdk.model.partial_shipment import PartialShipment as PartialShipmentSchema
from ship_engine_python_sdk.model.label_layout import LabelLayout as LabelLayoutSchema
from ship_engine_python_sdk.model.label_status import LabelStatus as LabelStatusSchema
from ship_engine_python_sdk.model.label import Label as LabelSchema
from ship_engine_python_sdk.model.monetary_value import MonetaryValue as MonetaryValueSchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.display_scheme import DisplayScheme as DisplaySchemeSchema
from ship_engine_python_sdk.model.optional_link import OptionalLink as OptionalLinkSchema
from ship_engine_python_sdk.model.date_time import DateTime as DateTimeSchema
from ship_engine_python_sdk.model.service_code import ServiceCode as ServiceCodeSchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema
from ship_engine_python_sdk.model.label_charge_event import LabelChargeEvent as LabelChargeEventSchema
from ship_engine_python_sdk.model.label_packages import LabelPackages as LabelPackagesSchema
from ship_engine_python_sdk.model.validate_address import ValidateAddress as ValidateAddressSchema
from ship_engine_python_sdk.model.label_download_type import LabelDownloadType as LabelDownloadTypeSchema
from ship_engine_python_sdk.model.alternative_identifier import AlternativeIdentifier as AlternativeIdentifierSchema
from ship_engine_python_sdk.model.image_id_nullable import ImageIdNullable as ImageIdNullableSchema
from ship_engine_python_sdk.model.date import Date as DateSchema
from ship_engine_python_sdk.model.label_format import LabelFormat as LabelFormatSchema

from ship_engine_python_sdk.type.label import Label
from ship_engine_python_sdk.type.validate_address import ValidateAddress
from ship_engine_python_sdk.type.alternative_identifier import AlternativeIdentifier
from ship_engine_python_sdk.type.date import Date
from ship_engine_python_sdk.type.optional_link_nullable import OptionalLinkNullable
from ship_engine_python_sdk.type.label_charge_event import LabelChargeEvent
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.label_download_type import LabelDownloadType
from ship_engine_python_sdk.type.service_code import ServiceCode
from ship_engine_python_sdk.type.package_code import PackageCode
from ship_engine_python_sdk.type.label_status import LabelStatus
from ship_engine_python_sdk.type.image_id_nullable import ImageIdNullable
from ship_engine_python_sdk.type.monetary_value import MonetaryValue
from ship_engine_python_sdk.type.label_packages import LabelPackages
from ship_engine_python_sdk.type.partial_shipment import PartialShipment
from ship_engine_python_sdk.type.carrier_code import CarrierCode
from ship_engine_python_sdk.type.label_format import LabelFormat
from ship_engine_python_sdk.type.label_layout import LabelLayout
from ship_engine_python_sdk.type.optional_link import OptionalLink
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.label_download import LabelDownload
from ship_engine_python_sdk.type.display_scheme import DisplayScheme
from ship_engine_python_sdk.type.date_time import DateTime
from ship_engine_python_sdk.type.tracking_status import TrackingStatus

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.date_time import DateTime as DateTimePydantic
from ship_engine_python_sdk.pydantic.label_download_type import LabelDownloadType as LabelDownloadTypePydantic
from ship_engine_python_sdk.pydantic.partial_shipment import PartialShipment as PartialShipmentPydantic
from ship_engine_python_sdk.pydantic.display_scheme import DisplayScheme as DisplaySchemePydantic
from ship_engine_python_sdk.pydantic.alternative_identifier import AlternativeIdentifier as AlternativeIdentifierPydantic
from ship_engine_python_sdk.pydantic.tracking_status import TrackingStatus as TrackingStatusPydantic
from ship_engine_python_sdk.pydantic.validate_address import ValidateAddress as ValidateAddressPydantic
from ship_engine_python_sdk.pydantic.label_status import LabelStatus as LabelStatusPydantic
from ship_engine_python_sdk.pydantic.label_packages import LabelPackages as LabelPackagesPydantic
from ship_engine_python_sdk.pydantic.optional_link_nullable import OptionalLinkNullable as OptionalLinkNullablePydantic
from ship_engine_python_sdk.pydantic.label_layout import LabelLayout as LabelLayoutPydantic
from ship_engine_python_sdk.pydantic.optional_link import OptionalLink as OptionalLinkPydantic
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.label import Label as LabelPydantic
from ship_engine_python_sdk.pydantic.service_code import ServiceCode as ServiceCodePydantic
from ship_engine_python_sdk.pydantic.monetary_value import MonetaryValue as MonetaryValuePydantic
from ship_engine_python_sdk.pydantic.label_charge_event import LabelChargeEvent as LabelChargeEventPydantic
from ship_engine_python_sdk.pydantic.date import Date as DatePydantic
from ship_engine_python_sdk.pydantic.package_code import PackageCode as PackageCodePydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from ship_engine_python_sdk.pydantic.label_download import LabelDownload as LabelDownloadPydantic
from ship_engine_python_sdk.pydantic.image_id_nullable import ImageIdNullable as ImageIdNullablePydantic
from ship_engine_python_sdk.pydantic.carrier_code import CarrierCode as CarrierCodePydantic
from ship_engine_python_sdk.pydantic.label_format import LabelFormat as LabelFormatPydantic

# body param
SchemaForRequestBodyApplicationJson = LabelSchema


request_body_label = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = LabelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Label


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Label


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

    def _label_mapped_args(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if label_id is not None:
            _body["label_id"] = label_id
        if status is not None:
            _body["status"] = status
        if shipment_id is not None:
            _body["shipment_id"] = shipment_id
        if shipment is not None:
            _body["shipment"] = shipment
        if ship_date is not None:
            _body["ship_date"] = ship_date
        if created_at is not None:
            _body["created_at"] = created_at
        if shipment_cost is not None:
            _body["shipment_cost"] = shipment_cost
        if insurance_cost is not None:
            _body["insurance_cost"] = insurance_cost
        if requested_comparison_amount is not None:
            _body["requested_comparison_amount"] = requested_comparison_amount
        if tracking_number is not None:
            _body["tracking_number"] = tracking_number
        if is_return_label is not None:
            _body["is_return_label"] = is_return_label
        if rma_number is not None:
            _body["rma_number"] = rma_number
        if is_international is not None:
            _body["is_international"] = is_international
        if batch_id is not None:
            _body["batch_id"] = batch_id
        if carrier_id is not None:
            _body["carrier_id"] = carrier_id
        if charge_event is not None:
            _body["charge_event"] = charge_event
        if outbound_label_id is not None:
            _body["outbound_label_id"] = outbound_label_id
        if service_code is not None:
            _body["service_code"] = service_code
        if test_label is not None:
            _body["test_label"] = test_label
        if package_code is not None:
            _body["package_code"] = package_code
        if validate_address is not None:
            _body["validate_address"] = validate_address
        if voided is not None:
            _body["voided"] = voided
        if voided_at is not None:
            _body["voided_at"] = voided_at
        if label_download_type is not None:
            _body["label_download_type"] = label_download_type
        if label_format is not None:
            _body["label_format"] = label_format
        if display_scheme is not None:
            _body["display_scheme"] = display_scheme
        if label_layout is not None:
            _body["label_layout"] = label_layout
        if trackable is not None:
            _body["trackable"] = trackable
        if label_image_id is not None:
            _body["label_image_id"] = label_image_id
        if carrier_code is not None:
            _body["carrier_code"] = carrier_code
        if tracking_status is not None:
            _body["tracking_status"] = tracking_status
        if label_download is not None:
            _body["label_download"] = label_download
        if form_download is not None:
            _body["form_download"] = form_download
        if insurance_claim is not None:
            _body["insurance_claim"] = insurance_claim
        if packages is not None:
            _body["packages"] = packages
        if alternative_identifiers is not None:
            _body["alternative_identifiers"] = alternative_identifiers
        args.body = _body
        return args

    async def _alabel_oapg(
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
        Purchase Label
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
            path_template='/v1/labels',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_label.serialize(body, content_type)
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


    def _label_oapg(
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
        Purchase Label
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
            path_template='/v1/labels',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_label.serialize(body, content_type)
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


class LabelRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alabel(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._label_mapped_args(
            label_id=label_id,
            status=status,
            shipment_id=shipment_id,
            shipment=shipment,
            ship_date=ship_date,
            created_at=created_at,
            shipment_cost=shipment_cost,
            insurance_cost=insurance_cost,
            requested_comparison_amount=requested_comparison_amount,
            tracking_number=tracking_number,
            is_return_label=is_return_label,
            rma_number=rma_number,
            is_international=is_international,
            batch_id=batch_id,
            carrier_id=carrier_id,
            charge_event=charge_event,
            outbound_label_id=outbound_label_id,
            service_code=service_code,
            test_label=test_label,
            package_code=package_code,
            validate_address=validate_address,
            voided=voided,
            voided_at=voided_at,
            label_download_type=label_download_type,
            label_format=label_format,
            display_scheme=display_scheme,
            label_layout=label_layout,
            trackable=trackable,
            label_image_id=label_image_id,
            carrier_code=carrier_code,
            tracking_status=tracking_status,
            label_download=label_download,
            form_download=form_download,
            insurance_claim=insurance_claim,
            packages=packages,
            alternative_identifiers=alternative_identifiers,
        )
        return await self._alabel_oapg(
            body=args.body,
            **kwargs,
        )
    
    def label(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._label_mapped_args(
            label_id=label_id,
            status=status,
            shipment_id=shipment_id,
            shipment=shipment,
            ship_date=ship_date,
            created_at=created_at,
            shipment_cost=shipment_cost,
            insurance_cost=insurance_cost,
            requested_comparison_amount=requested_comparison_amount,
            tracking_number=tracking_number,
            is_return_label=is_return_label,
            rma_number=rma_number,
            is_international=is_international,
            batch_id=batch_id,
            carrier_id=carrier_id,
            charge_event=charge_event,
            outbound_label_id=outbound_label_id,
            service_code=service_code,
            test_label=test_label,
            package_code=package_code,
            validate_address=validate_address,
            voided=voided,
            voided_at=voided_at,
            label_download_type=label_download_type,
            label_format=label_format,
            display_scheme=display_scheme,
            label_layout=label_layout,
            trackable=trackable,
            label_image_id=label_image_id,
            carrier_code=carrier_code,
            tracking_status=tracking_status,
            label_download=label_download,
            form_download=form_download,
            insurance_claim=insurance_claim,
            packages=packages,
            alternative_identifiers=alternative_identifiers,
        )
        return self._label_oapg(
            body=args.body,
        )

class Label(BaseApi):

    async def alabel(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> LabelPydantic:
        raw_response = await self.raw.alabel(
            label_id=label_id,
            status=status,
            shipment_id=shipment_id,
            shipment=shipment,
            ship_date=ship_date,
            created_at=created_at,
            shipment_cost=shipment_cost,
            insurance_cost=insurance_cost,
            requested_comparison_amount=requested_comparison_amount,
            tracking_number=tracking_number,
            is_return_label=is_return_label,
            rma_number=rma_number,
            is_international=is_international,
            batch_id=batch_id,
            carrier_id=carrier_id,
            charge_event=charge_event,
            outbound_label_id=outbound_label_id,
            service_code=service_code,
            test_label=test_label,
            package_code=package_code,
            validate_address=validate_address,
            voided=voided,
            voided_at=voided_at,
            label_download_type=label_download_type,
            label_format=label_format,
            display_scheme=display_scheme,
            label_layout=label_layout,
            trackable=trackable,
            label_image_id=label_image_id,
            carrier_code=carrier_code,
            tracking_status=tracking_status,
            label_download=label_download,
            form_download=form_download,
            insurance_claim=insurance_claim,
            packages=packages,
            alternative_identifiers=alternative_identifiers,
            **kwargs,
        )
        if validate:
            return LabelPydantic(**raw_response.body)
        return api_client.construct_model_instance(LabelPydantic, raw_response.body)
    
    
    def label(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
        validate: bool = False,
    ) -> LabelPydantic:
        raw_response = self.raw.label(
            label_id=label_id,
            status=status,
            shipment_id=shipment_id,
            shipment=shipment,
            ship_date=ship_date,
            created_at=created_at,
            shipment_cost=shipment_cost,
            insurance_cost=insurance_cost,
            requested_comparison_amount=requested_comparison_amount,
            tracking_number=tracking_number,
            is_return_label=is_return_label,
            rma_number=rma_number,
            is_international=is_international,
            batch_id=batch_id,
            carrier_id=carrier_id,
            charge_event=charge_event,
            outbound_label_id=outbound_label_id,
            service_code=service_code,
            test_label=test_label,
            package_code=package_code,
            validate_address=validate_address,
            voided=voided,
            voided_at=voided_at,
            label_download_type=label_download_type,
            label_format=label_format,
            display_scheme=display_scheme,
            label_layout=label_layout,
            trackable=trackable,
            label_image_id=label_image_id,
            carrier_code=carrier_code,
            tracking_status=tracking_status,
            label_download=label_download,
            form_download=form_download,
            insurance_claim=insurance_claim,
            packages=packages,
            alternative_identifiers=alternative_identifiers,
        )
        if validate:
            return LabelPydantic(**raw_response.body)
        return api_client.construct_model_instance(LabelPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._label_mapped_args(
            label_id=label_id,
            status=status,
            shipment_id=shipment_id,
            shipment=shipment,
            ship_date=ship_date,
            created_at=created_at,
            shipment_cost=shipment_cost,
            insurance_cost=insurance_cost,
            requested_comparison_amount=requested_comparison_amount,
            tracking_number=tracking_number,
            is_return_label=is_return_label,
            rma_number=rma_number,
            is_international=is_international,
            batch_id=batch_id,
            carrier_id=carrier_id,
            charge_event=charge_event,
            outbound_label_id=outbound_label_id,
            service_code=service_code,
            test_label=test_label,
            package_code=package_code,
            validate_address=validate_address,
            voided=voided,
            voided_at=voided_at,
            label_download_type=label_download_type,
            label_format=label_format,
            display_scheme=display_scheme,
            label_layout=label_layout,
            trackable=trackable,
            label_image_id=label_image_id,
            carrier_code=carrier_code,
            tracking_status=tracking_status,
            label_download=label_download,
            form_download=form_download,
            insurance_claim=insurance_claim,
            packages=packages,
            alternative_identifiers=alternative_identifiers,
        )
        return await self._alabel_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        label_id: typing.Optional[SeId] = None,
        status: typing.Optional[LabelStatus] = None,
        shipment_id: typing.Optional[SeId] = None,
        shipment: typing.Optional[PartialShipment] = None,
        ship_date: typing.Optional[Date] = None,
        created_at: typing.Optional[DateTime] = None,
        shipment_cost: typing.Optional[MonetaryValue] = None,
        insurance_cost: typing.Optional[MonetaryValue] = None,
        requested_comparison_amount: typing.Optional[MonetaryValue] = None,
        tracking_number: typing.Optional[str] = None,
        is_return_label: typing.Optional[bool] = None,
        rma_number: typing.Optional[typing.Optional[str]] = None,
        is_international: typing.Optional[bool] = None,
        batch_id: typing.Optional[SeId] = None,
        carrier_id: typing.Optional[SeId] = None,
        charge_event: typing.Optional[LabelChargeEvent] = None,
        outbound_label_id: typing.Optional[SeId] = None,
        service_code: typing.Optional[ServiceCode] = None,
        test_label: typing.Optional[bool] = None,
        package_code: typing.Optional[PackageCode] = None,
        validate_address: typing.Optional[ValidateAddress] = None,
        voided: typing.Optional[bool] = None,
        voided_at: typing.Optional[DateTime] = None,
        label_download_type: typing.Optional[LabelDownloadType] = None,
        label_format: typing.Optional[LabelFormat] = None,
        display_scheme: typing.Optional[DisplayScheme] = None,
        label_layout: typing.Optional[LabelLayout] = None,
        trackable: typing.Optional[bool] = None,
        label_image_id: typing.Optional[ImageIdNullable] = None,
        carrier_code: typing.Optional[CarrierCode] = None,
        tracking_status: typing.Optional[TrackingStatus] = None,
        label_download: typing.Optional[LabelDownload] = None,
        form_download: typing.Optional[OptionalLinkNullable] = None,
        insurance_claim: typing.Optional[OptionalLink] = None,
        packages: typing.Optional[LabelPackages] = None,
        alternative_identifiers: typing.Optional[typing.Optional[typing.List[AlternativeIdentifier]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._label_mapped_args(
            label_id=label_id,
            status=status,
            shipment_id=shipment_id,
            shipment=shipment,
            ship_date=ship_date,
            created_at=created_at,
            shipment_cost=shipment_cost,
            insurance_cost=insurance_cost,
            requested_comparison_amount=requested_comparison_amount,
            tracking_number=tracking_number,
            is_return_label=is_return_label,
            rma_number=rma_number,
            is_international=is_international,
            batch_id=batch_id,
            carrier_id=carrier_id,
            charge_event=charge_event,
            outbound_label_id=outbound_label_id,
            service_code=service_code,
            test_label=test_label,
            package_code=package_code,
            validate_address=validate_address,
            voided=voided,
            voided_at=voided_at,
            label_download_type=label_download_type,
            label_format=label_format,
            display_scheme=display_scheme,
            label_layout=label_layout,
            trackable=trackable,
            label_image_id=label_image_id,
            carrier_code=carrier_code,
            tracking_status=tracking_status,
            label_download=label_download,
            form_download=form_download,
            insurance_claim=insurance_claim,
            packages=packages,
            alternative_identifiers=alternative_identifiers,
        )
        return self._label_oapg(
            body=args.body,
        )

