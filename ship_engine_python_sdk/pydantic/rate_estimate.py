# coding: utf-8

"""
    ShipEngine API

    ShipEngine's easy-to-use REST API lets you manage all of your shipping needs without worrying about the complexities of different carrier APIs and protocols. We handle all the heavy lifting so you can focus on providing a first-class shipping experience for your customers at the best possible prices.  Each of ShipEngine's features can be used by itself or in conjunction with each other to build powerful shipping functionality into your application or service.  ## Getting Started If you're new to REST APIs then be sure to read our [introduction to REST](https://www.shipengine.com/docs/rest/) to understand the basics.  Learn how to [authenticate yourself to ShipEngine](https://www.shipengine.com/docs/auth/), and then use our [sandbox environment](https://www.shipengine.com/docs/sandbox/) to kick the tires and get familiar with our API. If you run into any problems, then be sure to check the [error handling guide](https://www.shipengine.com/docs/errors/) for tips.  Here are some step-by-step **tutorials** to get you started:    - [Learn how to create your first shipping label](https://www.shipengine.com/docs/labels/create-a-label/)   - [Calculate shipping costs and compare rates across carriers](https://www.shipengine.com/docs/rates/)   - [Track packages on-demand or in real time](https://www.shipengine.com/docs/tracking/)   - [Validate mailing addresses anywhere on Earth](https://www.shipengine.com/docs/addresses/validation/)   ## Shipping Labels for Every Major Carrier ShipEngine makes it easy to [create shipping labels for any carrier](https://www.shipengine.com/docs/labels/create-a-label/) and [download them](https://www.shipengine.com/docs/labels/downloading/) in a [variety of file formats](https://www.shipengine.com/docs/labels/formats/). You can even customize labels with your own [messages](https://www.shipengine.com/docs/labels/messages/) and [images](https://www.shipengine.com/docs/labels/branding/).   ## Real-Time Package Tracking With ShipEngine you can [get the current status of a package](https://www.shipengine.com/docs/tracking/) or [subscribe to real-time tracking updates](https://www.shipengine.com/docs/tracking/webhooks/) via webhooks. You can also create [custimized tracking pages](https://www.shipengine.com/docs/tracking/branded-tracking-page/) with your own branding so your customers will always know where their package is.   ## Compare Shipping Costs Across Carriers Make sure you ship as cost-effectively as possible by [comparing rates across carriers](https://www.shipengine.com/docs/rates/get-shipment-rates/) using the ShipEngine Rates API. Or if you don't know the full shipment details yet, then you can [get rate estimates](https://www.shipengine.com/docs/rates/estimate/) with limited address info.   ## Worldwide Address Validation ShipEngine supports [address validation](https://www.shipengine.com/docs/addresses/validation/) for virtually [every country on Earth](https://www.shipengine.com/docs/addresses/validation/countries/), including the United States, Canada, Great Britain, Australia, Germany, France, Norway, Spain, Sweden, Israel, Italy, and over 160 others. 

    The version of the OpenAPI document: 1.1.202403202303
    Contact: sales@shipengine.com
    Created by: https://www.shipengine.com/contact/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from ship_engine_python_sdk.pydantic.date import Date
from ship_engine_python_sdk.pydantic.monetary_value import MonetaryValue
from ship_engine_python_sdk.pydantic.rate_estimate_error_messages import RateEstimateErrorMessages
from ship_engine_python_sdk.pydantic.rate_estimate_warning_messages import RateEstimateWarningMessages
from ship_engine_python_sdk.pydantic.rate_type import RateType
from ship_engine_python_sdk.pydantic.se_id import SeId
from ship_engine_python_sdk.pydantic.validation_status import ValidationStatus

class RateEstimate(BaseModel):
    rate_type: RateType = Field(alias='rate_type')

    # A string that uniquely identifies the carrier
    carrier_id: SeId = Field(alias='carrier_id')

    # The shipping amount
    shipping_amount: MonetaryValue = Field(alias='shipping_amount')

    # The insurance amount
    insurance_amount: MonetaryValue = Field(alias='insurance_amount')

    # The confirmation amount
    confirmation_amount: MonetaryValue = Field(alias='confirmation_amount')

    # Any other charges associated with this rate
    other_amount: MonetaryValue = Field(alias='other_amount')

    # Certain carriers base [their rates](https://blog.stamps.com/2017/09/08/usps-postal-zones/) off of custom zones that vary depending upon the ship_to and ship_from location 
    zone: typing.Optional[int] = Field(alias='zone')

    # package type that this rate was estimated for
    package_type: typing.Optional[str] = Field(alias='package_type')

    # Indicates if the rate is guaranteed.
    guaranteed_service: bool = Field(alias='guaranteed_service')

    # Indicates if the rates been negotiated
    negotiated_rate: bool = Field(alias='negotiated_rate')

    # service type
    service_type: str = Field(alias='service_type')

    # service code for the rate
    service_code: str = Field(alias='service_code')

    # Indicates if rate is trackable
    trackable: bool = Field(alias='trackable')

    # A [shipping carrier](https://www.shipengine.com/docs/carriers/setup/), such as `fedex`, `dhl_express`, `stamps_com`, etc.
    carrier_code: str = Field(alias='carrier_code')

    # carrier nickname
    carrier_nickname: str = Field(alias='carrier_nickname')

    # carrier friendly name
    carrier_friendly_name: str = Field(alias='carrier_friendly_name')

    validation_status: ValidationStatus = Field(alias='validation_status')

    warning_messages: RateEstimateWarningMessages = Field(alias='warning_messages')

    error_messages: RateEstimateErrorMessages = Field(alias='error_messages')

    # Tariff and additional taxes associated with an international shipment.
    tax_amount: typing.Optional[MonetaryValue] = Field(None, alias='tax_amount')

    # The number of days estimated for delivery, this will show the _actual_ delivery time if for example, the package gets shipped on a Friday 
    delivery_days: typing.Optional[int] = Field(None, alias='delivery_days')

    estimated_delivery_date: typing.Optional[Date] = Field(None, alias='estimated_delivery_date')

    # The carrier delivery days
    carrier_delivery_days: typing.Optional[str] = Field(None, alias='carrier_delivery_days')

    # ship date
    ship_date: typing.Optional[datetime] = Field(None, alias='ship_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
