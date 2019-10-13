# sel_dedicated_codegen.ServicesApi

All URIs are relative to *https://api.selectel.ru/servers/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network**](ServicesApi.md#get_network) | **GET** /service/network/{uuid} | Show network details
[**get_network_list**](ServicesApi.md#get_network_list) | **GET** /service/network | List network
[**get_server**](ServicesApi.md#get_server) | **GET** /service/server/{uuid} | Show server details
[**get_server_chip**](ServicesApi.md#get_server_chip) | **GET** /service/serverchip/{uuid} | Show chipcore server details
[**get_server_chip_list**](ServicesApi.md#get_server_chip_list) | **GET** /service/serverchip | List chipcore servers
[**get_server_list**](ServicesApi.md#get_server_list) | **GET** /service/server | List servers
[**get_service**](ServicesApi.md#get_service) | **GET** /service/{uuid} | Show service details
[**get_service_list**](ServicesApi.md#get_service_list) | **GET** /service | List services


# **get_network**
> ResponseNetworkResult get_network(uuid)

Show network details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
uuid = 'uuid_example' # str | 

try:
    # Show network details
    api_response = api_instance.get_network(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseNetworkResult**](ResponseNetworkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Network Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_list**
> ResponseNetworkListResult get_network_list(state=state, sort=sort, order=order)

List network

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
state = 'state_example' # str | billing state (optional)
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')

try:
    # List network
    api_response = api_instance.get_network_list(state=state, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_network_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| billing state | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]

### Return type

[**ResponseNetworkListResult**](ResponseNetworkListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of Network Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> ResponseServerResult get_server(uuid)

Show server details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
uuid = 'uuid_example' # str | 

try:
    # Show server details
    api_response = api_instance.get_server(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseServerResult**](ResponseServerResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Dedicated Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_chip**
> ResponseServerResult get_server_chip(uuid)

Show chipcore server details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
uuid = 'uuid_example' # str | 

try:
    # Show chipcore server details
    api_response = api_instance.get_server_chip(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_server_chip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseServerResult**](ResponseServerResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns LDedicated Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_chip_list**
> ResponseServerListResult get_server_chip_list(sort=sort, order=order)

List chipcore servers

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')

try:
    # List chipcore servers
    api_response = api_instance.get_server_chip_list(sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_server_chip_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]

### Return type

[**ResponseServerListResult**](ResponseServerListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of Dedicated Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_list**
> ResponseServerListResult get_server_list(state=state, sort=sort, order=order)

List servers

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
state = 'state_example' # str | billing state (optional)
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')

try:
    # List servers
    api_response = api_instance.get_server_list(state=state, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_server_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| billing state | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]

### Return type

[**ResponseServerListResult**](ResponseServerListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of Dedicated Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ResponseServiceResult get_service(uuid)

Show service details

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
uuid = 'uuid_example' # str | 

try:
    # Show service details
    api_response = api_instance.get_service(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ResponseServiceResult**](ResponseServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_list**
> ResponseServiceListResult get_service_list(sort=sort, order=order, is_primary=is_primary, state=state, model=model)

List services

### Example

```python
from __future__ import print_function
import time
import sel_dedicated_codegen
from sel_dedicated_codegen.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sel_dedicated_codegen.ServicesApi()
sort = 'created' # str |  (optional) (default to 'created')
order = 'asc' # str | Order direction: [\"desc\", \"asc\"] (optional) (default to 'asc')
is_primary = True # bool |  (optional)
state = 'state_example' # str | billing state (optional)
model = 'model_example' # str | service model (optional)

try:
    # List services
    api_response = api_instance.get_service_list(sort=sort, order=order, is_primary=is_primary, state=state, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]
 **order** | **str**| Order direction: [\&quot;desc\&quot;, \&quot;asc\&quot;] | [optional] [default to &#39;asc&#39;]
 **is_primary** | **bool**|  | [optional] 
 **state** | **str**| billing state | [optional] 
 **model** | **str**| service model | [optional] 

### Return type

[**ResponseServiceListResult**](ResponseServiceListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

