# coding: utf-8

"""
    WordLift Fact-Checking API

    API for semi-automated fact-checking. Returns schema.org/ClaimReview markup. This markup is structured data that contains information about the fact check -- for example, what was the claim being assessed, who made the claim, what was the verdict.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.node_request_metadata_value import NodeRequestMetadataValue

class TestNodeRequestMetadataValue(unittest.TestCase):
    """NodeRequestMetadataValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeRequestMetadataValue:
        """Test NodeRequestMetadataValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeRequestMetadataValue`
        """
        model = NodeRequestMetadataValue()
        if include_optional:
            return NodeRequestMetadataValue(
            )
        else:
            return NodeRequestMetadataValue(
        )
        """

    def testNodeRequestMetadataValue(self):
        """Test NodeRequestMetadataValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
