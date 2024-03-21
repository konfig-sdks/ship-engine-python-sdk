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

from ship_engine_python_sdk.pydantic.ancillary_service_endorsement import AncillaryServiceEndorsement
from ship_engine_python_sdk.pydantic.ups_invoice import UpsInvoice
from ship_engine_python_sdk.pydantic.ups_pickup_type import UpsPickupType

class UpsAccountSettings(BaseModel):
    # nickname
    nickname: typing.Optional[str] = Field(None, alias='nickname')

    # Indicates if this is the primary UPS account
    is_primary_account: typing.Optional[bool] = Field(None, alias='is_primary_account')

    pickup_type: typing.Optional[UpsPickupType] = Field(None, alias='pickup_type')

    # The use carbon neutral shipping program
    use_carbon_neutral_shipping_program: typing.Optional[bool] = Field(None, alias='use_carbon_neutral_shipping_program')

    # The use ground freight pricing
    use_ground_freight_pricing: typing.Optional[bool] = Field(None, alias='use_ground_freight_pricing')

    # The use consolidation services
    use_consolidation_services: typing.Optional[bool] = Field(None, alias='use_consolidation_services')

    # The use order number on mail innovations labels
    use_order_number_on_mail_innovations_labels: typing.Optional[bool] = Field(None, alias='use_order_number_on_mail_innovations_labels')

    mail_innovations_endorsement: typing.Optional[AncillaryServiceEndorsement] = Field(None, alias='mail_innovations_endorsement')

    # mail innovations cost center
    mail_innovations_cost_center: typing.Optional[str] = Field(None, alias='mail_innovations_cost_center')

    # The use negotiated rates
    use_negotiated_rates: typing.Optional[bool] = Field(None, alias='use_negotiated_rates')

    # account postal code
    account_postal_code: typing.Optional[str] = Field(None, alias='account_postal_code')

    # The invoice
    invoice: typing.Optional[UpsInvoice] = Field(None, alias='invoice')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
