# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ship_engine_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SHIPMENTS = "shipments"
    BATCHES = "batches"
    LABELS = "labels"
    CARRIERS = "carriers"
    ACCOUNT = "account"
    WAREHOUSES = "warehouses"
    PACKAGE_TYPES = "package_types"
    WEBHOOKS = "webhooks"
    CARRIER_ACCOUNTS = "carrier_accounts"
    INSURANCE = "insurance"
    MANIFESTS = "manifests"
    PACKAGE_PICKUPS = "package_pickups"
    RATES = "rates"
    TAGS = "tags"
    TRACKING = "tracking"
    ADDRESSES = "addresses"
    SERVICE_POINTS = "service_points"
    DOWNLOADS = "downloads"
    TOKENS = "tokens"
