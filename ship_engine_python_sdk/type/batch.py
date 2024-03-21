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

from ship_engine_python_sdk.type.batch_status import BatchStatus
from ship_engine_python_sdk.type.date_time import DateTime
from ship_engine_python_sdk.type.date_time_nullable import DateTimeNullable
from ship_engine_python_sdk.type.error import Error
from ship_engine_python_sdk.type.label_download import LabelDownload
from ship_engine_python_sdk.type.label_format import LabelFormat
from ship_engine_python_sdk.type.label_layout import LabelLayout
from ship_engine_python_sdk.type.optional_link import OptionalLink
from ship_engine_python_sdk.type.se_id import SeId

class RequiredBatch(TypedDict):
    # label layout
    label_layout: LabelLayout

    label_format: LabelFormat

    # A string that uniquely identifies the batch
    batch_id: SeId

    # The batch number.
    batch_number: str

    # A string that uniquely identifies the external batch
    external_batch_id: typing.Optional[str]

    # Custom notes you can add for each created batch
    batch_notes: typing.Optional[str]

    # The date and time the batch was created in ShipEngine
    created_at: DateTime

    # The date and time the batch was processed in ShipEngine
    processed_at: DateTimeNullable

    # The number of errors that occurred while generating the batch
    errors: int

    # The errors associated with the failed API call
    process_errors: typing.List[Error]

    # The number of warnings that occurred while generating the batch
    warnings: int

    # The number of labels generated in the batch
    completed: int

    # The number of forms for customs that are available for download
    forms: int

    # The total of errors, warnings, and completed properties
    count: int

    # The batch shipments endpoint
    batch_shipments_url: OptionalLink

    # Link to batch labels query
    batch_labels_url: OptionalLink

    # Link to batch errors endpoint
    batch_errors_url: OptionalLink

    # The label download for the batch
    label_download: LabelDownload

    # The form download for any customs that are needed
    form_download: OptionalLink

    status: BatchStatus

class OptionalBatch(TypedDict, total=False):
    pass

class Batch(RequiredBatch, OptionalBatch):
    pass
