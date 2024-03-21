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

from ship_engine_python_sdk.pydantic.country_code import CountryCode
from ship_engine_python_sdk.pydantic.date_time import DateTime
from ship_engine_python_sdk.pydantic.status_code import StatusCode

class TrackEvent(BaseModel):
    # Timestamp for carrier event
    occurred_at: DateTime = Field(alias='occurred_at')

    # City locality
    city_locality: str = Field(alias='city_locality')

    # State province
    state_province: str = Field(alias='state_province')

    # Postal code
    postal_code: str = Field(alias='postal_code')

    # Carrier detail code
    carrier_detail_code: str = Field(alias='carrier_detail_code')

    status_code: StatusCode = Field(alias='status_code')

    # Event Status Description
    status_description: str = Field(alias='status_description')

    # Carrier status code
    carrier_status_code: str = Field(alias='carrier_status_code')

    # carrier status description
    carrier_status_description: str = Field(alias='carrier_status_description')

    # Event description
    description: typing.Optional[str] = Field(None, alias='description')

    # Carrier timestamp for the event, it is assumed to be the local time of where the event occurred.
    carrier_occurred_at: typing.Optional[DateTime] = Field(None, alias='carrier_occurred_at')

    country_code: typing.Optional[CountryCode] = Field(None, alias='country_code')

    # Company Name
    company_name: typing.Optional[str] = Field(None, alias='company_name')

    # Signer information
    signer: typing.Optional[str] = Field(None, alias='signer')

    # Event Code
    event_code: typing.Optional[str] = Field(None, alias='event_code')

    # Latitude coordinate of tracking event.
    latitude: typing.Optional[typing.Union[int, float]] = Field(None, alias='latitude')

    # Longitude coordinate of tracking event.
    longitude: typing.Optional[typing.Union[int, float]] = Field(None, alias='longitude')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
