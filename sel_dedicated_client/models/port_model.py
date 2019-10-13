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


class PortModel(object):
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
        'created': 'int',
        'updated': 'int',
        'port_type': 'str',
        'speed': 'str',
        'is_enabled': 'bool',
        'port_name': 'str',
        'is_apply': 'bool',
        'hw_uuid': 'str',
        'network': 'list[NetworkModel]',
        'is_processing': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'created': 'created',
        'updated': 'updated',
        'port_type': 'port_type',
        'speed': 'speed',
        'is_enabled': 'is_enabled',
        'port_name': 'port_name',
        'is_apply': 'is_apply',
        'hw_uuid': 'hw_uuid',
        'network': 'network',
        'is_processing': 'is_processing'
    }

    def __init__(self, uuid=None, created=None, updated=None, port_type=None, speed=None, is_enabled=None, port_name=None, is_apply=None, hw_uuid=None, network=None, is_processing=None):  # noqa: E501
        """PortModel - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._created = None
        self._updated = None
        self._port_type = None
        self._speed = None
        self._is_enabled = None
        self._port_name = None
        self._is_apply = None
        self._hw_uuid = None
        self._network = None
        self._is_processing = None
        self.discriminator = None

        self.uuid = uuid
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        self.port_type = port_type
        self.speed = speed
        self.is_enabled = is_enabled
        self.port_name = port_name
        self.is_apply = is_apply
        self.hw_uuid = hw_uuid
        if network is not None:
            self.network = network
        self.is_processing = is_processing

    @property
    def uuid(self):
        """Gets the uuid of this PortModel.  # noqa: E501


        :return: The uuid of this PortModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PortModel.


        :param uuid: The uuid of this PortModel.  # noqa: E501
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
    def created(self):
        """Gets the created of this PortModel.  # noqa: E501


        :return: The created of this PortModel.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PortModel.


        :param created: The created of this PortModel.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this PortModel.  # noqa: E501


        :return: The updated of this PortModel.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PortModel.


        :param updated: The updated of this PortModel.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def port_type(self):
        """Gets the port_type of this PortModel.  # noqa: E501


        :return: The port_type of this PortModel.  # noqa: E501
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this PortModel.


        :param port_type: The port_type of this PortModel.  # noqa: E501
        :type: str
        """
        if port_type is None:
            raise ValueError("Invalid value for `port_type`, must not be `None`")  # noqa: E501
        allowed_values = ["local", "inet"]  # noqa: E501
        if port_type not in allowed_values:
            raise ValueError(
                "Invalid value for `port_type` ({0}), must be one of {1}"  # noqa: E501
                .format(port_type, allowed_values)
            )

        self._port_type = port_type

    @property
    def speed(self):
        """Gets the speed of this PortModel.  # noqa: E501


        :return: The speed of this PortModel.  # noqa: E501
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this PortModel.


        :param speed: The speed of this PortModel.  # noqa: E501
        :type: str
        """
        if speed is None:
            raise ValueError("Invalid value for `speed`, must not be `None`")  # noqa: E501
        allowed_values = ["AUTO", "10M", "100M", "1G"]  # noqa: E501
        if speed not in allowed_values:
            raise ValueError(
                "Invalid value for `speed` ({0}), must be one of {1}"  # noqa: E501
                .format(speed, allowed_values)
            )

        self._speed = speed

    @property
    def is_enabled(self):
        """Gets the is_enabled of this PortModel.  # noqa: E501


        :return: The is_enabled of this PortModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this PortModel.


        :param is_enabled: The is_enabled of this PortModel.  # noqa: E501
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def port_name(self):
        """Gets the port_name of this PortModel.  # noqa: E501


        :return: The port_name of this PortModel.  # noqa: E501
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """Sets the port_name of this PortModel.


        :param port_name: The port_name of this PortModel.  # noqa: E501
        :type: str
        """
        if port_name is None:
            raise ValueError("Invalid value for `port_name`, must not be `None`")  # noqa: E501

        self._port_name = port_name

    @property
    def is_apply(self):
        """Gets the is_apply of this PortModel.  # noqa: E501


        :return: The is_apply of this PortModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_apply

    @is_apply.setter
    def is_apply(self, is_apply):
        """Sets the is_apply of this PortModel.


        :param is_apply: The is_apply of this PortModel.  # noqa: E501
        :type: bool
        """
        if is_apply is None:
            raise ValueError("Invalid value for `is_apply`, must not be `None`")  # noqa: E501

        self._is_apply = is_apply

    @property
    def hw_uuid(self):
        """Gets the hw_uuid of this PortModel.  # noqa: E501


        :return: The hw_uuid of this PortModel.  # noqa: E501
        :rtype: str
        """
        return self._hw_uuid

    @hw_uuid.setter
    def hw_uuid(self, hw_uuid):
        """Sets the hw_uuid of this PortModel.


        :param hw_uuid: The hw_uuid of this PortModel.  # noqa: E501
        :type: str
        """
        if hw_uuid is None:
            raise ValueError("Invalid value for `hw_uuid`, must not be `None`")  # noqa: E501
        if hw_uuid is not None and len(hw_uuid) > 36:
            raise ValueError("Invalid value for `hw_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if hw_uuid is not None and len(hw_uuid) < 36:
            raise ValueError("Invalid value for `hw_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._hw_uuid = hw_uuid

    @property
    def network(self):
        """Gets the network of this PortModel.  # noqa: E501


        :return: The network of this PortModel.  # noqa: E501
        :rtype: list[NetworkModel]
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this PortModel.


        :param network: The network of this PortModel.  # noqa: E501
        :type: list[NetworkModel]
        """

        self._network = network

    @property
    def is_processing(self):
        """Gets the is_processing of this PortModel.  # noqa: E501


        :return: The is_processing of this PortModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_processing

    @is_processing.setter
    def is_processing(self, is_processing):
        """Sets the is_processing of this PortModel.


        :param is_processing: The is_processing of this PortModel.  # noqa: E501
        :type: bool
        """
        if is_processing is None:
            raise ValueError("Invalid value for `is_processing`, must not be `None`")  # noqa: E501

        self._is_processing = is_processing

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
        if not isinstance(other, PortModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
