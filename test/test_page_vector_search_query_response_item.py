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

from wordlift_client.models.page_vector_search_query_response_item import PageVectorSearchQueryResponseItem

class TestPageVectorSearchQueryResponseItem(unittest.TestCase):
    """PageVectorSearchQueryResponseItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageVectorSearchQueryResponseItem:
        """Test PageVectorSearchQueryResponseItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageVectorSearchQueryResponseItem`
        """
        model = PageVectorSearchQueryResponseItem()
        if include_optional:
            return PageVectorSearchQueryResponseItem(
                first = '',
                items = [
                    wordlift_client.models.vector_search_query_response_item.VectorSearchQueryResponseItem(
                        dataset_uri = '', 
                        id = '', 
                        iri = '', 
                        metadata = {
                            'key' : None
                            }, 
                        node_id = '', 
                        score = 1.337, 
                        text = '', )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = ''
            )
        else:
            return PageVectorSearchQueryResponseItem(
                first = '',
                items = [
                    wordlift_client.models.vector_search_query_response_item.VectorSearchQueryResponseItem(
                        dataset_uri = '', 
                        id = '', 
                        iri = '', 
                        metadata = {
                            'key' : None
                            }, 
                        node_id = '', 
                        score = 1.337, 
                        text = '', )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = '',
        )
        """

    def testPageVectorSearchQueryResponseItem(self):
        """Test PageVectorSearchQueryResponseItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
