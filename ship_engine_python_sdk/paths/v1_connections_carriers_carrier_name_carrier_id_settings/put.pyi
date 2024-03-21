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

from ship_engine_python_sdk.model.ancillary_service_endorsement import AncillaryServiceEndorsement as AncillaryServiceEndorsementSchema
from ship_engine_python_sdk.model.update_carrier_settings_request_body import UpdateCarrierSettingsRequestBody as UpdateCarrierSettingsRequestBodySchema
from ship_engine_python_sdk.model.empty_response_body import EmptyResponseBody as EmptyResponseBodySchema
from ship_engine_python_sdk.model.smart_post_hub import SmartPostHub as SmartPostHubSchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.ups_invoice import UpsInvoice as UpsInvoiceSchema
from ship_engine_python_sdk.model.carrier_name_with_settings import CarrierNameWithSettings as CarrierNameWithSettingsSchema
from ship_engine_python_sdk.model.ups_pickup_type import UpsPickupType as UpsPickupTypeSchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema

from ship_engine_python_sdk.type.update_carrier_settings_request_body import UpdateCarrierSettingsRequestBody
from ship_engine_python_sdk.type.ancillary_service_endorsement import AncillaryServiceEndorsement
from ship_engine_python_sdk.type.smart_post_hub import SmartPostHub
from ship_engine_python_sdk.type.carrier_name_with_settings import CarrierNameWithSettings
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.ups_pickup_type import UpsPickupType
from ship_engine_python_sdk.type.empty_response_body import EmptyResponseBody
from ship_engine_python_sdk.type.ups_invoice import UpsInvoice

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.carrier_name_with_settings import CarrierNameWithSettings as CarrierNameWithSettingsPydantic
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.empty_response_body import EmptyResponseBody as EmptyResponseBodyPydantic
from ship_engine_python_sdk.pydantic.update_carrier_settings_request_body import UpdateCarrierSettingsRequestBody as UpdateCarrierSettingsRequestBodyPydantic
from ship_engine_python_sdk.pydantic.ups_invoice import UpsInvoice as UpsInvoicePydantic
from ship_engine_python_sdk.pydantic.smart_post_hub import SmartPostHub as SmartPostHubPydantic
from ship_engine_python_sdk.pydantic.ancillary_service_endorsement import AncillaryServiceEndorsement as AncillaryServiceEndorsementPydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from ship_engine_python_sdk.pydantic.ups_pickup_type import UpsPickupType as UpsPickupTypePydantic

# Path params
CarrierNameSchema = CarrierNameWithSettingsSchema
CarrierIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'carrier_name': typing.Union[CarrierNameWithSettingsSchema, ],
        'carrier_id': typing.Union[SeIdSchema, ],
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


request_path_carrier_name = api_client.PathParameter(
    name="carrier_name",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CarrierNameWithSettingsSchema,
    required=True,
)
request_path_carrier_id = api_client.PathParameter(
    name="carrier_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateCarrierSettingsRequestBodySchema


request_body_update_carrier_settings_request_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor204ResponseBodyApplicationJson = schemas.Schema
SchemaFor204ResponseBodyTextPlain = schemas.Schema


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: EmptyResponseBody


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: EmptyResponseBody


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor204ResponseBodyApplicationJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor204ResponseBodyTextPlain),
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
    'text/plain',
)


