# coding: utf-8

"""
    ShipEngine API

    ShipEngine's easy-to-use REST API lets you manage all of your shipping needs without worrying about the complexities of different carrier APIs and protocols. We handle all the heavy lifting so you can focus on providing a first-class shipping experience for your customers at the best possible prices.  Each of ShipEngine's features can be used by itself or in conjunction with each other to build powerful shipping functionality into your application or service.  ## Getting Started If you're new to REST APIs then be sure to read our [introduction to REST](https://www.shipengine.com/docs/rest/) to understand the basics.  Learn how to [authenticate yourself to ShipEngine](https://www.shipengine.com/docs/auth/), and then use our [sandbox environment](https://www.shipengine.com/docs/sandbox/) to kick the tires and get familiar with our API. If you run into any problems, then be sure to check the [error handling guide](https://www.shipengine.com/docs/errors/) for tips.  Here are some step-by-step **tutorials** to get you started:    - [Learn how to create your first shipping label](https://www.shipengine.com/docs/labels/create-a-label/)   - [Calculate shipping costs and compare rates across carriers](https://www.shipengine.com/docs/rates/)   - [Track packages on-demand or in real time](https://www.shipengine.com/docs/tracking/)   - [Validate mailing addresses anywhere on Earth](https://www.shipengine.com/docs/addresses/validation/)   ## Shipping Labels for Every Major Carrier ShipEngine makes it easy to [create shipping labels for any carrier](https://www.shipengine.com/docs/labels/create-a-label/) and [download them](https://www.shipengine.com/docs/labels/downloading/) in a [variety of file formats](https://www.shipengine.com/docs/labels/formats/). You can even customize labels with your own [messages](https://www.shipengine.com/docs/labels/messages/) and [images](https://www.shipengine.com/docs/labels/branding/).   ## Real-Time Package Tracking With ShipEngine you can [get the current status of a package](https://www.shipengine.com/docs/tracking/) or [subscribe to real-time tracking updates](https://www.shipengine.com/docs/tracking/webhooks/) via webhooks. You can also create [custimized tracking pages](https://www.shipengine.com/docs/tracking/branded-tracking-page/) with your own branding so your customers will always know where their package is.   ## Compare Shipping Costs Across Carriers Make sure you ship as cost-effectively as possible by [comparing rates across carriers](https://www.shipengine.com/docs/rates/get-shipment-rates/) using the ShipEngine Rates API. Or if you don't know the full shipment details yet, then you can [get rate estimates](https://www.shipengine.com/docs/rates/estimate/) with limited address info.   ## Worldwide Address Validation ShipEngine supports [address validation](https://www.shipengine.com/docs/addresses/validation/) for virtually [every country on Earth](https://www.shipengine.com/docs/addresses/validation/countries/), including the United States, Canada, Great Britain, Australia, Germany, France, Norway, Spain, Sweden, Israel, Italy, and over 160 others. 

    The version of the OpenAPI document: 1.1.202403202303
    Contact: sales@shipengine.com
    Created by: https://www.shipengine.com/contact/
"""

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


