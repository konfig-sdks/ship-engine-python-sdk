# coding: utf-8
"""
    ShipEngine API

    ShipEngine's easy-to-use REST API lets you manage all of your shipping needs without worrying about the complexities of different carrier APIs and protocols. We handle all the heavy lifting so you can focus on providing a first-class shipping experience for your customers at the best possible prices.  Each of ShipEngine's features can be used by itself or in conjunction with each other to build powerful shipping functionality into your application or service.  ## Getting Started If you're new to REST APIs then be sure to read our [introduction to REST](https://www.shipengine.com/docs/rest/) to understand the basics.  Learn how to [authenticate yourself to ShipEngine](https://www.shipengine.com/docs/auth/), and then use our [sandbox environment](https://www.shipengine.com/docs/sandbox/) to kick the tires and get familiar with our API. If you run into any problems, then be sure to check the [error handling guide](https://www.shipengine.com/docs/errors/) for tips.  Here are some step-by-step **tutorials** to get you started:    - [Learn how to create your first shipping label](https://www.shipengine.com/docs/labels/create-a-label/)   - [Calculate shipping costs and compare rates across carriers](https://www.shipengine.com/docs/rates/)   - [Track packages on-demand or in real time](https://www.shipengine.com/docs/tracking/)   - [Validate mailing addresses anywhere on Earth](https://www.shipengine.com/docs/addresses/validation/)   ## Shipping Labels for Every Major Carrier ShipEngine makes it easy to [create shipping labels for any carrier](https://www.shipengine.com/docs/labels/create-a-label/) and [download them](https://www.shipengine.com/docs/labels/downloading/) in a [variety of file formats](https://www.shipengine.com/docs/labels/formats/). You can even customize labels with your own [messages](https://www.shipengine.com/docs/labels/messages/) and [images](https://www.shipengine.com/docs/labels/branding/).   ## Real-Time Package Tracking With ShipEngine you can [get the current status of a package](https://www.shipengine.com/docs/tracking/) or [subscribe to real-time tracking updates](https://www.shipengine.com/docs/tracking/webhooks/) via webhooks. You can also create [custimized tracking pages](https://www.shipengine.com/docs/tracking/branded-tracking-page/) with your own branding so your customers will always know where their package is.   ## Compare Shipping Costs Across Carriers Make sure you ship as cost-effectively as possible by [comparing rates across carriers](https://www.shipengine.com/docs/rates/get-shipment-rates/) using the ShipEngine Rates API. Or if you don't know the full shipment details yet, then you can [get rate estimates](https://www.shipengine.com/docs/rates/estimate/) with limited address info.   ## Worldwide Address Validation ShipEngine supports [address validation](https://www.shipengine.com/docs/addresses/validation/) for virtually [every country on Earth](https://www.shipengine.com/docs/addresses/validation/countries/), including the United States, Canada, Great Britain, Australia, Germany, France, Norway, Spain, Sweden, Israel, Italy, and over 160 others. 

    The version of the OpenAPI document: 1.1.202403202303
    Contact: sales@shipengine.com
    Created by: https://www.shipengine.com/contact/
"""

import typing
import inspect
from datetime import date, datetime
from ship_engine_python_sdk.client_custom import ClientCustom
from ship_engine_python_sdk.configuration import Configuration
from ship_engine_python_sdk.api_client import ApiClient
from ship_engine_python_sdk.type_util import copy_signature
from ship_engine_python_sdk.apis.tags.account_api import AccountApi
from ship_engine_python_sdk.apis.tags.addresses_api import AddressesApi
from ship_engine_python_sdk.apis.tags.batches_api import BatchesApi
from ship_engine_python_sdk.apis.tags.carrier_accounts_api import CarrierAccountsApi
from ship_engine_python_sdk.apis.tags.carriers_api import CarriersApi
from ship_engine_python_sdk.apis.tags.downloads_api import DownloadsApi
from ship_engine_python_sdk.apis.tags.insurance_api import InsuranceApi
from ship_engine_python_sdk.apis.tags.labels_api import LabelsApi
from ship_engine_python_sdk.apis.tags.manifests_api import ManifestsApi
from ship_engine_python_sdk.apis.tags.package_pickups_api import PackagePickupsApi
from ship_engine_python_sdk.apis.tags.package_types_api import PackageTypesApi
from ship_engine_python_sdk.apis.tags.rates_api import RatesApi
from ship_engine_python_sdk.apis.tags.service_points_api import ServicePointsApi
from ship_engine_python_sdk.apis.tags.shipments_api import ShipmentsApi
from ship_engine_python_sdk.apis.tags.tags_api import TagsApi
from ship_engine_python_sdk.apis.tags.tokens_api import TokensApi
from ship_engine_python_sdk.apis.tags.tracking_api import TrackingApi
from ship_engine_python_sdk.apis.tags.warehouses_api import WarehousesApi
from ship_engine_python_sdk.apis.tags.webhooks_api import WebhooksApi



class ShipEngine(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.account: AccountApi = AccountApi(api_client)
        self.addresses: AddressesApi = AddressesApi(api_client)
        self.batches: BatchesApi = BatchesApi(api_client)
        self.carrier_accounts: CarrierAccountsApi = CarrierAccountsApi(api_client)
        self.carriers: CarriersApi = CarriersApi(api_client)
        self.downloads: DownloadsApi = DownloadsApi(api_client)
        self.insurance: InsuranceApi = InsuranceApi(api_client)
        self.labels: LabelsApi = LabelsApi(api_client)
        self.manifests: ManifestsApi = ManifestsApi(api_client)
        self.package_pickups: PackagePickupsApi = PackagePickupsApi(api_client)
        self.package_types: PackageTypesApi = PackageTypesApi(api_client)
        self.rates: RatesApi = RatesApi(api_client)
        self.service_points: ServicePointsApi = ServicePointsApi(api_client)
        self.shipments: ShipmentsApi = ShipmentsApi(api_client)
        self.tags: TagsApi = TagsApi(api_client)
        self.tokens: TokensApi = TokensApi(api_client)
        self.tracking: TrackingApi = TrackingApi(api_client)
        self.warehouses: WarehousesApi = WarehousesApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)
