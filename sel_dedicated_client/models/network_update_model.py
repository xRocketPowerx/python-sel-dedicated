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


class NetworkUpdateModel(object):
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
        'user_desc': 'str'
    }

    attribute_map = {
        'user_desc': 'user_desc'
    }

    def __init__(self, user_desc=None):  # noqa: E501
        """NetworkUpdateModel - a model defined in OpenAPI"""  # noqa: E501

        self._user_desc = None
        self.discriminator = None

        if user_desc is not None:
            self.user_desc = user_desc

    @property
    def user_desc(self):
        """Gets the user_desc of this NetworkUpdateModel.  # noqa: E501

        User network description  # noqa: E501

        :return: The user_desc of this NetworkUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._user_desc

    @user_desc.setter
    def user_desc(self, user_desc):
        """Sets the user_desc of this NetworkUpdateModel.

        User network description  # noqa: E501

        :param user_desc: The user_desc of this NetworkUpdateModel.  # noqa: E501
        :type: str
        """

        self._user_desc = user_desc

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
        if not isinstance(other, NetworkUpdateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other