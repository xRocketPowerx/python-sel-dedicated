# sel_dedicated_codegen.BootManagerApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_template_list_view**](BootManagerApi.md#get_device_template_list_view) | **GET** /boot/template/device | List boot templates
[**get_device_view**](BootManagerApi.md#get_device_view) | **GET** /boot/device/{resource_uuid} | Show server boot details
[**get_os_template_list_view**](BootManagerApi.md#get_os_template_list_view) | **GET** /boot/template/os | List OS configurations
[**get_os_view**](BootManagerApi.md#get_os_view) | **GET** /boot/os/{resource_uuid} | Show server OS details
[**patch_os_view**](BootManagerApi.md#patch_os_view) | **PATCH** /boot/os/{resource_uuid} | Update OS install configuration
[**post_device_view**](BootManagerApi.md#post_device_view) | **POST** /boot/device/{resource_uuid} | Set server boot template
[**post_os_view**](BootManagerApi.md#post_os_view) | **POST** /boot/os/{resource_uuid} | Install server new OS configuration


# **get_device_template_list_view**
> ResponseDeviceInfoList get_device_template_list_view()

List boot templates

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()

try:
    # List boot templates
    api_response = api_instance.get_device_template_list_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->get_device_template_list_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDeviceInfoList**](ResponseDeviceInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return list of available boot devices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_view**
> ResponseDevice get_device_view(resource_uuid)

Show server boot details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()
resource_uuid = 'resource_uuid_example' # str | 

try:
    # Show server boot details
    api_response = api_instance.get_device_view(resource_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->get_device_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 

### Return type

[**ResponseDevice**](ResponseDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return current boot device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_template_list_view**
> ResponseOSTemplateList get_os_template_list_view()

List OS configurations

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()

try:
    # List OS configurations
    api_response = api_instance.get_os_template_list_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->get_os_template_list_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseOSTemplateList**](ResponseOSTemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return list of OS templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_view**
> ResponseOSConfig get_os_view(resource_uuid)

Show server OS details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()
resource_uuid = 'resource_uuid_example' # str | 

try:
    # Show server OS details
    api_response = api_instance.get_os_view(resource_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->get_os_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 

### Return type

[**ResponseOSConfig**](ResponseOSConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return current OS config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_os_view**
> ResponseOSConfig patch_os_view(resource_uuid, payload)

Update OS install configuration

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()
resource_uuid = 'resource_uuid_example' # str | 
payload = sel_dedicated_codegen.ReinstallInput() # ReinstallInput | 

try:
    # Update OS install configuration
    api_response = api_instance.patch_os_view(resource_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->patch_os_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **payload** | [**ReinstallInput**](ReinstallInput.md)|  | 

### Return type

[**ResponseOSConfig**](ResponseOSConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device_view**
> ResponseDevice post_device_view(resource_uuid, payload)

Set server boot template

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()
resource_uuid = 'resource_uuid_example' # str | 
payload = sel_dedicated_codegen.Device() # Device | 

try:
    # Set server boot template
    api_response = api_instance.post_device_view(resource_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->post_device_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **payload** | [**Device**](Device.md)|  | 

### Return type

[**ResponseDevice**](ResponseDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set boot device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_os_view**
> ResponseOSConfig post_os_view(resource_uuid, payload)

Install server new OS configuration

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.BootManagerApi()
resource_uuid = 'resource_uuid_example' # str | 
payload = sel_dedicated_codegen.OSConfigInput() # OSConfigInput | 

try:
    # Install server new OS configuration
    api_response = api_instance.post_os_view(resource_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootManagerApi->post_os_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **payload** | [**OSConfigInput**](OSConfigInput.md)|  | 

### Return type

[**ResponseOSConfig**](ResponseOSConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set OS config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

