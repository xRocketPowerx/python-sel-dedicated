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


class Partition(object):
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
        'mount': 'str',
        'fstype': 'str',
        'size': 'int',
        'expand': 'bool',
        'editable': 'bool'
    }

    attribute_map = {
        'mount': 'mount',
        'fstype': 'fstype',
        'size': 'size',
        'expand': 'expand',
        'editable': 'editable'
    }

    def __init__(self, mount='/', fstype='ext4', size=None, expand=True, editable=True):  # noqa: E501
        """Partition - a model defined in OpenAPI"""  # noqa: E501

        self._mount = None
        self._fstype = None
        self._size = None
        self._expand = None
        self._editable = None
        self.discriminator = None

        if mount is not None:
            self.mount = mount
        if fstype is not None:
            self.fstype = fstype
        if size is not None:
            self.size = size
        if expand is not None:
            self.expand = expand
        if editable is not None:
            self.editable = editable

    @property
    def mount(self):
        """Gets the mount of this Partition.  # noqa: E501


        :return: The mount of this Partition.  # noqa: E501
        :rtype: str
        """
        return self._mount

    @mount.setter
    def mount(self, mount):
        """Sets the mount of this Partition.


        :param mount: The mount of this Partition.  # noqa: E501
        :type: str
        """

        self._mount = mount

    @property
    def fstype(self):
        """Gets the fstype of this Partition.  # noqa: E501


        :return: The fstype of this Partition.  # noqa: E501
        :rtype: str
        """
        return self._fstype

    @fstype.setter
    def fstype(self, fstype):
        """Sets the fstype of this Partition.


        :param fstype: The fstype of this Partition.  # noqa: E501
        :type: str
        """

        self._fstype = fstype

    @property
    def size(self):
        """Gets the size of this Partition.  # noqa: E501


        :return: The size of this Partition.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Partition.


        :param size: The size of this Partition.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def expand(self):
        """Gets the expand of this Partition.  # noqa: E501


        :return: The expand of this Partition.  # noqa: E501
        :rtype: bool
        """
        return self._expand

    @expand.setter
    def expand(self, expand):
        """Sets the expand of this Partition.


        :param expand: The expand of this Partition.  # noqa: E501
        :type: bool
        """

        self._expand = expand

    @property
    def editable(self):
        """Gets the editable of this Partition.  # noqa: E501


        :return: The editable of this Partition.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this Partition.


        :param editable: The editable of this Partition.  # noqa: E501
        :type: bool
        """

        self._editable = editable

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
        if not isinstance(other, Partition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other