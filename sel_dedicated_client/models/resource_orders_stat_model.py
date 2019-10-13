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


class ResourceOrdersStatModel(object):
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
        'month': 'str',
        'order': 'list[ResourceOrdersModel]'
    }

    attribute_map = {
        'month': 'month',
        'order': 'order'
    }

    def __init__(self, month=None, order=None):  # noqa: E501
        """ResourceOrdersStatModel - a model defined in OpenAPI"""  # noqa: E501

        self._month = None
        self._order = None
        self.discriminator = None

        self.month = month
        if order is not None:
            self.order = order

    @property
    def month(self):
        """Gets the month of this ResourceOrdersStatModel.  # noqa: E501


        :return: The month of this ResourceOrdersStatModel.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ResourceOrdersStatModel.


        :param month: The month of this ResourceOrdersStatModel.  # noqa: E501
        :type: str
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def order(self):
        """Gets the order of this ResourceOrdersStatModel.  # noqa: E501


        :return: The order of this ResourceOrdersStatModel.  # noqa: E501
        :rtype: list[ResourceOrdersModel]
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ResourceOrdersStatModel.


        :param order: The order of this ResourceOrdersStatModel.  # noqa: E501
        :type: list[ResourceOrdersModel]
        """

        self._order = order

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
        if not isinstance(other, ResourceOrdersStatModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
