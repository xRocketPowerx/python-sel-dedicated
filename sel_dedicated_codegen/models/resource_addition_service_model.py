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


class ResourceAdditionServiceModel(object):
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
        'state': 'str',
        'price': 'PricePeriodModel',
        'setup_fee': 'PricePeriodModel',
        'quantity': 'int',
        'is_qchange': 'bool',
        'price_plan_available': 'list[str]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'state': 'state',
        'price': 'price',
        'setup_fee': 'setup_fee',
        'quantity': 'quantity',
        'is_qchange': 'is_qchange',
        'price_plan_available': 'price_plan_available'
    }

    def __init__(self, uuid=None, name=None, state=None, price=None, setup_fee=None, quantity=None, is_qchange=None, price_plan_available=None):  # noqa: E501
        """ResourceAdditionServiceModel - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._name = None
        self._state = None
        self._price = None
        self._setup_fee = None
        self._quantity = None
        self._is_qchange = None
        self._price_plan_available = None
        self.discriminator = None

        self.uuid = uuid
        self.name = name
        self.state = state
        self.price = price
        self.setup_fee = setup_fee
        self.quantity = quantity
        if is_qchange is not None:
            self.is_qchange = is_qchange
        self.price_plan_available = price_plan_available

    @property
    def uuid(self):
        """Gets the uuid of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The uuid of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ResourceAdditionServiceModel.


        :param uuid: The uuid of this ResourceAdditionServiceModel.  # noqa: E501
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
        """Gets the name of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The name of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceAdditionServiceModel.


        :param name: The name of this ResourceAdditionServiceModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The state of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ResourceAdditionServiceModel.


        :param state: The state of this ResourceAdditionServiceModel.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def price(self):
        """Gets the price of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The price of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: PricePeriodModel
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ResourceAdditionServiceModel.


        :param price: The price of this ResourceAdditionServiceModel.  # noqa: E501
        :type: PricePeriodModel
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def setup_fee(self):
        """Gets the setup_fee of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The setup_fee of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: PricePeriodModel
        """
        return self._setup_fee

    @setup_fee.setter
    def setup_fee(self, setup_fee):
        """Sets the setup_fee of this ResourceAdditionServiceModel.


        :param setup_fee: The setup_fee of this ResourceAdditionServiceModel.  # noqa: E501
        :type: PricePeriodModel
        """
        if setup_fee is None:
            raise ValueError("Invalid value for `setup_fee`, must not be `None`")  # noqa: E501

        self._setup_fee = setup_fee

    @property
    def quantity(self):
        """Gets the quantity of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The quantity of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ResourceAdditionServiceModel.


        :param quantity: The quantity of this ResourceAdditionServiceModel.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def is_qchange(self):
        """Gets the is_qchange of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The is_qchange of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_qchange

    @is_qchange.setter
    def is_qchange(self, is_qchange):
        """Sets the is_qchange of this ResourceAdditionServiceModel.


        :param is_qchange: The is_qchange of this ResourceAdditionServiceModel.  # noqa: E501
        :type: bool
        """

        self._is_qchange = is_qchange

    @property
    def price_plan_available(self):
        """Gets the price_plan_available of this ResourceAdditionServiceModel.  # noqa: E501


        :return: The price_plan_available of this ResourceAdditionServiceModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._price_plan_available

    @price_plan_available.setter
    def price_plan_available(self, price_plan_available):
        """Sets the price_plan_available of this ResourceAdditionServiceModel.


        :param price_plan_available: The price_plan_available of this ResourceAdditionServiceModel.  # noqa: E501
        :type: list[str]
        """
        if price_plan_available is None:
            raise ValueError("Invalid value for `price_plan_available`, must not be `None`")  # noqa: E501

        self._price_plan_available = price_plan_available

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
        if not isinstance(other, ResourceAdditionServiceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
