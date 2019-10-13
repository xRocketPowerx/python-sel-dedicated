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


class IpAllocateModel(object):
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
        'resource_uuid': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'resource_uuid': 'resource_uuid',
        'ip': 'ip'
    }

    def __init__(self, resource_uuid=None, ip=None):  # noqa: E501
        """IpAllocateModel - a model defined in OpenAPI"""  # noqa: E501

        self._resource_uuid = None
        self._ip = None
        self.discriminator = None

        self.resource_uuid = resource_uuid
        if ip is not None:
            self.ip = ip

    @property
    def resource_uuid(self):
        """Gets the resource_uuid of this IpAllocateModel.  # noqa: E501


        :return: The resource_uuid of this IpAllocateModel.  # noqa: E501
        :rtype: str
        """
        return self._resource_uuid

    @resource_uuid.setter
    def resource_uuid(self, resource_uuid):
        """Sets the resource_uuid of this IpAllocateModel.


        :param resource_uuid: The resource_uuid of this IpAllocateModel.  # noqa: E501
        :type: str
        """
        if resource_uuid is None:
            raise ValueError("Invalid value for `resource_uuid`, must not be `None`")  # noqa: E501
        if resource_uuid is not None and len(resource_uuid) > 36:
            raise ValueError("Invalid value for `resource_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if resource_uuid is not None and len(resource_uuid) < 36:
            raise ValueError("Invalid value for `resource_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._resource_uuid = resource_uuid

    @property
    def ip(self):
        """Gets the ip of this IpAllocateModel.  # noqa: E501


        :return: The ip of this IpAllocateModel.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpAllocateModel.


        :param ip: The ip of this IpAllocateModel.  # noqa: E501
        :type: str
        """
        if ip is not None and len(ip) > 43:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `43`")  # noqa: E501
        if ip is not None and len(ip) < 6:
            raise ValueError("Invalid value for `ip`, length must be greater than or equal to `6`")  # noqa: E501

        self._ip = ip

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
        if not isinstance(other, IpAllocateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
