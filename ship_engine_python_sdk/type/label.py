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

from ship_engine_python_sdk.type.alternative_identifier import AlternativeIdentifier
from ship_engine_python_sdk.type.carrier_code import CarrierCode
from ship_engine_python_sdk.type.date import Date
from ship_engine_python_sdk.type.date_time import DateTime
from ship_engine_python_sdk.type.display_scheme import DisplayScheme
from ship_engine_python_sdk.type.image_id_nullable import ImageIdNullable
from ship_engine_python_sdk.type.label_charge_event import LabelChargeEvent
from ship_engine_python_sdk.type.label_download import LabelDownload
from ship_engine_python_sdk.type.label_download_type import LabelDownloadType
from ship_engine_python_sdk.type.label_format import LabelFormat
from ship_engine_python_sdk.type.label_layout import LabelLayout
from ship_engine_python_sdk.type.label_packages import LabelPackages
from ship_engine_python_sdk.type.label_status import LabelStatus
from ship_engine_python_sdk.type.monetary_value import MonetaryValue
from ship_engine_python_sdk.type.optional_link import OptionalLink
from ship_engine_python_sdk.type.optional_link_nullable import OptionalLinkNullable
from ship_engine_python_sdk.type.package_code import PackageCode
from ship_engine_python_sdk.type.partial_shipment import PartialShipment
from ship_engine_python_sdk.type.se_id import SeId
from ship_engine_python_sdk.type.service_code import ServiceCode
from ship_engine_python_sdk.type.tracking_status import TrackingStatus
from ship_engine_python_sdk.type.validate_address import ValidateAddress

class RequiredLabel(TypedDict):
    pass

class OptionalLabel(TypedDict, total=False):
    # A string that uniquely identifies the label. This ID is generated by ShipEngine when the label is created. 
    label_id: SeId

    status: LabelStatus

    # The shipment that this label is for.  ShipEngine can create a shipment for you automatically when you [create a label](https://www.shipengine.com/docs/labels/create-a-label/), or you can [create your own shipment](https://www.shipengine.com/docs/shipping/create-a-shipment/) and then [use it to print a label](https://www.shipengine.com/docs/labels/create-from-shipment/) 
    shipment_id: SeId

    # The shipment information used to generate the label
    shipment: PartialShipment

    # The date that the package was (or will be) shippped.  ShipEngine will take the day of week into consideration. For example, if the carrier does not operate on Sundays, then a package that would have shipped on Sunday will ship on Monday instead. 
    ship_date: Date

    # The date and time that the label was created in ShipEngine.
    created_at: DateTime

    # The cost of shipping, delivery confirmation, and other carrier charges.  This amount **does not** include insurance costs. 
    shipment_cost: MonetaryValue

    # The insurance cost for this package.  Add this to the `shipment_cost` field to get the total cost. 
    insurance_cost: MonetaryValue

    # The total shipping cost for the specified comparison_rate_type. 
    requested_comparison_amount: MonetaryValue

    # The tracking number for the package. Tracking number formats vary across carriers.
    tracking_number: str

    # Indicates whether this is a return label.  You may also want to set the `rma_number` so you know what is being returned. 
    is_return_label: bool

    # An optional Return Merchandise Authorization number.  This field is useful for return labels.  You can set it to any string value. 
    rma_number: typing.Optional[str]

    # Indicates whether this is an international shipment.  That is, the originating country and destination country are different. 
    is_international: bool

    # If this label was created as part of a [batch](https://www.shipengine.com/docs/labels/bulk/), then this is the unique ID of that batch. 
    batch_id: SeId

    # The unique ID of the [carrier account](https://www.shipengine.com/docs/carriers/setup/) that was used to create this label 
    carrier_id: SeId

    # The label charge event. 
    charge_event: LabelChargeEvent

    # The `label_id` of the original (outgoing) label that the return label is for. This associates the two labels together, which is required by some carriers. 
    outbound_label_id: SeId

    # The [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc. 
    service_code: ServiceCode

    # WARNING: This property is deprecated
    # Indicate if this label is being used only for testing purposes. If true, then no charge will be added to your account.
    test_label: bool

    # The [package type](https://www.shipengine.com/docs/reference/list-carrier-packages/), such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc.  The code `package` indicates a custom or unknown package type. 
    package_code: PackageCode

    validate_address: ValidateAddress

    # Indicates whether the label has been [voided](https://www.shipengine.com/docs/labels/voiding/) 
    voided: bool

    # The date and time that the label was [voided](https://www.shipengine.com/docs/labels/voiding/), or `null` if the label has not been voided 
    voided_at: DateTime

    label_download_type: LabelDownloadType

    # The file format that you want the label to be in.  We recommend `pdf` format because it is supported by all carriers, whereas some carriers do not support the `png` or `zpl` formats. 
    label_format: LabelFormat

    # The display format that the label should be shown in.
    display_scheme: DisplayScheme

    # The layout (size) that you want the label to be in.  The `label_format` determines which sizes are allowed.  `4x6` is supported for all label formats, whereas `letter` (8.5\" x 11\") is only supported for `pdf` format. 
    label_layout: LabelLayout

    # Indicates whether the shipment is trackable, in which case the `tracking_status` field will reflect the current status and each package will have a `tracking_number`. 
    trackable: bool

    # The label image resource that was used to create a custom label image.
    label_image_id: ImageIdNullable

    # The [shipping carrier](https://www.shipengine.com/docs/carriers/setup/) who will ship the package, such as `fedex`, `dhl_express`, `stamps_com`, etc. 
    carrier_code: CarrierCode

    # The current status of the package, such as `in_transit` or `delivered`
    tracking_status: TrackingStatus

    label_download: LabelDownload

    # The link to download the customs form (a.k.a. commercial invoice) for this shipment, if any.  Forms are in PDF format. This field is null if the shipment does not require a customs form, or if the carrier does not support it. 
    form_download: typing.Optional[OptionalLinkNullable]

    # The link to submit an insurance claim for the shipment.  This field is null if the shipment is not insured or if the insurance provider does not support online claim submission. 
    insurance_claim: OptionalLink

    packages: LabelPackages

    # Additional information some carriers may provide by which to identify a given label in their system.  
    alternative_identifiers: typing.Optional[typing.List[AlternativeIdentifier]]

class Label(RequiredLabel, OptionalLabel):
    pass
