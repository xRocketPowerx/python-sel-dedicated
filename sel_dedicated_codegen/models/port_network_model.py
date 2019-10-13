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


class PortNetworkModel(object):
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
        'network_uuid': 'str'
    }

    attribute_map = {
        'network_uuid': 'network_uuid'
    }

    def __init__(self, network_uuid=None):  # noqa: E501
        """PortNetworkModel - a model defined in OpenAPI"""  # noqa: E501

        self._network_uuid = None
        self.discriminator = None

        self.network_uuid = network_uuid

    @property
    def network_uuid(self):
        """Gets the network_uuid of this PortNetworkModel.  # noqa: E501


        :return: The network_uuid of this PortNetworkModel.  # noqa: E501
        :rtype: str
        """
        return self._network_uuid

    @network_uuid.setter
    def network_uuid(self, network_uuid):
        """Sets the network_uuid of this PortNetworkModel.


        :param network_uuid: The network_uuid of this PortNetworkModel.  # noqa: E501
        :type: str
        """
        if network_uuid is None:
            raise ValueError("Invalid value for `network_uuid`, must not be `None`")  # noqa: E501
        if network_uuid is not None and len(network_uuid) > 36:
            raise ValueError("Invalid value for `network_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if network_uuid is not None and len(network_uuid) < 36:
            raise ValueError("Invalid value for `network_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._network_uuid = network_uuid

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
        if not isinstance(other, PortNetworkModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other