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

from wordlift_client.models.build_authorize_uri_request import BuildAuthorizeUriRequest

class TestBuildAuthorizeUriRequest(unittest.TestCase):
    """BuildAuthorizeUriRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuildAuthorizeUriRequest:
        """Test BuildAuthorizeUriRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildAuthorizeUriRequest`
        """
        model = BuildAuthorizeUriRequest()
        if include_optional:
            return BuildAuthorizeUriRequest(
                redirect_uri = ''
            )
        else:
            return BuildAuthorizeUriRequest(
                redirect_uri = '',
        )
        """

    def testBuildAuthorizeUriRequest(self):
        """Test BuildAuthorizeUriRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
