# sel_dedicated_client.ConsumptionApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_graph_resource_view**](ConsumptionApi.md#get_graph_resource_view) | **GET** /consumption/speed/resource/{resource_uuid} | Get Resource speed points
[**get_traffic_resource_view**](ConsumptionApi.md#get_traffic_resource_view) | **GET** /consumption/traffic/resource/{resource_uuid} | Get traffic consumption


# **get_graph_resource_view**
> ResponseSpeedGraph get_graph_resource_view(resource_uuid, local=local, interval=interval, till=till, _from=_from)

Get Resource speed points

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ConsumptionApi()
resource_uuid = 'resource_uuid_example' # str | 
local = 'false' # str | Switch which port type needs to be shown (optional) (default to 'false')
interval = 'min5' # str | Interval to group points by (optional) (default to 'min5')
till = 1570963348 # int | Time from which speed points will ends, Unix timestamp (optional) (default to 1570963348)
_from = 1570959748 # int | Time from which speed points will starts, Unix timestamp (optional) (default to 1570959748)

try:
    # Get Resource speed points
    api_response = api_instance.get_graph_resource_view(resource_uuid, local=local, interval=interval, till=till, _from=_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumptionApi->get_graph_resource_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **local** | **str**| Switch which port type needs to be shown | [optional] [default to &#39;false&#39;]
 **interval** | **str**| Interval to group points by | [optional] [default to &#39;min5&#39;]
 **till** | **int**| Time from which speed points will ends, Unix timestamp | [optional] [default to 1570963348]
 **_from** | **int**| Time from which speed points will starts, Unix timestamp | [optional] [default to 1570959748]

### Return type

[**ResponseSpeedGraph**](ResponseSpeedGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of speed points |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traffic_resource_view**
> ResponseTrafficConsumption get_traffic_resource_view(resource_uuid, month=month)

Get traffic consumption

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.ConsumptionApi()
resource_uuid = 'resource_uuid_example' # str | 
month = 10 # int | month to which traffic will calculated, integer (optional) (default to 10)

try:
    # Get traffic consumption
    api_response = api_instance.get_traffic_resource_view(resource_uuid, month=month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumptionApi->get_traffic_resource_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **month** | **int**| month to which traffic will calculated, integer | [optional] [default to 10]

### Return type

[**ResponseTrafficConsumption**](ResponseTrafficConsumption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns traffic consumption data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