class BaseApi(api_client.Api):

    def _update_settings_mapped_args(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if nickname is not None:
            _body["nickname"] = nickname
        if should_hide_account_number_on_archive_doc is not None:
            _body["should_hide_account_number_on_archive_doc"] = should_hide_account_number_on_archive_doc
        if is_primary_account is not None:
            _body["is_primary_account"] = is_primary_account
        if pickup_type is not None:
            _body["pickup_type"] = pickup_type
        if smart_post_hub is not None:
            _body["smart_post_hub"] = smart_post_hub
        if smart_post_endorsement is not None:
            _body["smart_post_endorsement"] = smart_post_endorsement
        if signature_image is not None:
            _body["signature_image"] = signature_image
        if letterhead_image is not None:
            _body["letterhead_image"] = letterhead_image
        if include_barcode_with_order_number is not None:
            _body["include_barcode_with_order_number"] = include_barcode_with_order_number
        if receive_email_on_manifest_processing is not None:
            _body["receive_email_on_manifest_processing"] = receive_email_on_manifest_processing
        if use_carbon_neutral_shipping_program is not None:
            _body["use_carbon_neutral_shipping_program"] = use_carbon_neutral_shipping_program
        if use_ground_freight_pricing is not None:
            _body["use_ground_freight_pricing"] = use_ground_freight_pricing
        if use_consolidation_services is not None:
            _body["use_consolidation_services"] = use_consolidation_services
        if use_order_number_on_mail_innovations_labels is not None:
            _body["use_order_number_on_mail_innovations_labels"] = use_order_number_on_mail_innovations_labels
        if mail_innovations_endorsement is not None:
            _body["mail_innovations_endorsement"] = mail_innovations_endorsement
        if mail_innovations_cost_center is not None:
            _body["mail_innovations_cost_center"] = mail_innovations_cost_center
        if use_negotiated_rates is not None:
            _body["use_negotiated_rates"] = use_negotiated_rates
        if account_postal_code is not None:
            _body["account_postal_code"] = account_postal_code
        if invoice is not None:
            _body["invoice"] = invoice
        if email is not None:
            _body["email"] = email
        args.body = body if body is not None else _body
        if carrier_name is not None:
            _path_params["carrier_name"] = carrier_name
        if carrier_id is not None:
            _path_params["carrier_id"] = carrier_id
        args.path = _path_params
        return args

    async def _aupdate_settings_oapg(
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
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update carrier settings
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_carrier_name,
            request_path_carrier_id,
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
            path_template='/v1/connections/carriers/{carrier_name}/{carrier_id}/settings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_carrier_settings_request_body.serialize(body, content_type)
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


    def _update_settings_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update carrier settings
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_carrier_name,
            request_path_carrier_id,
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
            path_template='/v1/connections/carriers/{carrier_name}/{carrier_id}/settings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_carrier_settings_request_body.serialize(body, content_type)
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


class UpdateSettingsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_settings(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_settings_mapped_args(
            body=body,
            carrier_name=carrier_name,
            carrier_id=carrier_id,
            nickname=nickname,
            should_hide_account_number_on_archive_doc=should_hide_account_number_on_archive_doc,
            is_primary_account=is_primary_account,
            pickup_type=pickup_type,
            smart_post_hub=smart_post_hub,
            smart_post_endorsement=smart_post_endorsement,
            signature_image=signature_image,
            letterhead_image=letterhead_image,
            include_barcode_with_order_number=include_barcode_with_order_number,
            receive_email_on_manifest_processing=receive_email_on_manifest_processing,
            use_carbon_neutral_shipping_program=use_carbon_neutral_shipping_program,
            use_ground_freight_pricing=use_ground_freight_pricing,
            use_consolidation_services=use_consolidation_services,
            use_order_number_on_mail_innovations_labels=use_order_number_on_mail_innovations_labels,
            mail_innovations_endorsement=mail_innovations_endorsement,
            mail_innovations_cost_center=mail_innovations_cost_center,
            use_negotiated_rates=use_negotiated_rates,
            account_postal_code=account_postal_code,
            invoice=invoice,
            email=email,
        )
        return await self._aupdate_settings_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_settings(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_settings_mapped_args(
            body=body,
            carrier_name=carrier_name,
            carrier_id=carrier_id,
            nickname=nickname,
            should_hide_account_number_on_archive_doc=should_hide_account_number_on_archive_doc,
            is_primary_account=is_primary_account,
            pickup_type=pickup_type,
            smart_post_hub=smart_post_hub,
            smart_post_endorsement=smart_post_endorsement,
            signature_image=signature_image,
            letterhead_image=letterhead_image,
            include_barcode_with_order_number=include_barcode_with_order_number,
            receive_email_on_manifest_processing=receive_email_on_manifest_processing,
            use_carbon_neutral_shipping_program=use_carbon_neutral_shipping_program,
            use_ground_freight_pricing=use_ground_freight_pricing,
            use_consolidation_services=use_consolidation_services,
            use_order_number_on_mail_innovations_labels=use_order_number_on_mail_innovations_labels,
            mail_innovations_endorsement=mail_innovations_endorsement,
            mail_innovations_cost_center=mail_innovations_cost_center,
            use_negotiated_rates=use_negotiated_rates,
            account_postal_code=account_postal_code,
            invoice=invoice,
            email=email,
        )
        return self._update_settings_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateSettings(BaseApi):

    async def aupdate_settings(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmptyResponseBodyPydantic:
        raw_response = await self.raw.aupdate_settings(
            body=body,
            carrier_name=carrier_name,
            carrier_id=carrier_id,
            nickname=nickname,
            should_hide_account_number_on_archive_doc=should_hide_account_number_on_archive_doc,
            is_primary_account=is_primary_account,
            pickup_type=pickup_type,
            smart_post_hub=smart_post_hub,
            smart_post_endorsement=smart_post_endorsement,
            signature_image=signature_image,
            letterhead_image=letterhead_image,
            include_barcode_with_order_number=include_barcode_with_order_number,
            receive_email_on_manifest_processing=receive_email_on_manifest_processing,
            use_carbon_neutral_shipping_program=use_carbon_neutral_shipping_program,
            use_ground_freight_pricing=use_ground_freight_pricing,
            use_consolidation_services=use_consolidation_services,
            use_order_number_on_mail_innovations_labels=use_order_number_on_mail_innovations_labels,
            mail_innovations_endorsement=mail_innovations_endorsement,
            mail_innovations_cost_center=mail_innovations_cost_center,
            use_negotiated_rates=use_negotiated_rates,
            account_postal_code=account_postal_code,
            invoice=invoice,
            email=email,
            **kwargs,
        )
        if validate:
            return EmptyResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmptyResponseBodyPydantic, raw_response.body)
    
    
    def update_settings(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmptyResponseBodyPydantic:
        raw_response = self.raw.update_settings(
            body=body,
            carrier_name=carrier_name,
            carrier_id=carrier_id,
            nickname=nickname,
            should_hide_account_number_on_archive_doc=should_hide_account_number_on_archive_doc,
            is_primary_account=is_primary_account,
            pickup_type=pickup_type,
            smart_post_hub=smart_post_hub,
            smart_post_endorsement=smart_post_endorsement,
            signature_image=signature_image,
            letterhead_image=letterhead_image,
            include_barcode_with_order_number=include_barcode_with_order_number,
            receive_email_on_manifest_processing=receive_email_on_manifest_processing,
            use_carbon_neutral_shipping_program=use_carbon_neutral_shipping_program,
            use_ground_freight_pricing=use_ground_freight_pricing,
            use_consolidation_services=use_consolidation_services,
            use_order_number_on_mail_innovations_labels=use_order_number_on_mail_innovations_labels,
            mail_innovations_endorsement=mail_innovations_endorsement,
            mail_innovations_cost_center=mail_innovations_cost_center,
            use_negotiated_rates=use_negotiated_rates,
            account_postal_code=account_postal_code,
            invoice=invoice,
            email=email,
        )
        if validate:
            return EmptyResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmptyResponseBodyPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_settings_mapped_args(
            body=body,
            carrier_name=carrier_name,
            carrier_id=carrier_id,
            nickname=nickname,
            should_hide_account_number_on_archive_doc=should_hide_account_number_on_archive_doc,
            is_primary_account=is_primary_account,
            pickup_type=pickup_type,
            smart_post_hub=smart_post_hub,
            smart_post_endorsement=smart_post_endorsement,
            signature_image=signature_image,
            letterhead_image=letterhead_image,
            include_barcode_with_order_number=include_barcode_with_order_number,
            receive_email_on_manifest_processing=receive_email_on_manifest_processing,
            use_carbon_neutral_shipping_program=use_carbon_neutral_shipping_program,
            use_ground_freight_pricing=use_ground_freight_pricing,
            use_consolidation_services=use_consolidation_services,
            use_order_number_on_mail_innovations_labels=use_order_number_on_mail_innovations_labels,
            mail_innovations_endorsement=mail_innovations_endorsement,
            mail_innovations_cost_center=mail_innovations_cost_center,
            use_negotiated_rates=use_negotiated_rates,
            account_postal_code=account_postal_code,
            invoice=invoice,
            email=email,
        )
        return await self._aupdate_settings_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        carrier_name: CarrierNameWithSettings,
        carrier_id: SeId,
        body: typing.Optional[UpdateCarrierSettingsRequestBody] = None,
        nickname: typing.Optional[str] = None,
        should_hide_account_number_on_archive_doc: typing.Optional[bool] = None,
        is_primary_account: typing.Optional[bool] = None,
        pickup_type: typing.Optional[UpsPickupType] = None,
        smart_post_hub: typing.Optional[SmartPostHub] = None,
        smart_post_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        signature_image: typing.Optional[str] = None,
        letterhead_image: typing.Optional[str] = None,
        include_barcode_with_order_number: typing.Optional[bool] = None,
        receive_email_on_manifest_processing: typing.Optional[bool] = None,
        use_carbon_neutral_shipping_program: typing.Optional[bool] = None,
        use_ground_freight_pricing: typing.Optional[bool] = None,
        use_consolidation_services: typing.Optional[bool] = None,
        use_order_number_on_mail_innovations_labels: typing.Optional[bool] = None,
        mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        mail_innovations_cost_center: typing.Optional[str] = None,
        use_negotiated_rates: typing.Optional[bool] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        email: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_settings_mapped_args(
            body=body,
            carrier_name=carrier_name,
            carrier_id=carrier_id,
            nickname=nickname,
            should_hide_account_number_on_archive_doc=should_hide_account_number_on_archive_doc,
            is_primary_account=is_primary_account,
            pickup_type=pickup_type,
            smart_post_hub=smart_post_hub,
            smart_post_endorsement=smart_post_endorsement,
            signature_image=signature_image,
            letterhead_image=letterhead_image,
            include_barcode_with_order_number=include_barcode_with_order_number,
            receive_email_on_manifest_processing=receive_email_on_manifest_processing,
            use_carbon_neutral_shipping_program=use_carbon_neutral_shipping_program,
            use_ground_freight_pricing=use_ground_freight_pricing,
            use_consolidation_services=use_consolidation_services,
            use_order_number_on_mail_innovations_labels=use_order_number_on_mail_innovations_labels,
            mail_innovations_endorsement=mail_innovations_endorsement,
            mail_innovations_cost_center=mail_innovations_cost_center,
            use_negotiated_rates=use_negotiated_rates,
            account_postal_code=account_postal_code,
            invoice=invoice,
            email=email,
        )
        return self._update_settings_oapg(
            body=args.body,
            path_params=args.path,
        )

