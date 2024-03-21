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

from ship_engine_python_sdk.pydantic.connect_access_worldwide_request_body import ConnectAccessWorldwideRequestBody
from ship_engine_python_sdk.pydantic.connect_amazon_buy_shipping_request_body import ConnectAmazonBuyShippingRequestBody
from ship_engine_python_sdk.pydantic.connect_amazon_shipping_uk import ConnectAmazonShippingUk
from ship_engine_python_sdk.pydantic.connect_apc_request_body import ConnectApcRequestBody
from ship_engine_python_sdk.pydantic.connect_asendia_request_body import ConnectAsendiaRequestBody
from ship_engine_python_sdk.pydantic.connect_australia_post_request_body import ConnectAustraliaPostRequestBody
from ship_engine_python_sdk.pydantic.connect_canada_post_request_body import ConnectCanadaPostRequestBody
from ship_engine_python_sdk.pydantic.connect_dhl_ecommerce_request_body import ConnectDhlEcommerceRequestBody
from ship_engine_python_sdk.pydantic.connect_dhl_express_au_request_body import ConnectDhlExpressAuRequestBody
from ship_engine_python_sdk.pydantic.connect_dhl_express_ca_request_body import ConnectDhlExpressCaRequestBody
from ship_engine_python_sdk.pydantic.connect_dhl_express_request_body import ConnectDhlExpressRequestBody
from ship_engine_python_sdk.pydantic.connect_dhl_express_uk_request_body import ConnectDhlExpressUkRequestBody
from ship_engine_python_sdk.pydantic.connect_dpd_request_body import ConnectDpdRequestBody
from ship_engine_python_sdk.pydantic.connect_endicia_request_body import ConnectEndiciaRequestBody
from ship_engine_python_sdk.pydantic.connect_fedex_request_body import ConnectFedexRequestBody
from ship_engine_python_sdk.pydantic.connect_fedex_uk_request_body import ConnectFedexUkRequestBody
from ship_engine_python_sdk.pydantic.connect_firstmile_request_body import ConnectFirstmileRequestBody
from ship_engine_python_sdk.pydantic.connect_imex_request_body import ConnectImexRequestBody
from ship_engine_python_sdk.pydantic.connect_newgistics_request_body import ConnectNewgisticsRequestBody
from ship_engine_python_sdk.pydantic.connect_ontrac_request_body import ConnectOntracRequestBody
from ship_engine_python_sdk.pydantic.connect_purolator_request_body import ConnectPurolatorRequestBody
from ship_engine_python_sdk.pydantic.connect_royal_mail_request_body import ConnectRoyalMailRequestBody
from ship_engine_python_sdk.pydantic.connect_rr_donnelley_request_body import ConnectRrDonnelleyRequestBody
from ship_engine_python_sdk.pydantic.connect_seko_request_body import ConnectSekoRequestBody
from ship_engine_python_sdk.pydantic.connect_sendle_request_body import ConnectSendleRequestBody
from ship_engine_python_sdk.pydantic.connect_stamps_request_body import ConnectStampsRequestBody
from ship_engine_python_sdk.pydantic.connect_ups_request_body import ConnectUpsRequestBody

ConnectCarrierRequestBody = typing.Union[ConnectAccessWorldwideRequestBody,ConnectAmazonBuyShippingRequestBody,ConnectAmazonShippingUk,ConnectApcRequestBody,ConnectAsendiaRequestBody,ConnectAustraliaPostRequestBody,ConnectCanadaPostRequestBody,ConnectDhlEcommerceRequestBody,ConnectDhlExpressRequestBody,ConnectDhlExpressAuRequestBody,ConnectDhlExpressCaRequestBody,ConnectDhlExpressUkRequestBody,ConnectDpdRequestBody,ConnectEndiciaRequestBody,ConnectFedexRequestBody,ConnectFedexUkRequestBody,ConnectFirstmileRequestBody,ConnectImexRequestBody,ConnectNewgisticsRequestBody,ConnectOntracRequestBody,ConnectPurolatorRequestBody,ConnectRoyalMailRequestBody,ConnectRrDonnelleyRequestBody,ConnectSekoRequestBody,ConnectSendleRequestBody,ConnectStampsRequestBody,ConnectUpsRequestBody]
