# ResourceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**info** | **str** |  | [optional] 
**created** | **int** |  | [optional] 
**is_processing** | **bool** |  | 
**hw_uuid** | **str** |  | 
**owner_id** | **int** |  | 
**state** | **str** |  | 
**previous_state** | **str** |  | 
**location_uuid** | **str** |  | 
**user_desc** | **str** |  | [optional] 
**pay_day** | **int** |  | [optional] 
**primary_uuid** | **str** |  | [optional] 
**is_primary** | **bool** |  | 
**is_single_prolonged** | **bool** |  | 
**service_uuid** | **str** |  | 
**quantity** | **int** |  | 
**service_type** | **str** |  | 
**config_name** | **str** |  | 
**billing** | [**BillingModel**](BillingModel.md) |  | 
**paid_till** | **int** | Start order date from resource | 
**actual_grace_date** | **int** | Actual grace date from resource | [optional] 
**actual_dead_date** | **int** | Actual dead date from resource | [optional] 
**tags** | [**list[ResourceTagModel]**](ResourceTagModel.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


