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


class IpModel(object):
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
        'resource_uuid': 'str',
        'ip': 'str',
        'subnet_uuid': 'str',
        'network_uuid': 'str',
        'subnet': 'str',
        'netmask': 'str',
        'gateway': 'str',
        'broadcast': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'created': 'created',
        'updated': 'updated',
        'resource_uuid': 'resource_uuid',
        'ip': 'ip',
        'subnet_uuid': 'subnet_uuid',
        'network_uuid': 'network_uuid',
        'subnet': 'subnet',
        'netmask': 'netmask',
        'gateway': 'gateway',
        'broadcast': 'broadcast'
    }

    def __init__(self, uuid=None, created=None, updated=None, resource_uuid=None, ip=None, subnet_uuid=None, network_uuid=None, subnet=None, netmask=None, gateway=None, broadcast=None):  # noqa: E501
        """IpModel - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._created = None
        self._updated = None
        self._resource_uuid = None
        self._ip = None
        self._subnet_uuid = None
        self._network_uuid = None
        self._subnet = None
        self._netmask = None
        self._gateway = None
        self._broadcast = None
        self.discriminator = None

        self.uuid = uuid
        self.created = created
        self.updated = updated
        if resource_uuid is not None:
            self.resource_uuid = resource_uuid
        self.ip = ip
        self.subnet_uuid = subnet_uuid
        self.network_uuid = network_uuid
        self.subnet = subnet
        self.netmask = netmask
        self.gateway = gateway
        self.broadcast = broadcast

    @property
    def uuid(self):
        """Gets the uuid of this IpModel.  # noqa: E501


        :return: The uuid of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this IpModel.


        :param uuid: The uuid of this IpModel.  # noqa: E501
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
        """Gets the created of this IpModel.  # noqa: E501


        :return: The created of this IpModel.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IpModel.


        :param created: The created of this IpModel.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this IpModel.  # noqa: E501


        :return: The updated of this IpModel.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this IpModel.


        :param updated: The updated of this IpModel.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def resource_uuid(self):
        """Gets the resource_uuid of this IpModel.  # noqa: E501


        :return: The resource_uuid of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._resource_uuid

    @resource_uuid.setter
    def resource_uuid(self, resource_uuid):
        """Sets the resource_uuid of this IpModel.


        :param resource_uuid: The resource_uuid of this IpModel.  # noqa: E501
        :type: str
        """
        if resource_uuid is not None and len(resource_uuid) > 36:
            raise ValueError("Invalid value for `resource_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if resource_uuid is not None and len(resource_uuid) < 36:
            raise ValueError("Invalid value for `resource_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._resource_uuid = resource_uuid

    @property
    def ip(self):
        """Gets the ip of this IpModel.  # noqa: E501


        :return: The ip of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpModel.


        :param ip: The ip of this IpModel.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501
        if ip is not None and len(ip) > 43:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `43`")  # noqa: E501
        if ip is not None and len(ip) < 6:
            raise ValueError("Invalid value for `ip`, length must be greater than or equal to `6`")  # noqa: E501

        self._ip = ip

    @property
    def subnet_uuid(self):
        """Gets the subnet_uuid of this IpModel.  # noqa: E501


        :return: The subnet_uuid of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._subnet_uuid

    @subnet_uuid.setter
    def subnet_uuid(self, subnet_uuid):
        """Sets the subnet_uuid of this IpModel.


        :param subnet_uuid: The subnet_uuid of this IpModel.  # noqa: E501
        :type: str
        """
        if subnet_uuid is None:
            raise ValueError("Invalid value for `subnet_uuid`, must not be `None`")  # noqa: E501
        if subnet_uuid is not None and len(subnet_uuid) > 36:
            raise ValueError("Invalid value for `subnet_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if subnet_uuid is not None and len(subnet_uuid) < 36:
            raise ValueError("Invalid value for `subnet_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._subnet_uuid = subnet_uuid

    @property
    def network_uuid(self):
        """Gets the network_uuid of this IpModel.  # noqa: E501


        :return: The network_uuid of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._network_uuid

    @network_uuid.setter
    def network_uuid(self, network_uuid):
        """Sets the network_uuid of this IpModel.


        :param network_uuid: The network_uuid of this IpModel.  # noqa: E501
        :type: str
        """
        if network_uuid is None:
            raise ValueError("Invalid value for `network_uuid`, must not be `None`")  # noqa: E501
        if network_uuid is not None and len(network_uuid) > 36:
            raise ValueError("Invalid value for `network_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if network_uuid is not None and len(network_uuid) < 36:
            raise ValueError("Invalid value for `network_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._network_uuid = network_uuid

    @property
    def subnet(self):
        """Gets the subnet of this IpModel.  # noqa: E501


        :return: The subnet of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this IpModel.


        :param subnet: The subnet of this IpModel.  # noqa: E501
        :type: str
        """
        if subnet is None:
            raise ValueError("Invalid value for `subnet`, must not be `None`")  # noqa: E501
        if subnet is not None and len(subnet) > 43:
            raise ValueError("Invalid value for `subnet`, length must be less than or equal to `43`")  # noqa: E501
        if subnet is not None and len(subnet) < 8:
            raise ValueError("Invalid value for `subnet`, length must be greater than or equal to `8`")  # noqa: E501

        self._subnet = subnet

    @property
    def netmask(self):
        """Gets the netmask of this IpModel.  # noqa: E501


        :return: The netmask of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IpModel.


        :param netmask: The netmask of this IpModel.  # noqa: E501
        :type: str
        """
        if netmask is None:
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

    @property
    def gateway(self):
        """Gets the gateway of this IpModel.  # noqa: E501


        :return: The gateway of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IpModel.


        :param gateway: The gateway of this IpModel.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def broadcast(self):
        """Gets the broadcast of this IpModel.  # noqa: E501


        :return: The broadcast of this IpModel.  # noqa: E501
        :rtype: str
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        """Sets the broadcast of this IpModel.


        :param broadcast: The broadcast of this IpModel.  # noqa: E501
        :type: str
        """
        if broadcast is None:
            raise ValueError("Invalid value for `broadcast`, must not be `None`")  # noqa: E501

        self._broadcast = broadcast

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
        if not isinstance(other, IpModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
