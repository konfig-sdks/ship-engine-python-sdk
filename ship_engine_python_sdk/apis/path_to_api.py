import typing_extensions

from ship_engine_python_sdk.paths import PathValues
from ship_engine_python_sdk.apis.paths.v1_account_settings import V1AccountSettings
from ship_engine_python_sdk.apis.paths.v1_account_settings_images import V1AccountSettingsImages
from ship_engine_python_sdk.apis.paths.v1_account_settings_images_label_image_id import V1AccountSettingsImagesLabelImageId
from ship_engine_python_sdk.apis.paths.v1_addresses_recognize import V1AddressesRecognize
from ship_engine_python_sdk.apis.paths.v1_addresses_validate import V1AddressesValidate
from ship_engine_python_sdk.apis.paths.v1_batches import V1Batches
from ship_engine_python_sdk.apis.paths.v1_batches_external_batch_id_external_batch_id import V1BatchesExternalBatchIdExternalBatchId
from ship_engine_python_sdk.apis.paths.v1_batches_batch_id import V1BatchesBatchId
from ship_engine_python_sdk.apis.paths.v1_batches_batch_id_add import V1BatchesBatchIdAdd
from ship_engine_python_sdk.apis.paths.v1_batches_batch_id_errors import V1BatchesBatchIdErrors
from ship_engine_python_sdk.apis.paths.v1_batches_batch_id_process_labels import V1BatchesBatchIdProcessLabels
from ship_engine_python_sdk.apis.paths.v1_batches_batch_id_remove import V1BatchesBatchIdRemove
from ship_engine_python_sdk.apis.paths.v1_carriers import V1Carriers
from ship_engine_python_sdk.apis.paths.v1_carriers_carrier_id import V1CarriersCarrierId
from ship_engine_python_sdk.apis.paths.v1_carriers_carrier_id_add_funds import V1CarriersCarrierIdAddFunds
from ship_engine_python_sdk.apis.paths.v1_carriers_carrier_id_options import V1CarriersCarrierIdOptions
from ship_engine_python_sdk.apis.paths.v1_carriers_carrier_id_packages import V1CarriersCarrierIdPackages
from ship_engine_python_sdk.apis.paths.v1_carriers_carrier_id_services import V1CarriersCarrierIdServices
from ship_engine_python_sdk.apis.paths.v1_connections_carriers_carrier_name import V1ConnectionsCarriersCarrierName
from ship_engine_python_sdk.apis.paths.v1_connections_carriers_carrier_name_carrier_id import V1ConnectionsCarriersCarrierNameCarrierId
from ship_engine_python_sdk.apis.paths.v1_connections_carriers_carrier_name_carrier_id_settings import V1ConnectionsCarriersCarrierNameCarrierIdSettings
from ship_engine_python_sdk.apis.paths.v1_connections_insurance_shipsurance import V1ConnectionsInsuranceShipsurance
from ship_engine_python_sdk.apis.paths.v1_downloads_dir_subdir_filename import V1DownloadsDirSubdirFilename
from ship_engine_python_sdk.apis.paths.v1_environment_webhooks import V1EnvironmentWebhooks
from ship_engine_python_sdk.apis.paths.v1_environment_webhooks_webhook_id import V1EnvironmentWebhooksWebhookId
from ship_engine_python_sdk.apis.paths.v1_insurance_shipsurance_add_funds import V1InsuranceShipsuranceAddFunds
from ship_engine_python_sdk.apis.paths.v1_insurance_shipsurance_balance import V1InsuranceShipsuranceBalance
from ship_engine_python_sdk.apis.paths.v1_labels import V1Labels
from ship_engine_python_sdk.apis.paths.v1_labels_external_shipment_id_external_shipment_id import V1LabelsExternalShipmentIdExternalShipmentId
from ship_engine_python_sdk.apis.paths.v1_labels_rates_rate_id import V1LabelsRatesRateId
from ship_engine_python_sdk.apis.paths.v1_labels_shipment_shipment_id import V1LabelsShipmentShipmentId
from ship_engine_python_sdk.apis.paths.v1_labels_label_id import V1LabelsLabelId
from ship_engine_python_sdk.apis.paths.v1_labels_label_id_return import V1LabelsLabelIdReturn
from ship_engine_python_sdk.apis.paths.v1_labels_label_id_track import V1LabelsLabelIdTrack
from ship_engine_python_sdk.apis.paths.v1_labels_label_id_void import V1LabelsLabelIdVoid
from ship_engine_python_sdk.apis.paths.v1_manifests import V1Manifests
from ship_engine_python_sdk.apis.paths.v1_manifests_manifest_id import V1ManifestsManifestId
from ship_engine_python_sdk.apis.paths.v1_manifests_requests_manifest_request_id import V1ManifestsRequestsManifestRequestId
from ship_engine_python_sdk.apis.paths.v1_packages import V1Packages
from ship_engine_python_sdk.apis.paths.v1_packages_package_id import V1PackagesPackageId
from ship_engine_python_sdk.apis.paths.v1_pickups import V1Pickups
from ship_engine_python_sdk.apis.paths.v1_pickups_pickup_id import V1PickupsPickupId
from ship_engine_python_sdk.apis.paths.v1_rates import V1Rates
from ship_engine_python_sdk.apis.paths.v1_rates_bulk import V1RatesBulk
from ship_engine_python_sdk.apis.paths.v1_rates_estimate import V1RatesEstimate
from ship_engine_python_sdk.apis.paths.v1_rates_rate_id import V1RatesRateId
from ship_engine_python_sdk.apis.paths.v1_service_points_list import V1ServicePointsList
from ship_engine_python_sdk.apis.paths.v1_service_points_carrier_code_country_code_service_point_id import V1ServicePointsCarrierCodeCountryCodeServicePointId
from ship_engine_python_sdk.apis.paths.v1_shipments import V1Shipments
from ship_engine_python_sdk.apis.paths.v1_shipments_external_shipment_id_external_shipment_id import V1ShipmentsExternalShipmentIdExternalShipmentId
from ship_engine_python_sdk.apis.paths.v1_shipments_recognize import V1ShipmentsRecognize
from ship_engine_python_sdk.apis.paths.v1_shipments_shipment_id import V1ShipmentsShipmentId
from ship_engine_python_sdk.apis.paths.v1_shipments_shipment_id_cancel import V1ShipmentsShipmentIdCancel
from ship_engine_python_sdk.apis.paths.v1_shipments_shipment_id_rates import V1ShipmentsShipmentIdRates
from ship_engine_python_sdk.apis.paths.v1_shipments_tags import V1ShipmentsTags
from ship_engine_python_sdk.apis.paths.v1_shipments_shipment_id_tags import V1ShipmentsShipmentIdTags
from ship_engine_python_sdk.apis.paths.v1_shipments_shipment_id_tags_tag_name import V1ShipmentsShipmentIdTagsTagName
from ship_engine_python_sdk.apis.paths.v1_tags import V1Tags
from ship_engine_python_sdk.apis.paths.v1_tags_tag_name import V1TagsTagName
from ship_engine_python_sdk.apis.paths.v1_tags_tag_name_new_tag_name import V1TagsTagNameNewTagName
from ship_engine_python_sdk.apis.paths.v1_tokens_ephemeral import V1TokensEphemeral
from ship_engine_python_sdk.apis.paths.v1_tracking import V1Tracking
from ship_engine_python_sdk.apis.paths.v1_tracking_start import V1TrackingStart
from ship_engine_python_sdk.apis.paths.v1_tracking_stop import V1TrackingStop
from ship_engine_python_sdk.apis.paths.v1_warehouses import V1Warehouses
from ship_engine_python_sdk.apis.paths.v1_warehouses_warehouse_id import V1WarehousesWarehouseId
from ship_engine_python_sdk.apis.paths.v1_warehouses_warehouse_id_settings import V1WarehousesWarehouseIdSettings

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ACCOUNT_SETTINGS: V1AccountSettings,
        PathValues.V1_ACCOUNT_SETTINGS_IMAGES: V1AccountSettingsImages,
        PathValues.V1_ACCOUNT_SETTINGS_IMAGES_LABEL_IMAGE_ID: V1AccountSettingsImagesLabelImageId,
        PathValues.V1_ADDRESSES_RECOGNIZE: V1AddressesRecognize,
        PathValues.V1_ADDRESSES_VALIDATE: V1AddressesValidate,
        PathValues.V1_BATCHES: V1Batches,
        PathValues.V1_BATCHES_EXTERNAL_BATCH_ID_EXTERNAL_BATCH_ID: V1BatchesExternalBatchIdExternalBatchId,
        PathValues.V1_BATCHES_BATCH_ID: V1BatchesBatchId,
        PathValues.V1_BATCHES_BATCH_ID_ADD: V1BatchesBatchIdAdd,
        PathValues.V1_BATCHES_BATCH_ID_ERRORS: V1BatchesBatchIdErrors,
        PathValues.V1_BATCHES_BATCH_ID_PROCESS_LABELS: V1BatchesBatchIdProcessLabels,
        PathValues.V1_BATCHES_BATCH_ID_REMOVE: V1BatchesBatchIdRemove,
        PathValues.V1_CARRIERS: V1Carriers,
        PathValues.V1_CARRIERS_CARRIER_ID: V1CarriersCarrierId,
        PathValues.V1_CARRIERS_CARRIER_ID_ADD_FUNDS: V1CarriersCarrierIdAddFunds,
        PathValues.V1_CARRIERS_CARRIER_ID_OPTIONS: V1CarriersCarrierIdOptions,
        PathValues.V1_CARRIERS_CARRIER_ID_PACKAGES: V1CarriersCarrierIdPackages,
        PathValues.V1_CARRIERS_CARRIER_ID_SERVICES: V1CarriersCarrierIdServices,
        PathValues.V1_CONNECTIONS_CARRIERS_CARRIER_NAME: V1ConnectionsCarriersCarrierName,
        PathValues.V1_CONNECTIONS_CARRIERS_CARRIER_NAME_CARRIER_ID: V1ConnectionsCarriersCarrierNameCarrierId,
        PathValues.V1_CONNECTIONS_CARRIERS_CARRIER_NAME_CARRIER_ID_SETTINGS: V1ConnectionsCarriersCarrierNameCarrierIdSettings,
        PathValues.V1_CONNECTIONS_INSURANCE_SHIPSURANCE: V1ConnectionsInsuranceShipsurance,
        PathValues.V1_DOWNLOADS_DIR_SUBDIR_FILENAME: V1DownloadsDirSubdirFilename,
        PathValues.V1_ENVIRONMENT_WEBHOOKS: V1EnvironmentWebhooks,
        PathValues.V1_ENVIRONMENT_WEBHOOKS_WEBHOOK_ID: V1EnvironmentWebhooksWebhookId,
        PathValues.V1_INSURANCE_SHIPSURANCE_ADD_FUNDS: V1InsuranceShipsuranceAddFunds,
        PathValues.V1_INSURANCE_SHIPSURANCE_BALANCE: V1InsuranceShipsuranceBalance,
        PathValues.V1_LABELS: V1Labels,
        PathValues.V1_LABELS_EXTERNAL_SHIPMENT_ID_EXTERNAL_SHIPMENT_ID: V1LabelsExternalShipmentIdExternalShipmentId,
        PathValues.V1_LABELS_RATES_RATE_ID: V1LabelsRatesRateId,
        PathValues.V1_LABELS_SHIPMENT_SHIPMENT_ID: V1LabelsShipmentShipmentId,
        PathValues.V1_LABELS_LABEL_ID: V1LabelsLabelId,
        PathValues.V1_LABELS_LABEL_ID_RETURN: V1LabelsLabelIdReturn,
        PathValues.V1_LABELS_LABEL_ID_TRACK: V1LabelsLabelIdTrack,
        PathValues.V1_LABELS_LABEL_ID_VOID: V1LabelsLabelIdVoid,
        PathValues.V1_MANIFESTS: V1Manifests,
        PathValues.V1_MANIFESTS_MANIFEST_ID: V1ManifestsManifestId,
        PathValues.V1_MANIFESTS_REQUESTS_MANIFEST_REQUEST_ID: V1ManifestsRequestsManifestRequestId,
        PathValues.V1_PACKAGES: V1Packages,
        PathValues.V1_PACKAGES_PACKAGE_ID: V1PackagesPackageId,
        PathValues.V1_PICKUPS: V1Pickups,
        PathValues.V1_PICKUPS_PICKUP_ID: V1PickupsPickupId,
        PathValues.V1_RATES: V1Rates,
        PathValues.V1_RATES_BULK: V1RatesBulk,
        PathValues.V1_RATES_ESTIMATE: V1RatesEstimate,
        PathValues.V1_RATES_RATE_ID: V1RatesRateId,
        PathValues.V1_SERVICE_POINTS_LIST: V1ServicePointsList,
        PathValues.V1_SERVICE_POINTS_CARRIER_CODE_COUNTRY_CODE_SERVICE_POINT_ID: V1ServicePointsCarrierCodeCountryCodeServicePointId,
        PathValues.V1_SHIPMENTS: V1Shipments,
        PathValues.V1_SHIPMENTS_EXTERNAL_SHIPMENT_ID_EXTERNAL_SHIPMENT_ID: V1ShipmentsExternalShipmentIdExternalShipmentId,
        PathValues.V1_SHIPMENTS_RECOGNIZE: V1ShipmentsRecognize,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID: V1ShipmentsShipmentId,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_CANCEL: V1ShipmentsShipmentIdCancel,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_RATES: V1ShipmentsShipmentIdRates,
        PathValues.V1_SHIPMENTS_TAGS: V1ShipmentsTags,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_TAGS: V1ShipmentsShipmentIdTags,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_TAGS_TAG_NAME: V1ShipmentsShipmentIdTagsTagName,
        PathValues.V1_TAGS: V1Tags,
        PathValues.V1_TAGS_TAG_NAME: V1TagsTagName,
        PathValues.V1_TAGS_TAG_NAME_NEW_TAG_NAME: V1TagsTagNameNewTagName,
        PathValues.V1_TOKENS_EPHEMERAL: V1TokensEphemeral,
        PathValues.V1_TRACKING: V1Tracking,
        PathValues.V1_TRACKING_START: V1TrackingStart,
        PathValues.V1_TRACKING_STOP: V1TrackingStop,
        PathValues.V1_WAREHOUSES: V1Warehouses,
        PathValues.V1_WAREHOUSES_WAREHOUSE_ID: V1WarehousesWarehouseId,
        PathValues.V1_WAREHOUSES_WAREHOUSE_ID_SETTINGS: V1WarehousesWarehouseIdSettings,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ACCOUNT_SETTINGS: V1AccountSettings,
        PathValues.V1_ACCOUNT_SETTINGS_IMAGES: V1AccountSettingsImages,
        PathValues.V1_ACCOUNT_SETTINGS_IMAGES_LABEL_IMAGE_ID: V1AccountSettingsImagesLabelImageId,
        PathValues.V1_ADDRESSES_RECOGNIZE: V1AddressesRecognize,
        PathValues.V1_ADDRESSES_VALIDATE: V1AddressesValidate,
        PathValues.V1_BATCHES: V1Batches,
        PathValues.V1_BATCHES_EXTERNAL_BATCH_ID_EXTERNAL_BATCH_ID: V1BatchesExternalBatchIdExternalBatchId,
        PathValues.V1_BATCHES_BATCH_ID: V1BatchesBatchId,
        PathValues.V1_BATCHES_BATCH_ID_ADD: V1BatchesBatchIdAdd,
        PathValues.V1_BATCHES_BATCH_ID_ERRORS: V1BatchesBatchIdErrors,
        PathValues.V1_BATCHES_BATCH_ID_PROCESS_LABELS: V1BatchesBatchIdProcessLabels,
        PathValues.V1_BATCHES_BATCH_ID_REMOVE: V1BatchesBatchIdRemove,
        PathValues.V1_CARRIERS: V1Carriers,
        PathValues.V1_CARRIERS_CARRIER_ID: V1CarriersCarrierId,
        PathValues.V1_CARRIERS_CARRIER_ID_ADD_FUNDS: V1CarriersCarrierIdAddFunds,
        PathValues.V1_CARRIERS_CARRIER_ID_OPTIONS: V1CarriersCarrierIdOptions,
        PathValues.V1_CARRIERS_CARRIER_ID_PACKAGES: V1CarriersCarrierIdPackages,
        PathValues.V1_CARRIERS_CARRIER_ID_SERVICES: V1CarriersCarrierIdServices,
        PathValues.V1_CONNECTIONS_CARRIERS_CARRIER_NAME: V1ConnectionsCarriersCarrierName,
        PathValues.V1_CONNECTIONS_CARRIERS_CARRIER_NAME_CARRIER_ID: V1ConnectionsCarriersCarrierNameCarrierId,
        PathValues.V1_CONNECTIONS_CARRIERS_CARRIER_NAME_CARRIER_ID_SETTINGS: V1ConnectionsCarriersCarrierNameCarrierIdSettings,
        PathValues.V1_CONNECTIONS_INSURANCE_SHIPSURANCE: V1ConnectionsInsuranceShipsurance,
        PathValues.V1_DOWNLOADS_DIR_SUBDIR_FILENAME: V1DownloadsDirSubdirFilename,
        PathValues.V1_ENVIRONMENT_WEBHOOKS: V1EnvironmentWebhooks,
        PathValues.V1_ENVIRONMENT_WEBHOOKS_WEBHOOK_ID: V1EnvironmentWebhooksWebhookId,
        PathValues.V1_INSURANCE_SHIPSURANCE_ADD_FUNDS: V1InsuranceShipsuranceAddFunds,
        PathValues.V1_INSURANCE_SHIPSURANCE_BALANCE: V1InsuranceShipsuranceBalance,
        PathValues.V1_LABELS: V1Labels,
        PathValues.V1_LABELS_EXTERNAL_SHIPMENT_ID_EXTERNAL_SHIPMENT_ID: V1LabelsExternalShipmentIdExternalShipmentId,
        PathValues.V1_LABELS_RATES_RATE_ID: V1LabelsRatesRateId,
        PathValues.V1_LABELS_SHIPMENT_SHIPMENT_ID: V1LabelsShipmentShipmentId,
        PathValues.V1_LABELS_LABEL_ID: V1LabelsLabelId,
        PathValues.V1_LABELS_LABEL_ID_RETURN: V1LabelsLabelIdReturn,
        PathValues.V1_LABELS_LABEL_ID_TRACK: V1LabelsLabelIdTrack,
        PathValues.V1_LABELS_LABEL_ID_VOID: V1LabelsLabelIdVoid,
        PathValues.V1_MANIFESTS: V1Manifests,
        PathValues.V1_MANIFESTS_MANIFEST_ID: V1ManifestsManifestId,
        PathValues.V1_MANIFESTS_REQUESTS_MANIFEST_REQUEST_ID: V1ManifestsRequestsManifestRequestId,
        PathValues.V1_PACKAGES: V1Packages,
        PathValues.V1_PACKAGES_PACKAGE_ID: V1PackagesPackageId,
        PathValues.V1_PICKUPS: V1Pickups,
        PathValues.V1_PICKUPS_PICKUP_ID: V1PickupsPickupId,
        PathValues.V1_RATES: V1Rates,
        PathValues.V1_RATES_BULK: V1RatesBulk,
        PathValues.V1_RATES_ESTIMATE: V1RatesEstimate,
        PathValues.V1_RATES_RATE_ID: V1RatesRateId,
        PathValues.V1_SERVICE_POINTS_LIST: V1ServicePointsList,
        PathValues.V1_SERVICE_POINTS_CARRIER_CODE_COUNTRY_CODE_SERVICE_POINT_ID: V1ServicePointsCarrierCodeCountryCodeServicePointId,
        PathValues.V1_SHIPMENTS: V1Shipments,
        PathValues.V1_SHIPMENTS_EXTERNAL_SHIPMENT_ID_EXTERNAL_SHIPMENT_ID: V1ShipmentsExternalShipmentIdExternalShipmentId,
        PathValues.V1_SHIPMENTS_RECOGNIZE: V1ShipmentsRecognize,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID: V1ShipmentsShipmentId,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_CANCEL: V1ShipmentsShipmentIdCancel,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_RATES: V1ShipmentsShipmentIdRates,
        PathValues.V1_SHIPMENTS_TAGS: V1ShipmentsTags,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_TAGS: V1ShipmentsShipmentIdTags,
        PathValues.V1_SHIPMENTS_SHIPMENT_ID_TAGS_TAG_NAME: V1ShipmentsShipmentIdTagsTagName,
        PathValues.V1_TAGS: V1Tags,
        PathValues.V1_TAGS_TAG_NAME: V1TagsTagName,
        PathValues.V1_TAGS_TAG_NAME_NEW_TAG_NAME: V1TagsTagNameNewTagName,
        PathValues.V1_TOKENS_EPHEMERAL: V1TokensEphemeral,
        PathValues.V1_TRACKING: V1Tracking,
        PathValues.V1_TRACKING_START: V1TrackingStart,
        PathValues.V1_TRACKING_STOP: V1TrackingStop,
        PathValues.V1_WAREHOUSES: V1Warehouses,
        PathValues.V1_WAREHOUSES_WAREHOUSE_ID: V1WarehousesWarehouseId,
        PathValues.V1_WAREHOUSES_WAREHOUSE_ID_SETTINGS: V1WarehousesWarehouseIdSettings,
    }
)
