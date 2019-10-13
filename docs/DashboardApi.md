# sel_dedicated_codegen.DashboardApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_task_view**](DashboardApi.md#get_active_task_view) | **GET** /dashboard/task | Get current active tasks
[**get_maintenance_view**](DashboardApi.md#get_maintenance_view) | **GET** /dashboard/maintenance | Get current maintenance status


# **get_active_task_view**
> ResultActiveTasks get_active_task_view()

Get current active tasks

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.DashboardApi()

try:
    # Get current active tasks
    api_response = api_instance.get_active_task_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_active_task_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultActiveTasks**](ResultActiveTasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current active tasks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_view**
> MaintenanceStatusResponse get_maintenance_view()

Get current maintenance status

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.DashboardApi()

try:
    # Get current maintenance status
    api_response = api_instance.get_maintenance_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_maintenance_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MaintenanceStatusResponse**](MaintenanceStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current maintenance status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

