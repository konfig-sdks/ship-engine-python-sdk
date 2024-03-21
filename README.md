<div align="left">

[![Visit Shipengine](./header.png)](https://shipengine.com)

# Shipengine<a id="shipengine"></a>

ShipEngine's easy-to-use REST API lets you manage all of your shipping needs without worrying about the complexities of different carrier APIs and protocols. We handle all the heavy lifting so you can focus on providing a first-class shipping experience for your customers at the best possible prices.

Each of ShipEngine's features can be used by itself or in conjunction with each other to build powerful shipping functionality into your application or service.

## Getting Started<a id="getting-started"></a>
If you're new to REST APIs then be sure to read our [introduction to REST](https://www.shipengine.com/docs/rest/) to understand the basics.  Learn how to [authenticate yourself to ShipEngine](https://www.shipengine.com/docs/auth/), and then use our [sandbox environment](https://www.shipengine.com/docs/sandbox/) to kick the tires and get familiar with our API. If you run into any problems, then be sure to check the [error handling guide](https://www.shipengine.com/docs/errors/) for tips.

Here are some step-by-step **tutorials** to get you started:

  - [Learn how to create your first shipping label](https://www.shipengine.com/docs/labels/create-a-label/)
  - [Calculate shipping costs and compare rates across carriers](https://www.shipengine.com/docs/rates/)
  - [Track packages on-demand or in real time](https://www.shipengine.com/docs/tracking/)
  - [Validate mailing addresses anywhere on Earth](https://www.shipengine.com/docs/addresses/validation/)


## Shipping Labels for Every Major Carrier<a id="shipping-labels-for-every-major-carrier"></a>
ShipEngine makes it easy to [create shipping labels for any carrier](https://www.shipengine.com/docs/labels/create-a-label/) and [download them](https://www.shipengine.com/docs/labels/downloading/) in a [variety of file formats](https://www.shipengine.com/docs/labels/formats/). You can even customize labels with your own [messages](https://www.shipengine.com/docs/labels/messages/) and [images](https://www.shipengine.com/docs/labels/branding/).


## Real-Time Package Tracking<a id="real-time-package-tracking"></a>
With ShipEngine you can [get the current status of a package](https://www.shipengine.com/docs/tracking/) or [subscribe to real-time tracking updates](https://www.shipengine.com/docs/tracking/webhooks/) via webhooks. You can also create [custimized tracking pages](https://www.shipengine.com/docs/tracking/branded-tracking-page/) with your own branding so your customers will always know where their package is.


## Compare Shipping Costs Across Carriers<a id="compare-shipping-costs-across-carriers"></a>
Make sure you ship as cost-effectively as possible by [comparing rates across carriers](https://www.shipengine.com/docs/rates/get-shipment-rates/) using the ShipEngine Rates API. Or if you don't know the full shipment details yet, then you can [get rate estimates](https://www.shipengine.com/docs/rates/estimate/) with limited address info.


## Worldwide Address Validation<a id="worldwide-address-validation"></a>
ShipEngine supports [address validation](https://www.shipengine.com/docs/addresses/validation/) for virtually [every country on Earth](https://www.shipengine.com/docs/addresses/validation/countries/), including the United States, Canada, Great Britain, Australia, Germany, France, Norway, Spain, Sweden, Israel, Italy, and over 160 others.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`shipengine.account.create_image`](#shipengineaccountcreate_image)
  * [`shipengine.account.delete_image_by_id`](#shipengineaccountdelete_image_by_id)
  * [`shipengine.account.get_image_by_id`](#shipengineaccountget_image_by_id)
  * [`shipengine.account.list_images`](#shipengineaccountlist_images)
  * [`shipengine.account.list_settings`](#shipengineaccountlist_settings)
  * [`shipengine.account.update_image_by_id`](#shipengineaccountupdate_image_by_id)
  * [`shipengine.addresses.address`](#shipengineaddressesaddress)
  * [`shipengine.addresses.address_0`](#shipengineaddressesaddress_0)
  * [`shipengine.batches.add_to_batch`](#shipenginebatchesadd_to_batch)
  * [`shipengine.batches.batch`](#shipenginebatchesbatch)
  * [`shipengine.batches.batch_0`](#shipenginebatchesbatch_0)
  * [`shipengine.batches.batch_1`](#shipenginebatchesbatch_1)
  * [`shipengine.batches.batch_2`](#shipenginebatchesbatch_2)
  * [`shipengine.batches.batches`](#shipenginebatchesbatches)
  * [`shipengine.batches.get_by_external_id`](#shipenginebatchesget_by_external_id)
  * [`shipengine.batches.get_by_id`](#shipenginebatchesget_by_id)
  * [`shipengine.batches.get_errors`](#shipenginebatchesget_errors)
  * [`shipengine.batches.remove_from_batch`](#shipenginebatchesremove_from_batch)
  * [`shipengine.carrier_accounts.carrier`](#shipenginecarrier_accountscarrier)
  * [`shipengine.carrier_accounts.carrier_0`](#shipenginecarrier_accountscarrier_0)
  * [`shipengine.carrier_accounts.get_settings`](#shipenginecarrier_accountsget_settings)
  * [`shipengine.carrier_accounts.update_settings`](#shipenginecarrier_accountsupdate_settings)
  * [`shipengine.carriers.add_funds_to_carrier`](#shipenginecarriersadd_funds_to_carrier)
  * [`shipengine.carriers.carriers`](#shipenginecarrierscarriers)
  * [`shipengine.carriers.disconnect_by_id`](#shipenginecarriersdisconnect_by_id)
  * [`shipengine.carriers.get_by_id`](#shipenginecarriersget_by_id)
  * [`shipengine.carriers.get_options`](#shipenginecarriersget_options)
  * [`shipengine.carriers.list_package_types`](#shipenginecarrierslist_package_types)
  * [`shipengine.carriers.list_services`](#shipenginecarrierslist_services)
  * [`shipengine.downloads.file`](#shipenginedownloadsfile)
  * [`shipengine.insurance.auto_fund_account`](#shipengineinsuranceauto_fund_account)
  * [`shipengine.insurance.get_funds_balance`](#shipengineinsuranceget_funds_balance)
  * [`shipengine.insurance.insurer`](#shipengineinsuranceinsurer)
  * [`shipengine.insurance.insurer_0`](#shipengineinsuranceinsurer_0)
  * [`shipengine.labels.create_return_label`](#shipenginelabelscreate_return_label)
  * [`shipengine.labels.get_by_external_shipment_id`](#shipenginelabelsget_by_external_shipment_id)
  * [`shipengine.labels.get_by_id`](#shipenginelabelsget_by_id)
  * [`shipengine.labels.get_tracking_info`](#shipenginelabelsget_tracking_info)
  * [`shipengine.labels.label`](#shipenginelabelslabel)
  * [`shipengine.labels.label_0`](#shipenginelabelslabel_0)
  * [`shipengine.labels.labels`](#shipenginelabelslabels)
  * [`shipengine.labels.purchase_label_with_rate_id`](#shipenginelabelspurchase_label_with_rate_id)
  * [`shipengine.labels.purchase_label_with_shipment_id`](#shipenginelabelspurchase_label_with_shipment_id)
  * [`shipengine.manifests.get_by_id`](#shipenginemanifestsget_by_id)
  * [`shipengine.manifests.get_request_by_id`](#shipenginemanifestsget_request_by_id)
  * [`shipengine.manifests.manifest`](#shipenginemanifestsmanifest)
  * [`shipengine.manifests.manifests`](#shipenginemanifestsmanifests)
  * [`shipengine.package_pickups.get_by_id`](#shipenginepackage_pickupsget_by_id)
  * [`shipengine.package_pickups.list_scheduled_pickups`](#shipenginepackage_pickupslist_scheduled_pickups)
  * [`shipengine.package_pickups.pickup`](#shipenginepackage_pickupspickup)
  * [`shipengine.package_pickups.remove_scheduled_pickup`](#shipenginepackage_pickupsremove_scheduled_pickup)
  * [`shipengine.package_types.create_custom_package_type`](#shipenginepackage_typescreate_custom_package_type)
  * [`shipengine.package_types.delete_custom_package_by_id`](#shipenginepackage_typesdelete_custom_package_by_id)
  * [`shipengine.package_types.get_by_id`](#shipenginepackage_typesget_by_id)
  * [`shipengine.package_types.list_custom_package_types`](#shipenginepackage_typeslist_custom_package_types)
  * [`shipengine.package_types.update_custom_package_type_by_id`](#shipenginepackage_typesupdate_custom_package_type_by_id)
  * [`shipengine.rates.get_bulk_shipment_rates`](#shipengineratesget_bulk_shipment_rates)
  * [`shipengine.rates.get_by_id`](#shipengineratesget_by_id)
  * [`shipengine.rates.rates`](#shipengineratesrates)
  * [`shipengine.rates.rates_0`](#shipengineratesrates_0)
  * [`shipengine.service_points.get_by_id`](#shipengineservice_pointsget_by_id)
  * [`shipengine.service_points.get_by_location`](#shipengineservice_pointsget_by_location)
  * [`shipengine.shipments.get_by_external_id`](#shipengineshipmentsget_by_external_id)
  * [`shipengine.shipments.get_by_id`](#shipengineshipmentsget_by_id)
  * [`shipengine.shipments.get_rates_for_shipment`](#shipengineshipmentsget_rates_for_shipment)
  * [`shipengine.shipments.get_tags_by_id`](#shipengineshipmentsget_tags_by_id)
  * [`shipengine.shipments.shipment`](#shipengineshipmentsshipment)
  * [`shipengine.shipments.shipment_0`](#shipengineshipmentsshipment_0)
  * [`shipengine.shipments.shipment_1`](#shipengineshipmentsshipment_1)
  * [`shipengine.shipments.shipment_2`](#shipengineshipmentsshipment_2)
  * [`shipengine.shipments.shipments`](#shipengineshipmentsshipments)
  * [`shipengine.shipments.shipments_0`](#shipengineshipmentsshipments_0)
  * [`shipengine.shipments.shipments_1`](#shipengineshipmentsshipments_1)
  * [`shipengine.shipments.update_tags`](#shipengineshipmentsupdate_tags)
  * [`shipengine.tags.tag`](#shipenginetagstag)
  * [`shipengine.tags.tag_0`](#shipenginetagstag_0)
  * [`shipengine.tags.tag_1`](#shipenginetagstag_1)
  * [`shipengine.tags.tags`](#shipenginetagstags)
  * [`shipengine.tokens.generate_ephemeral_token`](#shipenginetokensgenerate_ephemeral_token)
  * [`shipengine.tracking.info_retrieval`](#shipenginetrackinginfo_retrieval)
  * [`shipengine.tracking.tracking`](#shipenginetrackingtracking)
  * [`shipengine.tracking.tracking_0`](#shipenginetrackingtracking_0)
  * [`shipengine.warehouses.get_by_id`](#shipenginewarehousesget_by_id)
  * [`shipengine.warehouses.update_settings`](#shipenginewarehousesupdate_settings)
  * [`shipengine.warehouses.warehouse`](#shipenginewarehouseswarehouse)
  * [`shipengine.warehouses.warehouse_0`](#shipenginewarehouseswarehouse_0)
  * [`shipengine.warehouses.warehouse_1`](#shipenginewarehouseswarehouse_1)
  * [`shipengine.warehouses.warehouses`](#shipenginewarehouseswarehouses)
  * [`shipengine.webhooks.get_by_id`](#shipenginewebhooksget_by_id)
  * [`shipengine.webhooks.webhook`](#shipenginewebhookswebhook)
  * [`shipengine.webhooks.webhook_0`](#shipenginewebhookswebhook_0)
  * [`shipengine.webhooks.webhook_1`](#shipenginewebhookswebhook_1)
  * [`shipengine.webhooks.webhooks`](#shipenginewebhookswebhooks)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=ShipEngine&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from ship_engine_python_sdk import ShipEngine, ApiException

shipengine = ShipEngine(

        api_key = 'YOUR_API_KEY',
)

try:
    # Create an Account Image
    create_image_response = shipengine.account.create_image(
        label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
        name="My logo",
        is_default=False,
        image_content_type="image/png",
        image_data="iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAiVJREFUSEu91j3IeVEcB/CvSTIoBrFSikEZMdjsjExeUspgUEp5SUpeshrIgEFJJmWwMZHJQGHDhJSXTPfpnH/8ebzd56HnN93u7ZzP/f1+55x7Ob1ejxEKheByufh0HI9HrFYrcKbTKUMu5HI5BALBx5zNZoPxeAySAGc2mzF8Pp/e+BR0Ash8u93uHyKVSnH54J2Mvs8zn8//I6RO70L3xt8g70CPXvAu8hvoWQUeIj+BXpX4KcIGegWQOV4izyA2AGvkHsQW+BFyCUkkEiwWC9Ybl1W5Ls8ZMoAABCIbmE3cINFoFMFgEEajEeVyGSKRCJ1OB3q9ns5nMpmQTCaxXq9/l8loNEKj0YDX66UACYvFQq9brRYcDgdUKhU9RD/SEwLm83lEIhGUSiX0+33E4/GrU5otRMs1mUyYbDYLu90OhUJBMzhlZbPZ4Pf7odFo4HQ6b1rABqJIvV5nttstLc0pSIn2+z0tTy6XQ6FQoI/a7TZ0Ot0V9gqiiMFgYKrVKm0yieVyCZ/PB6vVSpF0Ok2zJHEqIY/HYw1RxOfzMYlE4jwoEAhAJpPBbDZf9eBwOCCVSsHtdp9f6FJ6egorlUqmVqvRfjSbTXS7XXg8nptP8Svk0RF01ROtVguSUTgchlgsPpeOZBaLxTAcDlEsFpHJZPC9XM8yoshgMGBCoRBdQWTCU7hcLjohWb5kM6rValQqlfMKfLbbb77xf/K38hf/XV9ilOpnLqvnogAAAABJRU5ErkJggg==",
        created_at="2018-09-23T15:00:00.000Z",
        modified_at="2018-09-23T15:00:00.000Z",
    )
    print(create_image_response)
except ApiException as e:
    print("Exception when calling AccountApi.create_image: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from ship_engine_python_sdk import ShipEngine, ApiException

shipengine = ShipEngine(

        api_key = 'YOUR_API_KEY',
)

async def main():
    try:
        # Create an Account Image
        create_image_response = await shipengine.account.acreate_image(
            label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
            name="My logo",
            is_default=False,
            image_content_type="image/png",
            image_data="iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAiVJREFUSEu91j3IeVEcB/CvSTIoBrFSikEZMdjsjExeUspgUEp5SUpeshrIgEFJJmWwMZHJQGHDhJSXTPfpnH/8ebzd56HnN93u7ZzP/f1+55x7Ob1ejxEKheByufh0HI9HrFYrcKbTKUMu5HI5BALBx5zNZoPxeAySAGc2mzF8Pp/e+BR0Ash8u93uHyKVSnH54J2Mvs8zn8//I6RO70L3xt8g70CPXvAu8hvoWQUeIj+BXpX4KcIGegWQOV4izyA2AGvkHsQW+BFyCUkkEiwWC9Ybl1W5Ls8ZMoAABCIbmE3cINFoFMFgEEajEeVyGSKRCJ1OB3q9ns5nMpmQTCaxXq9/l8loNEKj0YDX66UACYvFQq9brRYcDgdUKhU9RD/SEwLm83lEIhGUSiX0+33E4/GrU5otRMs1mUyYbDYLu90OhUJBMzhlZbPZ4Pf7odFo4HQ6b1rABqJIvV5nttstLc0pSIn2+z0tTy6XQ6FQoI/a7TZ0Ot0V9gqiiMFgYKrVKm0yieVyCZ/PB6vVSpF0Ok2zJHEqIY/HYw1RxOfzMYlE4jwoEAhAJpPBbDZf9eBwOCCVSsHtdp9f6FJ6egorlUqmVqvRfjSbTXS7XXg8nptP8Svk0RF01ROtVguSUTgchlgsPpeOZBaLxTAcDlEsFpHJZPC9XM8yoshgMGBCoRBdQWTCU7hcLjohWb5kM6rValQqlfMKfLbbb77xf/K38hf/XV9ilOpnLqvnogAAAABJRU5ErkJggg==",
            created_at="2018-09-23T15:00:00.000Z",
            modified_at="2018-09-23T15:00:00.000Z",
        )
        print(create_image_response)
    except ApiException as e:
        print("Exception when calling AccountApi.create_image: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from ship_engine_python_sdk import ShipEngine, ApiException

shipengine = ShipEngine(

        api_key = 'YOUR_API_KEY',
)

try:
    # Create an Account Image
    create_image_response = shipengine.account.raw.create_image(
        label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
        name="My logo",
        is_default=False,
        image_content_type="image/png",
        image_data="iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAiVJREFUSEu91j3IeVEcB/CvSTIoBrFSikEZMdjsjExeUspgUEp5SUpeshrIgEFJJmWwMZHJQGHDhJSXTPfpnH/8ebzd56HnN93u7ZzP/f1+55x7Ob1ejxEKheByufh0HI9HrFYrcKbTKUMu5HI5BALBx5zNZoPxeAySAGc2mzF8Pp/e+BR0Ash8u93uHyKVSnH54J2Mvs8zn8//I6RO70L3xt8g70CPXvAu8hvoWQUeIj+BXpX4KcIGegWQOV4izyA2AGvkHsQW+BFyCUkkEiwWC9Ybl1W5Ls8ZMoAABCIbmE3cINFoFMFgEEajEeVyGSKRCJ1OB3q9ns5nMpmQTCaxXq9/l8loNEKj0YDX66UACYvFQq9brRYcDgdUKhU9RD/SEwLm83lEIhGUSiX0+33E4/GrU5otRMs1mUyYbDYLu90OhUJBMzhlZbPZ4Pf7odFo4HQ6b1rABqJIvV5nttstLc0pSIn2+z0tTy6XQ6FQoI/a7TZ0Ot0V9gqiiMFgYKrVKm0yieVyCZ/PB6vVSpF0Ok2zJHEqIY/HYw1RxOfzMYlE4jwoEAhAJpPBbDZf9eBwOCCVSsHtdp9f6FJ6egorlUqmVqvRfjSbTXS7XXg8nptP8Svk0RF01ROtVguSUTgchlgsPpeOZBaLxTAcDlEsFpHJZPC9XM8yoshgMGBCoRBdQWTCU7hcLjohWb5kM6rValQqlfMKfLbbb77xf/K38hf/XV9ilOpnLqvnogAAAABJRU5ErkJggg==",
        created_at="2018-09-23T15:00:00.000Z",
        modified_at="2018-09-23T15:00:00.000Z",
    )
    pprint(create_image_response.body)
    pprint(create_image_response.body["label_image_id"])
    pprint(create_image_response.body["name"])
    pprint(create_image_response.body["is_default"])
    pprint(create_image_response.body["image_content_type"])
    pprint(create_image_response.body["image_data"])
    pprint(create_image_response.body["created_at"])
    pprint(create_image_response.body["modified_at"])
    pprint(create_image_response.headers)
    pprint(create_image_response.status)
    pprint(create_image_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountApi.create_image: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `shipengine.account.create_image`<a id="shipengineaccountcreate_image"></a>

Create an Account Image

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_image_response = shipengine.account.create_image(
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
    name="My logo",
    is_default=False,
    image_content_type="image/png",
    image_data="iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAiVJREFUSEu91j3IeVEcB/CvSTIoBrFSikEZMdjsjExeUspgUEp5SUpeshrIgEFJJmWwMZHJQGHDhJSXTPfpnH/8ebzd56HnN93u7ZzP/f1+55x7Ob1ejxEKheByufh0HI9HrFYrcKbTKUMu5HI5BALBx5zNZoPxeAySAGc2mzF8Pp/e+BR0Ash8u93uHyKVSnH54J2Mvs8zn8//I6RO70L3xt8g70CPXvAu8hvoWQUeIj+BXpX4KcIGegWQOV4izyA2AGvkHsQW+BFyCUkkEiwWC9Ybl1W5Ls8ZMoAABCIbmE3cINFoFMFgEEajEeVyGSKRCJ1OB3q9ns5nMpmQTCaxXq9/l8loNEKj0YDX66UACYvFQq9brRYcDgdUKhU9RD/SEwLm83lEIhGUSiX0+33E4/GrU5otRMs1mUyYbDYLu90OhUJBMzhlZbPZ4Pf7odFo4HQ6b1rABqJIvV5nttstLc0pSIn2+z0tTy6XQ6FQoI/a7TZ0Ot0V9gqiiMFgYKrVKm0yieVyCZ/PB6vVSpF0Ok2zJHEqIY/HYw1RxOfzMYlE4jwoEAhAJpPBbDZf9eBwOCCVSsHtdp9f6FJ6egorlUqmVqvRfjSbTXS7XXg8nptP8Svk0RF01ROtVguSUTgchlgsPpeOZBaLxTAcDlEsFpHJZPC9XM8yoshgMGBCoRBdQWTCU7hcLjohWb5kM6rValQqlfMKfLbbb77xf/K38hf/XV9ilOpnLqvnogAAAABJRU5ErkJggg==",
    created_at="2018-09-23T15:00:00.000Z",
    modified_at="2018-09-23T15:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_image_id: [`ImageId`](./ship_engine_python_sdk/type/image_id.py)<a id="label_image_id-imageidship_engine_python_sdktypeimage_idpy"></a>

A string that uniquely identifies the image. This ID is generated by ShipEngine when the image is uploaded. 

##### name: `str`<a id="name-str"></a>

A human readable name for the image. 

##### is_default: `bool`<a id="is_default-bool"></a>

Indicates whether this image is set as default. 

##### image_content_type: `str`<a id="image_content_type-str"></a>

The file type of the image.  

##### image_data: `str`<a id="image_data-str"></a>

A base64 encoded string representation of the image. 

##### created_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="created_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the image was created in ShipEngine.

##### modified_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="modified_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the image was modified in ShipEngine.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountSettingsImages`](./ship_engine_python_sdk/type/account_settings_images.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccountSettingsImages`](./ship_engine_python_sdk/pydantic/account_settings_images.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/account/settings/images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.account.delete_image_by_id`<a id="shipengineaccountdelete_image_by_id"></a>

Delete Account Image By Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_image_by_id_response = shipengine.account.delete_image_by_id(
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_image_id: [`ImageId`](./ship_engine_python_sdk/type/.py)<a id="label_image_id-imageidship_engine_python_sdktypepy"></a>

Label Image Id

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/account/settings/images/{label_image_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.account.get_image_by_id`<a id="shipengineaccountget_image_by_id"></a>

Retrieve information for an account image.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_image_by_id_response = shipengine.account.get_image_by_id(
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_image_id: [`ImageId`](./ship_engine_python_sdk/type/.py)<a id="label_image_id-imageidship_engine_python_sdktypepy"></a>

Label Image Id

#### 🔄 Return<a id="🔄-return"></a>

[`AccountSettingsImages`](./ship_engine_python_sdk/pydantic/account_settings_images.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/account/settings/images/{label_image_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.account.list_images`<a id="shipengineaccountlist_images"></a>

List all account images for the ShipEngine account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_images_response = shipengine.account.list_images()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PagedListResponseBody`](./ship_engine_python_sdk/pydantic/paged_list_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/account/settings/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.account.list_settings`<a id="shipengineaccountlist_settings"></a>

List all account settings for the ShipEngine account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_settings_response = shipengine.account.list_settings()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AccountSettings`](./ship_engine_python_sdk/pydantic/account_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/account/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.account.update_image_by_id`<a id="shipengineaccountupdate_image_by_id"></a>

Update information for an account image.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_image_by_id_response = shipengine.account.update_image_by_id(
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
    name="My logo",
    is_default=False,
    image_content_type="image/png",
    image_data="iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAiVJREFUSEu91j3IeVEcB/CvSTIoBrFSikEZMdjsjExeUspgUEp5SUpeshrIgEFJJmWwMZHJQGHDhJSXTPfpnH/8ebzd56HnN93u7ZzP/f1+55x7Ob1ejxEKheByufh0HI9HrFYrcKbTKUMu5HI5BALBx5zNZoPxeAySAGc2mzF8Pp/e+BR0Ash8u93uHyKVSnH54J2Mvs8zn8//I6RO70L3xt8g70CPXvAu8hvoWQUeIj+BXpX4KcIGegWQOV4izyA2AGvkHsQW+BFyCUkkEiwWC9Ybl1W5Ls8ZMoAABCIbmE3cINFoFMFgEEajEeVyGSKRCJ1OB3q9ns5nMpmQTCaxXq9/l8loNEKj0YDX66UACYvFQq9brRYcDgdUKhU9RD/SEwLm83lEIhGUSiX0+33E4/GrU5otRMs1mUyYbDYLu90OhUJBMzhlZbPZ4Pf7odFo4HQ6b1rABqJIvV5nttstLc0pSIn2+z0tTy6XQ6FQoI/a7TZ0Ot0V9gqiiMFgYKrVKm0yieVyCZ/PB6vVSpF0Ok2zJHEqIY/HYw1RxOfzMYlE4jwoEAhAJpPBbDZf9eBwOCCVSsHtdp9f6FJ6egorlUqmVqvRfjSbTXS7XXg8nptP8Svk0RF01ROtVguSUTgchlgsPpeOZBaLxTAcDlEsFpHJZPC9XM8yoshgMGBCoRBdQWTCU7hcLjohWb5kM6rValQqlfMKfLbbb77xf/K38hf/XV9ilOpnLqvnogAAAABJRU5ErkJggg==",
    created_at="2018-09-23T15:00:00.000Z",
    modified_at="2018-09-23T15:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_image_id: [`ImageId`](./ship_engine_python_sdk/type/.py)<a id="label_image_id-imageidship_engine_python_sdktypepy"></a>

Label Image Id

##### requestBody: [`AccountSettingsImages`](./ship_engine_python_sdk/type/account_settings_images.py)<a id="requestbody-accountsettingsimagesship_engine_python_sdktypeaccount_settings_imagespy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/account/settings/images/{label_image_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.addresses.address`<a id="shipengineaddressesaddress"></a>

The address-recognition API makes it easy for you to extract address data from unstructured text, including the recipient name, line 1, line 2, city, postal code, and more.

Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine's address-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed address data is returned in the same structure that's used for other ShipEngine APIs, such as address validation, rate quotes, and shipping labels.

> **Note:** Address recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
address_response = shipengine.addresses.address(
    text="Margie McMiller at 3800 North Lamar suite 200 in austin, tx.  The zip code there is 78652.",
    address={
        "name": "John Doe",
        "phone": "+1 204-253-9411 ext. 123",
        "email": "example@example.com",
        "company_name": "The Home Depot",
        "address_line1": "1999 Bishop Grandin Blvd.",
        "address_line2": "Unit 408",
        "address_line3": "Building #7",
        "city_locality": "Winnipeg",
        "state_province": "Manitoba",
        "postal_code": "78756-3717",
        "country_code": "CA",
        "address_residential_indicator": "unknown",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

The unstructured text that contains address-related entities

##### address: [`PartialAddress`](./ship_engine_python_sdk/type/partial_address.py)<a id="address-partialaddressship_engine_python_sdktypepartial_addresspy"></a>


You can optionally provide any already-known address values. For example, you may already know the recipient's name, city, and country, and only want to parse the street address into separate lines. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ParseAddressRequestBody`](./ship_engine_python_sdk/type/parse_address_request_body.py)
The only required field is `text`, which is the text to be parsed. You can optionally also provide an `address` containing already-known values. For example, you may already know the recipient's name, city, and country, and only want to parse the street address into separate lines. 

#### 🔄 Return<a id="🔄-return"></a>

[`ParseAddressResponseBody`](./ship_engine_python_sdk/pydantic/parse_address_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/addresses/recognize` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.addresses.address_0`<a id="shipengineaddressesaddress_0"></a>

Address validation ensures accurate addresses and can lead to reduced shipping costs by preventing address correction surcharges.
ShipEngine cross references multiple databases to validate addresses and identify potential deliverability issues.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
address_0_response = shipengine.addresses.address_0(
    body=[{"name":"Mickey and Minnie Mouse","phone":"714-781-4565","company_name":"The Walt Disney Company","address_line1":"500 South Buena Vista Street","city_locality":"Burbank","state_province":"CA","postal_code":91521,"country_code":"US"}],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ValidateAddressRequestBody`](./ship_engine_python_sdk/type/validate_address_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ValidateAddressResponseBody`](./ship_engine_python_sdk/pydantic/validate_address_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/addresses/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.add_to_batch`<a id="shipenginebatchesadd_to_batch"></a>

Add a Shipment or Rate to a Batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_batch_response = shipengine.batches.add_to_batch(
    batch_id="se-28529731",
    shipment_ids=[
        "se-q6zgc"
    ],
    rate_ids=[
        "se-q6zgc"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

##### shipment_ids: List[`SeId`]<a id="shipment_ids-listseid"></a>

The Shipment Ids to be modified on the batch

##### rate_ids: List[`SeId`]<a id="rate_ids-listseid"></a>

Array of Rate IDs to be modifed on the batch

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ModifyBatch`](./ship_engine_python_sdk/type/modify_batch.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.batch`<a id="shipenginebatchesbatch"></a>

Create a Batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batch_response = shipengine.batches.batch(
    body=None,
    external_batch_id="se-28529731",
    batch_notes="This is my batch",
    shipment_ids=[
        "se-q6zgc"
    ],
    rate_ids=[
        "se-q6zgc"
    ],
    process_labels={
        "ship_date": "2018-09-23T15:00:00.000Z",
        "label_layout": "4x6",
        "label_format": "pdf",
        "display_scheme": "label",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_batch_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="external_batch_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the external batch

##### batch_notes: `str`<a id="batch_notes-str"></a>

Add custom messages for a particular batch

##### shipment_ids: List[`SeId`]<a id="shipment_ids-listseid"></a>

Array of shipment IDs used in the batch

##### rate_ids: List[`SeId`]<a id="rate_ids-listseid"></a>

Array of rate IDs used in the batch

##### process_labels: [`CreateAndProcessBatchRequestBodyProcessLabels`](./ship_engine_python_sdk/type/create_and_process_batch_request_body_process_labels.py)<a id="process_labels-createandprocessbatchrequestbodyprocesslabelsship_engine_python_sdktypecreate_and_process_batch_request_body_process_labelspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateBatchRequest`](./ship_engine_python_sdk/type/create_batch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Batch`](./ship_engine_python_sdk/pydantic/batch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.batch_0`<a id="shipenginebatchesbatch_0"></a>

Update Batch By Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batch_0_response = shipengine.batches.batch_0(
    batch_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.batch_1`<a id="shipenginebatchesbatch_1"></a>

Delete Batch By Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batch_1_response = shipengine.batches.batch_1(
    batch_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.batch_2`<a id="shipenginebatchesbatch_2"></a>

Process Batch ID Labels

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batch_2_response = shipengine.batches.batch_2(
    batch_id="se-28529731",
    ship_date="2018-09-23T15:00:00.000Z",
    label_layout="4x6",
    label_format="pdf",
    display_scheme="label",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

##### ship_date: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="ship_date-datetimeship_engine_python_sdktypedate_timepy"></a>

The Ship date the batch is being processed for

##### label_layout: [`LabelLayout`](./ship_engine_python_sdk/type/label_layout.py)<a id="label_layout-labellayoutship_engine_python_sdktypelabel_layoutpy"></a>

##### label_format: [`LabelFormat`](./ship_engine_python_sdk/type/label_format.py)<a id="label_format-labelformatship_engine_python_sdktypelabel_formatpy"></a>

##### display_scheme: [`DisplayScheme`](./ship_engine_python_sdk/type/display_scheme.py)<a id="display_scheme-displayschemeship_engine_python_sdktypedisplay_schemepy"></a>

The display format that the label should be shown in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProcessBatchRequestBody`](./ship_engine_python_sdk/type/process_batch_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}/process/labels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.batches`<a id="shipenginebatchesbatches"></a>

List Batches associated with your Shipengine account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batches_response = shipengine.batches.batches(
    status="open",
    page=2,
    page_size=50,
    sort_dir="asc",
    batch_number="string_example",
    sort_by="ship_date",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: [`BatchStatus`](./ship_engine_python_sdk/type/.py)<a id="status-batchstatusship_engine_python_sdktypepy"></a>

##### page: `int`<a id="page-int"></a>

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 

##### page_size: `int`<a id="page_size-int"></a>

The number of results to return per response.

##### sort_dir: [`SortDir`](./ship_engine_python_sdk/type/.py)<a id="sort_dir-sortdirship_engine_python_sdktypepy"></a>

Controls the sort order of the query.

##### batch_number: `str`<a id="batch_number-str"></a>

Batch Number

##### sort_by: [`BatchesSortBy`](./ship_engine_python_sdk/type/.py)<a id="sort_by-batchessortbyship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ListBatchesResponseBody`](./ship_engine_python_sdk/pydantic/list_batches_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.get_by_external_id`<a id="shipenginebatchesget_by_external_id"></a>

Get Batch By External ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_external_id_response = shipengine.batches.get_by_external_id(
    external_batch_id="13553d7f-3c87-4771-bae1-c49bacef11cb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_batch_id: `str`<a id="external_batch_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Batch`](./ship_engine_python_sdk/pydantic/batch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/external_batch_id/{external_batch_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.get_by_id`<a id="shipenginebatchesget_by_id"></a>

Get Batch By ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.batches.get_by_id(
    batch_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

#### 🔄 Return<a id="🔄-return"></a>

[`Batch`](./ship_engine_python_sdk/pydantic/batch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.get_errors`<a id="shipenginebatchesget_errors"></a>

Error handling in batches are handled differently than in a single synchronous request.
You must retrieve the status of your batch by [getting a batch](https://www.shipengine.com/docs/reference/get-batch-by-id/) and getting an overview of the statuses or you can list errors directly here below to get detailed information about the errors.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_errors_response = shipengine.batches.get_errors(
    batch_id="se-28529731",
    page=2,
    pagesize=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

##### page: `int`<a id="page-int"></a>

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 

##### pagesize: `int`<a id="pagesize-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ListBatchErrorsResponseBody`](./ship_engine_python_sdk/pydantic/list_batch_errors_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}/errors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.batches.remove_from_batch`<a id="shipenginebatchesremove_from_batch"></a>

Remove a shipment or rate from a batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_from_batch_response = shipengine.batches.remove_from_batch(
    batch_id="se-28529731",
    shipment_ids=[
        "se-q6zgc"
    ],
    rate_ids=[
        "se-q6zgc"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

##### shipment_ids: List[`SeId`]<a id="shipment_ids-listseid"></a>

The Shipment Ids to be modified on the batch

##### rate_ids: List[`SeId`]<a id="rate_ids-listseid"></a>

Array of Rate IDs to be modifed on the batch

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ModifyBatch`](./ship_engine_python_sdk/type/modify_batch.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/batches/{batch_id}/remove` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carrier_accounts.carrier`<a id="shipenginecarrier_accountscarrier"></a>

Connect a carrier account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
carrier_response = shipengine.carrier_accounts.carrier(
    body=None,
    carrier_name="dhl_express",
    nickname="a",
    username="a",
    password="a",
    merchant_seller_id="a",
    mws_auth_token="a",
    email="john.doe@example.com",
    auth_code="a",
    account_number="a",
    ftp_username="a",
    ftp_password="a",
    api_key="a",
    api_secret="a",
    contract_id="a",
    client_id="a",
    pickup_number="a",
    distribution_center="a",
    ancillary_endorsement="none",
    sold_to="string_example",
    registration_id="string_example",
    software_name="string_example",
    site_id="se-28529731",
    country_code="a",
    account="a",
    passphrase="a",
    address1="a",
    address2="a",
    city="a",
    company="a",
    first_name="a",
    last_name="a",
    phone="a",
    postal_code="a",
    state="a",
    agree_to_eula=True,
    meter_number="a",
    mailer_id=0,
    profile_name="a",
    merchant_id=0,
    induction_site="a",
    activation_key="a",
    oba_email="john.doe@example.com",
    contact_name="a",
    company_name="a",
    street_line1="a",
    street_line2="a",
    street_line3="a",
    access_key="a",
    sendle_id="se-28529731",
    title="a",
    account_country_code="a",
    account_postal_code="a",
    invoice={
        "control_id": "se-28529731",
    },
    invoice_amount=3.14,
    invoice_currency_code="string_example",
    agree_to_technology_agreement=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_name: [`CarrierName`](./ship_engine_python_sdk/type/.py)<a id="carrier_name-carriernameship_engine_python_sdktypepy"></a>

The carrier name, such as `stamps_com`, `ups`, `fedex`, or `dhl_express`.

##### nickname: `str`<a id="nickname-str"></a>

Nickname

##### username: `str`<a id="username-str"></a>

Username

##### password: `str`<a id="password-str"></a>

Password

##### merchant_seller_id: `str`<a id="merchant_seller_id-str"></a>

##### mws_auth_token: `str`<a id="mws_auth_token-str"></a>

##### email: [`Email`](./ship_engine_python_sdk/type/email.py)<a id="email-emailship_engine_python_sdktypeemailpy"></a>

The email address

##### auth_code: `str`<a id="auth_code-str"></a>

Amazon UK Shipping auth code.

##### account_number: `str`<a id="account_number-str"></a>

Account number

##### ftp_username: `str`<a id="ftp_username-str"></a>

FTP username

##### ftp_password: `str`<a id="ftp_password-str"></a>

FTP password

##### api_key: `str`<a id="api_key-str"></a>

API key

##### api_secret: `str`<a id="api_secret-str"></a>

The DHL E-Commerce API secret. This field is optional, but if not set you will not be able to get rates for this account. 

##### contract_id: `str`<a id="contract_id-str"></a>

Canada Post Account Contract ID

##### client_id: `str`<a id="client_id-str"></a>

The client id

##### pickup_number: `str`<a id="pickup_number-str"></a>

The pickup number

##### distribution_center: `str`<a id="distribution_center-str"></a>

The distribution center

##### ancillary_endorsement: [`AncillaryServiceEndorsement`](./ship_engine_python_sdk/type/ancillary_service_endorsement.py)<a id="ancillary_endorsement-ancillaryserviceendorsementship_engine_python_sdktypeancillary_service_endorsementpy"></a>

##### sold_to: `str`<a id="sold_to-str"></a>

Sold To field

##### registration_id: `str`<a id="registration_id-str"></a>

##### software_name: `str`<a id="software_name-str"></a>

##### site_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="site_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the site

##### country_code: `str`<a id="country_code-str"></a>

Country code

##### account: `str`<a id="account-str"></a>

Account

##### passphrase: `str`<a id="passphrase-str"></a>

Passphrase

##### address1: `str`<a id="address1-str"></a>

Address Line 1

##### address2: `str`<a id="address2-str"></a>

Address Line 2

##### city: `str`<a id="city-str"></a>

City

##### company: `str`<a id="company-str"></a>

Company

##### first_name: `str`<a id="first_name-str"></a>

First name

##### last_name: `str`<a id="last_name-str"></a>

Last name

##### phone: `str`<a id="phone-str"></a>

Phone

##### postal_code: `str`<a id="postal_code-str"></a>

Postal code

##### state: `str`<a id="state-str"></a>

State

##### agree_to_eula: `bool`<a id="agree_to_eula-bool"></a>

Boolean signaling agreement to the Fedex End User License Agreement

##### meter_number: `str`<a id="meter_number-str"></a>

Meter number

##### mailer_id: `int`<a id="mailer_id-int"></a>

Mailer id

##### profile_name: `str`<a id="profile_name-str"></a>

Profile name

##### merchant_id: `int`<a id="merchant_id-int"></a>

Merchant id

##### induction_site: `str`<a id="induction_site-str"></a>

Induction site

##### activation_key: `str`<a id="activation_key-str"></a>

Activation key

##### oba_email: [`Email`](./ship_engine_python_sdk/type/email.py)<a id="oba_email-emailship_engine_python_sdktypeemailpy"></a>

The oba email address

##### contact_name: `str`<a id="contact_name-str"></a>

Contact name

##### company_name: `str`<a id="company_name-str"></a>

Company name

##### street_line1: `str`<a id="street_line1-str"></a>

Street line1

##### street_line2: `str`<a id="street_line2-str"></a>

Street line2

##### street_line3: `str`<a id="street_line3-str"></a>

Street line3

##### access_key: `str`<a id="access_key-str"></a>

Seko Account Access Key

##### sendle_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="sendle_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the sendle

##### title: `str`<a id="title-str"></a>

Title

##### account_country_code: `str`<a id="account_country_code-str"></a>

Account country code

##### account_postal_code: `str`<a id="account_postal_code-str"></a>

Account postal code

##### invoice: [`UpsInvoice`](./ship_engine_python_sdk/type/ups_invoice.py)<a id="invoice-upsinvoiceship_engine_python_sdktypeups_invoicepy"></a>


The UPS invoice

##### invoice_amount: `Union[int, float]`<a id="invoice_amount-unionint-float"></a>

The invoice amount

##### invoice_currency_code: `str`<a id="invoice_currency_code-str"></a>

The invoice currency code

##### agree_to_technology_agreement: `bool`<a id="agree_to_technology_agreement-bool"></a>

The Agreement to the [UPS Technology Agreement](https://www.ups.com/assets/resources/media/UTA_with_EUR.pdf)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectCarrierRequestBody`](./ship_engine_python_sdk/type/connect_carrier_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectCarrierResponseBody`](./ship_engine_python_sdk/pydantic/connect_carrier_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/connections/carriers/{carrier_name}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carrier_accounts.carrier_0`<a id="shipenginecarrier_accountscarrier_0"></a>

Disconnect a carrier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
carrier_0_response = shipengine.carrier_accounts.carrier_0(
    carrier_name="dhl_express",
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_name: [`CarrierName`](./ship_engine_python_sdk/type/.py)<a id="carrier_name-carriernameship_engine_python_sdktypepy"></a>

The carrier name, such as `stamps_com`, `ups`, `fedex`, or `dhl_express`.

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/connections/carriers/{carrier_name}/{carrier_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carrier_accounts.get_settings`<a id="shipenginecarrier_accountsget_settings"></a>

Get carrier settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = shipengine.carrier_accounts.get_settings(
    carrier_name="dhl_express",
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_name: [`CarrierNameWithSettings`](./ship_engine_python_sdk/type/.py)<a id="carrier_name-carriernamewithsettingsship_engine_python_sdktypepy"></a>

The carrier name, such as `ups`, `fedex`, or `dhl_express`.

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`GetCarrierSettingsResponseBody`](./ship_engine_python_sdk/pydantic/get_carrier_settings_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/connections/carriers/{carrier_name}/{carrier_id}/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carrier_accounts.update_settings`<a id="shipenginecarrier_accountsupdate_settings"></a>

Update carrier settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_settings_response = shipengine.carrier_accounts.update_settings(
    body=None,
    carrier_name="dhl_express",
    carrier_id="se-28529731",
    nickname="a",
    should_hide_account_number_on_archive_doc=True,
    is_primary_account=True,
    pickup_type="daily_pickup",
    smart_post_hub="none",
    smart_post_endorsement="none",
    signature_image="string_example",
    letterhead_image="string_example",
    include_barcode_with_order_number=True,
    receive_email_on_manifest_processing=True,
    use_carbon_neutral_shipping_program=True,
    use_ground_freight_pricing=True,
    use_consolidation_services=True,
    use_order_number_on_mail_innovations_labels=True,
    mail_innovations_endorsement="none",
    mail_innovations_cost_center="",
    use_negotiated_rates=True,
    account_postal_code="aaaaa",
    invoice={
        "control_id": "se-28529731",
    },
    email="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_name: [`CarrierNameWithSettings`](./ship_engine_python_sdk/type/.py)<a id="carrier_name-carriernamewithsettingsship_engine_python_sdktypepy"></a>

The carrier name, such as `ups`, `fedex`, or `dhl_express`.

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

##### nickname: `str`<a id="nickname-str"></a>

nickname

##### should_hide_account_number_on_archive_doc: `bool`<a id="should_hide_account_number_on_archive_doc-bool"></a>

Indicates if the account number should be hidden on the archive documentation

##### is_primary_account: `bool`<a id="is_primary_account-bool"></a>

Indicates if this is the primary UPS account

##### pickup_type: [`UpsPickupType`](./ship_engine_python_sdk/type/ups_pickup_type.py)<a id="pickup_type-upspickuptypeship_engine_python_sdktypeups_pickup_typepy"></a>

##### smart_post_hub: [`SmartPostHub`](./ship_engine_python_sdk/type/smart_post_hub.py)<a id="smart_post_hub-smartposthubship_engine_python_sdktypesmart_post_hubpy"></a>

##### smart_post_endorsement: [`AncillaryServiceEndorsement`](./ship_engine_python_sdk/type/ancillary_service_endorsement.py)<a id="smart_post_endorsement-ancillaryserviceendorsementship_engine_python_sdktypeancillary_service_endorsementpy"></a>

##### signature_image: `str`<a id="signature_image-str"></a>

##### letterhead_image: `str`<a id="letterhead_image-str"></a>

##### include_barcode_with_order_number: `bool`<a id="include_barcode_with_order_number-bool"></a>

##### receive_email_on_manifest_processing: `bool`<a id="receive_email_on_manifest_processing-bool"></a>

##### use_carbon_neutral_shipping_program: `bool`<a id="use_carbon_neutral_shipping_program-bool"></a>

The use carbon neutral shipping program

##### use_ground_freight_pricing: `bool`<a id="use_ground_freight_pricing-bool"></a>

The use ground freight pricing

##### use_consolidation_services: `bool`<a id="use_consolidation_services-bool"></a>

The use consolidation services

##### use_order_number_on_mail_innovations_labels: `bool`<a id="use_order_number_on_mail_innovations_labels-bool"></a>

The use order number on mail innovations labels

##### mail_innovations_endorsement: [`AncillaryServiceEndorsement`](./ship_engine_python_sdk/type/ancillary_service_endorsement.py)<a id="mail_innovations_endorsement-ancillaryserviceendorsementship_engine_python_sdktypeancillary_service_endorsementpy"></a>

##### mail_innovations_cost_center: `str`<a id="mail_innovations_cost_center-str"></a>

mail innovations cost center

##### use_negotiated_rates: `bool`<a id="use_negotiated_rates-bool"></a>

The use negotiated rates

##### account_postal_code: `str`<a id="account_postal_code-str"></a>

account postal code

##### invoice: [`UpsInvoice`](./ship_engine_python_sdk/type/ups_invoice.py)<a id="invoice-upsinvoiceship_engine_python_sdktypeups_invoicepy"></a>


The invoice

##### email: `str`<a id="email-str"></a>

Email

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCarrierSettingsRequestBody`](./ship_engine_python_sdk/type/update_carrier_settings_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/connections/carriers/{carrier_name}/{carrier_id}/settings` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.add_funds_to_carrier`<a id="shipenginecarriersadd_funds_to_carrier"></a>

Add Funds To A Carrier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_funds_to_carrier_response = shipengine.carriers.add_funds_to_carrier(
    currency="string_example",
    amount=0,
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currencies that are supported by ShipEngine are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html 

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The monetary amount, in the specified currency.

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MonetaryValue`](./ship_engine_python_sdk/type/monetary_value.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddFundsToCarrierResponseBody`](./ship_engine_python_sdk/pydantic/add_funds_to_carrier_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers/{carrier_id}/add_funds` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.carriers`<a id="shipenginecarrierscarriers"></a>

List all carriers that have been added to this account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
carriers_response = shipengine.carriers.carriers()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetCarriersResponseBody`](./ship_engine_python_sdk/pydantic/get_carriers_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.disconnect_by_id`<a id="shipenginecarriersdisconnect_by_id"></a>

Disconnect a Carrier of the given ID from the account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
disconnect_by_id_response = shipengine.carriers.disconnect_by_id(
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers/{carrier_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.get_by_id`<a id="shipenginecarriersget_by_id"></a>

Retrive carrier info by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.carriers.get_by_id(
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`Carrier`](./ship_engine_python_sdk/pydantic/carrier.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers/{carrier_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.get_options`<a id="shipenginecarriersget_options"></a>

Get a list of the options available for the carrier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_options_response = shipengine.carriers.get_options(
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`GetCarrierOptionsResponseBody`](./ship_engine_python_sdk/pydantic/get_carrier_options_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers/{carrier_id}/options` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.list_package_types`<a id="shipenginecarrierslist_package_types"></a>

List the package types associated with the carrier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_package_types_response = shipengine.carriers.list_package_types(
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`ListCarrierPackageTypesResponseBody`](./ship_engine_python_sdk/pydantic/list_carrier_package_types_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers/{carrier_id}/packages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.carriers.list_services`<a id="shipenginecarrierslist_services"></a>

List the services associated with the carrier ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_services_response = shipengine.carriers.list_services(
    carrier_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

#### 🔄 Return<a id="🔄-return"></a>

[`ListCarrierServicesResponseBody`](./ship_engine_python_sdk/pydantic/list_carrier_services_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/carriers/{carrier_id}/services` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.downloads.file`<a id="shipenginedownloadsfile"></a>

Get File

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_response = shipengine.downloads.file(
    subdir="subdir_example",
    filename="filename_example",
    dir="dir_example",
    download="string_example",
    rotation=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subdir: `str`<a id="subdir-str"></a>

##### filename: `str`<a id="filename-str"></a>

##### dir: `str`<a id="dir-str"></a>

##### download: `str`<a id="download-str"></a>

##### rotation: `int`<a id="rotation-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/downloads/{dir}/{subdir}/{filename}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.insurance.auto_fund_account`<a id="shipengineinsuranceauto_fund_account"></a>

You may need to auto fund your account from time to time. For example, if you don't normally ship items over $100,
and may want to add funds to insurance rather than keeping the account funded.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
auto_fund_account_response = shipengine.insurance.auto_fund_account(
    currency="string_example",
    amount=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currencies that are supported by ShipEngine are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html 

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The monetary amount, in the specified currency.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MonetaryValue`](./ship_engine_python_sdk/type/monetary_value.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MonetaryValue`](./ship_engine_python_sdk/pydantic/monetary_value.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/insurance/shipsurance/add_funds` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.insurance.get_funds_balance`<a id="shipengineinsuranceget_funds_balance"></a>

Retrieve the balance of your Shipsurance account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_funds_balance_response = shipengine.insurance.get_funds_balance()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MonetaryValue`](./ship_engine_python_sdk/pydantic/monetary_value.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/insurance/shipsurance/balance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.insurance.insurer`<a id="shipengineinsuranceinsurer"></a>

Connect a Shipsurance Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
insurer_response = shipengine.insurance.insurer(
    email="john.doe@example.com",
    policy_id="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: [`Email`](./ship_engine_python_sdk/type/email.py)<a id="email-emailship_engine_python_sdktypeemailpy"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectInsurerRequestBody`](./ship_engine_python_sdk/type/connect_insurer_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/connections/insurance/shipsurance` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.insurance.insurer_0`<a id="shipengineinsuranceinsurer_0"></a>

Disconnect a Shipsurance Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
insurer_0_response = shipengine.insurance.insurer_0()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/connections/insurance/shipsurance` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.create_return_label`<a id="shipenginelabelscreate_return_label"></a>

Create a return label

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_return_label_response = shipengine.labels.create_return_label(
    label_id="se-28529731",
    charge_event="carrier_default",
    label_layout="4x6",
    label_format="pdf",
    label_download_type="url",
    display_scheme="label",
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="label_id-seidship_engine_python_sdktypepy"></a>

Label ID

##### charge_event: [`LabelChargeEvent`](./ship_engine_python_sdk/type/label_charge_event.py)<a id="charge_event-labelchargeeventship_engine_python_sdktypelabel_charge_eventpy"></a>

The label charge event. 

##### label_layout: [`LabelLayout`](./ship_engine_python_sdk/type/label_layout.py)<a id="label_layout-labellayoutship_engine_python_sdktypelabel_layoutpy"></a>

The layout (size) that you want the label to be in.  The `label_format` determines which sizes are allowed.  `4x6` is supported for all label formats, whereas `letter` (8.5\\\" x 11\\\") is only supported for `pdf` format. 

##### label_format: [`LabelFormat`](./ship_engine_python_sdk/type/label_format.py)<a id="label_format-labelformatship_engine_python_sdktypelabel_formatpy"></a>

The file format that you want the label to be in.  We recommend `pdf` format because it is supported by all carriers, whereas some carriers do not support the `png` or `zpl` formats. 

##### label_download_type: [`LabelDownloadType`](./ship_engine_python_sdk/type/label_download_type.py)<a id="label_download_type-labeldownloadtypeship_engine_python_sdktypelabel_download_typepy"></a>

##### display_scheme: [`DisplayScheme`](./ship_engine_python_sdk/type/display_scheme.py)<a id="display_scheme-displayschemeship_engine_python_sdktypedisplay_schemepy"></a>

The display format that the label should be shown in.

##### label_image_id: [`ImageIdNullable`](./ship_engine_python_sdk/type/image_id_nullable.py)<a id="label_image_id-imageidnullableship_engine_python_sdktypeimage_id_nullablepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateReturnLabelRequestBody`](./ship_engine_python_sdk/type/create_return_label_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Label`](./ship_engine_python_sdk/pydantic/label.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/{label_id}/return` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.get_by_external_shipment_id`<a id="shipenginelabelsget_by_external_shipment_id"></a>

Find a label by using the external shipment id that was used during label creation


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_external_shipment_id_response = shipengine.labels.get_by_external_shipment_id(
    external_shipment_id="0bcb569d-1727-4ff9-ab49-b2fec0cee5ae",
    label_download_type="url",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_shipment_id: `str`<a id="external_shipment_id-str"></a>

##### label_download_type: [`LabelDownloadType`](./ship_engine_python_sdk/type/.py)<a id="label_download_type-labeldownloadtypeship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Label`](./ship_engine_python_sdk/pydantic/label.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/external_shipment_id/{external_shipment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.get_by_id`<a id="shipenginelabelsget_by_id"></a>

Retrieve information for individual labels.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.labels.get_by_id(
    label_id="se-28529731",
    label_download_type="url",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="label_id-seidship_engine_python_sdktypepy"></a>

Label ID

##### label_download_type: [`LabelDownloadType`](./ship_engine_python_sdk/type/.py)<a id="label_download_type-labeldownloadtypeship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Label`](./ship_engine_python_sdk/pydantic/label.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/{label_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.get_tracking_info`<a id="shipenginelabelsget_tracking_info"></a>

Retrieve the label's tracking information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tracking_info_response = shipengine.labels.get_tracking_info(
    label_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="label_id-seidship_engine_python_sdktypepy"></a>

Label ID

#### 🔄 Return<a id="🔄-return"></a>

[`TrackingInformation`](./ship_engine_python_sdk/pydantic/tracking_information.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/{label_id}/track` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.label`<a id="shipenginelabelslabel"></a>

Purchase and print a label for shipment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
label_response = shipengine.labels.label(
    label_id="se-28529731",
    status="processing",
    shipment_id="se-28529731",
    shipment={
        "tags": [],
        "shipment_id": "se-28529731",
        "carrier_id": "se-28529731",
        "service_code": "usps_first_class_mail",
        "items": [],
        "ship_date": "2018-09-23T00:00:00.000Z",
        "created_at": "2018-09-23T15:00:00.000Z",
        "modified_at": "2018-09-23T15:00:00.000Z",
        "shipment_status": "pending",
        "warehouse_id": "se-28529731",
        "is_return": False,
        "confirmation": "none",
        "insurance_provider": "none",
        "order_source_code": "amazon_ca",
        "comparison_rate_type": "retail",
    },
    ship_date="2018-09-23T00:00:00.000Z",
    created_at="2018-09-23T15:00:00.000Z",
    shipment_cost={
        "currency": "currency_example",
        "amount": 0,
    },
    insurance_cost={
        "currency": "currency_example",
        "amount": 0,
    },
    requested_comparison_amount={
        "currency": "currency_example",
        "amount": 0,
    },
    tracking_number="782758401696",
    is_return_label=True,
    rma_number="string_example",
    is_international=True,
    batch_id="se-28529731",
    carrier_id="se-28529731",
    charge_event="carrier_default",
    outbound_label_id="se-28529731",
    service_code="usps_first_class_mail",
    test_label=False,
    package_code="small_flat_rate_box",
    validate_address="no_validation",
    voided=True,
    voided_at="2018-09-23T15:00:00.000Z",
    label_download_type="url",
    label_format="pdf",
    display_scheme="label",
    label_layout="4x6",
    trackable=True,
    label_image_id="img_DtBXupDBxREpHnwEXhTfgK",
    carrier_code="dhl_express",
    tracking_status="unknown",
    label_download={
        "href": "http://api.shipengine.com/v1/labels/se-28529731",
        "pdf": "http://api.shipengine.com/v1/labels/se-28529731",
        "png": "http://api.shipengine.com/v1/labels/se-28529731",
        "zpl": "http://api.shipengine.com/v1/labels/se-28529731",
    },
    form_download={
        "href": "http://api.shipengine.com/v1/labels/se-28529731",
    },
    insurance_claim={
        "href": "http://api.shipengine.com/v1/labels/se-28529731",
    },
    packages=[
        None
    ],
    alternative_identifiers=[
        {
            "type": "last_mile_tracking_number",
            "value": "12345678912345678912",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="label_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the label. This ID is generated by ShipEngine when the label is created. 

##### status: [`LabelStatus`](./ship_engine_python_sdk/type/label_status.py)<a id="status-labelstatusship_engine_python_sdktypelabel_statuspy"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="shipment_id-seidship_engine_python_sdktypese_idpy"></a>

The shipment that this label is for.  ShipEngine can create a shipment for you automatically when you [create a label](https://www.shipengine.com/docs/labels/create-a-label/), or you can [create your own shipment](https://www.shipengine.com/docs/shipping/create-a-shipment/) and then [use it to print a label](https://www.shipengine.com/docs/labels/create-from-shipment/) 

##### shipment: [`PartialShipment`](./ship_engine_python_sdk/type/partial_shipment.py)<a id="shipment-partialshipmentship_engine_python_sdktypepartial_shipmentpy"></a>


The shipment information used to generate the label

##### ship_date: [`Date`](./ship_engine_python_sdk/type/date.py)<a id="ship_date-dateship_engine_python_sdktypedatepy"></a>

The date that the package was (or will be) shippped.  ShipEngine will take the day of week into consideration. For example, if the carrier does not operate on Sundays, then a package that would have shipped on Sunday will ship on Monday instead. 

##### created_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="created_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the label was created in ShipEngine.

##### shipment_cost: [`MonetaryValue`](./ship_engine_python_sdk/type/monetary_value.py)<a id="shipment_cost-monetaryvalueship_engine_python_sdktypemonetary_valuepy"></a>


The cost of shipping, delivery confirmation, and other carrier charges.  This amount **does not** include insurance costs. 

##### insurance_cost: [`MonetaryValue`](./ship_engine_python_sdk/type/monetary_value.py)<a id="insurance_cost-monetaryvalueship_engine_python_sdktypemonetary_valuepy"></a>


The insurance cost for this package.  Add this to the `shipment_cost` field to get the total cost. 

##### requested_comparison_amount: [`MonetaryValue`](./ship_engine_python_sdk/type/monetary_value.py)<a id="requested_comparison_amount-monetaryvalueship_engine_python_sdktypemonetary_valuepy"></a>


The total shipping cost for the specified comparison_rate_type. 

##### tracking_number: `str`<a id="tracking_number-str"></a>

The tracking number for the package. Tracking number formats vary across carriers.

##### is_return_label: `bool`<a id="is_return_label-bool"></a>

Indicates whether this is a return label.  You may also want to set the `rma_number` so you know what is being returned. 

##### rma_number: `Optional[str]`<a id="rma_number-optionalstr"></a>

An optional Return Merchandise Authorization number.  This field is useful for return labels.  You can set it to any string value. 

##### is_international: `bool`<a id="is_international-bool"></a>

Indicates whether this is an international shipment.  That is, the originating country and destination country are different. 

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="batch_id-seidship_engine_python_sdktypese_idpy"></a>

If this label was created as part of a [batch](https://www.shipengine.com/docs/labels/bulk/), then this is the unique ID of that batch. 

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="carrier_id-seidship_engine_python_sdktypese_idpy"></a>

The unique ID of the [carrier account](https://www.shipengine.com/docs/carriers/setup/) that was used to create this label 

##### charge_event: [`LabelChargeEvent`](./ship_engine_python_sdk/type/label_charge_event.py)<a id="charge_event-labelchargeeventship_engine_python_sdktypelabel_charge_eventpy"></a>

The label charge event. 

##### outbound_label_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="outbound_label_id-seidship_engine_python_sdktypese_idpy"></a>

The `label_id` of the original (outgoing) label that the return label is for. This associates the two labels together, which is required by some carriers. 

##### service_code: [`ServiceCode`](./ship_engine_python_sdk/type/service_code.py)<a id="service_code-servicecodeship_engine_python_sdktypeservice_codepy"></a>

The [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc. 

##### test_label: `bool`<a id="test_label-bool"></a>

Indicate if this label is being used only for testing purposes. If true, then no charge will be added to your account.

##### package_code: [`PackageCode`](./ship_engine_python_sdk/type/package_code.py)<a id="package_code-packagecodeship_engine_python_sdktypepackage_codepy"></a>

The [package type](https://www.shipengine.com/docs/reference/list-carrier-packages/), such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc.  The code `package` indicates a custom or unknown package type. 

##### validate_address: [`ValidateAddress`](./ship_engine_python_sdk/type/validate_address.py)<a id="validate_address-validateaddressship_engine_python_sdktypevalidate_addresspy"></a>

##### voided: `bool`<a id="voided-bool"></a>

Indicates whether the label has been [voided](https://www.shipengine.com/docs/labels/voiding/) 

##### voided_at: `DateTime`<a id="voided_at-datetime"></a>

The date and time that the label was [voided](https://www.shipengine.com/docs/labels/voiding/), or `null` if the label has not been voided 

##### label_download_type: [`LabelDownloadType`](./ship_engine_python_sdk/type/label_download_type.py)<a id="label_download_type-labeldownloadtypeship_engine_python_sdktypelabel_download_typepy"></a>

##### label_format: [`LabelFormat`](./ship_engine_python_sdk/type/label_format.py)<a id="label_format-labelformatship_engine_python_sdktypelabel_formatpy"></a>

The file format that you want the label to be in.  We recommend `pdf` format because it is supported by all carriers, whereas some carriers do not support the `png` or `zpl` formats. 

##### display_scheme: [`DisplayScheme`](./ship_engine_python_sdk/type/display_scheme.py)<a id="display_scheme-displayschemeship_engine_python_sdktypedisplay_schemepy"></a>

The display format that the label should be shown in.

##### label_layout: [`LabelLayout`](./ship_engine_python_sdk/type/label_layout.py)<a id="label_layout-labellayoutship_engine_python_sdktypelabel_layoutpy"></a>

The layout (size) that you want the label to be in.  The `label_format` determines which sizes are allowed.  `4x6` is supported for all label formats, whereas `letter` (8.5\\\" x 11\\\") is only supported for `pdf` format. 

##### trackable: `bool`<a id="trackable-bool"></a>

Indicates whether the shipment is trackable, in which case the `tracking_status` field will reflect the current status and each package will have a `tracking_number`. 

##### label_image_id: [`ImageIdNullable`](./ship_engine_python_sdk/type/image_id_nullable.py)<a id="label_image_id-imageidnullableship_engine_python_sdktypeimage_id_nullablepy"></a>

The label image resource that was used to create a custom label image.

##### carrier_code: [`CarrierCode`](./ship_engine_python_sdk/type/carrier_code.py)<a id="carrier_code-carriercodeship_engine_python_sdktypecarrier_codepy"></a>

The [shipping carrier](https://www.shipengine.com/docs/carriers/setup/) who will ship the package, such as `fedex`, `dhl_express`, `stamps_com`, etc. 

##### tracking_status: [`TrackingStatus`](./ship_engine_python_sdk/type/tracking_status.py)<a id="tracking_status-trackingstatusship_engine_python_sdktypetracking_statuspy"></a>

The current status of the package, such as `in_transit` or `delivered`

##### label_download: [`LabelDownload`](./ship_engine_python_sdk/type/label_download.py)<a id="label_download-labeldownloadship_engine_python_sdktypelabel_downloadpy"></a>


##### form_download: [`OptionalLinkNullable`](./ship_engine_python_sdk/type/optional_link_nullable.py)<a id="form_download-optionallinknullableship_engine_python_sdktypeoptional_link_nullablepy"></a>


The link to download the customs form (a.k.a. commercial invoice) for this shipment, if any.  Forms are in PDF format. This field is null if the shipment does not require a customs form, or if the carrier does not support it. 

##### insurance_claim: [`OptionalLink`](./ship_engine_python_sdk/type/optional_link.py)<a id="insurance_claim-optionallinkship_engine_python_sdktypeoptional_linkpy"></a>


The link to submit an insurance claim for the shipment.  This field is null if the shipment is not insured or if the insurance provider does not support online claim submission. 

##### packages: [`LabelPackages`](./ship_engine_python_sdk/type/label_packages.py)<a id="packages-labelpackagesship_engine_python_sdktypelabel_packagespy"></a>

##### alternative_identifiers: List[`AlternativeIdentifier`]<a id="alternative_identifiers-listalternativeidentifier"></a>

Additional information some carriers may provide by which to identify a given label in their system.  

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Label`](./ship_engine_python_sdk/type/label.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Label`](./ship_engine_python_sdk/pydantic/label.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.label_0`<a id="shipenginelabelslabel_0"></a>

Void a label by ID to get a refund.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
label_0_response = shipengine.labels.label_0(
    label_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="label_id-seidship_engine_python_sdktypepy"></a>

Label ID

#### 🔄 Return<a id="🔄-return"></a>

[`VoidLabelResponseBody`](./ship_engine_python_sdk/pydantic/void_label_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/{label_id}/void` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.labels`<a id="shipenginelabelslabels"></a>

This endpoint returns a list of labels that you've [created](https://www.shipengine.com/docs/labels/create-a-label/). You can optionally filter the results as well as control their sort order and the number of results returned at a time.

By default, all labels are returned, 25 at a time, starting with the most recently created ones.  You can combine multiple filter options to narrow-down the results.  For example, if you only want to get your UPS labels for your east coast warehouse you could query by both `warehouse_id` and `carrier_id`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
labels_response = shipengine.labels.labels(
    label_status="processing",
    service_code="usps_first_class_mail",
    carrier_id="se-28529731",
    tracking_number="9405511899223197428490",
    batch_id="se-28529731",
    rate_id="se-28529731",
    shipment_id="se-28529731",
    warehouse_id="se-28529731",
    created_at_start="2019-03-12T19:24:13.657Z",
    created_at_end="2019-03-12T19:24:13.657Z",
    page=2,
    page_size=50,
    sort_dir="asc",
    sort_by="created_at",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label_status: [`LabelStatus`](./ship_engine_python_sdk/type/.py)<a id="label_status-labelstatusship_engine_python_sdktypepy"></a>

Only return labels that are currently in the specified status

##### service_code: [`ServiceCode`](./ship_engine_python_sdk/type/.py)<a id="service_code-servicecodeship_engine_python_sdktypepy"></a>

Only return labels for a specific [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/)

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Only return labels for a specific [carrier account](https://www.shipengine.com/docs/carriers/setup/)

##### tracking_number: `str`<a id="tracking_number-str"></a>

Only return labels with a specific tracking number

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Only return labels that were created in a specific [batch](https://www.shipengine.com/docs/labels/bulk/)

##### rate_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="rate_id-seidship_engine_python_sdktypepy"></a>

Rate ID

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Only return labels that originate from a specific [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/)

##### created_at_start: `datetime`<a id="created_at_start-datetime"></a>

Only return labels that were created on or after a specific date/time

##### created_at_end: `datetime`<a id="created_at_end-datetime"></a>

Only return labels that were created on or before a specific date/time

##### page: `int`<a id="page-int"></a>

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 

##### page_size: `int`<a id="page_size-int"></a>

The number of results to return per response.

##### sort_dir: [`SortDir`](./ship_engine_python_sdk/type/.py)<a id="sort_dir-sortdirship_engine_python_sdktypepy"></a>

Controls the sort order of the query.

##### sort_by: `str`<a id="sort_by-str"></a>

Controls which field the query is sorted by.

#### 🔄 Return<a id="🔄-return"></a>

[`PagedListResponseBody`](./ship_engine_python_sdk/pydantic/paged_list_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.purchase_label_with_rate_id`<a id="shipenginelabelspurchase_label_with_rate_id"></a>

When retrieving rates for shipments using the `/rates` endpoint, the returned information contains a `rate_id` property that can be used
to generate a label without having to refill in the shipment information repeatedly.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
purchase_label_with_rate_id_response = shipengine.labels.purchase_label_with_rate_id(
    rate_id="se-28529731",
    validate_address="no_validation",
    label_layout="4x6",
    label_format="pdf",
    label_download_type="url",
    display_scheme="label",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rate_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="rate_id-seidship_engine_python_sdktypepy"></a>

Rate ID

##### validate_address: [`ValidateAddress`](./ship_engine_python_sdk/type/validate_address.py)<a id="validate_address-validateaddressship_engine_python_sdktypevalidate_addresspy"></a>

##### label_layout: [`LabelLayout`](./ship_engine_python_sdk/type/label_layout.py)<a id="label_layout-labellayoutship_engine_python_sdktypelabel_layoutpy"></a>

##### label_format: [`LabelFormat`](./ship_engine_python_sdk/type/label_format.py)<a id="label_format-labelformatship_engine_python_sdktypelabel_formatpy"></a>

##### label_download_type: [`LabelDownloadType`](./ship_engine_python_sdk/type/label_download_type.py)<a id="label_download_type-labeldownloadtypeship_engine_python_sdktypelabel_download_typepy"></a>

##### display_scheme: [`DisplayScheme`](./ship_engine_python_sdk/type/display_scheme.py)<a id="display_scheme-displayschemeship_engine_python_sdktypedisplay_schemepy"></a>

The display format that the label should be shown in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PurchaseLabelWithoutShipment`](./ship_engine_python_sdk/type/purchase_label_without_shipment.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Label`](./ship_engine_python_sdk/pydantic/label.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/rates/{rate_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.labels.purchase_label_with_shipment_id`<a id="shipenginelabelspurchase_label_with_shipment_id"></a>

Purchase a label using a shipment ID that has already been created with the desired address and
package info.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
purchase_label_with_shipment_id_response = shipengine.labels.purchase_label_with_shipment_id(
    shipment_id="se-28529731",
    validate_address="no_validation",
    label_layout="4x6",
    label_format="pdf",
    label_download_type="url",
    display_scheme="label",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

##### validate_address: [`ValidateAddress`](./ship_engine_python_sdk/type/validate_address.py)<a id="validate_address-validateaddressship_engine_python_sdktypevalidate_addresspy"></a>

##### label_layout: [`LabelLayout`](./ship_engine_python_sdk/type/label_layout.py)<a id="label_layout-labellayoutship_engine_python_sdktypelabel_layoutpy"></a>

##### label_format: [`LabelFormat`](./ship_engine_python_sdk/type/label_format.py)<a id="label_format-labelformatship_engine_python_sdktypelabel_formatpy"></a>

##### label_download_type: [`LabelDownloadType`](./ship_engine_python_sdk/type/label_download_type.py)<a id="label_download_type-labeldownloadtypeship_engine_python_sdktypelabel_download_typepy"></a>

##### display_scheme: [`DisplayScheme`](./ship_engine_python_sdk/type/display_scheme.py)<a id="display_scheme-displayschemeship_engine_python_sdktypedisplay_schemepy"></a>

The display format that the label should be shown in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateLabelFromShipmentRequestBody`](./ship_engine_python_sdk/type/create_label_from_shipment_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Label`](./ship_engine_python_sdk/pydantic/label.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/labels/shipment/{shipment_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.manifests.get_by_id`<a id="shipenginemanifestsget_by_id"></a>

Get Manifest By Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.manifests.get_by_id(
    manifest_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### manifest_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="manifest_id-seidship_engine_python_sdktypepy"></a>

The Manifest Id

#### 🔄 Return<a id="🔄-return"></a>

[`Manifest`](./ship_engine_python_sdk/pydantic/manifest.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/manifests/{manifest_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.manifests.get_request_by_id`<a id="shipenginemanifestsget_request_by_id"></a>

Get Manifest Request By Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_request_by_id_response = shipengine.manifests.get_request_by_id(
    manifest_request_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### manifest_request_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="manifest_request_id-seidship_engine_python_sdktypepy"></a>

The Manifest Request Id

#### 🔄 Return<a id="🔄-return"></a>

[`CreateManifestResponseBody`](./ship_engine_python_sdk/pydantic/create_manifest_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/manifests/requests/{manifest_request_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.manifests.manifest`<a id="shipenginemanifestsmanifest"></a>

Each ShipEngine manifest is created for a specific warehouse, so you'll need to provide the warehouse_id
rather than the ship_from address. You can create a warehouse for each location that you want to create manifests for.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
manifest_response = shipengine.manifests.manifest(
    body=None,
    carrier_id="se-28529731",
    excluded_label_ids=[
        "se-q6zgc"
    ],
    label_ids=[
        "se-q6zgc"
    ],
    warehouse_id="se-28529731",
    ship_date="2018-09-23T15:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="carrier_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the carrier

##### excluded_label_ids: List[`SeId`]<a id="excluded_label_ids-listseid"></a>

The list of label ids to exclude from the manifest

##### label_ids: List[`SeId`]<a id="label_ids-listseid"></a>

The list of label ids to include in the manifest

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="warehouse_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the warehouse

##### ship_date: `datetime`<a id="ship_date-datetime"></a>

The ship date that the shipment will be sent out on

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateManifestRequestBody`](./ship_engine_python_sdk/type/create_manifest_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateManifestResponseBody`](./ship_engine_python_sdk/pydantic/create_manifest_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/manifests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.manifests.manifests`<a id="shipenginemanifestsmanifests"></a>

Similar to querying shipments, we allow you to query manifests since there will likely be a large number over a long period of time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
manifests_response = shipengine.manifests.manifests(
    warehouse_id="se-28529731",
    ship_date_start="2018-09-23T15:00:00.000Z",
    ship_date_end="2018-09-23T15:00:00.000Z",
    created_at_start="2019-03-12T19:24:13.657Z",
    created_at_end="2019-03-12T19:24:13.657Z",
    carrier_id="se-28529731",
    page=2,
    page_size=50,
    label_ids=[
        "se-q6zgc"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Warehouse ID

##### ship_date_start: `datetime`<a id="ship_date_start-datetime"></a>

ship date start range

##### ship_date_end: `datetime`<a id="ship_date_end-datetime"></a>

ship date end range

##### created_at_start: `datetime`<a id="created_at_start-datetime"></a>

Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)

##### created_at_end: `datetime`<a id="created_at_end-datetime"></a>

Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

##### page: `int`<a id="page-int"></a>

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 

##### page_size: `int`<a id="page_size-int"></a>

The number of results to return per response.

##### label_ids: List[`str`]<a id="label_ids-liststr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ListManifestsResponseBody`](./ship_engine_python_sdk/pydantic/list_manifests_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/manifests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_pickups.get_by_id`<a id="shipenginepackage_pickupsget_by_id"></a>

Get Pickup By ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.package_pickups.get_by_id(
    pickup_id="pik_3YcKU5zdtJuCqoeNwyqqbW",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pickup_id: [`PickupResourceId`](./ship_engine_python_sdk/type/.py)<a id="pickup_id-pickupresourceidship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetPickupByIdResponseBody`](./ship_engine_python_sdk/pydantic/get_pickup_by_id_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/pickups/{pickup_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_pickups.list_scheduled_pickups`<a id="shipenginepackage_pickupslist_scheduled_pickups"></a>

List all pickups that have been scheduled for this carrier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_scheduled_pickups_response = shipengine.package_pickups.list_scheduled_pickups(
    carrier_id="se-28529731",
    warehouse_id="se-28529731",
    created_at_start="2019-03-12T19:24:13.657Z",
    created_at_end="2019-03-12T19:24:13.657Z",
    page=2,
    page_size=50,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="carrier_id-seidship_engine_python_sdktypepy"></a>

Carrier ID

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Warehouse ID

##### created_at_start: `datetime`<a id="created_at_start-datetime"></a>

Only return scheduled pickups that were created on or after a specific date/time

##### created_at_end: `datetime`<a id="created_at_end-datetime"></a>

Only return scheduled pickups that were created on or before a specific date/time

##### page: `int`<a id="page-int"></a>

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 

##### page_size: `int`<a id="page_size-int"></a>

The number of results to return per response.

#### 🔄 Return<a id="🔄-return"></a>

[`GetPickupsResponseBody`](./ship_engine_python_sdk/pydantic/get_pickups_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/pickups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_pickups.pickup`<a id="shipenginepackage_pickupspickup"></a>

Schedule a package pickup with a carrier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pickup_response = shipengine.package_pickups.pickup(
    pickup_id="pik_3YcKU5zdtJuCqoeNwyqqbW",
    label_ids=[
        "se-q6zgc"
    ],
    created_at="2018-09-23T15:00:00.000Z",
    cancelled_at="2018-09-23T15:00:00.000Z",
    carrier_id="se-28529731",
    confirmation_number="292513CL4A3",
    warehouse_id="se-28529731",
    pickup_address={
        "name": "John Doe",
        "phone": "+1 204-253-9411 ext. 123",
        "email": "example@example.com",
        "company_name": "The Home Depot",
        "address_line1": "1999 Bishop Grandin Blvd.",
        "address_line2": "Unit 408",
        "address_line3": "Building #7",
        "city_locality": "Winnipeg",
        "state_province": "Manitoba",
        "postal_code": "78756-3717",
        "country_code": "CA",
        "address_residential_indicator": "unknown",
    },
    contact_details={
        "name": "name_example",
        "email": "john.doe@example.com",
        "phone": "phone_example",
    },
    pickup_notes="",
    pickup_window={
        "start_at": "2018-09-23T15:00:00.000Z",
        "end_at": "2018-09-23T15:00:00.000Z",
    },
    pickup_windows=[
        {
            "start_at": "2018-09-23T15:00:00.000Z",
            "end_at": "2018-09-23T15:00:00.000Z",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pickup_id: [`PickupResourceId`](./ship_engine_python_sdk/type/pickup_resource_id.py)<a id="pickup_id-pickupresourceidship_engine_python_sdktypepickup_resource_idpy"></a>

##### label_ids: List[`SeId`]<a id="label_ids-listseid"></a>

Label IDs that will be included in the pickup request

##### created_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="created_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the pickup was created in ShipEngine.

##### cancelled_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="cancelled_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the pickup was cancelled in ShipEngine.

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="carrier_id-seidship_engine_python_sdktypese_idpy"></a>

The carrier_id associated with the pickup

##### confirmation_number: `Optional[str]`<a id="confirmation_number-optionalstr"></a>

The carrier confirmation number for the scheduled pickup.

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="warehouse_id-seidship_engine_python_sdktypese_idpy"></a>

The warehouse_id associated with the pickup

##### pickup_address: [`PartialAddress`](./ship_engine_python_sdk/type/partial_address.py)<a id="pickup_address-partialaddressship_engine_python_sdktypepartial_addresspy"></a>


##### contact_details: [`ContactDetails`](./ship_engine_python_sdk/type/contact_details.py)<a id="contact_details-contactdetailsship_engine_python_sdktypecontact_detailspy"></a>


##### pickup_notes: `str`<a id="pickup_notes-str"></a>

Used by some carriers to give special instructions for a package pickup

##### pickup_window: [`PickupWindow`](./ship_engine_python_sdk/type/pickup_window.py)<a id="pickup_window-pickupwindowship_engine_python_sdktypepickup_windowpy"></a>


##### pickup_windows: List[`PickupWindows`]<a id="pickup_windows-listpickupwindows"></a>

An array of available pickup windows. Carriers can return multiple times that they will pickup packages. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Pickup`](./ship_engine_python_sdk/type/pickup.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SchedulePickupResponseBody`](./ship_engine_python_sdk/pydantic/schedule_pickup_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/pickups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_pickups.remove_scheduled_pickup`<a id="shipenginepackage_pickupsremove_scheduled_pickup"></a>

Delete a previously-scheduled pickup by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_scheduled_pickup_response = shipengine.package_pickups.remove_scheduled_pickup(
    pickup_id="pik_3YcKU5zdtJuCqoeNwyqqbW",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pickup_id: [`PickupResourceId`](./ship_engine_python_sdk/type/.py)<a id="pickup_id-pickupresourceidship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeletePickupByIdResponseBody`](./ship_engine_python_sdk/pydantic/delete_pickup_by_id_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/pickups/{pickup_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_types.create_custom_package_type`<a id="shipenginepackage_typescreate_custom_package_type"></a>

Create a custom package type to better assist in getting accurate rate estimates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_package_type_response = shipengine.package_types.create_custom_package_type(
    package_code="small_flat_rate_box",
    name="laptop_box",
    description="Packaging for laptops",
    package_id="se-28529731",
    dimensions={
        "unit": "inch",
        "length": 0,
        "width": 0,
        "height": 0,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### package_code: [`PackageCode`](./ship_engine_python_sdk/type/package_code.py)<a id="package_code-packagecodeship_engine_python_sdktypepackage_codepy"></a>

##### name: `str`<a id="name-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Provides a helpful description for the custom package.

##### package_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="package_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the package.

##### dimensions: [`Dimensions`](./ship_engine_python_sdk/type/dimensions.py)<a id="dimensions-dimensionsship_engine_python_sdktypedimensionspy"></a>


The custom dimensions for the package.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PackageType`](./ship_engine_python_sdk/type/package_type.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PackageType`](./ship_engine_python_sdk/pydantic/package_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/packages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_types.delete_custom_package_by_id`<a id="shipenginepackage_typesdelete_custom_package_by_id"></a>

Delete a custom package using the ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_custom_package_by_id_response = shipengine.package_types.delete_custom_package_by_id(
    package_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### package_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="package_id-seidship_engine_python_sdktypepy"></a>

Package ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/packages/{package_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_types.get_by_id`<a id="shipenginepackage_typesget_by_id"></a>

Get Custom Package Type by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.package_types.get_by_id(
    package_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### package_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="package_id-seidship_engine_python_sdktypepy"></a>

Package ID

#### 🔄 Return<a id="🔄-return"></a>

[`PackageType`](./ship_engine_python_sdk/pydantic/package_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/packages/{package_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_types.list_custom_package_types`<a id="shipenginepackage_typeslist_custom_package_types"></a>

List the custom package types associated with the account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_custom_package_types_response = shipengine.package_types.list_custom_package_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListPackageTypesResponseBody`](./ship_engine_python_sdk/pydantic/list_package_types_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/packages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.package_types.update_custom_package_type_by_id`<a id="shipenginepackage_typesupdate_custom_package_type_by_id"></a>

Update the custom package type object by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_package_type_by_id_response = shipengine.package_types.update_custom_package_type_by_id(
    package_code="small_flat_rate_box",
    name="laptop_box",
    package_id="se-28529731",
    description="Packaging for laptops",
    package_id="se-28529731",
    dimensions={
        "unit": "inch",
        "length": 0,
        "width": 0,
        "height": 0,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### package_code: [`PackageCode`](./ship_engine_python_sdk/type/package_code.py)<a id="package_code-packagecodeship_engine_python_sdktypepackage_codepy"></a>

##### name: `str`<a id="name-str"></a>

##### package_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="package_id-seidship_engine_python_sdktypepy"></a>

Package ID

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Provides a helpful description for the custom package.

##### package_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="package_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the package.

##### dimensions: [`Dimensions`](./ship_engine_python_sdk/type/dimensions.py)<a id="dimensions-dimensionsship_engine_python_sdktypedimensionspy"></a>


The custom dimensions for the package.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PackageType`](./ship_engine_python_sdk/type/package_type.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/packages/{package_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.rates.get_bulk_shipment_rates`<a id="shipengineratesget_bulk_shipment_rates"></a>

Get Bulk Shipment Rates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bulk_shipment_rates_response = shipengine.rates.get_bulk_shipment_rates(
    rate_options={
        "carrier_ids": [
            "se-28529731"
        ],
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rate_options: [`RateRequestBody`](./ship_engine_python_sdk/type/rate_request_body.py)<a id="rate_options-raterequestbodyship_engine_python_sdktyperate_request_bodypy"></a>


The rate options

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RateRequestRateOptions`](./ship_engine_python_sdk/type/rate_request_rate_options.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompareBulkRatesResponseBody`](./ship_engine_python_sdk/pydantic/compare_bulk_rates_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/rates/bulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.rates.get_by_id`<a id="shipengineratesget_by_id"></a>

Retrieve a previously queried rate by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.rates.get_by_id(
    rate_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rate_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="rate_id-seidship_engine_python_sdktypepy"></a>

Rate ID

#### 🔄 Return<a id="🔄-return"></a>

[`Rate`](./ship_engine_python_sdk/pydantic/rate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/rates/{rate_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.rates.rates`<a id="shipengineratesrates"></a>

It's not uncommon that you want to give your customer the choice between whether they want to ship the fastest, cheapest, or the most trusted route. Most companies don't solely ship things using a single shipping option;
so we provide functionality to show you all your options!


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rates_response = shipengine.rates.rates(
    rate_options={
        "carrier_ids": [
            "se-28529731"
        ],
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rate_options: [`RateRequestBody`](./ship_engine_python_sdk/type/rate_request_body.py)<a id="rate_options-raterequestbodyship_engine_python_sdktyperate_request_bodypy"></a>


The rate options

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RateRequestOptions`](./ship_engine_python_sdk/type/rate_request_options.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CalculateRatesResponseBody`](./ship_engine_python_sdk/pydantic/calculate_rates_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/rates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.rates.rates_0`<a id="shipengineratesrates_0"></a>

Get Rate Estimates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rates_0_response = shipengine.rates.rates_0(
    from_country_code="CA",
    from_postal_code="78756-3717",
    from_city_locality="Austin",
    from_state_province="Austin",
    to_country_code="CA",
    to_postal_code="78756-3717",
    to_city_locality="Austin",
    to_state_province="Houston",
    weight={
        "value": 0,
        "unit": "pound",
    },
    dimensions={
        "unit": "inch",
        "length": 0,
        "width": 0,
        "height": 0,
    },
    confirmation="none",
    address_residential_indicator="unknown",
    ship_date="2018-09-23T15:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### from_country_code: [`CountryCode`](./ship_engine_python_sdk/type/country_code.py)<a id="from_country_code-countrycodeship_engine_python_sdktypecountry_codepy"></a>

##### from_postal_code: [`PostalCode`](./ship_engine_python_sdk/type/postal_code.py)<a id="from_postal_code-postalcodeship_engine_python_sdktypepostal_codepy"></a>

##### from_city_locality: `str`<a id="from_city_locality-str"></a>

from postal code

##### from_state_province: `str`<a id="from_state_province-str"></a>

From state province

##### to_country_code: [`CountryCode`](./ship_engine_python_sdk/type/country_code.py)<a id="to_country_code-countrycodeship_engine_python_sdktypecountry_codepy"></a>

##### to_postal_code: [`PostalCode`](./ship_engine_python_sdk/type/postal_code.py)<a id="to_postal_code-postalcodeship_engine_python_sdktypepostal_codepy"></a>

##### to_city_locality: `str`<a id="to_city_locality-str"></a>

The city locality the package is being shipped to

##### to_state_province: `str`<a id="to_state_province-str"></a>

To state province

##### weight: [`Weight`](./ship_engine_python_sdk/type/weight.py)<a id="weight-weightship_engine_python_sdktypeweightpy"></a>


The weight of the package

##### dimensions: [`Dimensions`](./ship_engine_python_sdk/type/dimensions.py)<a id="dimensions-dimensionsship_engine_python_sdktypedimensionspy"></a>


The dimensions of the package

##### confirmation: [`DeliveryConfirmation`](./ship_engine_python_sdk/type/delivery_confirmation.py)<a id="confirmation-deliveryconfirmationship_engine_python_sdktypedelivery_confirmationpy"></a>

##### address_residential_indicator: [`AddressResidentialIndicator`](./ship_engine_python_sdk/type/address_residential_indicator.py)<a id="address_residential_indicator-addressresidentialindicatorship_engine_python_sdktypeaddress_residential_indicatorpy"></a>

##### ship_date: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="ship_date-datetimeship_engine_python_sdktypedate_timepy"></a>

ship date

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RateEstimateOptions`](./ship_engine_python_sdk/type/rate_estimate_options.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EstimateRatesResponseBody`](./ship_engine_python_sdk/pydantic/estimate_rates_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/rates/estimate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.service_points.get_by_id`<a id="shipengineservice_pointsget_by_id"></a>

Returns a carrier service point by using the service_point_id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.service_points.get_by_id(
    carrier_code="stamps_com",
    country_code="CA",
    service_point_id="614940",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_code: `str`<a id="carrier_code-str"></a>

Carrier code

##### country_code: `str`<a id="country_code-str"></a>

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) 

##### service_point_id: `str`<a id="service_point_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetServicePointByIdResponseBody`](./ship_engine_python_sdk/pydantic/get_service_point_by_id_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/service_points/{carrier_code}/{country_code}/{service_point_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.service_points.get_by_location`<a id="shipengineservice_pointsget_by_location"></a>

List carrier service points by location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_location_response = shipengine.service_points.get_by_location(
    body=None,
    address_query="177A Bleecker Street New York",
    address={
        "address_line1": "1999 Bishop Grandin Blvd.",
        "postal_code": "78756-3717",
        "country_code": "CA",
    },
    providers=[
        {
            "carrier_id": "se-123456",
        }
    ],
    lat=48.874518928233094,
    long=2.3591775711639404,
    radius=500,
    max_results=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### address_query: `str`<a id="address_query-str"></a>

Unstructured text to search for service points by.

##### address: [`GetServicePointsRequestBodyAddress`](./ship_engine_python_sdk/type/get_service_points_request_body_address.py)<a id="address-getservicepointsrequestbodyaddressship_engine_python_sdktypeget_service_points_request_body_addresspy"></a>


##### providers: [`GetServicePointsRequestBodyProviders`](./ship_engine_python_sdk/type/get_service_points_request_body_providers.py)<a id="providers-getservicepointsrequestbodyprovidersship_engine_python_sdktypeget_service_points_request_body_providerspy"></a>

##### lat: `Union[int, float]`<a id="lat-unionint-float"></a>

The latitude of the point. Represented as signed degrees. Required if long is provided. http://www.geomidpoint.com/latlon.html

##### long: `Union[int, float]`<a id="long-unionint-float"></a>

The longitude of the point. Represented as signed degrees. Required if lat is provided. http://www.geomidpoint.com/latlon.html

##### radius: `int`<a id="radius-int"></a>

Search radius in kilometers

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of service points to return

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetServicePointsRequest`](./ship_engine_python_sdk/type/get_service_points_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ListServicePointsResponseBody`](./ship_engine_python_sdk/pydantic/list_service_points_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/service_points/list` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.get_by_external_id`<a id="shipengineshipmentsget_by_external_id"></a>

Query Shipments created using your own custom ID convention using this endpint

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_external_id_response = shipengine.shipments.get_by_external_id(
    external_shipment_id="0bcb569d-1727-4ff9-ab49-b2fec0cee5ae",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_shipment_id: `str`<a id="external_shipment_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PartialShipment`](./ship_engine_python_sdk/pydantic/partial_shipment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/external_shipment_id/{external_shipment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.get_by_id`<a id="shipengineshipmentsget_by_id"></a>

Get an individual shipment based on its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.shipments.get_by_id(
    shipment_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

#### 🔄 Return<a id="🔄-return"></a>

[`PartialShipment`](./ship_engine_python_sdk/pydantic/partial_shipment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.get_rates_for_shipment`<a id="shipengineshipmentsget_rates_for_shipment"></a>

Get Rates for the shipment information associated with the shipment ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rates_for_shipment_response = shipengine.shipments.get_rates_for_shipment(
    shipment_id="se-28529731",
    created_at_start="2019-03-12T19:24:13.657Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

##### created_at_start: `datetime`<a id="created_at_start-datetime"></a>

Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)

#### 🔄 Return<a id="🔄-return"></a>

[`RatesInformation`](./ship_engine_python_sdk/pydantic/rates_information.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}/rates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.get_tags_by_id`<a id="shipengineshipmentsget_tags_by_id"></a>

Get Shipment tags based on its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tags_by_id_response = shipengine.shipments.get_tags_by_id(
    shipment_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

#### 🔄 Return<a id="🔄-return"></a>

[`TagShipmentResponseBody`](./ship_engine_python_sdk/pydantic/tag_shipment_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipment`<a id="shipengineshipmentsshipment"></a>

The shipment-recognition API makes it easy for you to extract shipping data from unstructured text, including people's names, addresses, package weights and dimensions, insurance and delivery requirements, and more.

Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine's shipment-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed shipment data is returned in the same structure that's used for other ShipEngine APIs, so you can easily use the parsed data to create a shipping label.

> **Note:** Shipment recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipment_response = shipengine.shipments.shipment(
    text="I have a 4oz package that's 5x10x14in, and I need to ship it to Margie McMiller at 3800 North Lamar suite 200 in austin, tx 78652. Please send it via USPS first class and require an adult signature. It also needs to be insured for $400.\n",
    shipment={
        "tags": [],
        "shipment_id": "se-28529731",
        "carrier_id": "se-28529731",
        "service_code": "usps_first_class_mail",
        "items": [],
        "ship_date": "2018-09-23T00:00:00.000Z",
        "created_at": "2018-09-23T15:00:00.000Z",
        "modified_at": "2018-09-23T15:00:00.000Z",
        "shipment_status": "pending",
        "warehouse_id": "se-28529731",
        "is_return": False,
        "confirmation": "none",
        "insurance_provider": "none",
        "order_source_code": "amazon_ca",
        "comparison_rate_type": "retail",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

The unstructured text that contains shipping-related entities

##### shipment: [`PartialShipment`](./ship_engine_python_sdk/type/partial_shipment.py)<a id="shipment-partialshipmentship_engine_python_sdktypepartial_shipmentpy"></a>


You can optionally provide a `shipment` object containing any already-known values. For example, you probably already know the `ship_from` address, and you may also already know what carrier and service you want to use. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ParseShipmentRequestBody`](./ship_engine_python_sdk/type/parse_shipment_request_body.py)
The only required field is `text`, which is the text to be parsed. You can optionally also provide a `shipment` containing any already-known values. For example, you probably already know the `ship_from` address, and you may also already know what carrier and service you want to use. 

#### 🔄 Return<a id="🔄-return"></a>

[`ParseShipmentResponseBody`](./ship_engine_python_sdk/pydantic/parse_shipment_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/recognize` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipment_0`<a id="shipengineshipmentsshipment_0"></a>

Update a shipment object based on its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipment_0_response = shipengine.shipments.shipment_0(
    ship_to={},
    ship_from={},
    shipment_id="se-28529731",
    tags=[],
    shipment_id="se-28529731",
    carrier_id="se-28529731",
    service_code="usps_first_class_mail",
    external_order_id="string_example",
    items=[],
    tax_identifiers=[
        {
            "taxable_entity_type": "shipper",
            "identifier_type": "vat",
            "issuing_authority": "issuing_authority_example",
            "value": "value_example",
        }
    ],
    external_shipment_id="string_example",
    shipment_number="string_example",
    ship_date="2018-09-23T00:00:00.000Z",
    created_at="2018-09-23T15:00:00.000Z",
    modified_at="2018-09-23T15:00:00.000Z",
    shipment_status="pending",
    warehouse_id="se-28529731",
    return_to={},
    is_return=False,
    confirmation="none",
    customs={
        "contents": "merchandise",
        "non_delivery": "return_to_sender",
        "terms_of_trade_code": "exw",
        "customs_items": [],
    },
    advanced_options={
        "bill_to_country_code": "CA",
        "bill_to_party": "recipient",
        "contains_alcohol": False,
        "delivered_duty_paid": False,
        "dry_ice": False,
        "non_machinable": False,
        "saturday_delivery": False,
        "freight_class": "77.5",
        "origin_type": "pickup",
        "third_party_consignee": False,
        "dangerous_goods": False,
    },
    insurance_provider="none",
    order_source_code="amazon_ca",
    packages=[
        {
            "package_id": "se-28529731",
            "package_code": "small_flat_rate_box",
            "content_description": "Hand knitted wool socks",
            "weight": {
                "value": 0,
                "unit": "pound",
            },
            "tracking_number": "1Z932R800392060079",
            "products": [],
        }
    ],
    total_weight={
        "value": 0,
        "unit": "pound",
    },
    comparison_rate_type="retail",
    validate_address="no_validation",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ship_to: [`ShippingAddressTo`](./ship_engine_python_sdk/type/shipping_address_to.py)<a id="ship_to-shippingaddresstoship_engine_python_sdktypeshipping_address_topy"></a>


The recipient's mailing address

##### ship_from: [`ShippingAddress`](./ship_engine_python_sdk/type/shipping_address.py)<a id="ship_from-shippingaddressship_engine_python_sdktypeshipping_addresspy"></a>


The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse](https://www.shipengine.com/docs/reference/create-warehouse/).  Then you can simply specify the `warehouse_id` rather than the complete address each time. 

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

##### tags: List[`Tag`]<a id="tags-listtag"></a>

Arbitrary tags associated with this shipment.  Tags can be used to categorize shipments, and shipments can be queried by their tags. 

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="shipment_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the shipment

##### carrier_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="carrier_id-seidship_engine_python_sdktypese_idpy"></a>

The carrier account that is billed for the shipping charges

##### service_code: [`ServiceCode`](./ship_engine_python_sdk/type/service_code.py)<a id="service_code-servicecodeship_engine_python_sdktypeservice_codepy"></a>

The [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc. 

##### external_order_id: `Optional[str]`<a id="external_order_id-optionalstr"></a>

ID that the Order Source assigned

##### items: List[`ShipmentItem`]<a id="items-listshipmentitem"></a>

Describe the packages included in this shipment as related to potential metadata that was imported from external order sources 

##### tax_identifiers: List[`TaxIdentifier`]<a id="tax_identifiers-listtaxidentifier"></a>

##### external_shipment_id: `Optional[str]`<a id="external_shipment_id-optionalstr"></a>

A unique user-defined key to identify a shipment.  This can be used to retrieve the shipment.  > **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated. 

##### shipment_number: `Optional[str]`<a id="shipment_number-optionalstr"></a>

A non-unique user-defined number used to identify a shipment.  If undefined, this will match the external_shipment_id of the shipment.  > **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated. 

##### ship_date: [`Date`](./ship_engine_python_sdk/type/date.py)<a id="ship_date-dateship_engine_python_sdktypedatepy"></a>

The date that the shipment was (or will be) shippped.  ShipEngine will take the day of week into consideration. For example, if the carrier does not operate on Sundays, then a package that would have shipped on Sunday will ship on Monday instead. 

##### created_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="created_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the shipment was created in ShipEngine.

##### modified_at: [`DateTime`](./ship_engine_python_sdk/type/date_time.py)<a id="modified_at-datetimeship_engine_python_sdktypedate_timepy"></a>

The date and time that the shipment was created or last modified.

##### shipment_status: [`ShipmentStatus`](./ship_engine_python_sdk/type/shipment_status.py)<a id="shipment_status-shipmentstatusship_engine_python_sdktypeshipment_statuspy"></a>

The current status of the shipment

##### warehouse_id: [`SeIdNullable`](./ship_engine_python_sdk/type/se_id_nullable.py)<a id="warehouse_id-seidnullableship_engine_python_sdktypese_id_nullablepy"></a>

The [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/) that the shipment is being shipped from.  Either `warehouse_id` or `ship_from` must be specified. 

##### return_to: [`ShippingAddress`](./ship_engine_python_sdk/type/shipping_address.py)<a id="return_to-shippingaddressship_engine_python_sdktypeshipping_addresspy"></a>


The return address for this shipment.  Defaults to the `ship_from` address. 

##### is_return: `Optional[bool]`<a id="is_return-optionalbool"></a>

An optional indicator if the shipment is intended to be a return. Defaults to false if not provided. 

##### confirmation: [`DeliveryConfirmation`](./ship_engine_python_sdk/type/delivery_confirmation.py)<a id="confirmation-deliveryconfirmationship_engine_python_sdktypedelivery_confirmationpy"></a>

The type of delivery confirmation that is required for this shipment.

##### customs: [`InternationalShipmentOptionsNullable`](./ship_engine_python_sdk/type/international_shipment_options_nullable.py)<a id="customs-internationalshipmentoptionsnullableship_engine_python_sdktypeinternational_shipment_options_nullablepy"></a>


Customs information.  This is usually only needed for international shipments. 

##### advanced_options: [`AdvancedShipmentOptions`](./ship_engine_python_sdk/type/advanced_shipment_options.py)<a id="advanced_options-advancedshipmentoptionsship_engine_python_sdktypeadvanced_shipment_optionspy"></a>


Advanced shipment options.  These are entirely optional.

##### insurance_provider: [`InsuranceProvider`](./ship_engine_python_sdk/type/insurance_provider.py)<a id="insurance_provider-insuranceprovidership_engine_python_sdktypeinsurance_providerpy"></a>

The insurance provider to use for any insured packages in the shipment. 

##### order_source_code: [`OrderSourceName`](./ship_engine_python_sdk/type/order_source_name.py)<a id="order_source_code-ordersourcenameship_engine_python_sdktypeorder_source_namepy"></a>

##### packages: List[`Package`]<a id="packages-listpackage"></a>

The packages in the shipment.  > **Note:** Some carriers only allow one package per shipment.  If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned. 

##### total_weight: [`Weight`](./ship_engine_python_sdk/type/weight.py)<a id="total_weight-weightship_engine_python_sdktypeweightpy"></a>


The combined weight of all packages in the shipment

##### comparison_rate_type: `Optional[str]`<a id="comparison_rate_type-optionalstr"></a>

Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default.  Only supported for UPS and USPS.

##### validate_address: [`ValidateAddress`](./ship_engine_python_sdk/type/validate_address.py)<a id="validate_address-validateaddressship_engine_python_sdktypevalidate_addresspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateShipmentRequestBody`](./ship_engine_python_sdk/type/update_shipment_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateAndValidateShipment`](./ship_engine_python_sdk/pydantic/create_and_validate_shipment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipment_1`<a id="shipengineshipmentsshipment_1"></a>

Add a tag to the shipment object

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipment_1_response = shipengine.shipments.shipment_1(
    shipment_id="se-28529731",
    tag_name="Fragile",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

##### tag_name: [`TagName`](./ship_engine_python_sdk/type/.py)<a id="tag_name-tagnameship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TagShipmentResponseBody`](./ship_engine_python_sdk/pydantic/tag_shipment_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}/tags/{tag_name}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipment_2`<a id="shipengineshipmentsshipment_2"></a>

Remove an existing tag from the Shipment object

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipment_2_response = shipengine.shipments.shipment_2(
    shipment_id="se-28529731",
    tag_name="Fragile",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

##### tag_name: [`TagName`](./ship_engine_python_sdk/type/.py)<a id="tag_name-tagnameship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}/tags/{tag_name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipments`<a id="shipengineshipmentsshipments"></a>

Get list of Shipments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipments_response = shipengine.shipments.shipments(
    shipment_status="pending",
    batch_id="se-28529731",
    tag="Letters_to_santa",
    created_at_start="2019-03-12T19:24:13.657Z",
    created_at_end="2019-03-12T19:24:13.657Z",
    modified_at_start="2019-03-12T19:24:13.657Z",
    modified_at_end="2019-03-12T19:24:13.657Z",
    page=2,
    page_size=50,
    sales_order_id="string_example",
    sort_dir="asc",
    sort_by="modified_at",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_status: [`ShipmentStatus`](./ship_engine_python_sdk/type/.py)<a id="shipment_status-shipmentstatusship_engine_python_sdktypepy"></a>

##### batch_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="batch_id-seidship_engine_python_sdktypepy"></a>

Batch ID

##### tag: `str`<a id="tag-str"></a>

Search for shipments based on the custom tag added to the shipment object

##### created_at_start: `datetime`<a id="created_at_start-datetime"></a>

Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)

##### created_at_end: `datetime`<a id="created_at_end-datetime"></a>

Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)

##### modified_at_start: `datetime`<a id="modified_at_start-datetime"></a>

Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time)

##### modified_at_end: `datetime`<a id="modified_at_end-datetime"></a>

Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time)

##### page: `int`<a id="page-int"></a>

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 

##### page_size: `int`<a id="page_size-int"></a>

The number of results to return per response.

##### sales_order_id: `str`<a id="sales_order_id-str"></a>

Sales Order ID

##### sort_dir: [`SortDir`](./ship_engine_python_sdk/type/.py)<a id="sort_dir-sortdirship_engine_python_sdktypepy"></a>

Controls the sort order of the query.

##### sort_by: [`ShipmentsSortBy`](./ship_engine_python_sdk/type/.py)<a id="sort_by-shipmentssortbyship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ListShipmentsResponseBody`](./ship_engine_python_sdk/pydantic/list_shipments_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipments_0`<a id="shipengineshipmentsshipments_0"></a>

Create one or multiple shipments.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipments_0_response = shipengine.shipments.shipments_0(
    shipments=[
        {}
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipments: List[`AddressValidatingShipment`]<a id="shipments-listaddressvalidatingshipment"></a>

An array of shipments to be created.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateShipmentsRequestBody`](./ship_engine_python_sdk/type/create_shipments_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateShipmentsResponseBody`](./ship_engine_python_sdk/pydantic/create_shipments_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.shipments_1`<a id="shipengineshipmentsshipments_1"></a>

Mark a shipment cancelled, if it is no longer needed or being used by your organized. Any label associated with the shipment needs to be voided first
An example use case would be if a batch label creation job is going to run at a set time and only queries `pending` shipments. Marking a shipment as cancelled
would remove it from this process


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipments_1_response = shipengine.shipments.shipments_1(
    shipment_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipment_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="shipment_id-seidship_engine_python_sdktypepy"></a>

Shipment ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/{shipment_id}/cancel` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.shipments.update_tags`<a id="shipengineshipmentsupdate_tags"></a>

Update Shipments Tags

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shipengine.shipments.update_tags(
    shipments_tags=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shipments_tags: [`UpdateShipmentsTagsShipmentsTags`](./ship_engine_python_sdk/type/update_shipments_tags_shipments_tags.py)<a id="shipments_tags-updateshipmentstagsshipmentstagsship_engine_python_sdktypeupdate_shipments_tags_shipments_tagspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateShipmentsTags`](./ship_engine_python_sdk/type/update_shipments_tags.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/shipments/tags` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tags.tag`<a id="shipenginetagstag"></a>

Create a new Tag for customizing how you track your shipments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tag_response = shipengine.tags.tag(
    tag_name="Fragile",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_name: [`TagName`](./ship_engine_python_sdk/type/.py)<a id="tag_name-tagnameship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Tag`](./ship_engine_python_sdk/pydantic/tag.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tags/{tag_name}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tags.tag_0`<a id="shipenginetagstag_0"></a>

Delete a tag that is no longer needed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tag_0_response = shipengine.tags.tag_0(
    tag_name="Fragile",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_name: [`TagName`](./ship_engine_python_sdk/type/.py)<a id="tag_name-tagnameship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tags/{tag_name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tags.tag_1`<a id="shipenginetagstag_1"></a>

Change a tag name while still keeping the relevant shipments attached to it

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tag_1_response = shipengine.tags.tag_1(
    tag_name="Fragile",
    new_tag_name="Fragile",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_name: [`TagName`](./ship_engine_python_sdk/type/.py)<a id="tag_name-tagnameship_engine_python_sdktypepy"></a>

##### new_tag_name: [`TagName`](./ship_engine_python_sdk/type/.py)<a id="new_tag_name-tagnameship_engine_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tags/{tag_name}/{new_tag_name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tags.tags`<a id="shipenginetagstags"></a>

Get a list of all tags associated with an account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tags_response = shipengine.tags.tags()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListTagsResponseBody`](./ship_engine_python_sdk/pydantic/list_tags_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tokens.generate_ephemeral_token`<a id="shipenginetokensgenerate_ephemeral_token"></a>

This endpoint returns a token that can be passed to an application for authorized access.  The lifetime of this token is 10 seconds.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_ephemeral_token_response = shipengine.tokens.generate_ephemeral_token(
    redirect="shipengine-dashboard",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### redirect: [`Redirect`](./ship_engine_python_sdk/type/.py)<a id="redirect-redirectship_engine_python_sdktypepy"></a>

Include a redirect url to the application formatted with the ephemeral token.

#### 🔄 Return<a id="🔄-return"></a>

[`TokensGetEphemeralTokenResponseBodyYaml`](./ship_engine_python_sdk/pydantic/tokens_get_ephemeral_token_response_body_yaml.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tokens/ephemeral` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tracking.info_retrieval`<a id="shipenginetrackinginfo_retrieval"></a>

Retrieve package tracking information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
info_retrieval_response = shipengine.tracking.info_retrieval(
    carrier_code="stamps_com",
    tracking_number="9405511899223197428490",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_code: `str`<a id="carrier_code-str"></a>

A [shipping carrier](https://www.shipengine.com/docs/carriers/setup/), such as `fedex`, `dhl_express`, `stamps_com`, etc. 

##### tracking_number: `str`<a id="tracking_number-str"></a>

The tracking number associated with a shipment

#### 🔄 Return<a id="🔄-return"></a>

[`TrackingInformation`](./ship_engine_python_sdk/pydantic/tracking_information.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tracking` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tracking.tracking`<a id="shipenginetrackingtracking"></a>

Allows you to subscribe to tracking updates for a package. You specify the carrier_code and tracking_number of the package,
and receive notifications via webhooks whenever the shipping status changes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tracking_response = shipengine.tracking.tracking(
    carrier_code="stamps_com",
    tracking_number="9405511899223197428490",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_code: `str`<a id="carrier_code-str"></a>

A [shipping carrier](https://www.shipengine.com/docs/carriers/setup/), such as `fedex`, `dhl_express`, `stamps_com`, etc. 

##### tracking_number: `str`<a id="tracking_number-str"></a>

The tracking number associated with a shipment

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tracking/start` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.tracking.tracking_0`<a id="shipenginetrackingtracking_0"></a>

Unsubscribe from tracking updates for a package.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tracking_0_response = shipengine.tracking.tracking_0(
    carrier_code="stamps_com",
    tracking_number="9405511899223197428490",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### carrier_code: `str`<a id="carrier_code-str"></a>

A [shipping carrier](https://www.shipengine.com/docs/carriers/setup/), such as `fedex`, `dhl_express`, `stamps_com`, etc. 

##### tracking_number: `str`<a id="tracking_number-str"></a>

The tracking number associated with a shipment

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tracking/stop` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.warehouses.get_by_id`<a id="shipenginewarehousesget_by_id"></a>

Retrieve warehouse data based on the warehouse ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.warehouses.get_by_id(
    warehouse_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Warehouse ID

#### 🔄 Return<a id="🔄-return"></a>

[`Warehouse`](./ship_engine_python_sdk/pydantic/warehouse.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/warehouses/{warehouse_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.warehouses.update_settings`<a id="shipenginewarehousesupdate_settings"></a>

Update Warehouse settings object information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_settings_response = shipengine.warehouses.update_settings(
    warehouse_id="se-28529731",
    is_default=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Warehouse ID

##### is_default: `Optional[bool]`<a id="is_default-optionalbool"></a>

The default property on the warehouse.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateWarehouseSettingsRequestBody`](./ship_engine_python_sdk/type/update_warehouse_settings_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/warehouses/{warehouse_id}/settings` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.warehouses.warehouse`<a id="shipenginewarehouseswarehouse"></a>

Create a warehouse location that you can use to create shipping items by simply passing in the generated warehouse id.
If the return address is not supplied in the request body then it is assumed that the origin address is the return address as well


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
warehouse_response = shipengine.warehouses.warehouse(
    warehouse_id="se-28529731",
    is_default=False,
    name="Zero Cool HQ",
    created_at="2019-06-25T18:12:35.583Z",
    origin_address={
        "name": "John Doe",
        "phone": "+1 204-253-9411 ext. 123",
        "email": "example@example.com",
        "company_name": "The Home Depot",
        "address_line1": "1999 Bishop Grandin Blvd.",
        "address_line2": "Unit 408",
        "address_line3": "Building #7",
        "city_locality": "Winnipeg",
        "state_province": "Manitoba",
        "postal_code": "78756-3717",
        "country_code": "CA",
        "address_residential_indicator": "unknown",
    },
    return_address={
        "name": "John Doe",
        "phone": "+1 204-253-9411 ext. 123",
        "email": "example@example.com",
        "company_name": "The Home Depot",
        "address_line1": "1999 Bishop Grandin Blvd.",
        "address_line2": "Unit 408",
        "address_line3": "Building #7",
        "city_locality": "Winnipeg",
        "state_province": "Manitoba",
        "postal_code": "78756-3717",
        "country_code": "CA",
        "address_residential_indicator": "unknown",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="warehouse_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the warehouse

##### is_default: `Optional[bool]`<a id="is_default-optionalbool"></a>

Designates which single warehouse is the default on the account

##### name: `str`<a id="name-str"></a>

Name of the warehouse

##### created_at: `datetime`<a id="created_at-datetime"></a>

Timestamp that indicates when the warehouse was created

##### origin_address: [`PartialAddress`](./ship_engine_python_sdk/type/partial_address.py)<a id="origin_address-partialaddressship_engine_python_sdktypepartial_addresspy"></a>


The origin address of the warehouse

##### return_address: [`PartialAddress`](./ship_engine_python_sdk/type/partial_address.py)<a id="return_address-partialaddressship_engine_python_sdktypepartial_addresspy"></a>


The return address associated with the warehouse

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Warehouse`](./ship_engine_python_sdk/type/warehouse.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Warehouse`](./ship_engine_python_sdk/pydantic/warehouse.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/warehouses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.warehouses.warehouse_0`<a id="shipenginewarehouseswarehouse_0"></a>

Update Warehouse object information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
warehouse_0_response = shipengine.warehouses.warehouse_0(
    warehouse_id="se-28529731",
    warehouse_id="se-28529731",
    is_default=False,
    name="Zero Cool HQ",
    created_at="2019-06-25T18:12:35.583Z",
    origin_address={
        "name": "John Doe",
        "phone": "+1 204-253-9411 ext. 123",
        "email": "example@example.com",
        "company_name": "The Home Depot",
        "address_line1": "1999 Bishop Grandin Blvd.",
        "address_line2": "Unit 408",
        "address_line3": "Building #7",
        "city_locality": "Winnipeg",
        "state_province": "Manitoba",
        "postal_code": "78756-3717",
        "country_code": "CA",
        "address_residential_indicator": "unknown",
    },
    return_address={
        "name": "John Doe",
        "phone": "+1 204-253-9411 ext. 123",
        "email": "example@example.com",
        "company_name": "The Home Depot",
        "address_line1": "1999 Bishop Grandin Blvd.",
        "address_line2": "Unit 408",
        "address_line3": "Building #7",
        "city_locality": "Winnipeg",
        "state_province": "Manitoba",
        "postal_code": "78756-3717",
        "country_code": "CA",
        "address_residential_indicator": "unknown",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Warehouse ID

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/se_id.py)<a id="warehouse_id-seidship_engine_python_sdktypese_idpy"></a>

A string that uniquely identifies the warehouse

##### is_default: `Optional[bool]`<a id="is_default-optionalbool"></a>

Designates which single warehouse is the default on the account

##### name: `str`<a id="name-str"></a>

Name of the warehouse

##### created_at: `datetime`<a id="created_at-datetime"></a>

Timestamp that indicates when the warehouse was created

##### origin_address: [`PartialAddress`](./ship_engine_python_sdk/type/partial_address.py)<a id="origin_address-partialaddressship_engine_python_sdktypepartial_addresspy"></a>


The origin address of the warehouse

##### return_address: [`PartialAddress`](./ship_engine_python_sdk/type/partial_address.py)<a id="return_address-partialaddressship_engine_python_sdktypepartial_addresspy"></a>


The return address associated with the warehouse

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Warehouse`](./ship_engine_python_sdk/type/warehouse.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/warehouses/{warehouse_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.warehouses.warehouse_1`<a id="shipenginewarehouseswarehouse_1"></a>

Delete a warehouse by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
warehouse_1_response = shipengine.warehouses.warehouse_1(
    warehouse_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### warehouse_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="warehouse_id-seidship_engine_python_sdktypepy"></a>

Warehouse ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/warehouses/{warehouse_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.warehouses.warehouses`<a id="shipenginewarehouseswarehouses"></a>

Retrieve a list of warehouses associated with this account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
warehouses_response = shipengine.warehouses.warehouses()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListWarehousesResponseBody`](./ship_engine_python_sdk/pydantic/list_warehouses_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/warehouses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.webhooks.get_by_id`<a id="shipenginewebhooksget_by_id"></a>

Retrieve individual webhook by an ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = shipengine.webhooks.get_by_id(
    webhook_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="webhook_id-seidship_engine_python_sdktypepy"></a>

Webhook ID

#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./ship_engine_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/environment/webhooks/{webhook_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.webhooks.webhook`<a id="shipenginewebhookswebhook"></a>

Create a webook for specific events in the environment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhook_response = shipengine.webhooks.webhook(
    event="batch",
    url="http://api.shipengine.com/v1/labels/se-28529731",
    headers=[
        {
            "key": "custom-key",
            "value": "custom-value",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event: [`WebhookEvent`](./ship_engine_python_sdk/type/webhook_event.py)<a id="event-webhookeventship_engine_python_sdktypewebhook_eventpy"></a>

##### url: [`Url`](./ship_engine_python_sdk/type/url.py)<a id="url-urlship_engine_python_sdktypeurlpy"></a>

The url that the webhook sends the request to

##### headers: List[`WebhookHeader`]<a id="headers-listwebhookheader"></a>

Array of custom webhook headers

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateWebhookRequestBody`](./ship_engine_python_sdk/type/create_webhook_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./ship_engine_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/environment/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.webhooks.webhook_0`<a id="shipenginewebhookswebhook_0"></a>

Update the webhook url property

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhook_0_response = shipengine.webhooks.webhook_0(
    webhook_id="se-28529731",
    url="http://api.shipengine.com/v1/labels/se-28529731",
    headers=[
        {
            "key": "custom-key",
            "value": "custom-value",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="webhook_id-seidship_engine_python_sdktypepy"></a>

Webhook ID

##### url: [`Url`](./ship_engine_python_sdk/type/url.py)<a id="url-urlship_engine_python_sdktypeurlpy"></a>

The url that the wehbook sends the request

##### headers: List[`WebhookHeader`]<a id="headers-listwebhookheader"></a>

Array of custom webhook headers

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateWebhookRequestBody`](./ship_engine_python_sdk/type/update_webhook_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/environment/webhooks/{webhook_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.webhooks.webhook_1`<a id="shipenginewebhookswebhook_1"></a>

Delete a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhook_1_response = shipengine.webhooks.webhook_1(
    webhook_id="se-28529731",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: [`SeId`](./ship_engine_python_sdk/type/.py)<a id="webhook_id-seidship_engine_python_sdktypepy"></a>

Webhook ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmptyResponseBody`](./ship_engine_python_sdk/pydantic/empty_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/environment/webhooks/{webhook_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shipengine.webhooks.webhooks`<a id="shipenginewebhookswebhooks"></a>

List all webhooks currently enabled for the account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhooks_response = shipengine.webhooks.webhooks()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListWebhooksResponseBody`](./ship_engine_python_sdk/pydantic/list_webhooks_response_body.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/environment/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
