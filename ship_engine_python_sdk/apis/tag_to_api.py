import typing_extensions

from ship_engine_python_sdk.apis.tags import TagValues
from ship_engine_python_sdk.apis.tags.shipments_api import ShipmentsApi
from ship_engine_python_sdk.apis.tags.batches_api import BatchesApi
from ship_engine_python_sdk.apis.tags.labels_api import LabelsApi
from ship_engine_python_sdk.apis.tags.carriers_api import CarriersApi
from ship_engine_python_sdk.apis.tags.account_api import AccountApi
from ship_engine_python_sdk.apis.tags.warehouses_api import WarehousesApi
from ship_engine_python_sdk.apis.tags.package_types_api import PackageTypesApi
from ship_engine_python_sdk.apis.tags.webhooks_api import WebhooksApi
from ship_engine_python_sdk.apis.tags.carrier_accounts_api import CarrierAccountsApi
from ship_engine_python_sdk.apis.tags.insurance_api import InsuranceApi
from ship_engine_python_sdk.apis.tags.manifests_api import ManifestsApi
from ship_engine_python_sdk.apis.tags.package_pickups_api import PackagePickupsApi
from ship_engine_python_sdk.apis.tags.rates_api import RatesApi
from ship_engine_python_sdk.apis.tags.tags_api import TagsApi
from ship_engine_python_sdk.apis.tags.tracking_api import TrackingApi
from ship_engine_python_sdk.apis.tags.addresses_api import AddressesApi
from ship_engine_python_sdk.apis.tags.service_points_api import ServicePointsApi
from ship_engine_python_sdk.apis.tags.downloads_api import DownloadsApi
from ship_engine_python_sdk.apis.tags.tokens_api import TokensApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SHIPMENTS: ShipmentsApi,
        TagValues.BATCHES: BatchesApi,
        TagValues.LABELS: LabelsApi,
        TagValues.CARRIERS: CarriersApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.WAREHOUSES: WarehousesApi,
        TagValues.PACKAGE_TYPES: PackageTypesApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.CARRIER_ACCOUNTS: CarrierAccountsApi,
        TagValues.INSURANCE: InsuranceApi,
        TagValues.MANIFESTS: ManifestsApi,
        TagValues.PACKAGE_PICKUPS: PackagePickupsApi,
        TagValues.RATES: RatesApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRACKING: TrackingApi,
        TagValues.ADDRESSES: AddressesApi,
        TagValues.SERVICE_POINTS: ServicePointsApi,
        TagValues.DOWNLOADS: DownloadsApi,
        TagValues.TOKENS: TokensApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SHIPMENTS: ShipmentsApi,
        TagValues.BATCHES: BatchesApi,
        TagValues.LABELS: LabelsApi,
        TagValues.CARRIERS: CarriersApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.WAREHOUSES: WarehousesApi,
        TagValues.PACKAGE_TYPES: PackageTypesApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.CARRIER_ACCOUNTS: CarrierAccountsApi,
        TagValues.INSURANCE: InsuranceApi,
        TagValues.MANIFESTS: ManifestsApi,
        TagValues.PACKAGE_PICKUPS: PackagePickupsApi,
        TagValues.RATES: RatesApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRACKING: TrackingApi,
        TagValues.ADDRESSES: AddressesApi,
        TagValues.SERVICE_POINTS: ServicePointsApi,
        TagValues.DOWNLOADS: DownloadsApi,
        TagValues.TOKENS: TokensApi,
    }
)
