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

from ship_engine_python_sdk.type.carrier_advanced_option import CarrierAdvancedOption
from ship_engine_python_sdk.type.carrier_code import CarrierCode
from ship_engine_python_sdk.type.package_type import PackageType
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.service import Service

class RequiredCarrier(TypedDict):
    pass

class OptionalCarrier(TypedDict, total=False):
    # A string that uniquely identifies the carrier.
    carrier_id: SeId

    # The [shipping carrier](https://www.shipengine.com/docs/carriers/setup/) who will ship the package, such as `fedex`, `dhl_express`, `stamps_com`, etc. 
    carrier_code: CarrierCode

    # The account number that the carrier is connected to.
    account_number: str

    # Indicates whether the carrier requires funding to use its services
    requires_funded_amount: bool

    # Current available balance
    balance: typing.Union[int, float]

    # Nickname given to the account when initially setting up the carrier.
    nickname: str

    # Screen readable name
    friendly_name: str

    # Is this the primary carrier that is used by default when no carrier is specified in label/shipment creation
    primary: bool

    # Carrier supports multiple packages per shipment
    has_multi_package_supporting_services: bool

    # The carrier supports adding custom label messages to an order.
    supports_label_messages: bool

    # The carrier is disabled by the current ShipEngine account's billing plan.
    disabled_by_billing_plan: bool

    # A list of services that are offered by the carrier
    services: typing.List[Service]

    # A list of package types that are supported by the carrier
    packages: typing.List[PackageType]

    # A list of options that are available to that carrier
    options: typing.List[CarrierAdvancedOption]

class Carrier(RequiredCarrier, OptionalCarrier):
    pass
