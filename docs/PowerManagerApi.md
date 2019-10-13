# sel_dedicated_codegen.PowerManagerApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_console_view**](PowerManagerApi.md#get_resource_console_view) | **GET** /power/{resource_uuid}/console | Show server console
[**get_resource_power_view**](PowerManagerApi.md#get_resource_power_view) | **GET** /power/{resource_uuid} | Show server power state
[**post_resource_console_view**](PowerManagerApi.md#post_resource_console_view) | **POST** /power/{resource_uuid}/console | Set server console resolution
[**post_resource_reboot_view**](PowerManagerApi.md#post_resource_reboot_view) | **POST** /power/{resource_uuid}/reboot | Reboot server
[**put_resource_power_view**](PowerManagerApi.md#put_resource_power_view) | **PUT** /power/{resource_uuid} | Set server power state


# **get_resource_console_view**
> ResponseConsole get_resource_console_view(resource_uuid)

Show server console

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.PowerManagerApi()
resource_uuid = 'resource_uuid_example' # str | 

try:
    # Show server console
    api_response = api_instance.get_resource_console_view(resource_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerManagerApi->get_resource_console_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 

### Return type

[**ResponseConsole**](ResponseConsole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Resource console |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_power_view**
> ResponsePowerStatus get_resource_power_view(resource_uuid)

Show server power state

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.PowerManagerApi()
resource_uuid = 'resource_uuid_example' # str | 

try:
    # Show server power state
    api_response = api_instance.get_resource_power_view(resource_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerManagerApi->get_resource_power_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 

### Return type

[**ResponsePowerStatus**](ResponsePowerStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Resource power state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_console_view**
> ResponseBaseModel post_resource_console_view(resource_uuid, payload)

Set server console resolution

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.PowerManagerApi()
resource_uuid = 'resource_uuid_example' # str | 
payload = sel_dedicated_codegen.ConsoleResolution() # ConsoleResolution | 

try:
    # Set server console resolution
    api_response = api_instance.post_resource_console_view(resource_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerManagerApi->post_resource_console_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **payload** | [**ConsoleResolution**](ConsoleResolution.md)|  | 

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
**200** | Set Resource console resolution |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_reboot_view**
> ResponseBaseModel post_resource_reboot_view(resource_uuid, payload)

Reboot server

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.PowerManagerApi()
resource_uuid = 'resource_uuid_example' # str | 
payload = sel_dedicated_codegen.PowerReboot() # PowerReboot | 

try:
    # Reboot server
    api_response = api_instance.post_resource_reboot_view(resource_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerManagerApi->post_resource_reboot_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **payload** | [**PowerReboot**](PowerReboot.md)|  | 

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
**200** | Reboot Resource HW |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_resource_power_view**
> ResponseBaseModel put_resource_power_view(resource_uuid, payload)

Set server power state

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.PowerManagerApi()
resource_uuid = 'resource_uuid_example' # str | 
payload = sel_dedicated_codegen.PowerSwitchStatus() # PowerSwitchStatus | 

try:
    # Set server power state
    api_response = api_instance.put_resource_power_view(resource_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerManagerApi->put_resource_power_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **payload** | [**PowerSwitchStatus**](PowerSwitchStatus.md)|  | 

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
**200** | Switch Resource power state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

