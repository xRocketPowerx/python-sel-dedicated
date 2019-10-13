# sel_dedicated_codegen.NetworkManagementApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ip_detail_view**](NetworkManagementApi.md#delete_ip_detail_view) | **DELETE** /network/ipam/ip/{uuid} | Release Ip
[**delete_network_subnet_view**](NetworkManagementApi.md#delete_network_subnet_view) | **DELETE** /network/{uuid}/subnet | Release subnet from network
[**delete_port_manager_view**](NetworkManagementApi.md#delete_port_manager_view) | **DELETE** /network/port/{uuid}/network | Delete Network for Port
[**get_ip_list_view**](NetworkManagementApi.md#get_ip_list_view) | **GET** /network/ipam/ip | Get Ip list
[**get_ip_view**](NetworkManagementApi.md#get_ip_view) | **GET** /network/ipam/subnet/{subnet_uuid}/ip | Get Ip list
[**get_network_detail_view**](NetworkManagementApi.md#get_network_detail_view) | **GET** /network/{uuid} | Get Network
[**get_network_limit_view**](NetworkManagementApi.md#get_network_limit_view) | **GET** /network/limit/{uuid} | Get Network Limit
[**get_network_view**](NetworkManagementApi.md#get_network_view) | **GET** /network | Get Network list
[**get_port_detail_view**](NetworkManagementApi.md#get_port_detail_view) | **GET** /network/port/{uuid} | Get Port
[**get_port_hw_view**](NetworkManagementApi.md#get_port_hw_view) | **GET** /network/port/hw/{hw_uuid} | Get Port from Hw
[**get_port_manager_view**](NetworkManagementApi.md#get_port_manager_view) | **GET** /network/port/{uuid}/network | Get Network for Port
[**get_port_view**](NetworkManagementApi.md#get_port_view) | **GET** /network/port | Get Port
[**get_subnet_detail_view**](NetworkManagementApi.md#get_subnet_detail_view) | **GET** /network/ipam/subnet/{uuid} | Get Subnet
[**get_subnet_view**](NetworkManagementApi.md#get_subnet_view) | **GET** /network/ipam/subnet | Get Subnet list
[**post_ip_view**](NetworkManagementApi.md#post_ip_view) | **POST** /network/ipam/subnet/{subnet_uuid}/ip | Create Ip
[**post_network_subnet_view**](NetworkManagementApi.md#post_network_subnet_view) | **POST** /network/{uuid}/subnet | Add subnet to network
[**post_port_detail_view**](NetworkManagementApi.md#post_port_detail_view) | **POST** /network/port/{uuid} | Apply Port config
[**post_port_manager_view**](NetworkManagementApi.md#post_port_manager_view) | **POST** /network/port/{uuid}/network | Set Network for Port
[**put_network_detail_view**](NetworkManagementApi.md#put_network_detail_view) | **PUT** /network/{uuid} | Update network
[**put_network_limit_view**](NetworkManagementApi.md#put_network_limit_view) | **PUT** /network/limit/{uuid} | Update Network Limit


# **delete_ip_detail_view**
> delete_ip_detail_view(uuid, payload)

Release Ip

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.IpReleaseModel() # IpReleaseModel | 

try:
    # Release Ip
    api_instance.delete_ip_detail_view(uuid, payload)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->delete_ip_detail_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**IpReleaseModel**](IpReleaseModel.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_subnet_view**
> NetworkResultModel delete_network_subnet_view(uuid, payload)

Release subnet from network

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.NetworkReleaseSubnetModel() # NetworkReleaseSubnetModel | 

try:
    # Release subnet from network
    api_response = api_instance.delete_network_subnet_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->delete_network_subnet_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**NetworkReleaseSubnetModel**](NetworkReleaseSubnetModel.md)|  | 

### Return type

[**NetworkResultModel**](NetworkResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Network |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port_manager_view**
> PortListResultModel delete_port_manager_view(uuid, payload)

Delete Network for Port

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.PortNetworkModel() # PortNetworkModel | 

try:
    # Delete Network for Port
    api_response = api_instance.delete_port_manager_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->delete_port_manager_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**PortNetworkModel**](PortNetworkModel.md)|  | 

### Return type

[**PortListResultModel**](PortListResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete Network for Port |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_list_view**
> IpResultListModel get_ip_list_view(is_shared=is_shared, owner_id=owner_id, network_uuid=network_uuid, subnet_uuid=subnet_uuid, location_uuid=location_uuid, limit=limit, page=page)

Get Ip list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
is_shared = True # bool | Shared network (optional)
owner_id = 56 # int | Owner ip (optional)
network_uuid = 'network_uuid_example' # str | IP network (optional)
subnet_uuid = 'subnet_uuid_example' # str | IP subnet (optional)
location_uuid = 'location_uuid_example' # str | IP location (optional)
limit = 56 # int | Items limit (optional)
page = 56 # int | Page number (optional)

try:
    # Get Ip list
    api_response = api_instance.get_ip_list_view(is_shared=is_shared, owner_id=owner_id, network_uuid=network_uuid, subnet_uuid=subnet_uuid, location_uuid=location_uuid, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_ip_list_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_shared** | **bool**| Shared network | [optional] 
 **owner_id** | **int**| Owner ip | [optional] 
 **network_uuid** | **str**| IP network | [optional] 
 **subnet_uuid** | **str**| IP subnet | [optional] 
 **location_uuid** | **str**| IP location | [optional] 
 **limit** | **int**| Items limit | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**IpResultListModel**](IpResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list ip |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_view**
> IpResultListModel get_ip_view(subnet_uuid)

Get Ip list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
subnet_uuid = 'subnet_uuid_example' # str | 

try:
    # Get Ip list
    api_response = api_instance.get_ip_view(subnet_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_ip_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_uuid** | **str**|  | 

### Return type

[**IpResultListModel**](IpResultListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list ip |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_detail_view**
> NetworkResultModel get_network_detail_view(uuid)

Get Network

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 

try:
    # Get Network
    api_response = api_instance.get_network_detail_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_network_detail_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**NetworkResultModel**](NetworkResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_limit_view**
> NetworkLimitResultModel get_network_limit_view(uuid)

Get Network Limit

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 

try:
    # Get Network Limit
    api_response = api_instance.get_network_limit_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_network_limit_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**NetworkLimitResultModel**](NetworkLimitResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns network limit by resource_uuid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_view**
> NetworkListResultModel get_network_view(is_shared=is_shared, location_uuid=location_uuid, resource_uuid=resource_uuid, limit=limit, page=page)

Get Network list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
is_shared = True # bool | Shared network (optional)
location_uuid = 'location_uuid_example' # str | Network location (optional)
resource_uuid = 'resource_uuid_example' # str | Network have ip for resource (optional)
limit = 56 # int | Items limit (optional)
page = 56 # int | Page number (optional)

try:
    # Get Network list
    api_response = api_instance.get_network_view(is_shared=is_shared, location_uuid=location_uuid, resource_uuid=resource_uuid, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_network_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_shared** | **bool**| Shared network | [optional] 
 **location_uuid** | **str**| Network location | [optional] 
 **resource_uuid** | **str**| Network have ip for resource | [optional] 
 **limit** | **int**| Items limit | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**NetworkListResultModel**](NetworkListResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_detail_view**
> PortResultModel get_port_detail_view(uuid)

Get Port

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 

try:
    # Get Port
    api_response = api_instance.get_port_detail_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_port_detail_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**PortResultModel**](PortResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Port |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_hw_view**
> PortResultModel get_port_hw_view(hw_uuid)

Get Port from Hw

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
hw_uuid = 'hw_uuid_example' # str | 

try:
    # Get Port from Hw
    api_response = api_instance.get_port_hw_view(hw_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_port_hw_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hw_uuid** | **str**|  | 

### Return type

[**PortResultModel**](PortResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Port for Hw |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_manager_view**
> NetworkListResultModel get_port_manager_view(uuid)

Get Network for Port

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 

try:
    # Get Network for Port
    api_response = api_instance.get_port_manager_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_port_manager_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**NetworkListResultModel**](NetworkListResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Network for Port |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_view**
> PortResultModel get_port_view()

Get Port

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()

try:
    # Get Port
    api_response = api_instance.get_port_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_port_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortResultModel**](PortResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Port |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnet_detail_view**
> SubnetResultModel get_subnet_detail_view(uuid)

Get Subnet

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 

try:
    # Get Subnet
    api_response = api_instance.get_subnet_detail_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_subnet_detail_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**SubnetResultModel**](SubnetResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Subnet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnet_view**
> SubnetListResultModel get_subnet_view()

Get Subnet list

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()

try:
    # Get Subnet list
    api_response = api_instance.get_subnet_view()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->get_subnet_view: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SubnetListResultModel**](SubnetListResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of master subnet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ip_view**
> IpResultModel post_ip_view(subnet_uuid, payload)

Create Ip

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
subnet_uuid = 'subnet_uuid_example' # str | 
payload = sel_dedicated_codegen.IpAllocateModel() # IpAllocateModel | 

try:
    # Create Ip
    api_response = api_instance.post_ip_view(subnet_uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->post_ip_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_uuid** | **str**|  | 
 **payload** | [**IpAllocateModel**](IpAllocateModel.md)|  | 

### Return type

[**IpResultModel**](IpResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns created Ip |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_network_subnet_view**
> NetworkResultModel post_network_subnet_view(uuid, payload)

Add subnet to network

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.NetworkAddSubnetModel() # NetworkAddSubnetModel | 

try:
    # Add subnet to network
    api_response = api_instance.post_network_subnet_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->post_network_subnet_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**NetworkAddSubnetModel**](NetworkAddSubnetModel.md)|  | 

### Return type

[**NetworkResultModel**](NetworkResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns Network |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_port_detail_view**
> PortResultModel post_port_detail_view(uuid)

Apply Port config

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 

try:
    # Apply Port config
    api_response = api_instance.post_port_detail_view(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->post_port_detail_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**PortResultModel**](PortResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apply data for Port |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_port_manager_view**
> PortListResultModel post_port_manager_view(uuid, payload)

Set Network for Port

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.PortNetworkModel() # PortNetworkModel | 

try:
    # Set Network for Port
    api_response = api_instance.post_port_manager_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->post_port_manager_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**PortNetworkModel**](PortNetworkModel.md)|  | 

### Return type

[**PortListResultModel**](PortListResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Set Network for Port |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_network_detail_view**
> NetworkResultModel put_network_detail_view(uuid, payload)

Update network

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.NetworkUpdateModel() # NetworkUpdateModel | 

try:
    # Update network
    api_response = api_instance.put_network_detail_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->put_network_detail_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**NetworkUpdateModel**](NetworkUpdateModel.md)|  | 

### Return type

[**NetworkResultModel**](NetworkResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Network |  -  |
**202** | Return task result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_network_limit_view**
> NetworkLimitResultModel put_network_limit_view(uuid, payload)

Update Network Limit

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.NetworkManagementApi()
uuid = 'uuid_example' # str | 
payload = sel_dedicated_codegen.NetworkLimitUpdateModel() # NetworkLimitUpdateModel | 

try:
    # Update Network Limit
    api_response = api_instance.put_network_limit_view(uuid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkManagementApi->put_network_limit_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **payload** | [**NetworkLimitUpdateModel**](NetworkLimitUpdateModel.md)|  | 

### Return type

[**NetworkLimitResultModel**](NetworkLimitResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns updated network limit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

