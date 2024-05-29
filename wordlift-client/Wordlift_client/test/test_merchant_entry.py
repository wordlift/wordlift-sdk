# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from Wordlift_client.models.merchant_entry import MerchantEntry

class TestMerchantEntry(unittest.TestCase):
    """MerchantEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantEntry:
        """Test MerchantEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantEntry`
        """
        model = MerchantEntry()
        if include_optional:
            return MerchantEntry(
                google_merchant_id = 56,
                website_url = ''
            )
        else:
            return MerchantEntry(
                google_merchant_id = 56,
                website_url = '',
        )
        """

    def testMerchantEntry(self):
        """Test MerchantEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
