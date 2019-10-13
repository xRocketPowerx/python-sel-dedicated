# sel_dedicated_codegen.TasksApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_view**](TasksApi.md#get_task_view) | **GET** /result/{uuid} | Show task details


# **get_task_view**
> ResponseBaseAsyncModel get_task_view(uuid)

Show task details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.TasksApi()
uuid = 'uuid_example' # str | 

try:
    # Show task details
    api_response = api_instance.get_task_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseBaseAsyncModel**](ResponseBaseAsyncModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return task result |  -  |
**303** | Return task result |  -  |
**404** | Return not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

