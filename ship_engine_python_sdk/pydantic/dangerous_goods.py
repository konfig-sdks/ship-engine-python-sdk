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

from ship_engine_python_sdk.pydantic.dangerous_amount import DangerousAmount
from ship_engine_python_sdk.pydantic.packaging_group import PackagingGroup
from ship_engine_python_sdk.pydantic.packaging_instruction_section import PackagingInstructionSection
from ship_engine_python_sdk.pydantic.regulation_level import RegulationLevel
from ship_engine_python_sdk.pydantic.transport_mean import TransportMean

class DangerousGoods(BaseModel):
    # UN number to identify the dangerous goods.
    id_number: typing.Optional[typing.Optional[str]] = Field(None, alias='id_number')

    # Trade description of the dangerous goods.
    shipping_name: typing.Optional[typing.Optional[str]] = Field(None, alias='shipping_name')

    # Recognized Technical or chemical name of dangerous goods.
    technical_name: typing.Optional[typing.Optional[str]] = Field(None, alias='technical_name')

    # Dangerous goods product class based on regulation.
    product_class: typing.Optional[typing.Optional[str]] = Field(None, alias='product_class')

    # A secondary of product class for substances presenting more than one particular hazard
    product_class_subsidiary: typing.Optional[typing.Optional[str]] = Field(None, alias='product_class_subsidiary')

    packaging_group: typing.Optional[PackagingGroup] = Field(None, alias='packaging_group')

    # This model represents the amount of the dangerous goods.
    dangerous_amount: typing.Optional[DangerousAmount] = Field(None, alias='dangerous_amount')

    # Quantity of dangerous goods.
    quantity: typing.Optional[int] = Field(None, alias='quantity')

    # The specific standardized packaging instructions from the relevant regulatory agency that have been applied to the parcel/container.
    packaging_instruction: typing.Optional[typing.Optional[str]] = Field(None, alias='packaging_instruction')

    packaging_instruction_section: typing.Optional[PackagingInstructionSection] = Field(None, alias='packaging_instruction_section')

    # The type of exterior packaging used to contain the dangerous good.
    packaging_type: typing.Optional[typing.Optional[str]] = Field(None, alias='packaging_type')

    transport_mean: typing.Optional[TransportMean] = Field(None, alias='transport_mean')

    # Transport category assign to dangerous goods for the transport purpose.
    transport_category: typing.Optional[typing.Optional[str]] = Field(None, alias='transport_category')

    # Name of the regulatory authority.
    regulation_authority: typing.Optional[typing.Optional[str]] = Field(None, alias='regulation_authority')

    regulation_level: typing.Optional[RegulationLevel] = Field(None, alias='regulation_level')

    # Indication if the substance is radioactive.
    radioactive: typing.Optional[typing.Optional[bool]] = Field(None, alias='radioactive')

    # Indication if the substance needs to be reported to regulatory authority based on the quantity.
    reportable_quantity: typing.Optional[typing.Optional[bool]] = Field(None, alias='reportable_quantity')

    # Defines which types of tunnels the shipment is allowed to go through
    tunnel_code: typing.Optional[typing.Optional[str]] = Field(None, alias='tunnel_code')

    # Provider additonal description regarding the dangerous goods. This is used as a placed holder to provider additional context and varies by carrier
    additional_description: typing.Optional[typing.Optional[str]] = Field(None, alias='additional_description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
