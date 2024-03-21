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

from ship_engine_python_sdk.pydantic.contact_details import ContactDetails
from ship_engine_python_sdk.pydantic.date_time import DateTime
from ship_engine_python_sdk.pydantic.partial_address import PartialAddress
from ship_engine_python_sdk.pydantic.pickup_resource_id import PickupResourceId
from ship_engine_python_sdk.pydantic.pickup_window import PickupWindow
from ship_engine_python_sdk.pydantic.pickup_windows import PickupWindows
from ship_engine_python_sdk.pydantic.se_id import SeId

class Pickup(BaseModel):
    pickup_id: typing.Optional[PickupResourceId] = Field(None, alias='pickup_id')

    # Label IDs that will be included in the pickup request
    label_ids: typing.Optional[typing.List[SeId]] = Field(None, alias='label_ids')

    # The date and time that the pickup was created in ShipEngine.
    created_at: typing.Optional[DateTime] = Field(None, alias='created_at')

    # The date and time that the pickup was cancelled in ShipEngine.
    cancelled_at: typing.Optional[DateTime] = Field(None, alias='cancelled_at')

    # The carrier_id associated with the pickup
    carrier_id: typing.Optional[SeId] = Field(None, alias='carrier_id')

    # The carrier confirmation number for the scheduled pickup.
    confirmation_number: typing.Optional[typing.Optional[str]] = Field(None, alias='confirmation_number')

    # The warehouse_id associated with the pickup
    warehouse_id: typing.Optional[SeId] = Field(None, alias='warehouse_id')

    pickup_address: typing.Optional[PartialAddress] = Field(None, alias='pickup_address')

    contact_details: typing.Optional[ContactDetails] = Field(None, alias='contact_details')

    # Used by some carriers to give special instructions for a package pickup
    pickup_notes: typing.Optional[str] = Field(None, alias='pickup_notes')

    pickup_window: typing.Optional[PickupWindow] = Field(None, alias='pickup_window')

    # An array of available pickup windows. Carriers can return multiple times that they will pickup packages. 
    pickup_windows: typing.Optional[typing.List[PickupWindows]] = Field(None, alias='pickup_windows')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
