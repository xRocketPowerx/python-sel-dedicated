# coding: utf-8

"""
    Seido User REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.4.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ServerViewModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'uuid': 'str',
        'name': 'str',
        'tariff_line': 'str',
        'model': 'str',
        'tags': 'list[str]',
        'state': 'str',
        'available': 'list[ServiceAvailable]',
        'is_order': 'bool',
        'is_preorder': 'bool',
        'setup_fee_collection': 'PriceModel',
        'price_collection': 'PriceModel',
        'service_tag': 'str',
        'is_primary': 'bool',
        'is_single_prolonged': 'bool',
        'quantity': 'int',
        'is_qchange': 'bool',
        'price_plan_available': 'list[str]',
        'addition': 'list[ServiceBase]',
        'primary': 'list[ServiceBase]',
        'config_name': 'str',
        'cpu': 'ServerCPU',
        'ram': 'list[ServerRAM]',
        'disk': 'list[ServerDisk]',
        'gpu': 'ServerGPU'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'tariff_line': 'tariff_line',
        'model': 'model',
        'tags': 'tags',
        'state': 'state',
        'available': 'available',
        'is_order': 'is_order',
        'is_preorder': 'is_preorder',
        'setup_fee_collection': 'setup_fee_collection',
        'price_collection': 'price_collection',
        'service_tag': 'service_tag',
        'is_primary': 'is_primary',
        'is_single_prolonged': 'is_single_prolonged',
        'quantity': 'quantity',
        'is_qchange': 'is_qchange',
        'price_plan_available': 'price_plan_available',
        'addition': 'addition',
        'primary': 'primary',
        'config_name': 'config_name',
        'cpu': 'cpu',
        'ram': 'ram',
        'disk': 'disk',
        'gpu': 'gpu'
    }

    def __init__(self, uuid=None, name='', tariff_line=None, model=None, tags=None, state=None, available=None, is_order=None, is_preorder=None, setup_fee_collection=None, price_collection=None, service_tag=None, is_primary=None, is_single_prolonged=None, quantity=None, is_qchange=None, price_plan_available=None, addition=None, primary=None, config_name=None, cpu=None, ram=None, disk=None, gpu=None):  # noqa: E501
        """ServerViewModel - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._name = None
        self._tariff_line = None
        self._model = None
        self._tags = None
        self._state = None
        self._available = None
        self._is_order = None
        self._is_preorder = None
        self._setup_fee_collection = None
        self._price_collection = None
        self._service_tag = None
        self._is_primary = None
        self._is_single_prolonged = None
        self._quantity = None
        self._is_qchange = None
        self._price_plan_available = None
        self._addition = None
        self._primary = None
        self._config_name = None
        self._cpu = None
        self._ram = None
        self._disk = None
        self._gpu = None
        self.discriminator = None

        self.uuid = uuid
        if name is not None:
            self.name = name
        self.tariff_line = tariff_line
        self.model = model
        self.tags = tags
        self.state = state
        self.available = available
        self.is_order = is_order
        self.is_preorder = is_preorder
        self.setup_fee_collection = setup_fee_collection
        self.price_collection = price_collection
        self.service_tag = service_tag
        self.is_primary = is_primary
        self.is_single_prolonged = is_single_prolonged
        if quantity is not None:
            self.quantity = quantity
        if is_qchange is not None:
            self.is_qchange = is_qchange
        self.price_plan_available = price_plan_available
        if addition is not None:
            self.addition = addition
        if primary is not None:
            self.primary = primary
        self.config_name = config_name
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        if gpu is not None:
            self.gpu = gpu

    @property
    def uuid(self):
        """Gets the uuid of this ServerViewModel.  # noqa: E501


        :return: The uuid of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ServerViewModel.


        :param uuid: The uuid of this ServerViewModel.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501
        if uuid is not None and len(uuid) > 36:
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `36`")  # noqa: E501
        if uuid is not None and len(uuid) < 36:
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this ServerViewModel.  # noqa: E501


        :return: The name of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerViewModel.


        :param name: The name of this ServerViewModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tariff_line(self):
        """Gets the tariff_line of this ServerViewModel.  # noqa: E501


        :return: The tariff_line of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._tariff_line

    @tariff_line.setter
    def tariff_line(self, tariff_line):
        """Sets the tariff_line of this ServerViewModel.


        :param tariff_line: The tariff_line of this ServerViewModel.  # noqa: E501
        :type: str
        """
        if tariff_line is None:
            raise ValueError("Invalid value for `tariff_line`, must not be `None`")  # noqa: E501

        self._tariff_line = tariff_line

    @property
    def model(self):
        """Gets the model of this ServerViewModel.  # noqa: E501


        :return: The model of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ServerViewModel.


        :param model: The model of this ServerViewModel.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def tags(self):
        """Gets the tags of this ServerViewModel.  # noqa: E501


        :return: The tags of this ServerViewModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServerViewModel.


        :param tags: The tags of this ServerViewModel.  # noqa: E501
        :type: list[str]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def state(self):
        """Gets the state of this ServerViewModel.  # noqa: E501

        service state  # noqa: E501

        :return: The state of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ServerViewModel.

        service state  # noqa: E501

        :param state: The state of this ServerViewModel.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def available(self):
        """Gets the available of this ServerViewModel.  # noqa: E501


        :return: The available of this ServerViewModel.  # noqa: E501
        :rtype: list[ServiceAvailable]
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this ServerViewModel.


        :param available: The available of this ServerViewModel.  # noqa: E501
        :type: list[ServiceAvailable]
        """
        if available is None:
            raise ValueError("Invalid value for `available`, must not be `None`")  # noqa: E501

        self._available = available

    @property
    def is_order(self):
        """Gets the is_order of this ServerViewModel.  # noqa: E501


        :return: The is_order of this ServerViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_order

    @is_order.setter
    def is_order(self, is_order):
        """Sets the is_order of this ServerViewModel.


        :param is_order: The is_order of this ServerViewModel.  # noqa: E501
        :type: bool
        """
        if is_order is None:
            raise ValueError("Invalid value for `is_order`, must not be `None`")  # noqa: E501

        self._is_order = is_order

    @property
    def is_preorder(self):
        """Gets the is_preorder of this ServerViewModel.  # noqa: E501


        :return: The is_preorder of this ServerViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_preorder

    @is_preorder.setter
    def is_preorder(self, is_preorder):
        """Sets the is_preorder of this ServerViewModel.


        :param is_preorder: The is_preorder of this ServerViewModel.  # noqa: E501
        :type: bool
        """
        if is_preorder is None:
            raise ValueError("Invalid value for `is_preorder`, must not be `None`")  # noqa: E501

        self._is_preorder = is_preorder

    @property
    def setup_fee_collection(self):
        """Gets the setup_fee_collection of this ServerViewModel.  # noqa: E501


        :return: The setup_fee_collection of this ServerViewModel.  # noqa: E501
        :rtype: PriceModel
        """
        return self._setup_fee_collection

    @setup_fee_collection.setter
    def setup_fee_collection(self, setup_fee_collection):
        """Sets the setup_fee_collection of this ServerViewModel.


        :param setup_fee_collection: The setup_fee_collection of this ServerViewModel.  # noqa: E501
        :type: PriceModel
        """
        if setup_fee_collection is None:
            raise ValueError("Invalid value for `setup_fee_collection`, must not be `None`")  # noqa: E501

        self._setup_fee_collection = setup_fee_collection

    @property
    def price_collection(self):
        """Gets the price_collection of this ServerViewModel.  # noqa: E501


        :return: The price_collection of this ServerViewModel.  # noqa: E501
        :rtype: PriceModel
        """
        return self._price_collection

    @price_collection.setter
    def price_collection(self, price_collection):
        """Sets the price_collection of this ServerViewModel.


        :param price_collection: The price_collection of this ServerViewModel.  # noqa: E501
        :type: PriceModel
        """
        if price_collection is None:
            raise ValueError("Invalid value for `price_collection`, must not be `None`")  # noqa: E501

        self._price_collection = price_collection

    @property
    def service_tag(self):
        """Gets the service_tag of this ServerViewModel.  # noqa: E501


        :return: The service_tag of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._service_tag

    @service_tag.setter
    def service_tag(self, service_tag):
        """Sets the service_tag of this ServerViewModel.


        :param service_tag: The service_tag of this ServerViewModel.  # noqa: E501
        :type: str
        """
        if service_tag is None:
            raise ValueError("Invalid value for `service_tag`, must not be `None`")  # noqa: E501

        self._service_tag = service_tag

    @property
    def is_primary(self):
        """Gets the is_primary of this ServerViewModel.  # noqa: E501


        :return: The is_primary of this ServerViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """Sets the is_primary of this ServerViewModel.


        :param is_primary: The is_primary of this ServerViewModel.  # noqa: E501
        :type: bool
        """
        if is_primary is None:
            raise ValueError("Invalid value for `is_primary`, must not be `None`")  # noqa: E501

        self._is_primary = is_primary

    @property
    def is_single_prolonged(self):
        """Gets the is_single_prolonged of this ServerViewModel.  # noqa: E501


        :return: The is_single_prolonged of this ServerViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_single_prolonged

    @is_single_prolonged.setter
    def is_single_prolonged(self, is_single_prolonged):
        """Sets the is_single_prolonged of this ServerViewModel.


        :param is_single_prolonged: The is_single_prolonged of this ServerViewModel.  # noqa: E501
        :type: bool
        """
        if is_single_prolonged is None:
            raise ValueError("Invalid value for `is_single_prolonged`, must not be `None`")  # noqa: E501

        self._is_single_prolonged = is_single_prolonged

    @property
    def quantity(self):
        """Gets the quantity of this ServerViewModel.  # noqa: E501


        :return: The quantity of this ServerViewModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ServerViewModel.


        :param quantity: The quantity of this ServerViewModel.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def is_qchange(self):
        """Gets the is_qchange of this ServerViewModel.  # noqa: E501


        :return: The is_qchange of this ServerViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_qchange

    @is_qchange.setter
    def is_qchange(self, is_qchange):
        """Sets the is_qchange of this ServerViewModel.


        :param is_qchange: The is_qchange of this ServerViewModel.  # noqa: E501
        :type: bool
        """

        self._is_qchange = is_qchange

    @property
    def price_plan_available(self):
        """Gets the price_plan_available of this ServerViewModel.  # noqa: E501


        :return: The price_plan_available of this ServerViewModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._price_plan_available

    @price_plan_available.setter
    def price_plan_available(self, price_plan_available):
        """Sets the price_plan_available of this ServerViewModel.


        :param price_plan_available: The price_plan_available of this ServerViewModel.  # noqa: E501
        :type: list[str]
        """
        if price_plan_available is None:
            raise ValueError("Invalid value for `price_plan_available`, must not be `None`")  # noqa: E501

        self._price_plan_available = price_plan_available

    @property
    def addition(self):
        """Gets the addition of this ServerViewModel.  # noqa: E501


        :return: The addition of this ServerViewModel.  # noqa: E501
        :rtype: list[ServiceBase]
        """
        return self._addition

    @addition.setter
    def addition(self, addition):
        """Sets the addition of this ServerViewModel.


        :param addition: The addition of this ServerViewModel.  # noqa: E501
        :type: list[ServiceBase]
        """

        self._addition = addition

    @property
    def primary(self):
        """Gets the primary of this ServerViewModel.  # noqa: E501


        :return: The primary of this ServerViewModel.  # noqa: E501
        :rtype: list[ServiceBase]
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this ServerViewModel.


        :param primary: The primary of this ServerViewModel.  # noqa: E501
        :type: list[ServiceBase]
        """

        self._primary = primary

    @property
    def config_name(self):
        """Gets the config_name of this ServerViewModel.  # noqa: E501


        :return: The config_name of this ServerViewModel.  # noqa: E501
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this ServerViewModel.


        :param config_name: The config_name of this ServerViewModel.  # noqa: E501
        :type: str
        """
        if config_name is None:
            raise ValueError("Invalid value for `config_name`, must not be `None`")  # noqa: E501

        self._config_name = config_name

    @property
    def cpu(self):
        """Gets the cpu of this ServerViewModel.  # noqa: E501


        :return: The cpu of this ServerViewModel.  # noqa: E501
        :rtype: ServerCPU
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ServerViewModel.


        :param cpu: The cpu of this ServerViewModel.  # noqa: E501
        :type: ServerCPU
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def ram(self):
        """Gets the ram of this ServerViewModel.  # noqa: E501


        :return: The ram of this ServerViewModel.  # noqa: E501
        :rtype: list[ServerRAM]
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ServerViewModel.


        :param ram: The ram of this ServerViewModel.  # noqa: E501
        :type: list[ServerRAM]
        """
        if ram is None:
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501

        self._ram = ram

    @property
    def disk(self):
        """Gets the disk of this ServerViewModel.  # noqa: E501


        :return: The disk of this ServerViewModel.  # noqa: E501
        :rtype: list[ServerDisk]
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this ServerViewModel.


        :param disk: The disk of this ServerViewModel.  # noqa: E501
        :type: list[ServerDisk]
        """
        if disk is None:
            raise ValueError("Invalid value for `disk`, must not be `None`")  # noqa: E501

        self._disk = disk

    @property
    def gpu(self):
        """Gets the gpu of this ServerViewModel.  # noqa: E501


        :return: The gpu of this ServerViewModel.  # noqa: E501
        :rtype: ServerGPU
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this ServerViewModel.


        :param gpu: The gpu of this ServerViewModel.  # noqa: E501
        :type: ServerGPU
        """

        self._gpu = gpu

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