class Carrier(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A carrier object that represents a provider such as UPS, USPS, DHL, etc
that has been tied to the current account.

    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def carrier_id() -> typing.Type['SeId']:
                return SeId
        
            @staticmethod
            def carrier_code() -> typing.Type['CarrierCode']:
                return CarrierCode
            
            
            class account_number(
                schemas.StrSchema
            ):
                pass
            requires_funded_amount = schemas.BoolSchema
            
            
            class balance(
                schemas.Float64Schema
            ):
                pass
            
            
            class nickname(
                schemas.StrSchema
            ):
                pass
            
            
            class friendly_name(
                schemas.StrSchema
            ):
                pass
            primary = schemas.BoolSchema
            has_multi_package_supporting_services = schemas.BoolSchema
            supports_label_messages = schemas.BoolSchema
            disabled_by_billing_plan = schemas.BoolSchema
            
            
            class services(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Service']:
                        return Service
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Service'], typing.List['Service']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'services':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Service':
                    return super().__getitem__(i)
            
            
            class packages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PackageType']:
                        return PackageType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PackageType'], typing.List['PackageType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'packages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PackageType':
                    return super().__getitem__(i)
            
            
            class options(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CarrierAdvancedOption']:
                        return CarrierAdvancedOption
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CarrierAdvancedOption'], typing.List['CarrierAdvancedOption']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'options':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CarrierAdvancedOption':
                    return super().__getitem__(i)
            __annotations__ = {
                "carrier_id": carrier_id,
                "carrier_code": carrier_code,
                "account_number": account_number,
                "requires_funded_amount": requires_funded_amount,
                "balance": balance,
                "nickname": nickname,
                "friendly_name": friendly_name,
                "primary": primary,
                "has_multi_package_supporting_services": has_multi_package_supporting_services,
                "supports_label_messages": supports_label_messages,
                "disabled_by_billing_plan": disabled_by_billing_plan,
                "services": services,
                "packages": packages,
                "options": options,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["carrier_id"]) -> 'SeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["carrier_code"]) -> 'CarrierCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_number"]) -> MetaOapg.properties.account_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requires_funded_amount"]) -> MetaOapg.properties.requires_funded_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nickname"]) -> MetaOapg.properties.nickname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["friendly_name"]) -> MetaOapg.properties.friendly_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_multi_package_supporting_services"]) -> MetaOapg.properties.has_multi_package_supporting_services: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_label_messages"]) -> MetaOapg.properties.supports_label_messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disabled_by_billing_plan"]) -> MetaOapg.properties.disabled_by_billing_plan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["packages"]) -> MetaOapg.properties.packages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["carrier_id", "carrier_code", "account_number", "requires_funded_amount", "balance", "nickname", "friendly_name", "primary", "has_multi_package_supporting_services", "supports_label_messages", "disabled_by_billing_plan", "services", "packages", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["carrier_id"]) -> typing.Union['SeId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["carrier_code"]) -> typing.Union['CarrierCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_number"]) -> typing.Union[MetaOapg.properties.account_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requires_funded_amount"]) -> typing.Union[MetaOapg.properties.requires_funded_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nickname"]) -> typing.Union[MetaOapg.properties.nickname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["friendly_name"]) -> typing.Union[MetaOapg.properties.friendly_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary"]) -> typing.Union[MetaOapg.properties.primary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_multi_package_supporting_services"]) -> typing.Union[MetaOapg.properties.has_multi_package_supporting_services, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_label_messages"]) -> typing.Union[MetaOapg.properties.supports_label_messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disabled_by_billing_plan"]) -> typing.Union[MetaOapg.properties.disabled_by_billing_plan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["services"]) -> typing.Union[MetaOapg.properties.services, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["packages"]) -> typing.Union[MetaOapg.properties.packages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["carrier_id", "carrier_code", "account_number", "requires_funded_amount", "balance", "nickname", "friendly_name", "primary", "has_multi_package_supporting_services", "supports_label_messages", "disabled_by_billing_plan", "services", "packages", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        carrier_id: typing.Union['SeId', schemas.Unset] = schemas.unset,
        carrier_code: typing.Union['CarrierCode', schemas.Unset] = schemas.unset,
        account_number: typing.Union[MetaOapg.properties.account_number, str, schemas.Unset] = schemas.unset,
        requires_funded_amount: typing.Union[MetaOapg.properties.requires_funded_amount, bool, schemas.Unset] = schemas.unset,
        balance: typing.Union[MetaOapg.properties.balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        nickname: typing.Union[MetaOapg.properties.nickname, str, schemas.Unset] = schemas.unset,
        friendly_name: typing.Union[MetaOapg.properties.friendly_name, str, schemas.Unset] = schemas.unset,
        primary: typing.Union[MetaOapg.properties.primary, bool, schemas.Unset] = schemas.unset,
        has_multi_package_supporting_services: typing.Union[MetaOapg.properties.has_multi_package_supporting_services, bool, schemas.Unset] = schemas.unset,
        supports_label_messages: typing.Union[MetaOapg.properties.supports_label_messages, bool, schemas.Unset] = schemas.unset,
        disabled_by_billing_plan: typing.Union[MetaOapg.properties.disabled_by_billing_plan, bool, schemas.Unset] = schemas.unset,
        services: typing.Union[MetaOapg.properties.services, list, tuple, schemas.Unset] = schemas.unset,
        packages: typing.Union[MetaOapg.properties.packages, list, tuple, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Carrier':
        return super().__new__(
            cls,
            *args,
            carrier_id=carrier_id,
            carrier_code=carrier_code,
            account_number=account_number,
            requires_funded_amount=requires_funded_amount,
            balance=balance,
            nickname=nickname,
            friendly_name=friendly_name,
            primary=primary,
            has_multi_package_supporting_services=has_multi_package_supporting_services,
            supports_label_messages=supports_label_messages,
            disabled_by_billing_plan=disabled_by_billing_plan,
            services=services,
            packages=packages,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from ship_engine_python_sdk.model.carrier_advanced_option import CarrierAdvancedOption
from ship_engine_python_sdk.model.carrier_code import CarrierCode
from ship_engine_python_sdk.model.package_type import PackageType
from ship_engine_python_sdk.model.se_id import SeId
from ship_engine_python_sdk.model.service import Service
