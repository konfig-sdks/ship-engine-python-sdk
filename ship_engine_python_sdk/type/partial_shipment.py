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

from ship_engine_python_sdk.type.advanced_shipment_options import AdvancedShipmentOptions
from ship_engine_python_sdk.type.date import Date
from ship_engine_python_sdk.type.date_time import DateTime
from ship_engine_python_sdk.type.delivery_confirmation import DeliveryConfirmation
from ship_engine_python_sdk.type.insurance_provider import InsuranceProvider
from ship_engine_python_sdk.type.international_shipment_options_nullable import InternationalShipmentOptionsNullable
from ship_engine_python_sdk.type.order_source_name import OrderSourceName
from ship_engine_python_sdk.type.package import Package
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.se_id_nullable import SeIdNullable
from ship_engine_python_sdk.type.service_code import ServiceCode
from ship_engine_python_sdk.type.shipment_item import ShipmentItem
from ship_engine_python_sdk.type.shipment_status import ShipmentStatus
from ship_engine_python_sdk.type.shipping_address import ShippingAddress
from ship_engine_python_sdk.type.shipping_address_to import ShippingAddressTo
from ship_engine_python_sdk.type.tag import Tag
from ship_engine_python_sdk.type.tax_identifier import TaxIdentifier
from ship_engine_python_sdk.type.weight import Weight

class RequiredPartialShipment(TypedDict):
    pass

class OptionalPartialShipment(TypedDict, total=False):
    # Arbitrary tags associated with this shipment.  Tags can be used to categorize shipments, and shipments can be queried by their tags. 
    tags: typing.List[Tag]

    # A string that uniquely identifies the shipment
    shipment_id: SeId

    # The carrier account that is billed for the shipping charges
    carrier_id: SeId

    # The [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc. 
    service_code: ServiceCode

    # ID that the Order Source assigned
    external_order_id: typing.Optional[str]

    # Describe the packages included in this shipment as related to potential metadata that was imported from external order sources 
    items: typing.List[ShipmentItem]

    tax_identifiers: typing.Optional[typing.List[TaxIdentifier]]

    # A unique user-defined key to identify a shipment.  This can be used to retrieve the shipment.  > **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated. 
    external_shipment_id: typing.Optional[str]

    # A non-unique user-defined number used to identify a shipment.  If undefined, this will match the external_shipment_id of the shipment.  > **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated. 
    shipment_number: typing.Optional[str]

    # The date that the shipment was (or will be) shippped.  ShipEngine will take the day of week into consideration. For example, if the carrier does not operate on Sundays, then a package that would have shipped on Sunday will ship on Monday instead. 
    ship_date: Date

    # The date and time that the shipment was created in ShipEngine.
    created_at: DateTime

    # The date and time that the shipment was created or last modified.
    modified_at: DateTime

    # The current status of the shipment
    shipment_status: ShipmentStatus

    # The recipient's mailing address
    ship_to: ShippingAddressTo

    # The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse](https://www.shipengine.com/docs/reference/create-warehouse/).  Then you can simply specify the `warehouse_id` rather than the complete address each time. 
    ship_from: ShippingAddress

    # The [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/) that the shipment is being shipped from.  Either `warehouse_id` or `ship_from` must be specified. 
    warehouse_id: SeIdNullable

    # The return address for this shipment.  Defaults to the `ship_from` address. 
    return_to: ShippingAddress

    # An optional indicator if the shipment is intended to be a return. Defaults to false if not provided. 
    is_return: typing.Optional[bool]

    # The type of delivery confirmation that is required for this shipment.
    confirmation: DeliveryConfirmation

    # Customs information.  This is usually only needed for international shipments. 
    customs: typing.Optional[InternationalShipmentOptionsNullable]

    # Advanced shipment options.  These are entirely optional.
    advanced_options: AdvancedShipmentOptions

    # The insurance provider to use for any insured packages in the shipment. 
    insurance_provider: InsuranceProvider

    order_source_code: OrderSourceName

    # The packages in the shipment.  > **Note:** Some carriers only allow one package per shipment.  If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned. 
    packages: typing.List[Package]

    # The combined weight of all packages in the shipment
    total_weight: Weight

    # Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default.  Only supported for UPS and USPS.
    comparison_rate_type: typing.Optional[str]

class PartialShipment(RequiredPartialShipment, OptionalPartialShipment):
    pass
