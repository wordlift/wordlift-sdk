# wordlift-client
GraphQL endpoint to query Knowledge Graphs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.38.0
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://wordlift.io](https://wordlift.io)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import wordlift_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wordlift_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountApi(api_client)

    try:
        # Get
        api_response = await api_instance.get_me()
        print("The response of AccountApi->get_me:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_me: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wordlift.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**get_me**](docs/AccountApi.md#get_me) | **GET** /accounts/me | Get
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /accounts/{id} | Get an account.
*AccountsApi* | [**list_accounts**](docs/AccountsApi.md#list_accounts) | **GET** /accounts | List
*AccountsApi* | [**update_account**](docs/AccountsApi.md#update_account) | **PUT** /accounts/{id} | Update an account.
*AddOnsApi* | [**list_configurations**](docs/AddOnsApi.md#list_configurations) | **GET** /addon/configurations | List
*AnalysesApi* | [**analyse**](docs/AnalysesApi.md#analyse) | **POST** /single | Analyse content
*AnalysesApi* | [**create**](docs/AnalysesApi.md#create) | **POST** /analysis/analyses | Create
*AnalysesApi* | [**merge**](docs/AnalysesApi.md#merge) | **POST** /merge | Analyse and Merge
*AnalysesApi* | [**v2_analysis**](docs/AnalysesApi.md#v2_analysis) | **POST** /v2/analyze | Analyse Web Page
*AnalyticsImportsApi* | [**create_analytics_import**](docs/AnalyticsImportsApi.md#create_analytics_import) | **POST** /analytics-imports | Create
*AutocompleteApi* | [**get3**](docs/AutocompleteApi.md#get3) | **GET** /autocomplete | Get
*BotifyCrawlImportsApi* | [**create_botify_crawl_import**](docs/BotifyCrawlImportsApi.md#create_botify_crawl_import) | **POST** /botify-crawl-imports | Create
*ClassificationsApi* | [**classify_using_post**](docs/ClassificationsApi.md#classify_using_post) | **POST** /classification/classify | Create
*ContentExpansionsApi* | [**create_content_expansion**](docs/ContentExpansionsApi.md#create_content_expansion) | **POST** /content-expansions | Create
*ContentGenerationCompletionApi* | [**create_completion**](docs/ContentGenerationCompletionApi.md#create_completion) | **POST** /completions | Create a completion
*ContentGenerationFieldsApi* | [**list_fields**](docs/ContentGenerationFieldsApi.md#list_fields) | **GET** /content-generations/{contentGenerationId}/fields | List
*ContentGenerationFieldsApi* | [**list_fields_for_graph_ql_query**](docs/ContentGenerationFieldsApi.md#list_fields_for_graph_ql_query) | **POST** /fields | List for GraphQl Query
*ContentGenerationModelsApi* | [**list_models**](docs/ContentGenerationModelsApi.md#list_models) | **GET** /models | List
*ContentGenerationPresetsApi* | [**list_presets**](docs/ContentGenerationPresetsApi.md#list_presets) | **GET** /graphql-query-presets | List
*ContentGenerationRecordsApi* | [**get_record**](docs/ContentGenerationRecordsApi.md#get_record) | **GET** /content-generations/{contentGenerationId}/records/{recordId} | Get
*ContentGenerationRecordsApi* | [**list_records**](docs/ContentGenerationRecordsApi.md#list_records) | **GET** /content-generations/{contentGenerationId}/records | List
*ContentGenerationRecordsApi* | [**list_records_as_events**](docs/ContentGenerationRecordsApi.md#list_records_as_events) | **GET** /content-generations/{contentGenerationId}/records-sse | List as Events
*ContentGenerationRecordsApi* | [**update_record**](docs/ContentGenerationRecordsApi.md#update_record) | **PUT** /content-generations/{contentGenerationId}/records/{recordId} | Update
*ContentGenerationRecordsApi* | [**update_records**](docs/ContentGenerationRecordsApi.md#update_records) | **PUT** /content-generations/{contentGenerationId}/records | Update
*ContentGenerationRecordsApi* | [**update_records_collection**](docs/ContentGenerationRecordsApi.md#update_records_collection) | **PUT** /content-generations/{contentGenerationId}/records-collection | Update
*ContentGenerationRecordsExportApi* | [**export**](docs/ContentGenerationRecordsExportApi.md#export) | **GET** /content-generations/{contentGenerationId}/records.tsv | 
*ContentGenerationRendersApi* | [**render_template**](docs/ContentGenerationRendersApi.md#render_template) | **POST** /content-generations/renders | Render
*ContentGenerationRendersApi* | [**render_template_collection**](docs/ContentGenerationRendersApi.md#render_template_collection) | **POST** /content-generations/renders-collection | Render
*ContentGenerationStatsApi* | [**get4**](docs/ContentGenerationStatsApi.md#get4) | **GET** /content-generations/{contentGenerationId}/stats | Get
*ContentGenerationSyncsApi* | [**create_sync1**](docs/ContentGenerationSyncsApi.md#create_sync1) | **POST** /content-generations/{contentGenerationId}/syncs | Create
*ContentGenerationWordBiasesApi* | [**create_word**](docs/ContentGenerationWordBiasesApi.md#create_word) | **POST** /content-generations/{contentGenerationId}/words | Create
*ContentGenerationWordBiasesApi* | [**create_words**](docs/ContentGenerationWordBiasesApi.md#create_words) | **PUT** /content-generations/{contentGenerationId}/words | Update for prompt
*ContentGenerationWordBiasesApi* | [**create_words_from_csv**](docs/ContentGenerationWordBiasesApi.md#create_words_from_csv) | **PUT** /content-generations/{contentGenerationId}/words/imports | Update from CSV
*ContentGenerationWordBiasesApi* | [**delete_word**](docs/ContentGenerationWordBiasesApi.md#delete_word) | **DELETE** /content-generations/{contentGenerationId}/words/{id} | Delete
*ContentGenerationWordBiasesApi* | [**list_words**](docs/ContentGenerationWordBiasesApi.md#list_words) | **GET** /content-generations/{contentGenerationId}/words | List
*ContentGenerationWordBiasesApi* | [**update_word**](docs/ContentGenerationWordBiasesApi.md#update_word) | **PUT** /content-generations/{contentGenerationId}/words/{id} | Update
*ContentGenerationsApi* | [**create_content_generation**](docs/ContentGenerationsApi.md#create_content_generation) | **POST** /content-generations | Create
*ContentGenerationsApi* | [**delete_content_generation**](docs/ContentGenerationsApi.md#delete_content_generation) | **DELETE** /content-generations/{id} | Delete
*ContentGenerationsApi* | [**duplicate_content_generation**](docs/ContentGenerationsApi.md#duplicate_content_generation) | **POST** /content-generations/{from_content_generation_id}/duplicates | Duplicate
*ContentGenerationsApi* | [**get_content_generation**](docs/ContentGenerationsApi.md#get_content_generation) | **GET** /content-generations/{id} | Get
*ContentGenerationsApi* | [**list_content_generations**](docs/ContentGenerationsApi.md#list_content_generations) | **GET** /content-generations | List
*ContentGenerationsApi* | [**update_content_generation**](docs/ContentGenerationsApi.md#update_content_generation) | **PUT** /content-generations/{id} | Update
*CustomDomainsApi* | [**validate**](docs/CustomDomainsApi.md#validate) | **POST** /validations | Validate
*DataURIApi* | [**get2**](docs/DataURIApi.md#get2) | **GET** /data-uri | Get the Web Data URI for a Web Page URL.
*DatasetApi* | [**create_or_update_entities1**](docs/DatasetApi.md#create_or_update_entities1) | **POST** /dataset/batch | Create or update many
*DatasetApi* | [**create_or_update_entity**](docs/DatasetApi.md#create_or_update_entity) | **POST** /dataset | Create or update one
*DatasetApi* | [**delete_all_entities**](docs/DatasetApi.md#delete_all_entities) | **DELETE** /dataset/all | Delete all
*DatasetApi* | [**delete_entity**](docs/DatasetApi.md#delete_entity) | **DELETE** /dataset | Delete one
*EmbeddingApi* | [**create_embedding**](docs/EmbeddingApi.md#create_embedding) | **POST** /kg/embeddings | Create
*EmbeddingsApi* | [**create_embeddings**](docs/EmbeddingsApi.md#create_embeddings) | **POST** /api/embeddings | Create Embeddings
*EntitiesApi* | [**create_entities**](docs/EntitiesApi.md#create_entities) | **POST** /entities | Create
*EntitiesApi* | [**create_or_update_entities**](docs/EntitiesApi.md#create_or_update_entities) | **PUT** /entities | Update (or create)
*EntitiesApi* | [**delete_entities**](docs/EntitiesApi.md#delete_entities) | **DELETE** /entities | Delete
*EntitiesApi* | [**get_entities**](docs/EntitiesApi.md#get_entities) | **GET** /entities | Get
*EntitiesApi* | [**patch_entities**](docs/EntitiesApi.md#patch_entities) | **PATCH** /entities | Patch Entity
*EntityGapsApi* | [**create_entity_gap**](docs/EntityGapsApi.md#create_entity_gap) | **POST** /entity-gaps | Create
*FactCheckApi* | [**submit_fact_check**](docs/FactCheckApi.md#submit_fact_check) | **POST** /fact-check/score | Submit a fact-checking request
*GoogleMerchantsApi* | [**list_google_merchants**](docs/GoogleMerchantsApi.md#list_google_merchants) | **GET** /ext/google/shopping/merchants | List
*GoogleSearchConsoleApi* | [**list_website_search**](docs/GoogleSearchConsoleApi.md#list_website_search) | **GET** /ext/google/searchconsole/searches | List Website Search data
*GoogleSearchConsoleApi* | [**list_websites**](docs/GoogleSearchConsoleApi.md#list_websites) | **GET** /ext/google/searchconsole/websites | List
*GoogleSearchConsoleOAuth2Api* | [**create_auth_code_exchange**](docs/GoogleSearchConsoleOAuth2Api.md#create_auth_code_exchange) | **POST** /google-search-console/oauth2/auth-code-exchanges | Get an Access Code
*GoogleSearchConsoleOAuth2Api* | [**create_authorize_uri**](docs/GoogleSearchConsoleOAuth2Api.md#create_authorize_uri) | **POST** /google-search-console/oauth2/authorize-uris | Create an Authorization URI
*GoogleSearchConsoleSearchesApi* | [**list_website_search1**](docs/GoogleSearchConsoleSearchesApi.md#list_website_search1) | **GET** /accounts/me/google/searches | List Website Search data
*GraphQLApi* | [**graphql_using_post**](docs/GraphQLApi.md#graphql_using_post) | **POST** /graphql | Query
*IncludeExcludesWordPressPluginApi* | [**list_include_excludes**](docs/IncludeExcludesWordPressPluginApi.md#list_include_excludes) | **GET** /accounts/me/include-excludes | List
*IncludeExcludesWordPressPluginApi* | [**update_include_excludes**](docs/IncludeExcludesWordPressPluginApi.md#update_include_excludes) | **PUT** /accounts/me/include-excludes | Update
*InspectorApi* | [**get1**](docs/InspectorApi.md#get1) | **GET** /inspect | Inspect
*InternalLinksApi* | [**create_internal_link**](docs/InternalLinksApi.md#create_internal_link) | **POST** /internal-links | Create
*LongTailsApi* | [**get2**](docs/LongTailsApi.md#get2) | **GET** /longtail | Get entities
*LongTailsApi* | [**get3**](docs/LongTailsApi.md#get3) | **GET** /longtail/hook | Get entities by rank (async)
*LongTailsApi* | [**get_v2**](docs/LongTailsApi.md#get_v2) | **GET** /longtail/v2 | Get entities by rank
*MerchantSyncsApi* | [**create_sync**](docs/MerchantSyncsApi.md#create_sync) | **POST** /merchants/{merchantId}/syncs | Start
*MerchantSyncsApi* | [**get_merchant_sync**](docs/MerchantSyncsApi.md#get_merchant_sync) | **GET** /merchants/{merchantId}/syncs/{id} | Get by id
*MerchantSyncsApi* | [**list_merchant_syncs**](docs/MerchantSyncsApi.md#list_merchant_syncs) | **GET** /merchants/{merchantId}/syncs | List
*MerchantsApi* | [**create_merchant**](docs/MerchantsApi.md#create_merchant) | **POST** /merchants | Create
*MerchantsApi* | [**delete_merchant**](docs/MerchantsApi.md#delete_merchant) | **DELETE** /merchants/{id} | Delete by id
*MerchantsApi* | [**get_merchant**](docs/MerchantsApi.md#get_merchant) | **GET** /merchants/{id} | Get by id
*MerchantsApi* | [**list_merchants**](docs/MerchantsApi.md#list_merchants) | **GET** /merchants | List
*MerchantsApi* | [**update_merchant**](docs/MerchantsApi.md#update_merchant) | **PUT** /merchants/{id} | Update
*MicrodataApi* | [**microdata_to_json_ld**](docs/MicrodataApi.md#microdata_to_json_ld) | **GET** /microdata-to-jsonld | Microdata to JSON-LD
*OAuth2AuthorizedClientsApi* | [**create_o_auth2_authorized_client**](docs/OAuth2AuthorizedClientsApi.md#create_o_auth2_authorized_client) | **POST** /oauth2/authorized-clients | Create
*OAuth2AuthorizedClientsApi* | [**delete_o_auth2_authorized_client**](docs/OAuth2AuthorizedClientsApi.md#delete_o_auth2_authorized_client) | **DELETE** /oauth2/authorized-clients/{id} | Delete
*OAuth2AuthorizedClientsApi* | [**get_o_auth2_authorized_client**](docs/OAuth2AuthorizedClientsApi.md#get_o_auth2_authorized_client) | **GET** /oauth2/authorized-clients/{id} | Get
*OAuth2AuthorizedClientsApi* | [**list_o_auth2_authorized_clients**](docs/OAuth2AuthorizedClientsApi.md#list_o_auth2_authorized_clients) | **GET** /oauth2/authorized-clients | List
*OAuth2AuthorizedClientsApi* | [**update_o_auth2_authorized_client**](docs/OAuth2AuthorizedClientsApi.md#update_o_auth2_authorized_client) | **PUT** /oauth2/authorized-clients/{id} | Update
*PlatformConsumptionsApi* | [**create_or_update_my_platform_consumption**](docs/PlatformConsumptionsApi.md#create_or_update_my_platform_consumption) | **PUT** /platform-limit/consumptions/me | Create or update the Platform Consumption
*PlatformConsumptionsApi* | [**get_my_platform_consumption**](docs/PlatformConsumptionsApi.md#get_my_platform_consumption) | **GET** /platform-limit/consumptions/me | Get the Platform Consumption
*PlatformLimitsApi* | [**create_platform_limit**](docs/PlatformLimitsApi.md#create_platform_limit) | **POST** /platform-limit/limits | Create Platform Limit
*PlatformLimitsApi* | [**delete_platform_limit**](docs/PlatformLimitsApi.md#delete_platform_limit) | **DELETE** /platform-limit/limits/{id} | Delete Platform Limit
*PlatformLimitsApi* | [**get_platform_limit**](docs/PlatformLimitsApi.md#get_platform_limit) | **GET** /platform-limit/limits/{id} | Get Platform Limit
*PlatformLimitsApi* | [**list_platform_limits**](docs/PlatformLimitsApi.md#list_platform_limits) | **GET** /platform-limit/limits | List Platform Limits
*PlatformLimitsApi* | [**update_platform_limit**](docs/PlatformLimitsApi.md#update_platform_limit) | **PUT** /platform-limit/limits/{id} | Update Platform Limit
*PluginDiagnosticsApi* | [**update_diagnostic_plugin_collection**](docs/PluginDiagnosticsApi.md#update_diagnostic_plugin_collection) | **PUT** /accounts/me/plugin/diagnostics/plugins-collection | Update
*PluginEventsApi* | [**create_event**](docs/PluginEventsApi.md#create_event) | **POST** /plugin/events | Create
*PluginEventsApi* | [**list_events**](docs/PluginEventsApi.md#list_events) | **GET** /plugin/events | List
*QuestionsAndAnswersApi* | [**create_question_and_answer**](docs/QuestionsAndAnswersApi.md#create_question_and_answer) | **POST** /questions-and-answers | Create
*QuestionsAndAnswersApi* | [**create_questions_and_answers_collection**](docs/QuestionsAndAnswersApi.md#create_questions_and_answers_collection) | **POST** /questions-and-answers-collection | Create
*QuestionsAndAnswersApi* | [**delete_question_and_answer**](docs/QuestionsAndAnswersApi.md#delete_question_and_answer) | **DELETE** /questions-and-answers/{id} | Delete
*QuestionsAndAnswersApi* | [**delete_questions_and_answers_collection**](docs/QuestionsAndAnswersApi.md#delete_questions_and_answers_collection) | **DELETE** /questions-and-answers-collection | Delete
*QuestionsAndAnswersApi* | [**get_questions_and_answers**](docs/QuestionsAndAnswersApi.md#get_questions_and_answers) | **GET** /questions-and-answers | Get
*QuestionsAndAnswersApi* | [**update_question_and_answer**](docs/QuestionsAndAnswersApi.md#update_question_and_answer) | **PUT** /questions-and-answers/{id} | Update
*QuestionsAndAnswersApi* | [**update_questions_and_answers_collection**](docs/QuestionsAndAnswersApi.md#update_questions_and_answers_collection) | **PUT** /questions-and-answers-collection | Update
*RedeemCodesApi* | [**redeem_code**](docs/RedeemCodesApi.md#redeem_code) | **POST** /redeem-codes | Redeem the provided code and get a key
*RulesApi* | [**copy_rules**](docs/RulesApi.md#copy_rules) | **POST** /rules/copies | Copy
*RulesApi* | [**create_rule**](docs/RulesApi.md#create_rule) | **POST** /rules | Create
*RulesApi* | [**delete_rule**](docs/RulesApi.md#delete_rule) | **DELETE** /rules/{id} | Delete
*RulesApi* | [**list_rules**](docs/RulesApi.md#list_rules) | **GET** /rules | List
*RulesApi* | [**update_rule**](docs/RulesApi.md#update_rule) | **PUT** /rules/{id} | Update
*RulesApi* | [**update_rule_collection**](docs/RulesApi.md#update_rule_collection) | **PUT** /rules-collection | Update
*SEOScoresApi* | [**create_seo_score**](docs/SEOScoresApi.md#create_seo_score) | **POST** /score | Create
*SitemapGeneratorApi* | [**generate_sitemap**](docs/SitemapGeneratorApi.md#generate_sitemap) | **POST** /build | Generate Sitemap
*SitemapImportsApi* | [**create_sitemap_import**](docs/SitemapImportsApi.md#create_sitemap_import) | **POST** /sitemap-imports | Create
*SummarizationsApi* | [**microdata_to_json_ld_using_post**](docs/SummarizationsApi.md#microdata_to_json_ld_using_post) | **POST** /summarize | Create
*VectorSearchNodesApi* | [**update_nodes_collection**](docs/VectorSearchNodesApi.md#update_nodes_collection) | **PUT** /vector-search/nodes-collection | Update
*VectorSearchQueriesApi* | [**create_query**](docs/VectorSearchQueriesApi.md#create_query) | **POST** /vector-search/queries | Create
*VectorSearchQuestionsApi* | [**create_vector_search_question**](docs/VectorSearchQuestionsApi.md#create_vector_search_question) | **POST** /vector-search/questions-collection | Create
*WebAsyncsMetadataApi* | [**get**](docs/WebAsyncsMetadataApi.md#get) | **GET** /webasyncs/{id} | Get by id
*WebAsyncsMetadataApi* | [**list**](docs/WebAsyncsMetadataApi.md#list) | **GET** /webasyncs | List
*WebAsyncsResponsesApi* | [**get1**](docs/WebAsyncsResponsesApi.md#get1) | **GET** /webasyncs/{id}/pull | Get by id


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountInfo](docs/AccountInfo.md)
 - [AccountSubscription](docs/AccountSubscription.md)
 - [ActiveAccount](docs/ActiveAccount.md)
 - [AddOnConfiguration](docs/AddOnConfiguration.md)
 - [AnalysesRequest](docs/AnalysesRequest.md)
 - [AnalysesResponse](docs/AnalysesResponse.md)
 - [AnalysesResponseItem](docs/AnalysesResponseItem.md)
 - [AnalyticsImportRequest](docs/AnalyticsImportRequest.md)
 - [Annotation](docs/Annotation.md)
 - [AutocompleteResult](docs/AutocompleteResult.md)
 - [BatchRequest](docs/BatchRequest.md)
 - [BotifyCrawlImportRequest](docs/BotifyCrawlImportRequest.md)
 - [BuildAuthorizeUriRequest](docs/BuildAuthorizeUriRequest.md)
 - [BuildAuthorizeUriResponse](docs/BuildAuthorizeUriResponse.md)
 - [ClassificationRequest](docs/ClassificationRequest.md)
 - [ClassificationResponse](docs/ClassificationResponse.md)
 - [CompletionRequest](docs/CompletionRequest.md)
 - [ContentExpansionRequest](docs/ContentExpansionRequest.md)
 - [ContentExpansionResponse](docs/ContentExpansionResponse.md)
 - [ContentGeneration](docs/ContentGeneration.md)
 - [ContentGenerationRequest](docs/ContentGenerationRequest.md)
 - [ContentGenerationStats](docs/ContentGenerationStats.md)
 - [CreateEmbeddingsInput](docs/CreateEmbeddingsInput.md)
 - [CreateSEOScore200Response](docs/CreateSEOScore200Response.md)
 - [CreateSEOScoreRequest](docs/CreateSEOScoreRequest.md)
 - [DiagnosticPlugin](docs/DiagnosticPlugin.md)
 - [DiagnosticPluginRequest](docs/DiagnosticPluginRequest.md)
 - [DomainValidationRequest](docs/DomainValidationRequest.md)
 - [EmbeddingRequest](docs/EmbeddingRequest.md)
 - [Entity](docs/Entity.md)
 - [Entity1](docs/Entity1.md)
 - [EntityGapRequest](docs/EntityGapRequest.md)
 - [EntityMatch](docs/EntityMatch.md)
 - [EntityPatchRequest](docs/EntityPatchRequest.md)
 - [Event](docs/Event.md)
 - [ExchangeAuthCodeRequest](docs/ExchangeAuthCodeRequest.md)
 - [ExchangeAuthCodeResponse](docs/ExchangeAuthCodeResponse.md)
 - [Filter](docs/Filter.md)
 - [FilterValue](docs/FilterValue.md)
 - [GenerateSitemap200Response](docs/GenerateSitemap200Response.md)
 - [GenerateSitemapRequest](docs/GenerateSitemapRequest.md)
 - [GraphqlRequest](docs/GraphqlRequest.md)
 - [Html](docs/Html.md)
 - [Image](docs/Image.md)
 - [IncludeExclude](docs/IncludeExclude.md)
 - [IncludeExcludeRequest](docs/IncludeExcludeRequest.md)
 - [InspectResponse](docs/InspectResponse.md)
 - [InternalLinkRequest](docs/InternalLinkRequest.md)
 - [Item](docs/Item.md)
 - [KgEmbeddingRequest](docs/KgEmbeddingRequest.md)
 - [LevelEnum](docs/LevelEnum.md)
 - [LongtailResponse](docs/LongtailResponse.md)
 - [Merchant](docs/Merchant.md)
 - [MerchantEntry](docs/MerchantEntry.md)
 - [MerchantRequest](docs/MerchantRequest.md)
 - [MerchantSync](docs/MerchantSync.md)
 - [MerchantView](docs/MerchantView.md)
 - [Model](docs/Model.md)
 - [ModelField](docs/ModelField.md)
 - [NetworkAccountInfo](docs/NetworkAccountInfo.md)
 - [NodeRequest](docs/NodeRequest.md)
 - [NodeRequestMetadataValue](docs/NodeRequestMetadataValue.md)
 - [OAuth2AuthorizedClient](docs/OAuth2AuthorizedClient.md)
 - [OAuth2AuthorizedClientRequest](docs/OAuth2AuthorizedClientRequest.md)
 - [PageActiveAccount](docs/PageActiveAccount.md)
 - [PageAddOnConfiguration](docs/PageAddOnConfiguration.md)
 - [PageContentGeneration](docs/PageContentGeneration.md)
 - [PageField](docs/PageField.md)
 - [PageMerchantEntry](docs/PageMerchantEntry.md)
 - [PageMerchantSync](docs/PageMerchantSync.md)
 - [PageMerchantView](docs/PageMerchantView.md)
 - [PageModel](docs/PageModel.md)
 - [PageOAuth2AuthorizedClient](docs/PageOAuth2AuthorizedClient.md)
 - [PagePlatformLimit](docs/PagePlatformLimit.md)
 - [PagePreset](docs/PagePreset.md)
 - [PageRecord](docs/PageRecord.md)
 - [PageRule](docs/PageRule.md)
 - [PageVectorSearchQueryResponseItem](docs/PageVectorSearchQueryResponseItem.md)
 - [PageVectorSearchQuestionResponseItem](docs/PageVectorSearchQuestionResponseItem.md)
 - [PageWebsite](docs/PageWebsite.md)
 - [PageWebsiteSearch](docs/PageWebsiteSearch.md)
 - [PageWithLimits](docs/PageWithLimits.md)
 - [PageWord](docs/PageWord.md)
 - [PlatformLimit](docs/PlatformLimit.md)
 - [PlatformLimitRequest](docs/PlatformLimitRequest.md)
 - [Preset](docs/Preset.md)
 - [ProblemDetail](docs/ProblemDetail.md)
 - [ProjectType](docs/ProjectType.md)
 - [Properties](docs/Properties.md)
 - [Properties1](docs/Properties1.md)
 - [QuestionAndAnswer](docs/QuestionAndAnswer.md)
 - [QuestionAndAnswerRequest](docs/QuestionAndAnswerRequest.md)
 - [RankEntities](docs/RankEntities.md)
 - [Record](docs/Record.md)
 - [RenderRequest](docs/RenderRequest.md)
 - [Request](docs/Request.md)
 - [Request1](docs/Request1.md)
 - [Request2](docs/Request2.md)
 - [Request3](docs/Request3.md)
 - [Response](docs/Response.md)
 - [Response1](docs/Response1.md)
 - [Response2](docs/Response2.md)
 - [Rule](docs/Rule.md)
 - [RuleRequest](docs/RuleRequest.md)
 - [Scope](docs/Scope.md)
 - [SitemapImportRequest](docs/SitemapImportRequest.md)
 - [SmartContent](docs/SmartContent.md)
 - [SmartContentRequest](docs/SmartContentRequest.md)
 - [SubmitFactCheck200Response](docs/SubmitFactCheck200Response.md)
 - [SubmitFactCheckRequest](docs/SubmitFactCheckRequest.md)
 - [Topic](docs/Topic.md)
 - [UpdateAccountRequest](docs/UpdateAccountRequest.md)
 - [UpdateQuestionAndAnswerRequest](docs/UpdateQuestionAndAnswerRequest.md)
 - [UpdateRecordRequest](docs/UpdateRecordRequest.md)
 - [UpdateRecordsRequest](docs/UpdateRecordsRequest.md)
 - [ValidationFix](docs/ValidationFix.md)
 - [ValidationResult](docs/ValidationResult.md)
 - [ValidationTypeEnum](docs/ValidationTypeEnum.md)
 - [VectorSearchQueryRequest](docs/VectorSearchQueryRequest.md)
 - [VectorSearchQueryResponseItem](docs/VectorSearchQueryResponseItem.md)
 - [VectorSearchQueryResponseItemFieldsValueInner](docs/VectorSearchQueryResponseItemFieldsValueInner.md)
 - [VectorSearchQueryResponseItemMetadataValue](docs/VectorSearchQueryResponseItemMetadataValue.md)
 - [VectorSearchQuestionRequest](docs/VectorSearchQuestionRequest.md)
 - [VectorSearchQuestionResponseItem](docs/VectorSearchQuestionResponseItem.md)
 - [WebAsync](docs/WebAsync.md)
 - [WebPage](docs/WebPage.md)
 - [WebpageProperties](docs/WebpageProperties.md)
 - [Website](docs/Website.md)
 - [WebsiteSearch](docs/WebsiteSearch.md)
 - [WhatOperandLhs](docs/WhatOperandLhs.md)
 - [WhatOperator](docs/WhatOperator.md)
 - [WhenOperator](docs/WhenOperator.md)
 - [WithLimits](docs/WithLimits.md)
 - [Word](docs/Word.md)
 - [WordRepetitionData](docs/WordRepetitionData.md)
 - [WordRequest](docs/WordRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKey"></a>
### ApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@wordlift.io


