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


class ResourceStartAdditionalModel(object):
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
        'service_uuid': 'str',
        'quantity': 'int',
        'demo': 'bool',
        'pay_currency': 'str',
        'extra_period': 'int',
        'pay_day': 'int'
    }

    attribute_map = {
        'service_uuid': 'service_uuid',
        'quantity': 'quantity',
        'demo': 'demo',
        'pay_currency': 'pay_currency',
        'extra_period': 'extra_period',
        'pay_day': 'pay_day'
    }

    def __init__(self, service_uuid=None, quantity=None, demo=None, pay_currency=None, extra_period=None, pay_day=None):  # noqa: E501
        """ResourceStartAdditionalModel - a model defined in OpenAPI"""  # noqa: E501

        self._service_uuid = None
        self._quantity = None
        self._demo = None
        self._pay_currency = None
        self._extra_period = None
        self._pay_day = None
        self.discriminator = None

        self.service_uuid = service_uuid
        if quantity is not None:
            self.quantity = quantity
        if demo is not None:
            self.demo = demo
        self.pay_currency = pay_currency
        if extra_period is not None:
            self.extra_period = extra_period
        if pay_day is not None:
            self.pay_day = pay_day

    @property
    def service_uuid(self):
        """Gets the service_uuid of this ResourceStartAdditionalModel.  # noqa: E501


        :return: The service_uuid of this ResourceStartAdditionalModel.  # noqa: E501
        :rtype: str
        """
        return self._service_uuid

    @service_uuid.setter
    def service_uuid(self, service_uuid):
        """Sets the service_uuid of this ResourceStartAdditionalModel.


        :param service_uuid: The service_uuid of this ResourceStartAdditionalModel.  # noqa: E501
        :type: str
        """
        if service_uuid is None:
            raise ValueError("Invalid value for `service_uuid`, must not be `None`")  # noqa: E501
        if service_uuid is not None and len(service_uuid) > 36:
            raise ValueError("Invalid value for `service_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if service_uuid is not None and len(service_uuid) < 36:
            raise ValueError("Invalid value for `service_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._service_uuid = service_uuid

    @property
    def quantity(self):
        """Gets the quantity of this ResourceStartAdditionalModel.  # noqa: E501


        :return: The quantity of this ResourceStartAdditionalModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ResourceStartAdditionalModel.


        :param quantity: The quantity of this ResourceStartAdditionalModel.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def demo(self):
        """Gets the demo of this ResourceStartAdditionalModel.  # noqa: E501


        :return: The demo of this ResourceStartAdditionalModel.  # noqa: E501
        :rtype: bool
        """
        return self._demo

    @demo.setter
    def demo(self, demo):
        """Sets the demo of this ResourceStartAdditionalModel.


        :param demo: The demo of this ResourceStartAdditionalModel.  # noqa: E501
        :type: bool
        """

        self._demo = demo

    @property
    def pay_currency(self):
        """Gets the pay_currency of this ResourceStartAdditionalModel.  # noqa: E501


        :return: The pay_currency of this ResourceStartAdditionalModel.  # noqa: E501
        :rtype: str
        """
        return self._pay_currency

    @pay_currency.setter
    def pay_currency(self, pay_currency):
        """Sets the pay_currency of this ResourceStartAdditionalModel.


        :param pay_currency: The pay_currency of this ResourceStartAdditionalModel.  # noqa: E501
        :type: str
        """
        if pay_currency is None:
            raise ValueError("Invalid value for `pay_currency`, must not be `None`")  # noqa: E501
        allowed_values = ["bonus", "main", "vk_rub"]  # noqa: E501
        if pay_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `pay_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(pay_currency, allowed_values)
            )

        self._pay_currency = pay_currency

    @property
    def extra_period(self):
        """Gets the extra_period of this ResourceStartAdditionalModel.  # noqa: E501

        Prepayment for base plan period  # noqa: E501

        :return: The extra_period of this ResourceStartAdditionalModel.  # noqa: E501
        :rtype: int
        """
        return self._extra_period

    @extra_period.setter
    def extra_period(self, extra_period):
        """Sets the extra_period of this ResourceStartAdditionalModel.

        Prepayment for base plan period  # noqa: E501

        :param extra_period: The extra_period of this ResourceStartAdditionalModel.  # noqa: E501
        :type: int
        """

        self._extra_period = extra_period

    @property
    def pay_day(self):
        """Gets the pay_day of this ResourceStartAdditionalModel.  # noqa: E501

        Prepayment day  # noqa: E501

        :return: The pay_day of this ResourceStartAdditionalModel.  # noqa: E501
        :rtype: int
        """
        return self._pay_day

    @pay_day.setter
    def pay_day(self, pay_day):
        """Sets the pay_day of this ResourceStartAdditionalModel.

        Prepayment day  # noqa: E501

        :param pay_day: The pay_day of this ResourceStartAdditionalModel.  # noqa: E501
        :type: int
        """

        self._pay_day = pay_day

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
        if not isinstance(other, ResourceStartAdditionalModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
