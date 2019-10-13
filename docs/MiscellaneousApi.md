# sel_dedicated_client.MiscellaneousApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_name_update_view**](MiscellaneousApi.md#delete_user_name_update_view) | **DELETE** /misc/user-name-service/name/{uuid} | Delete user name
[**get_name_tags_view**](MiscellaneousApi.md#get_name_tags_view) | **GET** /misc/name-service/name/{uuid}/tag | Get list of name&#39;s tags
[**get_name_update_view**](MiscellaneousApi.md#get_name_update_view) | **GET** /misc/name-service/name/{uuid} | Get name data
[**get_name_view**](MiscellaneousApi.md#get_name_view) | **GET** /misc/name-service/name | Get name list
[**get_random_name_view**](MiscellaneousApi.md#get_random_name_view) | **GET** /misc/name-service/random | Get random name
[**get_tag_names_view**](MiscellaneousApi.md#get_tag_names_view) | **GET** /misc/name-service/tag/{uuid}/name | Get list of tag&#39;s names
[**get_tag_update_view**](MiscellaneousApi.md#get_tag_update_view) | **GET** /misc/name-service/tag/{uuid} | Get tag data
[**get_tag_view**](MiscellaneousApi.md#get_tag_view) | **GET** /misc/name-service/tag | Get tag list
[**get_user_name_update_view**](MiscellaneousApi.md#get_user_name_update_view) | **GET** /misc/user-name-service/name/{uuid} | Get user name data
[**get_user_name_view**](MiscellaneousApi.md#get_user_name_view) | **GET** /misc/user-name-service/name | Get user name list
[**post_user_name_view**](MiscellaneousApi.md#post_user_name_view) | **POST** /misc/user-name-service/name | Create new user name
[**put_user_name_update_view**](MiscellaneousApi.md#put_user_name_update_view) | **PUT** /misc/user-name-service/name/{uuid} | Update user name data


# **delete_user_name_update_view**
> ResponseBaseModel delete_user_name_update_view(uuid)

Delete user name

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 

try:
    # Delete user name
    api_response = api_instance.delete_user_name_update_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->delete_user_name_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseBaseModel**](ResponseBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete user name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_tags_view**
> ResponseNameTagsListResult get_name_tags_view(uuid)

Get list of name's tags

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 

try:
    # Get list of name's tags
    api_response = api_instance.get_name_tags_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_name_tags_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseNameTagsListResult**](ResponseNameTagsListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of name&#39;s tags |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_update_view**
> ResponseNameResult get_name_update_view(uuid)

Get name data

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 

try:
    # Get name data
    api_response = api_instance.get_name_update_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_name_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseNameResult**](ResponseNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns name data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_view**
> ResponseNameListModel get_name_view(tags=tags, limit=limit, page=page, sort=sort, order=order)

Get name list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
tags = ['tags_example'] # list[str] | tags (optional)
limit = 10 # int |  (optional) (default to 10)
page = 1 # int |  (optional) (default to 1)
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')

try:
    # Get name list
    api_response = api_instance.get_name_view(tags=tags, limit=limit, page=page, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_name_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **page** | **int**|  | [optional] [default to 1]
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]

### Return type

[**ResponseNameListModel**](ResponseNameListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_name_view**
> ResponseNameResult get_random_name_view(get_user_name=get_user_name, tags=tags)

Get random name

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
get_user_name = False # bool | flag: need to return one of user's name (optional) (default to False)
tags = ['tags_example'] # list[str] | tags (optional)

try:
    # Get random name
    api_response = api_instance.get_random_name_view(get_user_name=get_user_name, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_random_name_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_user_name** | **bool**| flag: need to return one of user&#39;s name | [optional] [default to False]
 **tags** | [**list[str]**](str.md)| tags | [optional] 

### Return type

[**ResponseNameResult**](ResponseNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns random name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_names_view**
> ResponseTagNamesListResult get_tag_names_view(uuid)

Get list of tag's names

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 

try:
    # Get list of tag's names
    api_response = api_instance.get_tag_names_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_tag_names_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseTagNamesListResult**](ResponseTagNamesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of tag&#39;s names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_update_view**
> ResponseTagResult get_tag_update_view(uuid)

Get tag data

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 

try:
    # Get tag data
    api_response = api_instance.get_tag_update_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_tag_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseTagResult**](ResponseTagResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns tag data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_view**
> ResponseTagListResult get_tag_view(limit=limit, page=page, sort=sort, order=order)

Get tag list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
limit = 10 # int |  (optional) (default to 10)
page = 1 # int |  (optional) (default to 1)
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')

try:
    # Get tag list
    api_response = api_instance.get_tag_view(limit=limit, page=page, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_tag_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **page** | **int**|  | [optional] [default to 1]
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]

### Return type

[**ResponseTagListResult**](ResponseTagListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of tags |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_name_update_view**
> ResponseUserNameResult get_user_name_update_view(uuid)

Get user name data

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 

try:
    # Get user name data
    api_response = api_instance.get_user_name_update_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_user_name_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseUserNameResult**](ResponseUserNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user name data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_name_view**
> ResponseUserNameListResult get_user_name_view(limit=limit, page=page, sort=sort, order=order)

Get user name list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
limit = 10 # int |  (optional) (default to 10)
page = 1 # int |  (optional) (default to 1)
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')

try:
    # Get user name list
    api_response = api_instance.get_user_name_view(limit=limit, page=page, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_user_name_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **page** | **int**|  | [optional] [default to 1]
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]

### Return type

[**ResponseUserNameListResult**](ResponseUserNameListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of user names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_name_view**
> ResponseUserNameResult post_user_name_view(payload)

Create new user name

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
payload = sel_dedicated_client.UserNameAdd() # UserNameAdd | 

try:
    # Create new user name
    api_response = api_instance.post_user_name_view(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->post_user_name_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserNameAdd**](UserNameAdd.md)|  | 

### Return type

[**ResponseUserNameResult**](ResponseUserNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates new user name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_name_update_view**
> ResponseUserNameResult put_user_name_update_view(uuid, payload)

Update user name data

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.MiscellaneousApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_client.UserNameUpdate() # UserNameUpdate | 

try:
    # Update user name data
    api_response = api_instance.put_user_name_update_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->put_user_name_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**UserNameUpdate**](UserNameUpdate.md)|  | 

### Return type

[**ResponseUserNameResult**](ResponseUserNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns updated user name data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

