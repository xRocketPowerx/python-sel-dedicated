# sel_dedicated_client.PricePlansApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_price_plan_get_view**](PricePlansApi.md#get_price_plan_get_view) | **GET** /plan/{uuid} | Show price plan details
[**get_price_plan_view**](PricePlansApi.md#get_price_plan_view) | **GET** /plan | List price plans


# **get_price_plan_get_view**
> PricePlanResultModel get_price_plan_get_view(uuid)

Show price plan details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.PricePlansApi()
uuid = 'uuid_example' # str | 

try:
    # Show price plan details
    api_response = api_instance.get_price_plan_get_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricePlansApi->get_price_plan_get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**PricePlanResultModel**](PricePlanResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Price plan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_plan_view**
> PricePlanResultListModel get_price_plan_view()

List price plans

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_client
from sel_dedicated_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_client.PricePlansApi()

try:
    # List price plans
    api_response = api_instance.get_price_plan_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricePlansApi->get_price_plan_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PricePlanResultListModel**](PricePlanResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list Price plan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

