# sel_dedicated_codegen.LocationsApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_get_view**](LocationsApi.md#get_location_get_view) | **GET** /location/{uuid} | Show location info
[**get_location_view**](LocationsApi.md#get_location_view) | **GET** /location | List locations


# **get_location_get_view**
> LocationResultModel get_location_get_view(uuid)

Show location info

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.LocationsApi()
uuid = 'uuid_example' # str | 

try:
    # Show location info
    api_response = api_instance.get_location_get_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location_get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**LocationResultModel**](LocationResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Location |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_view**
> LocationResultListModel get_location_view()

List locations

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.LocationsApi()

try:
    # List locations
    api_response = api_instance.get_location_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LocationResultListModel**](LocationResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of Location |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

