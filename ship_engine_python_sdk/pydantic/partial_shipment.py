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

from ship_engine_python_sdk.pydantic.advanced_shipment_options import AdvancedShipmentOptions
from ship_engine_python_sdk.pydantic.date import Date
from ship_engine_python_sdk.pydantic.date_time import DateTime
from ship_engine_python_sdk.pydantic.delivery_confirmation import DeliveryConfirmation
from ship_engine_python_sdk.pydantic.insurance_provider import InsuranceProvider
from ship_engine_python_sdk.pydantic.international_shipment_options_nullable import InternationalShipmentOptionsNullable
from ship_engine_python_sdk.pydantic.order_source_name import OrderSourceName
from ship_engine_python_sdk.pydantic.package import Package
from ship_engine_python_sdk.pydantic.se_id import SeId
from ship_engine_python_sdk.pydantic.se_id_nullable import SeIdNullable
from ship_engine_python_sdk.pydantic.service_code import ServiceCode
from ship_engine_python_sdk.pydantic.shipment_item import ShipmentItem
from ship_engine_python_sdk.pydantic.shipment_status import ShipmentStatus
from ship_engine_python_sdk.pydantic.shipping_address import ShippingAddress
from ship_engine_python_sdk.pydantic.shipping_address_to import ShippingAddressTo
from ship_engine_python_sdk.pydantic.tag import Tag
from ship_engine_python_sdk.pydantic.tax_identifier import TaxIdentifier
from ship_engine_python_sdk.pydantic.weight import Weight

class PartialShipment(BaseModel):
    # Arbitrary tags associated with this shipment.  Tags can be used to categorize shipments, and shipments can be queried by their tags. 
    tags: typing.Optional[typing.List[Tag]] = Field(None, alias='tags')

    # A string that uniquely identifies the shipment
    shipment_id: typing.Optional[SeId] = Field(None, alias='shipment_id')

    # The carrier account that is billed for the shipping charges
    carrier_id: typing.Optional[SeId] = Field(None, alias='carrier_id')

    # The [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc. 
    service_code: typing.Optional[ServiceCode] = Field(None, alias='service_code')

    # ID that the Order Source assigned
    external_order_id: typing.Optional[typing.Optional[str]] = Field(None, alias='external_order_id')

    # Describe the packages included in this shipment as related to potential metadata that was imported from external order sources 
    items: typing.Optional[typing.List[ShipmentItem]] = Field(None, alias='items')

    tax_identifiers: typing.Optional[typing.Optional[typing.List[TaxIdentifier]]] = Field(None, alias='tax_identifiers')

    # A unique user-defined key to identify a shipment.  This can be used to retrieve the shipment.  > **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated. 
    external_shipment_id: typing.Optional[typing.Optional[str]] = Field(None, alias='external_shipment_id')

    # A non-unique user-defined number used to identify a shipment.  If undefined, this will match the external_shipment_id of the shipment.  > **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated. 
    shipment_number: typing.Optional[typing.Optional[str]] = Field(None, alias='shipment_number')

    # The date that the shipment was (or will be) shippped.  ShipEngine will take the day of week into consideration. For example, if the carrier does not operate on Sundays, then a package that would have shipped on Sunday will ship on Monday instead. 
    ship_date: typing.Optional[Date] = Field(None, alias='ship_date')

    # The date and time that the shipment was created in ShipEngine.
    created_at: typing.Optional[DateTime] = Field(None, alias='created_at')

    # The date and time that the shipment was created or last modified.
    modified_at: typing.Optional[DateTime] = Field(None, alias='modified_at')

    # The current status of the shipment
    shipment_status: typing.Optional[ShipmentStatus] = Field(None, alias='shipment_status')

    # The recipient's mailing address
    ship_to: typing.Optional[ShippingAddressTo] = Field(None, alias='ship_to')

    # The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse](https://www.shipengine.com/docs/reference/create-warehouse/).  Then you can simply specify the `warehouse_id` rather than the complete address each time. 
    ship_from: typing.Optional[ShippingAddress] = Field(None, alias='ship_from')

    # The [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/) that the shipment is being shipped from.  Either `warehouse_id` or `ship_from` must be specified. 
    warehouse_id: typing.Optional[SeIdNullable] = Field(None, alias='warehouse_id')

    # The return address for this shipment.  Defaults to the `ship_from` address. 
    return_to: typing.Optional[ShippingAddress] = Field(None, alias='return_to')

    # An optional indicator if the shipment is intended to be a return. Defaults to false if not provided. 
    is_return: typing.Optional[typing.Optional[bool]] = Field(None, alias='is_return')

    # The type of delivery confirmation that is required for this shipment.
    confirmation: typing.Optional[DeliveryConfirmation] = Field(None, alias='confirmation')

    # Customs information.  This is usually only needed for international shipments. 
    customs: typing.Optional[InternationalShipmentOptionsNullable] = Field(None, alias='customs')

    # Advanced shipment options.  These are entirely optional.
    advanced_options: typing.Optional[AdvancedShipmentOptions] = Field(None, alias='advanced_options')

    # The insurance provider to use for any insured packages in the shipment. 
    insurance_provider: typing.Optional[InsuranceProvider] = Field(None, alias='insurance_provider')

    order_source_code: typing.Optional[OrderSourceName] = Field(None, alias='order_source_code')

    # The packages in the shipment.  > **Note:** Some carriers only allow one package per shipment.  If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned. 
    packages: typing.Optional[typing.List[Package]] = Field(None, alias='packages')

    # The combined weight of all packages in the shipment
    total_weight: typing.Optional[Weight] = Field(None, alias='total_weight')

    # Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default.  Only supported for UPS and USPS.
    comparison_rate_type: typing.Optional[typing.Optional[str]] = Field(None, alias='comparison_rate_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
