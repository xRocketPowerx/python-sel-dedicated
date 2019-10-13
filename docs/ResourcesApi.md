# sel_dedicated_client.ResourcesApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_resource_billing_manage_view**](ResourcesApi.md#delete_resource_billing_manage_view) | **DELETE** /resource/billing/{uuid} | Cancel resource
[**delete_resource_tag_manage_view**](ResourcesApi.md#delete_resource_tag_manage_view) | **DELETE** /resource/{uuid}/tag | Remove user tag from resource
[**delete_resource_tag_view**](ResourcesApi.md#delete_resource_tag_view) | **DELETE** /resource/tag/{id} | Delete user tag
[**get_resource_compensation_view**](ResourcesApi.md#get_resource_compensation_view) | **GET** /resource/{uuid}/compensation | List compensation fact for Resource
[**get_resource_list_view**](ResourcesApi.md#get_resource_list_view) | **GET** /resource | List resources
[**get_resource_orders_view**](ResourcesApi.md#get_resource_orders_view) | **GET** /resource/order/{year} | 
[**get_resource_tag_list_view**](ResourcesApi.md#get_resource_tag_list_view) | **GET** /resource/tag | List all user tags
[**get_resource_view**](ResourcesApi.md#get_resource_view) | **GET** /resource/{uuid} | Show resource details
[**patch_resource_billing_manage_view**](ResourcesApi.md#patch_resource_billing_manage_view) | **PATCH** /resource/billing/{uuid} | Restore resource
[**patch_resource_view**](ResourcesApi.md#patch_resource_view) | **PATCH** /resource/{uuid} | Append resource
[**post_resource_billing_additional_manage_view**](ResourcesApi.md#post_resource_billing_additional_manage_view) | **POST** /resource/{uuid}/billing | Add and activate additional resource
[**post_resource_billing_manage_view**](ResourcesApi.md#post_resource_billing_manage_view) | **POST** /resource/billing/{uuid} | Activate resource
[**post_resource_billing_network_manage_view**](ResourcesApi.md#post_resource_billing_network_manage_view) | **POST** /resource/network/billing | Add and activate network resource
[**post_resource_billing_server_manage_view**](ResourcesApi.md#post_resource_billing_server_manage_view) | **POST** /resource/server/billing | Add and activate server resource
[**post_resource_billing_serverchip_manage_view**](ResourcesApi.md#post_resource_billing_serverchip_manage_view) | **POST** /resource/serverchip/billing | Add and activate serverchip resource
[**post_resource_list_view**](ResourcesApi.md#post_resource_list_view) | **POST** /resource | Create resource
[**post_resource_tag_list_view**](ResourcesApi.md#post_resource_tag_list_view) | **POST** /resource/tag | Create new user tag
[**post_resource_tag_manage_view**](ResourcesApi.md#post_resource_tag_manage_view) | **POST** /resource/{uuid}/tag | Add user tag to resource
[**put_resource_tag_view**](ResourcesApi.md#put_resource_tag_view) | **PUT** /resource/tag/{id} | Update user tag
[**put_resource_view**](ResourcesApi.md#put_resource_view) | **PUT** /resource/{uuid} | Update resource


# **delete_resource_billing_manage_view**
> ResponseBaseModel delete_resource_billing_manage_view(uuid, payload)

Cancel resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceCancelModel() # ResourceCancelModel | 

try:
    # Cancel resource
    api_response = api_instance.delete_resource_billing_manage_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->delete_resource_billing_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceCancelModel**](ResourceCancelModel.md)|  | 

### Return type

[**ResponseBaseModel**](ResponseBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_tag_manage_view**
> ResourceTagResultListModel delete_resource_tag_manage_view(uuid, payload)

Remove user tag from resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceTagManageModel() # ResourceTagManageModel | 

try:
    # Remove user tag from resource
    api_response = api_instance.delete_resource_tag_manage_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->delete_resource_tag_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceTagManageModel**](ResourceTagManageModel.md)|  | 

### Return type

[**ResourceTagResultListModel**](ResourceTagResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns current list of ResourceTag for the Resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_tag_view**
> ResourceTagResultModel delete_resource_tag_view(id)

Delete user tag

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
id = 56 # int | 

try:
    # Delete user tag
    api_response = api_instance.delete_resource_tag_view(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->delete_resource_tag_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceTagResultModel**](ResourceTagResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns deleted ResourceTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_compensation_view**
> ResourceOrderCompensationDetailModel get_resource_compensation_view(uuid)

List compensation fact for Resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 

try:
    # List compensation fact for Resource
    api_response = api_instance.get_resource_compensation_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_compensation_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResourceOrderCompensationDetailModel**](ResourceOrderCompensationDetailModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_list_view**
> ResourceResultListModel get_resource_list_view(resource_tag_id=resource_tag_id, limit=limit, page=page)

List resources

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
resource_tag_id = 56 # int | resource_tag_id (optional)
limit = 56 # int | Items limit (optional)
page = 56 # int | Page number (optional)

try:
    # List resources
    api_response = api_instance.get_resource_list_view(resource_tag_id=resource_tag_id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_list_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tag_id** | **int**| resource_tag_id | [optional] 
 **limit** | **int**| Items limit | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceResultListModel**](ResourceResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_orders_view**
> ResourceOrdersStatResultListModel get_resource_orders_view(year)



### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
year = 56 # int | 

try:
    api_response = api_instance.get_resource_orders_view(year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_orders_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 

### Return type

[**ResourceOrdersStatResultListModel**](ResourceOrdersStatResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource sort orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_tag_list_view**
> ResourceTagResultListModel get_resource_tag_list_view(limit=limit, page=page)

List all user tags

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
limit = 56 # int | Items limit (optional)
page = 56 # int | Page number (optional)

try:
    # List all user tags
    api_response = api_instance.get_resource_tag_list_view(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_tag_list_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Items limit | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceTagResultListModel**](ResourceTagResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of ResourceTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_view**
> ResourceResultModel get_resource_view(uuid)

Show resource details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 

try:
    # Show resource details
    api_response = api_instance.get_resource_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**303** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_resource_billing_manage_view**
> ResourceResultModel patch_resource_billing_manage_view(uuid, payload)

Restore resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceRestoreModel() # ResourceRestoreModel | 

try:
    # Restore resource
    api_response = api_instance.patch_resource_billing_manage_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->patch_resource_billing_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceRestoreModel**](ResourceRestoreModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_resource_view**
> ResourceResultModel patch_resource_view(uuid, payload)

Append resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceAppendModel() # ResourceAppendModel | 

try:
    # Append resource
    api_response = api_instance.patch_resource_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->patch_resource_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceAppendModel**](ResourceAppendModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_billing_additional_manage_view**
> ResourceResultModel post_resource_billing_additional_manage_view(uuid, payload)

Add and activate additional resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceStartAdditionalModel() # ResourceStartAdditionalModel | 

try:
    # Add and activate additional resource
    api_response = api_instance.post_resource_billing_additional_manage_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_billing_additional_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceStartAdditionalModel**](ResourceStartAdditionalModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_billing_manage_view**
> ResourceResultModel post_resource_billing_manage_view(uuid, payload)

Activate resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceStartModel() # ResourceStartModel | 

try:
    # Activate resource
    api_response = api_instance.post_resource_billing_manage_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_billing_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceStartModel**](ResourceStartModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_billing_network_manage_view**
> ResourceResultModel post_resource_billing_network_manage_view(payload)

Add and activate network resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
payload = sel_dedicated_client.ResourceStartNetworkModel() # ResourceStartNetworkModel | 

try:
    # Add and activate network resource
    api_response = api_instance.post_resource_billing_network_manage_view(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_billing_network_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ResourceStartNetworkModel**](ResourceStartNetworkModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_billing_server_manage_view**
> ResourceResultModel post_resource_billing_server_manage_view(payload)

Add and activate server resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
payload = sel_dedicated_client.ResourceStartServerModel() # ResourceStartServerModel | 

try:
    # Add and activate server resource
    api_response = api_instance.post_resource_billing_server_manage_view(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_billing_server_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ResourceStartServerModel**](ResourceStartServerModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_billing_serverchip_manage_view**
> ResourceResultModel post_resource_billing_serverchip_manage_view(payload)

Add and activate serverchip resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
payload = sel_dedicated_client.ResourceStartServerModel() # ResourceStartServerModel | 

try:
    # Add and activate serverchip resource
    api_response = api_instance.post_resource_billing_serverchip_manage_view(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_billing_serverchip_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ResourceStartServerModel**](ResourceStartServerModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_list_view**
> ResourceResultModel post_resource_list_view(payload)

Create resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
payload = sel_dedicated_client.ResourceAddModel() # ResourceAddModel | 

try:
    # Create resource
    api_response = api_instance.post_resource_list_view(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_list_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ResourceAddModel**](ResourceAddModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns new Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_tag_list_view**
> ResourceTagResultModel post_resource_tag_list_view(payload)

Create new user tag

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
payload = sel_dedicated_client.ResourceTagCreateUpdateModel() # ResourceTagCreateUpdateModel | 

try:
    # Create new user tag
    api_response = api_instance.post_resource_tag_list_view(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_tag_list_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ResourceTagCreateUpdateModel**](ResourceTagCreateUpdateModel.md)|  | 

### Return type

[**ResourceTagResultModel**](ResourceTagResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns new ResourceTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_tag_manage_view**
> ResourceTagResultListModel post_resource_tag_manage_view(uuid, payload)

Add user tag to resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceTagManageModel() # ResourceTagManageModel | 

try:
    # Add user tag to resource
    api_response = api_instance.post_resource_tag_manage_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->post_resource_tag_manage_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceTagManageModel**](ResourceTagManageModel.md)|  | 

### Return type

[**ResourceTagResultListModel**](ResourceTagResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns current list of ResourceTag for the Resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_resource_tag_view**
> ResourceTagResultModel put_resource_tag_view(id, payload)

Update user tag

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
id = 56 # int | 
payload = sel_dedicated_client.ResourceTagCreateUpdateModel() # ResourceTagCreateUpdateModel | 

try:
    # Update user tag
    api_response = api_instance.put_resource_tag_view(id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->put_resource_tag_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**ResourceTagCreateUpdateModel**](ResourceTagCreateUpdateModel.md)|  | 

### Return type

[**ResourceTagResultModel**](ResourceTagResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns updated ResourceTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_resource_view**
> ResourceResultModel put_resource_view(uuid, payload)

Update resource

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ResourcesApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.ResourceUpdateModel() # ResourceUpdateModel | 

try:
    # Update resource
    api_response = api_instance.put_resource_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->put_resource_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**ResourceUpdateModel**](ResourceUpdateModel.md)|  | 

### Return type

[**ResourceResultModel**](ResourceResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Resource |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

