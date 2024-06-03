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

from wordlift_client.models.vector_search_question_response_item import VectorSearchQuestionResponseItem

class TestVectorSearchQuestionResponseItem(unittest.TestCase):
    """VectorSearchQuestionResponseItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VectorSearchQuestionResponseItem:
        """Test VectorSearchQuestionResponseItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VectorSearchQuestionResponseItem`
        """
        model = VectorSearchQuestionResponseItem()
        if include_optional:
            return VectorSearchQuestionResponseItem(
                answer = '',
                question = ''
            )
        else:
            return VectorSearchQuestionResponseItem(
        )
        """

    def testVectorSearchQuestionResponseItem(self):
        """Test VectorSearchQuestionResponseItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
