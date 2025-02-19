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


class RateEstimateOptions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def from_country_code() -> typing.Type['CountryCode']:
                return CountryCode
        
            @staticmethod
            def from_postal_code() -> typing.Type['PostalCode']:
                return PostalCode
            
            
            class from_city_locality(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class from_state_province(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
        
            @staticmethod
            def to_country_code() -> typing.Type['CountryCode']:
                return CountryCode
        
            @staticmethod
            def to_postal_code() -> typing.Type['PostalCode']:
                return PostalCode
            
            
            class to_city_locality(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class to_state_province(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
        
            @staticmethod
            def weight() -> typing.Type['Weight']:
                return Weight
        
            @staticmethod
            def dimensions() -> typing.Type['Dimensions']:
                return Dimensions
        
            @staticmethod
            def confirmation() -> typing.Type['DeliveryConfirmation']:
                return DeliveryConfirmation
        
            @staticmethod
            def address_residential_indicator() -> typing.Type['AddressResidentialIndicator']:
                return AddressResidentialIndicator
        
            @staticmethod
            def ship_date() -> typing.Type['DateTime']:
                return DateTime
            __annotations__ = {
                "from_country_code": from_country_code,
                "from_postal_code": from_postal_code,
                "from_city_locality": from_city_locality,
                "from_state_province": from_state_province,
                "to_country_code": to_country_code,
                "to_postal_code": to_postal_code,
                "to_city_locality": to_city_locality,
                "to_state_province": to_state_province,
                "weight": weight,
                "dimensions": dimensions,
                "confirmation": confirmation,
                "address_residential_indicator": address_residential_indicator,
                "ship_date": ship_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_country_code"]) -> 'CountryCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_postal_code"]) -> 'PostalCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_city_locality"]) -> MetaOapg.properties.from_city_locality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_state_province"]) -> MetaOapg.properties.from_state_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_country_code"]) -> 'CountryCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_postal_code"]) -> 'PostalCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_city_locality"]) -> MetaOapg.properties.to_city_locality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_state_province"]) -> MetaOapg.properties.to_state_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weight"]) -> 'Weight': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dimensions"]) -> 'Dimensions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confirmation"]) -> 'DeliveryConfirmation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_residential_indicator"]) -> 'AddressResidentialIndicator': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ship_date"]) -> 'DateTime': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["from_country_code", "from_postal_code", "from_city_locality", "from_state_province", "to_country_code", "to_postal_code", "to_city_locality", "to_state_province", "weight", "dimensions", "confirmation", "address_residential_indicator", "ship_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_country_code"]) -> typing.Union['CountryCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_postal_code"]) -> typing.Union['PostalCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_city_locality"]) -> typing.Union[MetaOapg.properties.from_city_locality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_state_province"]) -> typing.Union[MetaOapg.properties.from_state_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_country_code"]) -> typing.Union['CountryCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_postal_code"]) -> typing.Union['PostalCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_city_locality"]) -> typing.Union[MetaOapg.properties.to_city_locality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_state_province"]) -> typing.Union[MetaOapg.properties.to_state_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weight"]) -> typing.Union['Weight', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dimensions"]) -> typing.Union['Dimensions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confirmation"]) -> typing.Union['DeliveryConfirmation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_residential_indicator"]) -> typing.Union['AddressResidentialIndicator', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ship_date"]) -> typing.Union['DateTime', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from_country_code", "from_postal_code", "from_city_locality", "from_state_province", "to_country_code", "to_postal_code", "to_city_locality", "to_state_province", "weight", "dimensions", "confirmation", "address_residential_indicator", "ship_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        from_country_code: typing.Union['CountryCode', schemas.Unset] = schemas.unset,
        from_postal_code: typing.Union['PostalCode', schemas.Unset] = schemas.unset,
        from_city_locality: typing.Union[MetaOapg.properties.from_city_locality, str, schemas.Unset] = schemas.unset,
        from_state_province: typing.Union[MetaOapg.properties.from_state_province, str, schemas.Unset] = schemas.unset,
        to_country_code: typing.Union['CountryCode', schemas.Unset] = schemas.unset,
        to_postal_code: typing.Union['PostalCode', schemas.Unset] = schemas.unset,
        to_city_locality: typing.Union[MetaOapg.properties.to_city_locality, str, schemas.Unset] = schemas.unset,
        to_state_province: typing.Union[MetaOapg.properties.to_state_province, str, schemas.Unset] = schemas.unset,
        weight: typing.Union['Weight', schemas.Unset] = schemas.unset,
        dimensions: typing.Union['Dimensions', schemas.Unset] = schemas.unset,
        confirmation: typing.Union['DeliveryConfirmation', schemas.Unset] = schemas.unset,
        address_residential_indicator: typing.Union['AddressResidentialIndicator', schemas.Unset] = schemas.unset,
        ship_date: typing.Union['DateTime', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RateEstimateOptions':
        return super().__new__(
            cls,
            *args,
            from_country_code=from_country_code,
            from_postal_code=from_postal_code,
            from_city_locality=from_city_locality,
            from_state_province=from_state_province,
            to_country_code=to_country_code,
            to_postal_code=to_postal_code,
            to_city_locality=to_city_locality,
            to_state_province=to_state_province,
            weight=weight,
            dimensions=dimensions,
            confirmation=confirmation,
            address_residential_indicator=address_residential_indicator,
            ship_date=ship_date,
            _configuration=_configuration,
            **kwargs,
        )

from ship_engine_python_sdk.model.address_residential_indicator import AddressResidentialIndicator
from ship_engine_python_sdk.model.country_code import CountryCode
from ship_engine_python_sdk.model.date_time import DateTime
from ship_engine_python_sdk.model.delivery_confirmation import DeliveryConfirmation
from ship_engine_python_sdk.model.dimensions import Dimensions
from ship_engine_python_sdk.model.postal_code import PostalCode
from ship_engine_python_sdk.model.weight import Weight
