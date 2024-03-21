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
from ship_engine_python_sdk.model.connect_carrier_request_body import ConnectCarrierRequestBody as ConnectCarrierRequestBodySchema
from ship_engine_python_sdk.model.email import Email as EmailSchema
from ship_engine_python_sdk.model.se_id import SeId as SeIdSchema
from ship_engine_python_sdk.model.ups_invoice import UpsInvoice as UpsInvoiceSchema
from ship_engine_python_sdk.model.connect_carrier_response_body import ConnectCarrierResponseBody as ConnectCarrierResponseBodySchema
from ship_engine_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema
from ship_engine_python_sdk.model.carrier_name import CarrierName as CarrierNameSchema

from ship_engine_python_sdk.type.connect_carrier_request_body import ConnectCarrierRequestBody
from ship_engine_python_sdk.type.connect_carrier_response_body import ConnectCarrierResponseBody
from ship_engine_python_sdk.type.ancillary_service_endorsement import AncillaryServiceEndorsement
from ship_engine_python_sdk.type.carrier_name import CarrierName
from ship_engine_python_sdk.type.error_response_body import ErrorResponseBody
from ship_engine_python_sdk.type.email import Email
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.ups_invoice import UpsInvoice

from ...api_client import Dictionary
from ship_engine_python_sdk.pydantic.se_id import SeId as SeIdPydantic
from ship_engine_python_sdk.pydantic.ups_invoice import UpsInvoice as UpsInvoicePydantic
from ship_engine_python_sdk.pydantic.email import Email as EmailPydantic
from ship_engine_python_sdk.pydantic.ancillary_service_endorsement import AncillaryServiceEndorsement as AncillaryServiceEndorsementPydantic
from ship_engine_python_sdk.pydantic.connect_carrier_request_body import ConnectCarrierRequestBody as ConnectCarrierRequestBodyPydantic
from ship_engine_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from ship_engine_python_sdk.pydantic.carrier_name import CarrierName as CarrierNamePydantic
from ship_engine_python_sdk.pydantic.connect_carrier_response_body import ConnectCarrierResponseBody as ConnectCarrierResponseBodyPydantic

from . import path

# Path params
CarrierNameSchema = CarrierNameSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'carrier_name': typing.Union[CarrierNameSchema, ],
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
    schema=CarrierNameSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ConnectCarrierRequestBodySchema


