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


class Pickup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The information necessary to schedule a package pickup

    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def pickup_id() -> typing.Type['PickupResourceId']:
                return PickupResourceId
            
            
            class label_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SeId']:
                        return SeId
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SeId'], typing.List['SeId']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'label_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SeId':
                    return super().__getitem__(i)
        
            @staticmethod
            def created_at() -> typing.Type['DateTime']:
                return DateTime
        
            @staticmethod
            def cancelled_at() -> typing.Type['DateTime']:
                return DateTime
        
            @staticmethod
            def carrier_id() -> typing.Type['SeId']:
                return SeId
            
            
            class confirmation_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'confirmation_number':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def warehouse_id() -> typing.Type['SeId']:
                return SeId
        
            @staticmethod
            def pickup_address() -> typing.Type['PartialAddress']:
                return PartialAddress
        
            @staticmethod
            def contact_details() -> typing.Type['ContactDetails']:
                return ContactDetails
            
            
            class pickup_notes(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def pickup_window() -> typing.Type['PickupWindow']:
                return PickupWindow
            
            
            class pickup_windows(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PickupWindows']:
                        return PickupWindows
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PickupWindows'], typing.List['PickupWindows']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pickup_windows':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PickupWindows':
                    return super().__getitem__(i)
            __annotations__ = {
                "pickup_id": pickup_id,
                "label_ids": label_ids,
                "created_at": created_at,
                "cancelled_at": cancelled_at,
                "carrier_id": carrier_id,
                "confirmation_number": confirmation_number,
                "warehouse_id": warehouse_id,
                "pickup_address": pickup_address,
                "contact_details": contact_details,
                "pickup_notes": pickup_notes,
                "pickup_window": pickup_window,
                "pickup_windows": pickup_windows,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pickup_id"]) -> 'PickupResourceId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label_ids"]) -> MetaOapg.properties.label_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> 'DateTime': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancelled_at"]) -> 'DateTime': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["carrier_id"]) -> 'SeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confirmation_number"]) -> MetaOapg.properties.confirmation_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warehouse_id"]) -> 'SeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pickup_address"]) -> 'PartialAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_details"]) -> 'ContactDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pickup_notes"]) -> MetaOapg.properties.pickup_notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pickup_window"]) -> 'PickupWindow': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pickup_windows"]) -> MetaOapg.properties.pickup_windows: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pickup_id", "label_ids", "created_at", "cancelled_at", "carrier_id", "confirmation_number", "warehouse_id", "pickup_address", "contact_details", "pickup_notes", "pickup_window", "pickup_windows", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pickup_id"]) -> typing.Union['PickupResourceId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label_ids"]) -> typing.Union[MetaOapg.properties.label_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union['DateTime', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancelled_at"]) -> typing.Union['DateTime', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["carrier_id"]) -> typing.Union['SeId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confirmation_number"]) -> typing.Union[MetaOapg.properties.confirmation_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warehouse_id"]) -> typing.Union['SeId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pickup_address"]) -> typing.Union['PartialAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_details"]) -> typing.Union['ContactDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pickup_notes"]) -> typing.Union[MetaOapg.properties.pickup_notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pickup_window"]) -> typing.Union['PickupWindow', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pickup_windows"]) -> typing.Union[MetaOapg.properties.pickup_windows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pickup_id", "label_ids", "created_at", "cancelled_at", "carrier_id", "confirmation_number", "warehouse_id", "pickup_address", "contact_details", "pickup_notes", "pickup_window", "pickup_windows", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pickup_id: typing.Union['PickupResourceId', schemas.Unset] = schemas.unset,
        label_ids: typing.Union[MetaOapg.properties.label_ids, list, tuple, schemas.Unset] = schemas.unset,
        created_at: typing.Union['DateTime', schemas.Unset] = schemas.unset,
        cancelled_at: typing.Union['DateTime', schemas.Unset] = schemas.unset,
        carrier_id: typing.Union['SeId', schemas.Unset] = schemas.unset,
        confirmation_number: typing.Union[MetaOapg.properties.confirmation_number, None, str, schemas.Unset] = schemas.unset,
        warehouse_id: typing.Union['SeId', schemas.Unset] = schemas.unset,
        pickup_address: typing.Union['PartialAddress', schemas.Unset] = schemas.unset,
        contact_details: typing.Union['ContactDetails', schemas.Unset] = schemas.unset,
        pickup_notes: typing.Union[MetaOapg.properties.pickup_notes, str, schemas.Unset] = schemas.unset,
        pickup_window: typing.Union['PickupWindow', schemas.Unset] = schemas.unset,
        pickup_windows: typing.Union[MetaOapg.properties.pickup_windows, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Pickup':
        return super().__new__(
            cls,
            *args,
            pickup_id=pickup_id,
            label_ids=label_ids,
            created_at=created_at,
            cancelled_at=cancelled_at,
            carrier_id=carrier_id,
            confirmation_number=confirmation_number,
            warehouse_id=warehouse_id,
            pickup_address=pickup_address,
            contact_details=contact_details,
            pickup_notes=pickup_notes,
            pickup_window=pickup_window,
            pickup_windows=pickup_windows,
            _configuration=_configuration,
            **kwargs,
        )

from ship_engine_python_sdk.model.contact_details import ContactDetails
from ship_engine_python_sdk.model.date_time import DateTime
from ship_engine_python_sdk.model.partial_address import PartialAddress
from ship_engine_python_sdk.model.pickup_resource_id import PickupResourceId
from ship_engine_python_sdk.model.pickup_window import PickupWindow
from ship_engine_python_sdk.model.pickup_windows import PickupWindows
from ship_engine_python_sdk.model.se_id import SeId
