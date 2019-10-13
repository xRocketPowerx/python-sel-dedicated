# sel_dedicated_codegen.EventsApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_manager**](EventsApi.md#get_event_manager) | **GET** /event | List events


# **get_event_manager**
> EventResultListModel get_event_manager(action_name=action_name, item_name=item_name, item_uuid=item_uuid, request_uuid=request_uuid, limit=limit, page=page)

List events

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.EventsApi()
action_name = 'action_name_example' # str | Action name (optional)
item_name = 'item_name_example' # str | Item name (optional)
item_uuid = 'item_uuid_example' # str | Items per page (optional)
request_uuid = 'request_uuid_example' # str | Staff id (optional)
limit = 56 # int | Items per page (optional)
page = 56 # int | Page number (optional)

try:
    # List events
    api_response = api_instance.get_event_manager(action_name=action_name, item_name=item_name, item_uuid=item_uuid, request_uuid=request_uuid, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_name** | **str**| Action name | [optional] 
 **item_name** | **str**| Item name | [optional] 
 **item_uuid** | **str**| Items per page | [optional] 
 **request_uuid** | **str**| Staff id | [optional] 
 **limit** | **int**| Items per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**EventResultListModel**](EventResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get event list |  -  |
**303** | Returns async result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