request_body_connect_carrier_request_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = ConnectCarrierResponseBodySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConnectCarrierResponseBody


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConnectCarrierResponseBody


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

    def _carrier_mapped_args(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if nickname is not None:
            _body["nickname"] = nickname
        if username is not None:
            _body["username"] = username
        if password is not None:
            _body["password"] = password
        if merchant_seller_id is not None:
            _body["merchant_seller_id"] = merchant_seller_id
        if mws_auth_token is not None:
            _body["mws_auth_token"] = mws_auth_token
        if email is not None:
            _body["email"] = email
        if auth_code is not None:
            _body["auth_code"] = auth_code
        if account_number is not None:
            _body["account_number"] = account_number
        if ftp_username is not None:
            _body["ftp_username"] = ftp_username
        if ftp_password is not None:
            _body["ftp_password"] = ftp_password
        if api_key is not None:
            _body["api_key"] = api_key
        if api_secret is not None:
            _body["api_secret"] = api_secret
        if contract_id is not None:
            _body["contract_id"] = contract_id
        if client_id is not None:
            _body["client_id"] = client_id
        if pickup_number is not None:
            _body["pickup_number"] = pickup_number
        if distribution_center is not None:
            _body["distribution_center"] = distribution_center
        if ancillary_endorsement is not None:
            _body["ancillary_endorsement"] = ancillary_endorsement
        if sold_to is not None:
            _body["sold_to"] = sold_to
        if registration_id is not None:
            _body["registration_id"] = registration_id
        if software_name is not None:
            _body["software_name"] = software_name
        if site_id is not None:
            _body["site_id"] = site_id
        if country_code is not None:
            _body["country_code"] = country_code
        if account is not None:
            _body["account"] = account
        if passphrase is not None:
            _body["passphrase"] = passphrase
        if address1 is not None:
            _body["address1"] = address1
        if address2 is not None:
            _body["address2"] = address2
        if city is not None:
            _body["city"] = city
        if company is not None:
            _body["company"] = company
        if first_name is not None:
            _body["first_name"] = first_name
        if last_name is not None:
            _body["last_name"] = last_name
        if phone is not None:
            _body["phone"] = phone
        if postal_code is not None:
            _body["postal_code"] = postal_code
        if state is not None:
            _body["state"] = state
        if agree_to_eula is not None:
            _body["agree_to_eula"] = agree_to_eula
        if meter_number is not None:
            _body["meter_number"] = meter_number
        if mailer_id is not None:
            _body["mailer_id"] = mailer_id
        if profile_name is not None:
            _body["profile_name"] = profile_name
        if merchant_id is not None:
            _body["merchant_id"] = merchant_id
        if induction_site is not None:
            _body["induction_site"] = induction_site
        if activation_key is not None:
            _body["activation_key"] = activation_key
        if oba_email is not None:
            _body["oba_email"] = oba_email
        if contact_name is not None:
            _body["contact_name"] = contact_name
        if company_name is not None:
            _body["company_name"] = company_name
        if street_line1 is not None:
            _body["street_line1"] = street_line1
        if street_line2 is not None:
            _body["street_line2"] = street_line2
        if street_line3 is not None:
            _body["street_line3"] = street_line3
        if access_key is not None:
            _body["access_key"] = access_key
        if sendle_id is not None:
            _body["sendle_id"] = sendle_id
        if title is not None:
            _body["title"] = title
        if account_country_code is not None:
            _body["account_country_code"] = account_country_code
        if account_postal_code is not None:
            _body["account_postal_code"] = account_postal_code
        if invoice is not None:
            _body["invoice"] = invoice
        if invoice_amount is not None:
            _body["invoice_amount"] = invoice_amount
        if invoice_currency_code is not None:
            _body["invoice_currency_code"] = invoice_currency_code
        if agree_to_technology_agreement is not None:
            _body["agree_to_technology_agreement"] = agree_to_technology_agreement
        args.body = body if body is not None else _body
        if carrier_name is not None:
            _path_params["carrier_name"] = carrier_name
        args.path = _path_params
        return args

    async def _acarrier_oapg(
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
        Connect a carrier account
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_carrier_name,
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
            path_template='/v1/connections/carriers/{carrier_name}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_connect_carrier_request_body.serialize(body, content_type)
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


    def _carrier_oapg(
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
        Connect a carrier account
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_carrier_name,
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
            path_template='/v1/connections/carriers/{carrier_name}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_connect_carrier_request_body.serialize(body, content_type)
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


class CarrierRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acarrier(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._carrier_mapped_args(
            body=body,
            carrier_name=carrier_name,
            nickname=nickname,
            username=username,
            password=password,
            merchant_seller_id=merchant_seller_id,
            mws_auth_token=mws_auth_token,
            email=email,
            auth_code=auth_code,
            account_number=account_number,
            ftp_username=ftp_username,
            ftp_password=ftp_password,
            api_key=api_key,
            api_secret=api_secret,
            contract_id=contract_id,
            client_id=client_id,
            pickup_number=pickup_number,
            distribution_center=distribution_center,
            ancillary_endorsement=ancillary_endorsement,
            sold_to=sold_to,
            registration_id=registration_id,
            software_name=software_name,
            site_id=site_id,
            country_code=country_code,
            account=account,
            passphrase=passphrase,
            address1=address1,
            address2=address2,
            city=city,
            company=company,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            agree_to_eula=agree_to_eula,
            meter_number=meter_number,
            mailer_id=mailer_id,
            profile_name=profile_name,
            merchant_id=merchant_id,
            induction_site=induction_site,
            activation_key=activation_key,
            oba_email=oba_email,
            contact_name=contact_name,
            company_name=company_name,
            street_line1=street_line1,
            street_line2=street_line2,
            street_line3=street_line3,
            access_key=access_key,
            sendle_id=sendle_id,
            title=title,
            account_country_code=account_country_code,
            account_postal_code=account_postal_code,
            invoice=invoice,
            invoice_amount=invoice_amount,
            invoice_currency_code=invoice_currency_code,
            agree_to_technology_agreement=agree_to_technology_agreement,
        )
        return await self._acarrier_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def carrier(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._carrier_mapped_args(
            body=body,
            carrier_name=carrier_name,
            nickname=nickname,
            username=username,
            password=password,
            merchant_seller_id=merchant_seller_id,
            mws_auth_token=mws_auth_token,
            email=email,
            auth_code=auth_code,
            account_number=account_number,
            ftp_username=ftp_username,
            ftp_password=ftp_password,
            api_key=api_key,
            api_secret=api_secret,
            contract_id=contract_id,
            client_id=client_id,
            pickup_number=pickup_number,
            distribution_center=distribution_center,
            ancillary_endorsement=ancillary_endorsement,
            sold_to=sold_to,
            registration_id=registration_id,
            software_name=software_name,
            site_id=site_id,
            country_code=country_code,
            account=account,
            passphrase=passphrase,
            address1=address1,
            address2=address2,
            city=city,
            company=company,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            agree_to_eula=agree_to_eula,
            meter_number=meter_number,
            mailer_id=mailer_id,
            profile_name=profile_name,
            merchant_id=merchant_id,
            induction_site=induction_site,
            activation_key=activation_key,
            oba_email=oba_email,
            contact_name=contact_name,
            company_name=company_name,
            street_line1=street_line1,
            street_line2=street_line2,
            street_line3=street_line3,
            access_key=access_key,
            sendle_id=sendle_id,
            title=title,
            account_country_code=account_country_code,
            account_postal_code=account_postal_code,
            invoice=invoice,
            invoice_amount=invoice_amount,
            invoice_currency_code=invoice_currency_code,
            agree_to_technology_agreement=agree_to_technology_agreement,
        )
        return self._carrier_oapg(
            body=args.body,
            path_params=args.path,
        )

class Carrier(BaseApi):

    async def acarrier(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConnectCarrierResponseBodyPydantic:
        raw_response = await self.raw.acarrier(
            body=body,
            carrier_name=carrier_name,
            nickname=nickname,
            username=username,
            password=password,
            merchant_seller_id=merchant_seller_id,
            mws_auth_token=mws_auth_token,
            email=email,
            auth_code=auth_code,
            account_number=account_number,
            ftp_username=ftp_username,
            ftp_password=ftp_password,
            api_key=api_key,
            api_secret=api_secret,
            contract_id=contract_id,
            client_id=client_id,
            pickup_number=pickup_number,
            distribution_center=distribution_center,
            ancillary_endorsement=ancillary_endorsement,
            sold_to=sold_to,
            registration_id=registration_id,
            software_name=software_name,
            site_id=site_id,
            country_code=country_code,
            account=account,
            passphrase=passphrase,
            address1=address1,
            address2=address2,
            city=city,
            company=company,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            agree_to_eula=agree_to_eula,
            meter_number=meter_number,
            mailer_id=mailer_id,
            profile_name=profile_name,
            merchant_id=merchant_id,
            induction_site=induction_site,
            activation_key=activation_key,
            oba_email=oba_email,
            contact_name=contact_name,
            company_name=company_name,
            street_line1=street_line1,
            street_line2=street_line2,
            street_line3=street_line3,
            access_key=access_key,
            sendle_id=sendle_id,
            title=title,
            account_country_code=account_country_code,
            account_postal_code=account_postal_code,
            invoice=invoice,
            invoice_amount=invoice_amount,
            invoice_currency_code=invoice_currency_code,
            agree_to_technology_agreement=agree_to_technology_agreement,
            **kwargs,
        )
        if validate:
            return ConnectCarrierResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConnectCarrierResponseBodyPydantic, raw_response.body)
    
    
    def carrier(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ConnectCarrierResponseBodyPydantic:
        raw_response = self.raw.carrier(
            body=body,
            carrier_name=carrier_name,
            nickname=nickname,
            username=username,
            password=password,
            merchant_seller_id=merchant_seller_id,
            mws_auth_token=mws_auth_token,
            email=email,
            auth_code=auth_code,
            account_number=account_number,
            ftp_username=ftp_username,
            ftp_password=ftp_password,
            api_key=api_key,
            api_secret=api_secret,
            contract_id=contract_id,
            client_id=client_id,
            pickup_number=pickup_number,
            distribution_center=distribution_center,
            ancillary_endorsement=ancillary_endorsement,
            sold_to=sold_to,
            registration_id=registration_id,
            software_name=software_name,
            site_id=site_id,
            country_code=country_code,
            account=account,
            passphrase=passphrase,
            address1=address1,
            address2=address2,
            city=city,
            company=company,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            agree_to_eula=agree_to_eula,
            meter_number=meter_number,
            mailer_id=mailer_id,
            profile_name=profile_name,
            merchant_id=merchant_id,
            induction_site=induction_site,
            activation_key=activation_key,
            oba_email=oba_email,
            contact_name=contact_name,
            company_name=company_name,
            street_line1=street_line1,
            street_line2=street_line2,
            street_line3=street_line3,
            access_key=access_key,
            sendle_id=sendle_id,
            title=title,
            account_country_code=account_country_code,
            account_postal_code=account_postal_code,
            invoice=invoice,
            invoice_amount=invoice_amount,
            invoice_currency_code=invoice_currency_code,
            agree_to_technology_agreement=agree_to_technology_agreement,
        )
        if validate:
            return ConnectCarrierResponseBodyPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConnectCarrierResponseBodyPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._carrier_mapped_args(
            body=body,
            carrier_name=carrier_name,
            nickname=nickname,
            username=username,
            password=password,
            merchant_seller_id=merchant_seller_id,
            mws_auth_token=mws_auth_token,
            email=email,
            auth_code=auth_code,
            account_number=account_number,
            ftp_username=ftp_username,
            ftp_password=ftp_password,
            api_key=api_key,
            api_secret=api_secret,
            contract_id=contract_id,
            client_id=client_id,
            pickup_number=pickup_number,
            distribution_center=distribution_center,
            ancillary_endorsement=ancillary_endorsement,
            sold_to=sold_to,
            registration_id=registration_id,
            software_name=software_name,
            site_id=site_id,
            country_code=country_code,
            account=account,
            passphrase=passphrase,
            address1=address1,
            address2=address2,
            city=city,
            company=company,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            agree_to_eula=agree_to_eula,
            meter_number=meter_number,
            mailer_id=mailer_id,
            profile_name=profile_name,
            merchant_id=merchant_id,
            induction_site=induction_site,
            activation_key=activation_key,
            oba_email=oba_email,
            contact_name=contact_name,
            company_name=company_name,
            street_line1=street_line1,
            street_line2=street_line2,
            street_line3=street_line3,
            access_key=access_key,
            sendle_id=sendle_id,
            title=title,
            account_country_code=account_country_code,
            account_postal_code=account_postal_code,
            invoice=invoice,
            invoice_amount=invoice_amount,
            invoice_currency_code=invoice_currency_code,
            agree_to_technology_agreement=agree_to_technology_agreement,
        )
        return await self._acarrier_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        carrier_name: CarrierName,
        body: typing.Optional[ConnectCarrierRequestBody] = None,
        nickname: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        merchant_seller_id: typing.Optional[str] = None,
        mws_auth_token: typing.Optional[str] = None,
        email: typing.Optional[Email] = None,
        auth_code: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        ftp_username: typing.Optional[str] = None,
        ftp_password: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        pickup_number: typing.Optional[str] = None,
        distribution_center: typing.Optional[str] = None,
        ancillary_endorsement: typing.Optional[AncillaryServiceEndorsement] = None,
        sold_to: typing.Optional[str] = None,
        registration_id: typing.Optional[str] = None,
        software_name: typing.Optional[str] = None,
        site_id: typing.Optional[SeId] = None,
        country_code: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        passphrase: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        agree_to_eula: typing.Optional[bool] = None,
        meter_number: typing.Optional[str] = None,
        mailer_id: typing.Optional[int] = None,
        profile_name: typing.Optional[str] = None,
        merchant_id: typing.Optional[int] = None,
        induction_site: typing.Optional[str] = None,
        activation_key: typing.Optional[str] = None,
        oba_email: typing.Optional[Email] = None,
        contact_name: typing.Optional[str] = None,
        company_name: typing.Optional[str] = None,
        street_line1: typing.Optional[str] = None,
        street_line2: typing.Optional[str] = None,
        street_line3: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        sendle_id: typing.Optional[SeId] = None,
        title: typing.Optional[str] = None,
        account_country_code: typing.Optional[str] = None,
        account_postal_code: typing.Optional[str] = None,
        invoice: typing.Optional[UpsInvoice] = None,
        invoice_amount: typing.Optional[typing.Union[int, float]] = None,
        invoice_currency_code: typing.Optional[str] = None,
        agree_to_technology_agreement: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._carrier_mapped_args(
            body=body,
            carrier_name=carrier_name,
            nickname=nickname,
            username=username,
            password=password,
            merchant_seller_id=merchant_seller_id,
            mws_auth_token=mws_auth_token,
            email=email,
            auth_code=auth_code,
            account_number=account_number,
            ftp_username=ftp_username,
            ftp_password=ftp_password,
            api_key=api_key,
            api_secret=api_secret,
            contract_id=contract_id,
            client_id=client_id,
            pickup_number=pickup_number,
            distribution_center=distribution_center,
            ancillary_endorsement=ancillary_endorsement,
            sold_to=sold_to,
            registration_id=registration_id,
            software_name=software_name,
            site_id=site_id,
            country_code=country_code,
            account=account,
            passphrase=passphrase,
            address1=address1,
            address2=address2,
            city=city,
            company=company,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            agree_to_eula=agree_to_eula,
            meter_number=meter_number,
            mailer_id=mailer_id,
            profile_name=profile_name,
            merchant_id=merchant_id,
            induction_site=induction_site,
            activation_key=activation_key,
            oba_email=oba_email,
            contact_name=contact_name,
            company_name=company_name,
            street_line1=street_line1,
            street_line2=street_line2,
            street_line3=street_line3,
            access_key=access_key,
            sendle_id=sendle_id,
            title=title,
            account_country_code=account_country_code,
            account_postal_code=account_postal_code,
            invoice=invoice,
            invoice_amount=invoice_amount,
            invoice_currency_code=invoice_currency_code,
            agree_to_technology_agreement=agree_to_technology_agreement,
        )
        return self._carrier_oapg(
            body=args.body,
            path_params=args.path,
        )

