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


class PowerStatus(object):
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
        'maintenance': 'bool',
        'maintenance_reason': 'str',
        'power_state': 'str',
        'target_power_state': 'str',
        'console_enabled': 'bool'
    }

    attribute_map = {
        'maintenance': 'maintenance',
        'maintenance_reason': 'maintenance_reason',
        'power_state': 'power_state',
        'target_power_state': 'target_power_state',
        'console_enabled': 'console_enabled'
    }

    def __init__(self, maintenance=None, maintenance_reason=None, power_state=None, target_power_state=None, console_enabled=None):  # noqa: E501
        """PowerStatus - a model defined in OpenAPI"""  # noqa: E501

        self._maintenance = None
        self._maintenance_reason = None
        self._power_state = None
        self._target_power_state = None
        self._console_enabled = None
        self.discriminator = None

        if maintenance is not None:
            self.maintenance = maintenance
        if maintenance_reason is not None:
            self.maintenance_reason = maintenance_reason
        if power_state is not None:
            self.power_state = power_state
        if target_power_state is not None:
            self.target_power_state = target_power_state
        if console_enabled is not None:
            self.console_enabled = console_enabled

    @property
    def maintenance(self):
        """Gets the maintenance of this PowerStatus.  # noqa: E501


        :return: The maintenance of this PowerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """Sets the maintenance of this PowerStatus.


        :param maintenance: The maintenance of this PowerStatus.  # noqa: E501
        :type: bool
        """

        self._maintenance = maintenance

    @property
    def maintenance_reason(self):
        """Gets the maintenance_reason of this PowerStatus.  # noqa: E501


        :return: The maintenance_reason of this PowerStatus.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_reason

    @maintenance_reason.setter
    def maintenance_reason(self, maintenance_reason):
        """Sets the maintenance_reason of this PowerStatus.


        :param maintenance_reason: The maintenance_reason of this PowerStatus.  # noqa: E501
        :type: str
        """

        self._maintenance_reason = maintenance_reason

    @property
    def power_state(self):
        """Gets the power_state of this PowerStatus.  # noqa: E501


        :return: The power_state of this PowerStatus.  # noqa: E501
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """Sets the power_state of this PowerStatus.


        :param power_state: The power_state of this PowerStatus.  # noqa: E501
        :type: str
        """

        self._power_state = power_state

    @property
    def target_power_state(self):
        """Gets the target_power_state of this PowerStatus.  # noqa: E501


        :return: The target_power_state of this PowerStatus.  # noqa: E501
        :rtype: str
        """
        return self._target_power_state

    @target_power_state.setter
    def target_power_state(self, target_power_state):
        """Sets the target_power_state of this PowerStatus.


        :param target_power_state: The target_power_state of this PowerStatus.  # noqa: E501
        :type: str
        """

        self._target_power_state = target_power_state

    @property
    def console_enabled(self):
        """Gets the console_enabled of this PowerStatus.  # noqa: E501


        :return: The console_enabled of this PowerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._console_enabled

    @console_enabled.setter
    def console_enabled(self, console_enabled):
        """Sets the console_enabled of this PowerStatus.


        :param console_enabled: The console_enabled of this PowerStatus.  # noqa: E501
        :type: bool
        """

        self._console_enabled = console_enabled

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
        if not isinstance(other, PowerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other