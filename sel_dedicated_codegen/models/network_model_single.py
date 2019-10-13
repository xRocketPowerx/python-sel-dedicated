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


class NetworkModelSingle(object):
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
        'owner_id': 'int',
        'location_uuid': 'str',
        'vlan': 'int',
        'tag': 'str',
        'user_desc': 'str',
        'network_type': 'str',
        'is_shared': 'bool',
        'subnet_count': 'int',
        'port_count': 'int',
        'is_processing': 'bool',
        'subnet': 'list[NetworkSubnetSmallModel]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'created': 'created',
        'updated': 'updated',
        'owner_id': 'owner_id',
        'location_uuid': 'location_uuid',
        'vlan': 'vlan',
        'tag': 'tag',
        'user_desc': 'user_desc',
        'network_type': 'network_type',
        'is_shared': 'is_shared',
        'subnet_count': 'subnet_count',
        'port_count': 'port_count',
        'is_processing': 'is_processing',
        'subnet': 'subnet'
    }

    def __init__(self, uuid=None, created=None, updated=None, owner_id=None, location_uuid=None, vlan=None, tag=None, user_desc=None, network_type=None, is_shared=None, subnet_count=None, port_count=None, is_processing=None, subnet=None):  # noqa: E501
        """NetworkModelSingle - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._created = None
        self._updated = None
        self._owner_id = None
        self._location_uuid = None
        self._vlan = None
        self._tag = None
        self._user_desc = None
        self._network_type = None
        self._is_shared = None
        self._subnet_count = None
        self._port_count = None
        self._is_processing = None
        self._subnet = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if owner_id is not None:
            self.owner_id = owner_id
        if location_uuid is not None:
            self.location_uuid = location_uuid
        if vlan is not None:
            self.vlan = vlan
        if tag is not None:
            self.tag = tag
        if user_desc is not None:
            self.user_desc = user_desc
        if network_type is not None:
            self.network_type = network_type
        self.is_shared = is_shared
        if subnet_count is not None:
            self.subnet_count = subnet_count
        if port_count is not None:
            self.port_count = port_count
        self.is_processing = is_processing
        if subnet is not None:
            self.subnet = subnet

    @property
    def uuid(self):
        """Gets the uuid of this NetworkModelSingle.  # noqa: E501


        :return: The uuid of this NetworkModelSingle.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this NetworkModelSingle.


        :param uuid: The uuid of this NetworkModelSingle.  # noqa: E501
        :type: str
        """
        if uuid is not None and len(uuid) > 36:
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `36`")  # noqa: E501
        if uuid is not None and len(uuid) < 36:
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._uuid = uuid

    @property
    def created(self):
        """Gets the created of this NetworkModelSingle.  # noqa: E501


        :return: The created of this NetworkModelSingle.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NetworkModelSingle.


        :param created: The created of this NetworkModelSingle.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this NetworkModelSingle.  # noqa: E501


        :return: The updated of this NetworkModelSingle.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NetworkModelSingle.


        :param updated: The updated of this NetworkModelSingle.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def owner_id(self):
        """Gets the owner_id of this NetworkModelSingle.  # noqa: E501


        :return: The owner_id of this NetworkModelSingle.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this NetworkModelSingle.


        :param owner_id: The owner_id of this NetworkModelSingle.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def location_uuid(self):
        """Gets the location_uuid of this NetworkModelSingle.  # noqa: E501


        :return: The location_uuid of this NetworkModelSingle.  # noqa: E501
        :rtype: str
        """
        return self._location_uuid

    @location_uuid.setter
    def location_uuid(self, location_uuid):
        """Sets the location_uuid of this NetworkModelSingle.


        :param location_uuid: The location_uuid of this NetworkModelSingle.  # noqa: E501
        :type: str
        """
        if location_uuid is not None and len(location_uuid) > 36:
            raise ValueError("Invalid value for `location_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if location_uuid is not None and len(location_uuid) < 36:
            raise ValueError("Invalid value for `location_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._location_uuid = location_uuid

    @property
    def vlan(self):
        """Gets the vlan of this NetworkModelSingle.  # noqa: E501

        Specified Vlan. DEPRECATED: use \"tag\" instead.  # noqa: E501

        :return: The vlan of this NetworkModelSingle.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this NetworkModelSingle.

        Specified Vlan. DEPRECATED: use \"tag\" instead.  # noqa: E501

        :param vlan: The vlan of this NetworkModelSingle.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def tag(self):
        """Gets the tag of this NetworkModelSingle.  # noqa: E501

        Specified tag  # noqa: E501

        :return: The tag of this NetworkModelSingle.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NetworkModelSingle.

        Specified tag  # noqa: E501

        :param tag: The tag of this NetworkModelSingle.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def user_desc(self):
        """Gets the user_desc of this NetworkModelSingle.  # noqa: E501

        User network description  # noqa: E501

        :return: The user_desc of this NetworkModelSingle.  # noqa: E501
        :rtype: str
        """
        return self._user_desc

    @user_desc.setter
    def user_desc(self, user_desc):
        """Sets the user_desc of this NetworkModelSingle.

        User network description  # noqa: E501

        :param user_desc: The user_desc of this NetworkModelSingle.  # noqa: E501
        :type: str
        """

        self._user_desc = user_desc

    @property
    def network_type(self):
        """Gets the network_type of this NetworkModelSingle.  # noqa: E501


        :return: The network_type of this NetworkModelSingle.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this NetworkModelSingle.


        :param network_type: The network_type of this NetworkModelSingle.  # noqa: E501
        :type: str
        """
        allowed_values = ["local", "inet"]  # noqa: E501
        if network_type not in allowed_values:
            raise ValueError(
                "Invalid value for `network_type` ({0}), must be one of {1}"  # noqa: E501
                .format(network_type, allowed_values)
            )

        self._network_type = network_type

    @property
    def is_shared(self):
        """Gets the is_shared of this NetworkModelSingle.  # noqa: E501

        Shared network  # noqa: E501

        :return: The is_shared of this NetworkModelSingle.  # noqa: E501
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Sets the is_shared of this NetworkModelSingle.

        Shared network  # noqa: E501

        :param is_shared: The is_shared of this NetworkModelSingle.  # noqa: E501
        :type: bool
        """
        if is_shared is None:
            raise ValueError("Invalid value for `is_shared`, must not be `None`")  # noqa: E501

        self._is_shared = is_shared

    @property
    def subnet_count(self):
        """Gets the subnet_count of this NetworkModelSingle.  # noqa: E501


        :return: The subnet_count of this NetworkModelSingle.  # noqa: E501
        :rtype: int
        """
        return self._subnet_count

    @subnet_count.setter
    def subnet_count(self, subnet_count):
        """Sets the subnet_count of this NetworkModelSingle.


        :param subnet_count: The subnet_count of this NetworkModelSingle.  # noqa: E501
        :type: int
        """

        self._subnet_count = subnet_count

    @property
    def port_count(self):
        """Gets the port_count of this NetworkModelSingle.  # noqa: E501


        :return: The port_count of this NetworkModelSingle.  # noqa: E501
        :rtype: int
        """
        return self._port_count

    @port_count.setter
    def port_count(self, port_count):
        """Sets the port_count of this NetworkModelSingle.


        :param port_count: The port_count of this NetworkModelSingle.  # noqa: E501
        :type: int
        """

        self._port_count = port_count

    @property
    def is_processing(self):
        """Gets the is_processing of this NetworkModelSingle.  # noqa: E501


        :return: The is_processing of this NetworkModelSingle.  # noqa: E501
        :rtype: bool
        """
        return self._is_processing

    @is_processing.setter
    def is_processing(self, is_processing):
        """Sets the is_processing of this NetworkModelSingle.


        :param is_processing: The is_processing of this NetworkModelSingle.  # noqa: E501
        :type: bool
        """
        if is_processing is None:
            raise ValueError("Invalid value for `is_processing`, must not be `None`")  # noqa: E501

        self._is_processing = is_processing

    @property
    def subnet(self):
        """Gets the subnet of this NetworkModelSingle.  # noqa: E501


        :return: The subnet of this NetworkModelSingle.  # noqa: E501
        :rtype: list[NetworkSubnetSmallModel]
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this NetworkModelSingle.


        :param subnet: The subnet of this NetworkModelSingle.  # noqa: E501
        :type: list[NetworkSubnetSmallModel]
        """

        self._subnet = subnet

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
        if not isinstance(other, NetworkModelSingle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other