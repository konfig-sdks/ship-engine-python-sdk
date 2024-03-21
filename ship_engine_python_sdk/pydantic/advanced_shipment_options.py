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

from ship_engine_python_sdk.pydantic.advanced_shipment_options_dangerous_goods_contact import AdvancedShipmentOptionsDangerousGoodsContact
from ship_engine_python_sdk.pydantic.advanced_shipment_options_fedex_freight import AdvancedShipmentOptionsFedexFreight
from ship_engine_python_sdk.pydantic.bill_to_party_nullable import BillToPartyNullable
from ship_engine_python_sdk.pydantic.collect_on_delivery import CollectOnDelivery
from ship_engine_python_sdk.pydantic.country_code import CountryCode
from ship_engine_python_sdk.pydantic.origin_type_nullable import OriginTypeNullable
from ship_engine_python_sdk.pydantic.weight_nullable import WeightNullable

class AdvancedShipmentOptions(BaseModel):
    # This field is used to [bill shipping costs to a third party](https://www.shipengine.com/docs/shipping/bill-to-third-party/).  This field must be used in conjunction with the `bill_to_country_code`, `bill_to_party`, and `bill_to_postal_code` fields. 
    bill_to_account: typing.Optional[typing.Optional[str]] = Field(None, alias='bill_to_account')

    # The two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the third-party that is responsible for shipping costs. 
    bill_to_country_code: typing.Optional[CountryCode] = Field(None, alias='bill_to_country_code')

    # Indicates whether to bill shipping costs to the recipient or to a third-party.  When billing to a third-party, the `bill_to_account`, `bill_to_country_code`, and `bill_to_postal_code` fields must also be set. 
    bill_to_party: typing.Optional[BillToPartyNullable] = Field(None, alias='bill_to_party')

    # The postal code of the third-party that is responsible for shipping costs. 
    bill_to_postal_code: typing.Optional[typing.Optional[str]] = Field(None, alias='bill_to_postal_code')

    # Indicates that the shipment contains alcohol.
    contains_alcohol: typing.Optional[bool] = Field(None, alias='contains_alcohol')

    # Indicates that the shipper is paying the international delivery duties for this shipment.  This option is supported by UPS, FedEx, and DHL Express. 
    delivered_duty_paid: typing.Optional[bool] = Field(None, alias='delivered_duty_paid')

    # Indicates if the shipment contain dry ice
    dry_ice: typing.Optional[bool] = Field(None, alias='dry_ice')

    # The weight of the dry ice in the shipment
    dry_ice_weight: typing.Optional[WeightNullable] = Field(None, alias='dry_ice_weight')

    # Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is primarily for USPS shipments.  See [Section 1.2 of the USPS parcel standards](https://pe.usps.com/text/dmm300/101.htm#ep1047495) for details. 
    non_machinable: typing.Optional[bool] = Field(None, alias='non_machinable')

    # Enables Saturday delivery, if supported by the carrier.
    saturday_delivery: typing.Optional[bool] = Field(None, alias='saturday_delivery')

    fedex_freight: typing.Optional[AdvancedShipmentOptionsFedexFreight] = Field(None, alias='fedex_freight')

    # Whether to use [UPS Ground Freight pricing](https://www.shipengine.com/docs/shipping/ups-ground-freight/).  If enabled, then a `freight_class` must also be specified. 
    use_ups_ground_freight_pricing: typing.Optional[typing.Optional[bool]] = Field(None, alias='use_ups_ground_freight_pricing')

    # The National Motor Freight Traffic Association [freight class](http://www.nmfta.org/pages/nmfc?AspxAutoDetectCookieSupport=1), such as \"77.5\", \"110\", or \"250\". 
    freight_class: typing.Optional[typing.Optional[str]] = Field(None, alias='freight_class')

    # An arbitrary field that can be used to store information about the shipment. 
    custom_field1: typing.Optional[typing.Optional[str]] = Field(None, alias='custom_field1')

    # An arbitrary field that can be used to store information about the shipment. 
    custom_field2: typing.Optional[typing.Optional[str]] = Field(None, alias='custom_field2')

    # An arbitrary field that can be used to store information about the shipment. 
    custom_field3: typing.Optional[typing.Optional[str]] = Field(None, alias='custom_field3')

    origin_type: typing.Optional[OriginTypeNullable] = Field(None, alias='origin_type')

    # Indicate to the carrier that this shipment requires additional handling. 
    additional_handling: typing.Optional[typing.Optional[bool]] = Field(None, alias='additional_handling')

    shipper_release: typing.Optional[typing.Optional[bool]] = Field(None, alias='shipper_release')

    collect_on_delivery: typing.Optional[CollectOnDelivery] = Field(None, alias='collect_on_delivery')

    # Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoices being attached
    third_party_consignee: typing.Optional[bool] = Field(None, alias='third_party_consignee')

    # Indicates if the Dangerous goods are present in the shipment
    dangerous_goods: typing.Optional[bool] = Field(None, alias='dangerous_goods')

    dangerous_goods_contact: typing.Optional[AdvancedShipmentOptionsDangerousGoodsContact] = Field(None, alias='dangerous_goods_contact')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
