# ServerViewModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**name** | **str** |  | [optional] [default to '']
**tariff_line** | **str** |  | 
**model** | **str** |  | 
**tags** | **list[str]** |  | 
**state** | **str** | service state | 
**available** | [**list[ServiceAvailable]**](ServiceAvailable.md) |  | 
**is_order** | **bool** |  | 
**is_preorder** | **bool** |  | 
**setup_fee_collection** | [**PriceModel**](PriceModel.md) |  | 
**price_collection** | [**PriceModel**](PriceModel.md) |  | 
**service_tag** | **str** |  | 
**is_primary** | **bool** |  | 
**is_single_prolonged** | **bool** |  | 
**quantity** | **int** |  | [optional] 
**is_qchange** | **bool** |  | [optional] 
**price_plan_available** | **list[str]** |  | 
**addition** | [**list[ServiceBase]**](ServiceBase.md) |  | [optional] 
**primary** | [**list[ServiceBase]**](ServiceBase.md) |  | [optional] 
**config_name** | **str** |  | 
**cpu** | [**ServerCPU**](ServerCPU.md) |  | 
**ram** | [**list[ServerRAM]**](ServerRAM.md) |  | 
**disk** | [**list[ServerDisk]**](ServerDisk.md) |  | 
**gpu** | [**ServerGPU**](ServerGPU.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


