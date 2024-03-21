# coding: utf-8

"""
    ShipEngine API

    ShipEngine's easy-to-use REST API lets you manage all of your shipping needs without worrying about the complexities of different carrier APIs and protocols. We handle all the heavy lifting so you can focus on providing a first-class shipping experience for your customers at the best possible prices.  Each of ShipEngine's features can be used by itself or in conjunction with each other to build powerful shipping functionality into your application or service.  ## Getting Started If you're new to REST APIs then be sure to read our [introduction to REST](https://www.shipengine.com/docs/rest/) to understand the basics.  Learn how to [authenticate yourself to ShipEngine](https://www.shipengine.com/docs/auth/), and then use our [sandbox environment](https://www.shipengine.com/docs/sandbox/) to kick the tires and get familiar with our API. If you run into any problems, then be sure to check the [error handling guide](https://www.shipengine.com/docs/errors/) for tips.  Here are some step-by-step **tutorials** to get you started:    - [Learn how to create your first shipping label](https://www.shipengine.com/docs/labels/create-a-label/)   - [Calculate shipping costs and compare rates across carriers](https://www.shipengine.com/docs/rates/)   - [Track packages on-demand or in real time](https://www.shipengine.com/docs/tracking/)   - [Validate mailing addresses anywhere on Earth](https://www.shipengine.com/docs/addresses/validation/)   ## Shipping Labels for Every Major Carrier ShipEngine makes it easy to [create shipping labels for any carrier](https://www.shipengine.com/docs/labels/create-a-label/) and [download them](https://www.shipengine.com/docs/labels/downloading/) in a [variety of file formats](https://www.shipengine.com/docs/labels/formats/). You can even customize labels with your own [messages](https://www.shipengine.com/docs/labels/messages/) and [images](https://www.shipengine.com/docs/labels/branding/).   ## Real-Time Package Tracking With ShipEngine you can [get the current status of a package](https://www.shipengine.com/docs/tracking/) or [subscribe to real-time tracking updates](https://www.shipengine.com/docs/tracking/webhooks/) via webhooks. You can also create [custimized tracking pages](https://www.shipengine.com/docs/tracking/branded-tracking-page/) with your own branding so your customers will always know where their package is.   ## Compare Shipping Costs Across Carriers Make sure you ship as cost-effectively as possible by [comparing rates across carriers](https://www.shipengine.com/docs/rates/get-shipment-rates/) using the ShipEngine Rates API. Or if you don't know the full shipment details yet, then you can [get rate estimates](https://www.shipengine.com/docs/rates/estimate/) with limited address info.   ## Worldwide Address Validation ShipEngine supports [address validation](https://www.shipengine.com/docs/addresses/validation/) for virtually [every country on Earth](https://www.shipengine.com/docs/addresses/validation/countries/), including the United States, Canada, Great Britain, Australia, Germany, France, Norway, Spain, Sweden, Israel, Italy, and over 160 others. 

    The version of the OpenAPI document: 1.1.202403202303
    Contact: sales@shipengine.com
    Created by: https://www.shipengine.com/contact/
"""

import unittest
from ship_engine_python_sdk.configuration import check_url
from ship_engine_python_sdk.exceptions import InvalidHostConfigurationError


class TestIsValidUrl(unittest.TestCase):
    def test_valid_urls(self):
        valid_urls = [
            "http://www.example.com",
            "https://www.example.com",
            "http://example.com",
            "https://example.com/path/to/resource",
            "http://example.com:8080",
            "https://example.co.uk",
            "https://subdomain.example.com",
            "https://api.example.com/v1/resource",
            "https://example.com/path/to/resource/123",
            "https://www.example.com:8080",
            "https://www.example.com:8080/path/to/resource",
            "http://sub.example.com:8080",
            "http://deep.sub.domain.example.com",
            "http://127.0.0.1:4010",
            "https://deep.sub.domain.example.com:8080/path",
            "http://example.io",
            "https://example.app",
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(check_url(url))

    def test_invalid_urls(self):
        invalid_urls = [
            "not_a_url",
            "http:/example.com",
            "http://",
            "http://.com",
            "example.com",
            "http://example.com#fragment",
            "www.example.com",
            "https://example.com/path/to/resource?query=value",
            "https://example.com/path/to/resource?query=value&key2=value2",
            "https://",
            "ftp://files.example.com",
            "//example.com",
            "https://example,com",
            "https:/example.com",
            "https:// example.com",
            "https://example.com path",
            "http://..com",
            "https://..example.com",
            "http://example..com",
            "https://example.com./path",
            "https://example.com..",
            "http://:8080",
            "https://example.com:",
            "http://example.com:abc",
            "https://.example.com",
            "http://example.",
            "https:// example:8080.com",
            "http:// example.com:8080/path",
            "https://:8080/path",
        ]
        for url in invalid_urls:
            with self.subTest(url=url):
                with self.assertRaises(InvalidHostConfigurationError):
                    check_url(url)
                    raise Exception("URL should be invalid: " + url)


if __name__ == "__main__":
    unittest.main()
