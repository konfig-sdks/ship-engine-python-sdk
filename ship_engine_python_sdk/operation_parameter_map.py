operation_parameter_map = {
    '/v1/account/settings/images-POST': {
        'parameters': [
            {
                'name': 'label_image_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'image_content_type'
            },
            {
                'name': 'image_data'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'modified_at'
            },
        ]
    },
    '/v1/account/settings/images/{label_image_id}-DELETE': {
        'parameters': [
            {
                'name': 'label_image_id'
            },
        ]
    },
    '/v1/account/settings/images/{label_image_id}-GET': {
        'parameters': [
            {
                'name': 'label_image_id'
            },
        ]
    },
    '/v1/account/settings/images-GET': {
        'parameters': [
        ]
    },
    '/v1/account/settings-GET': {
        'parameters': [
        ]
    },
    '/v1/account/settings/images/{label_image_id}-PUT': {
        'parameters': [
            {
                'name': 'label_image_id'
            },
            {
                'name': 'label_image_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'image_content_type'
            },
            {
                'name': 'image_data'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'modified_at'
            },
        ]
    },
    '/v1/addresses/recognize-PUT': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'address'
            },
        ]
    },
    '/v1/addresses/validate-POST': {
        'parameters': [
        ]
    },
    '/v1/batches/{batch_id}/add-POST': {
        'parameters': [
            {
                'name': 'batch_id'
            },
            {
                'name': 'shipment_ids'
            },
            {
                'name': 'rate_ids'
            },
        ]
    },
    '/v1/batches-POST': {
        'parameters': [
            {
                'name': 'external_batch_id'
            },
            {
                'name': 'batch_notes'
            },
            {
                'name': 'shipment_ids'
            },
            {
                'name': 'rate_ids'
            },
            {
                'name': 'process_labels'
            },
        ]
    },
    '/v1/batches/{batch_id}-PUT': {
        'parameters': [
            {
                'name': 'batch_id'
            },
        ]
    },
    '/v1/batches/{batch_id}-DELETE': {
        'parameters': [
            {
                'name': 'batch_id'
            },
        ]
    },
    '/v1/batches/{batch_id}/process/labels-POST': {
        'parameters': [
            {
                'name': 'batch_id'
            },
            {
                'name': 'ship_date'
            },
            {
                'name': 'label_layout'
            },
            {
                'name': 'label_format'
            },
            {
                'name': 'display_scheme'
            },
        ]
    },
    '/v1/batches-GET': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'sort_dir'
            },
            {
                'name': 'batch_number'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/v1/batches/external_batch_id/{external_batch_id}-GET': {
        'parameters': [
            {
                'name': 'external_batch_id'
            },
        ]
    },
    '/v1/batches/{batch_id}-GET': {
        'parameters': [
            {
                'name': 'batch_id'
            },
        ]
    },
    '/v1/batches/{batch_id}/errors-GET': {
        'parameters': [
            {
                'name': 'batch_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pagesize'
            },
        ]
    },
    '/v1/batches/{batch_id}/remove-POST': {
        'parameters': [
            {
                'name': 'batch_id'
            },
            {
                'name': 'shipment_ids'
            },
            {
                'name': 'rate_ids'
            },
        ]
    },
    '/v1/connections/carriers/{carrier_name}-POST': {
        'parameters': [
            {
                'name': 'carrier_name'
            },
            {
                'name': 'nickname'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'merchant_seller_id'
            },
            {
                'name': 'mws_auth_token'
            },
            {
                'name': 'email'
            },
            {
                'name': 'auth_code'
            },
            {
                'name': 'account_number'
            },
            {
                'name': 'ftp_username'
            },
            {
                'name': 'ftp_password'
            },
            {
                'name': 'api_key'
            },
            {
                'name': 'api_secret'
            },
            {
                'name': 'contract_id'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'pickup_number'
            },
            {
                'name': 'distribution_center'
            },
            {
                'name': 'ancillary_endorsement'
            },
            {
                'name': 'sold_to'
            },
            {
                'name': 'registration_id'
            },
            {
                'name': 'software_name'
            },
            {
                'name': 'site_id'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'account'
            },
            {
                'name': 'passphrase'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'company'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'postal_code'
            },
            {
                'name': 'state'
            },
            {
                'name': 'agree_to_eula'
            },
            {
                'name': 'meter_number'
            },
            {
                'name': 'mailer_id'
            },
            {
                'name': 'profile_name'
            },
            {
                'name': 'merchant_id'
            },
            {
                'name': 'induction_site'
            },
            {
                'name': 'activation_key'
            },
            {
                'name': 'oba_email'
            },
            {
                'name': 'contact_name'
            },
            {
                'name': 'company_name'
            },
            {
                'name': 'street_line1'
            },
            {
                'name': 'street_line2'
            },
            {
                'name': 'street_line3'
            },
            {
                'name': 'access_key'
            },
            {
                'name': 'sendle_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'account_country_code'
            },
            {
                'name': 'account_postal_code'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoice_amount'
            },
            {
                'name': 'invoice_currency_code'
            },
            {
                'name': 'agree_to_technology_agreement'
            },
        ]
    },
    '/v1/connections/carriers/{carrier_name}/{carrier_id}-DELETE': {
        'parameters': [
            {
                'name': 'carrier_name'
            },
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/connections/carriers/{carrier_name}/{carrier_id}/settings-GET': {
        'parameters': [
            {
                'name': 'carrier_name'
            },
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/connections/carriers/{carrier_name}/{carrier_id}/settings-PUT': {
        'parameters': [
            {
                'name': 'carrier_name'
            },
            {
                'name': 'carrier_id'
            },
            {
                'name': 'nickname'
            },
            {
                'name': 'should_hide_account_number_on_archive_doc'
            },
            {
                'name': 'is_primary_account'
            },
            {
                'name': 'pickup_type'
            },
            {
                'name': 'smart_post_hub'
            },
            {
                'name': 'smart_post_endorsement'
            },
            {
                'name': 'signature_image'
            },
            {
                'name': 'letterhead_image'
            },
            {
                'name': 'include_barcode_with_order_number'
            },
            {
                'name': 'receive_email_on_manifest_processing'
            },
            {
                'name': 'use_carbon_neutral_shipping_program'
            },
            {
                'name': 'use_ground_freight_pricing'
            },
            {
                'name': 'use_consolidation_services'
            },
            {
                'name': 'use_order_number_on_mail_innovations_labels'
            },
            {
                'name': 'mail_innovations_endorsement'
            },
            {
                'name': 'mail_innovations_cost_center'
            },
            {
                'name': 'use_negotiated_rates'
            },
            {
                'name': 'account_postal_code'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/v1/carriers/{carrier_id}/add_funds-PUT': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/carriers-GET': {
        'parameters': [
        ]
    },
    '/v1/carriers/{carrier_id}-DELETE': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/carriers/{carrier_id}-GET': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/carriers/{carrier_id}/options-GET': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/carriers/{carrier_id}/packages-GET': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/carriers/{carrier_id}/services-GET': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
        ]
    },
    '/v1/downloads/{dir}/{subdir}/{filename}-GET': {
        'parameters': [
            {
                'name': 'subdir'
            },
            {
                'name': 'filename'
            },
            {
                'name': 'dir'
            },
            {
                'name': 'download'
            },
            {
                'name': 'rotation'
            },
        ]
    },
    '/v1/insurance/shipsurance/add_funds-PATCH': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'amount'
            },
        ]
    },
    '/v1/insurance/shipsurance/balance-GET': {
        'parameters': [
        ]
    },
    '/v1/connections/insurance/shipsurance-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'policy_id'
            },
        ]
    },
    '/v1/connections/insurance/shipsurance-DELETE': {
        'parameters': [
        ]
    },
    '/v1/labels/{label_id}/return-POST': {
        'parameters': [
            {
                'name': 'label_id'
            },
            {
                'name': 'charge_event'
            },
            {
                'name': 'label_layout'
            },
            {
                'name': 'label_format'
            },
            {
                'name': 'label_download_type'
            },
            {
                'name': 'display_scheme'
            },
            {
                'name': 'label_image_id'
            },
        ]
    },
    '/v1/labels/external_shipment_id/{external_shipment_id}-GET': {
        'parameters': [
            {
                'name': 'external_shipment_id'
            },
            {
                'name': 'label_download_type'
            },
        ]
    },
    '/v1/labels/{label_id}-GET': {
        'parameters': [
            {
                'name': 'label_id'
            },
            {
                'name': 'label_download_type'
            },
        ]
    },
    '/v1/labels/{label_id}/track-GET': {
        'parameters': [
            {
                'name': 'label_id'
            },
        ]
    },
    '/v1/labels-POST': {
        'parameters': [
            {
                'name': 'label_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'shipment_id'
            },
            {
                'name': 'shipment'
            },
            {
                'name': 'ship_date'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'shipment_cost'
            },
            {
                'name': 'insurance_cost'
            },
            {
                'name': 'requested_comparison_amount'
            },
            {
                'name': 'tracking_number'
            },
            {
                'name': 'is_return_label'
            },
            {
                'name': 'rma_number'
            },
            {
                'name': 'is_international'
            },
            {
                'name': 'batch_id'
            },
            {
                'name': 'carrier_id'
            },
            {
                'name': 'charge_event'
            },
            {
                'name': 'outbound_label_id'
            },
            {
                'name': 'service_code'
            },
            {
                'name': 'test_label'
            },
            {
                'name': 'package_code'
            },
            {
                'name': 'validate_address'
            },
            {
                'name': 'voided'
            },
            {
                'name': 'voided_at'
            },
            {
                'name': 'label_download_type'
            },
            {
                'name': 'label_format'
            },
            {
                'name': 'display_scheme'
            },
            {
                'name': 'label_layout'
            },
            {
                'name': 'trackable'
            },
            {
                'name': 'label_image_id'
            },
            {
                'name': 'carrier_code'
            },
            {
                'name': 'tracking_status'
            },
            {
                'name': 'label_download'
            },
            {
                'name': 'form_download'
            },
            {
                'name': 'insurance_claim'
            },
            {
                'name': 'packages'
            },
            {
                'name': 'alternative_identifiers'
            },
        ]
    },
    '/v1/labels/{label_id}/void-PUT': {
        'parameters': [
            {
                'name': 'label_id'
            },
        ]
    },
    '/v1/labels-GET': {
        'parameters': [
            {
                'name': 'label_status'
            },
            {
                'name': 'service_code'
            },
            {
                'name': 'carrier_id'
            },
            {
                'name': 'tracking_number'
            },
            {
                'name': 'batch_id'
            },
            {
                'name': 'rate_id'
            },
            {
                'name': 'shipment_id'
            },
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'created_at_start'
            },
            {
                'name': 'created_at_end'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'sort_dir'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/v1/labels/rates/{rate_id}-POST': {
        'parameters': [
            {
                'name': 'rate_id'
            },
            {
                'name': 'validate_address'
            },
            {
                'name': 'label_layout'
            },
            {
                'name': 'label_format'
            },
            {
                'name': 'label_download_type'
            },
            {
                'name': 'display_scheme'
            },
        ]
    },
    '/v1/labels/shipment/{shipment_id}-POST': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
            {
                'name': 'validate_address'
            },
            {
                'name': 'label_layout'
            },
            {
                'name': 'label_format'
            },
            {
                'name': 'label_download_type'
            },
            {
                'name': 'display_scheme'
            },
        ]
    },
    '/v1/manifests/{manifest_id}-GET': {
        'parameters': [
            {
                'name': 'manifest_id'
            },
        ]
    },
    '/v1/manifests/requests/{manifest_request_id}-GET': {
        'parameters': [
            {
                'name': 'manifest_request_id'
            },
        ]
    },
    '/v1/manifests-POST': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
            {
                'name': 'excluded_label_ids'
            },
            {
                'name': 'label_ids'
            },
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'ship_date'
            },
        ]
    },
    '/v1/manifests-GET': {
        'parameters': [
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'ship_date_start'
            },
            {
                'name': 'ship_date_end'
            },
            {
                'name': 'created_at_start'
            },
            {
                'name': 'created_at_end'
            },
            {
                'name': 'carrier_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'label_ids'
            },
        ]
    },
    '/v1/pickups/{pickup_id}-GET': {
        'parameters': [
            {
                'name': 'pickup_id'
            },
        ]
    },
    '/v1/pickups-GET': {
        'parameters': [
            {
                'name': 'carrier_id'
            },
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'created_at_start'
            },
            {
                'name': 'created_at_end'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/pickups-POST': {
        'parameters': [
            {
                'name': 'pickup_id'
            },
            {
                'name': 'label_ids'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'cancelled_at'
            },
            {
                'name': 'carrier_id'
            },
            {
                'name': 'confirmation_number'
            },
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'pickup_address'
            },
            {
                'name': 'contact_details'
            },
            {
                'name': 'pickup_notes'
            },
            {
                'name': 'pickup_window'
            },
            {
                'name': 'pickup_windows'
            },
        ]
    },
    '/v1/pickups/{pickup_id}-DELETE': {
        'parameters': [
            {
                'name': 'pickup_id'
            },
        ]
    },
    '/v1/packages-POST': {
        'parameters': [
            {
                'name': 'package_code'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'package_id'
            },
            {
                'name': 'dimensions'
            },
        ]
    },
    '/v1/packages/{package_id}-DELETE': {
        'parameters': [
            {
                'name': 'package_id'
            },
        ]
    },
    '/v1/packages/{package_id}-GET': {
        'parameters': [
            {
                'name': 'package_id'
            },
        ]
    },
    '/v1/packages-GET': {
        'parameters': [
        ]
    },
    '/v1/packages/{package_id}-PUT': {
        'parameters': [
            {
                'name': 'package_code'
            },
            {
                'name': 'name'
            },
            {
                'name': 'package_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'package_id'
            },
            {
                'name': 'dimensions'
            },
        ]
    },
    '/v1/rates/bulk-POST': {
        'parameters': [
            {
                'name': 'rate_options'
            },
        ]
    },
    '/v1/rates/{rate_id}-GET': {
        'parameters': [
            {
                'name': 'rate_id'
            },
        ]
    },
    '/v1/rates-POST': {
        'parameters': [
            {
                'name': 'rate_options'
            },
        ]
    },
    '/v1/rates/estimate-POST': {
        'parameters': [
            {
                'name': 'from_country_code'
            },
            {
                'name': 'from_postal_code'
            },
            {
                'name': 'from_city_locality'
            },
            {
                'name': 'from_state_province'
            },
            {
                'name': 'to_country_code'
            },
            {
                'name': 'to_postal_code'
            },
            {
                'name': 'to_city_locality'
            },
            {
                'name': 'to_state_province'
            },
            {
                'name': 'weight'
            },
            {
                'name': 'dimensions'
            },
            {
                'name': 'confirmation'
            },
            {
                'name': 'address_residential_indicator'
            },
            {
                'name': 'ship_date'
            },
        ]
    },
    '/v1/service_points/{carrier_code}/{country_code}/{service_point_id}-GET': {
        'parameters': [
            {
                'name': 'carrier_code'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'service_point_id'
            },
        ]
    },
    '/v1/service_points/list-POST': {
        'parameters': [
            {
                'name': 'address_query'
            },
            {
                'name': 'address'
            },
            {
                'name': 'providers'
            },
            {
                'name': 'lat'
            },
            {
                'name': 'long'
            },
            {
                'name': 'radius'
            },
            {
                'name': 'max_results'
            },
        ]
    },
    '/v1/shipments/external_shipment_id/{external_shipment_id}-GET': {
        'parameters': [
            {
                'name': 'external_shipment_id'
            },
        ]
    },
    '/v1/shipments/{shipment_id}-GET': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
        ]
    },
    '/v1/shipments/{shipment_id}/rates-GET': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
            {
                'name': 'created_at_start'
            },
        ]
    },
    '/v1/shipments/{shipment_id}/tags-GET': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
        ]
    },
    '/v1/shipments/recognize-PUT': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'shipment'
            },
        ]
    },
    '/v1/shipments/{shipment_id}-PUT': {
        'parameters': [
            {
                'name': 'ship_to'
            },
            {
                'name': 'ship_from'
            },
            {
                'name': 'shipment_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'shipment_id'
            },
            {
                'name': 'carrier_id'
            },
            {
                'name': 'service_code'
            },
            {
                'name': 'external_order_id'
            },
            {
                'name': 'items'
            },
            {
                'name': 'tax_identifiers'
            },
            {
                'name': 'external_shipment_id'
            },
            {
                'name': 'shipment_number'
            },
            {
                'name': 'ship_date'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'modified_at'
            },
            {
                'name': 'shipment_status'
            },
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'return_to'
            },
            {
                'name': 'is_return'
            },
            {
                'name': 'confirmation'
            },
            {
                'name': 'customs'
            },
            {
                'name': 'advanced_options'
            },
            {
                'name': 'insurance_provider'
            },
            {
                'name': 'order_source_code'
            },
            {
                'name': 'packages'
            },
            {
                'name': 'total_weight'
            },
            {
                'name': 'comparison_rate_type'
            },
            {
                'name': 'validate_address'
            },
        ]
    },
    '/v1/shipments/{shipment_id}/tags/{tag_name}-POST': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
            {
                'name': 'tag_name'
            },
        ]
    },
    '/v1/shipments/{shipment_id}/tags/{tag_name}-DELETE': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
            {
                'name': 'tag_name'
            },
        ]
    },
    '/v1/shipments-GET': {
        'parameters': [
            {
                'name': 'shipment_status'
            },
            {
                'name': 'batch_id'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'created_at_start'
            },
            {
                'name': 'created_at_end'
            },
            {
                'name': 'modified_at_start'
            },
            {
                'name': 'modified_at_end'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'sales_order_id'
            },
            {
                'name': 'sort_dir'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/v1/shipments-POST': {
        'parameters': [
            {
                'name': 'shipments'
            },
        ]
    },
    '/v1/shipments/{shipment_id}/cancel-PUT': {
        'parameters': [
            {
                'name': 'shipment_id'
            },
        ]
    },
    '/v1/shipments/tags-PUT': {
        'parameters': [
            {
                'name': 'shipments_tags'
            },
        ]
    },
    '/v1/tags/{tag_name}-POST': {
        'parameters': [
            {
                'name': 'tag_name'
            },
        ]
    },
    '/v1/tags/{tag_name}-DELETE': {
        'parameters': [
            {
                'name': 'tag_name'
            },
        ]
    },
    '/v1/tags/{tag_name}/{new_tag_name}-PUT': {
        'parameters': [
            {
                'name': 'tag_name'
            },
            {
                'name': 'new_tag_name'
            },
        ]
    },
    '/v1/tags-GET': {
        'parameters': [
        ]
    },
    '/v1/tokens/ephemeral-POST': {
        'parameters': [
            {
                'name': 'redirect'
            },
        ]
    },
    '/v1/tracking-GET': {
        'parameters': [
            {
                'name': 'carrier_code'
            },
            {
                'name': 'tracking_number'
            },
        ]
    },
    '/v1/tracking/start-POST': {
        'parameters': [
            {
                'name': 'carrier_code'
            },
            {
                'name': 'tracking_number'
            },
        ]
    },
    '/v1/tracking/stop-POST': {
        'parameters': [
            {
                'name': 'carrier_code'
            },
            {
                'name': 'tracking_number'
            },
        ]
    },
    '/v1/warehouses/{warehouse_id}-GET': {
        'parameters': [
            {
                'name': 'warehouse_id'
            },
        ]
    },
    '/v1/warehouses/{warehouse_id}/settings-PUT': {
        'parameters': [
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'is_default'
            },
        ]
    },
    '/v1/warehouses-POST': {
        'parameters': [
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'name'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'origin_address'
            },
            {
                'name': 'return_address'
            },
        ]
    },
    '/v1/warehouses/{warehouse_id}-PUT': {
        'parameters': [
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'warehouse_id'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'name'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'origin_address'
            },
            {
                'name': 'return_address'
            },
        ]
    },
    '/v1/warehouses/{warehouse_id}-DELETE': {
        'parameters': [
            {
                'name': 'warehouse_id'
            },
        ]
    },
    '/v1/warehouses-GET': {
        'parameters': [
        ]
    },
    '/v1/environment/webhooks/{webhook_id}-GET': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/v1/environment/webhooks-POST': {
        'parameters': [
            {
                'name': 'event'
            },
            {
                'name': 'url'
            },
            {
                'name': 'headers'
            },
        ]
    },
    '/v1/environment/webhooks/{webhook_id}-PUT': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
            {
                'name': 'url'
            },
            {
                'name': 'headers'
            },
        ]
    },
    '/v1/environment/webhooks/{webhook_id}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/v1/environment/webhooks-GET': {
        'parameters': [
        ]
    },
};