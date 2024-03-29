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


class OSConfigAllOf(object):
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
        'login': 'str',
        'partitions': 'list[Partition]',
        'os_template': 'str',
        'password': 'str',
        'raid_type': 'str',
        'arch': 'str',
        'version': 'str',
        'userhostname': 'str',
        'user_ssh_key': 'str',
        'manage_agent': 'str',
        'ipv4_address': 'str',
        'ipv4_netmask': 'str',
        'ipv4_gateway': 'str',
        'ipv6_address': 'str',
        'ipv6_netmask': 'str',
        'ipv6_gateway': 'str',
        'reinstall': 'int'
    }

    attribute_map = {
        'login': 'login',
        'partitions': 'partitions',
        'os_template': 'os_template',
        'password': 'password',
        'raid_type': 'raid_type',
        'arch': 'arch',
        'version': 'version',
        'userhostname': 'userhostname',
        'user_ssh_key': 'user_ssh_key',
        'manage_agent': 'manage_agent',
        'ipv4_address': 'ipv4_address',
        'ipv4_netmask': 'ipv4_netmask',
        'ipv4_gateway': 'ipv4_gateway',
        'ipv6_address': 'ipv6_address',
        'ipv6_netmask': 'ipv6_netmask',
        'ipv6_gateway': 'ipv6_gateway',
        'reinstall': 'reinstall'
    }

    def __init__(self, login=None, partitions=None, os_template=None, password=None, raid_type=None, arch=None, version=None, userhostname=None, user_ssh_key=None, manage_agent='selectel', ipv4_address=None, ipv4_netmask=None, ipv4_gateway=None, ipv6_address=None, ipv6_netmask=None, ipv6_gateway=None, reinstall=None):  # noqa: E501
        """OSConfigAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._login = None
        self._partitions = None
        self._os_template = None
        self._password = None
        self._raid_type = None
        self._arch = None
        self._version = None
        self._userhostname = None
        self._user_ssh_key = None
        self._manage_agent = None
        self._ipv4_address = None
        self._ipv4_netmask = None
        self._ipv4_gateway = None
        self._ipv6_address = None
        self._ipv6_netmask = None
        self._ipv6_gateway = None
        self._reinstall = None
        self.discriminator = None

        if login is not None:
            self.login = login
        if partitions is not None:
            self.partitions = partitions
        self.os_template = os_template
        self.password = password
        self.raid_type = raid_type
        self.arch = arch
        self.version = version
        self.userhostname = userhostname
        if user_ssh_key is not None:
            self.user_ssh_key = user_ssh_key
        if manage_agent is not None:
            self.manage_agent = manage_agent
        if ipv4_address is not None:
            self.ipv4_address = ipv4_address
        if ipv4_netmask is not None:
            self.ipv4_netmask = ipv4_netmask
        if ipv4_gateway is not None:
            self.ipv4_gateway = ipv4_gateway
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if ipv6_netmask is not None:
            self.ipv6_netmask = ipv6_netmask
        if ipv6_gateway is not None:
            self.ipv6_gateway = ipv6_gateway
        if reinstall is not None:
            self.reinstall = reinstall

    @property
    def login(self):
        """Gets the login of this OSConfigAllOf.  # noqa: E501

        default OS login  # noqa: E501

        :return: The login of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this OSConfigAllOf.

        default OS login  # noqa: E501

        :param login: The login of this OSConfigAllOf.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def partitions(self):
        """Gets the partitions of this OSConfigAllOf.  # noqa: E501


        :return: The partitions of this OSConfigAllOf.  # noqa: E501
        :rtype: list[Partition]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this OSConfigAllOf.


        :param partitions: The partitions of this OSConfigAllOf.  # noqa: E501
        :type: list[Partition]
        """

        self._partitions = partitions

    @property
    def os_template(self):
        """Gets the os_template of this OSConfigAllOf.  # noqa: E501


        :return: The os_template of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._os_template

    @os_template.setter
    def os_template(self, os_template):
        """Sets the os_template of this OSConfigAllOf.


        :param os_template: The os_template of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if os_template is None:
            raise ValueError("Invalid value for `os_template`, must not be `None`")  # noqa: E501

        self._os_template = os_template

    @property
    def password(self):
        """Gets the password of this OSConfigAllOf.  # noqa: E501


        :return: The password of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OSConfigAllOf.


        :param password: The password of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def raid_type(self):
        """Gets the raid_type of this OSConfigAllOf.  # noqa: E501


        :return: The raid_type of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._raid_type

    @raid_type.setter
    def raid_type(self, raid_type):
        """Sets the raid_type of this OSConfigAllOf.


        :param raid_type: The raid_type of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if raid_type is None:
            raise ValueError("Invalid value for `raid_type`, must not be `None`")  # noqa: E501

        self._raid_type = raid_type

    @property
    def arch(self):
        """Gets the arch of this OSConfigAllOf.  # noqa: E501


        :return: The arch of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this OSConfigAllOf.


        :param arch: The arch of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if arch is None:
            raise ValueError("Invalid value for `arch`, must not be `None`")  # noqa: E501

        self._arch = arch

    @property
    def version(self):
        """Gets the version of this OSConfigAllOf.  # noqa: E501


        :return: The version of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OSConfigAllOf.


        :param version: The version of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def userhostname(self):
        """Gets the userhostname of this OSConfigAllOf.  # noqa: E501


        :return: The userhostname of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._userhostname

    @userhostname.setter
    def userhostname(self, userhostname):
        """Sets the userhostname of this OSConfigAllOf.


        :param userhostname: The userhostname of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if userhostname is None:
            raise ValueError("Invalid value for `userhostname`, must not be `None`")  # noqa: E501

        self._userhostname = userhostname

    @property
    def user_ssh_key(self):
        """Gets the user_ssh_key of this OSConfigAllOf.  # noqa: E501


        :return: The user_ssh_key of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._user_ssh_key

    @user_ssh_key.setter
    def user_ssh_key(self, user_ssh_key):
        """Sets the user_ssh_key of this OSConfigAllOf.


        :param user_ssh_key: The user_ssh_key of this OSConfigAllOf.  # noqa: E501
        :type: str
        """

        self._user_ssh_key = user_ssh_key

    @property
    def manage_agent(self):
        """Gets the manage_agent of this OSConfigAllOf.  # noqa: E501


        :return: The manage_agent of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._manage_agent

    @manage_agent.setter
    def manage_agent(self, manage_agent):
        """Sets the manage_agent of this OSConfigAllOf.


        :param manage_agent: The manage_agent of this OSConfigAllOf.  # noqa: E501
        :type: str
        """

        self._manage_agent = manage_agent

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this OSConfigAllOf.  # noqa: E501


        :return: The ipv4_address of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this OSConfigAllOf.


        :param ipv4_address: The ipv4_address of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if ipv4_address is not None and len(ipv4_address) > 43:
            raise ValueError("Invalid value for `ipv4_address`, length must be less than or equal to `43`")  # noqa: E501
        if ipv4_address is not None and len(ipv4_address) < 6:
            raise ValueError("Invalid value for `ipv4_address`, length must be greater than or equal to `6`")  # noqa: E501

        self._ipv4_address = ipv4_address

    @property
    def ipv4_netmask(self):
        """Gets the ipv4_netmask of this OSConfigAllOf.  # noqa: E501


        :return: The ipv4_netmask of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_netmask

    @ipv4_netmask.setter
    def ipv4_netmask(self, ipv4_netmask):
        """Sets the ipv4_netmask of this OSConfigAllOf.


        :param ipv4_netmask: The ipv4_netmask of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if ipv4_netmask is not None and len(ipv4_netmask) > 43:
            raise ValueError("Invalid value for `ipv4_netmask`, length must be less than or equal to `43`")  # noqa: E501
        if ipv4_netmask is not None and len(ipv4_netmask) < 6:
            raise ValueError("Invalid value for `ipv4_netmask`, length must be greater than or equal to `6`")  # noqa: E501

        self._ipv4_netmask = ipv4_netmask

    @property
    def ipv4_gateway(self):
        """Gets the ipv4_gateway of this OSConfigAllOf.  # noqa: E501


        :return: The ipv4_gateway of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_gateway

    @ipv4_gateway.setter
    def ipv4_gateway(self, ipv4_gateway):
        """Sets the ipv4_gateway of this OSConfigAllOf.


        :param ipv4_gateway: The ipv4_gateway of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if ipv4_gateway is not None and len(ipv4_gateway) > 43:
            raise ValueError("Invalid value for `ipv4_gateway`, length must be less than or equal to `43`")  # noqa: E501
        if ipv4_gateway is not None and len(ipv4_gateway) < 6:
            raise ValueError("Invalid value for `ipv4_gateway`, length must be greater than or equal to `6`")  # noqa: E501

        self._ipv4_gateway = ipv4_gateway

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this OSConfigAllOf.  # noqa: E501


        :return: The ipv6_address of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this OSConfigAllOf.


        :param ipv6_address: The ipv6_address of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if ipv6_address is not None and len(ipv6_address) > 43:
            raise ValueError("Invalid value for `ipv6_address`, length must be less than or equal to `43`")  # noqa: E501
        if ipv6_address is not None and len(ipv6_address) < 6:
            raise ValueError("Invalid value for `ipv6_address`, length must be greater than or equal to `6`")  # noqa: E501

        self._ipv6_address = ipv6_address

    @property
    def ipv6_netmask(self):
        """Gets the ipv6_netmask of this OSConfigAllOf.  # noqa: E501


        :return: The ipv6_netmask of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_netmask

    @ipv6_netmask.setter
    def ipv6_netmask(self, ipv6_netmask):
        """Sets the ipv6_netmask of this OSConfigAllOf.


        :param ipv6_netmask: The ipv6_netmask of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if ipv6_netmask is not None and len(ipv6_netmask) > 43:
            raise ValueError("Invalid value for `ipv6_netmask`, length must be less than or equal to `43`")  # noqa: E501
        if ipv6_netmask is not None and len(ipv6_netmask) < 6:
            raise ValueError("Invalid value for `ipv6_netmask`, length must be greater than or equal to `6`")  # noqa: E501

        self._ipv6_netmask = ipv6_netmask

    @property
    def ipv6_gateway(self):
        """Gets the ipv6_gateway of this OSConfigAllOf.  # noqa: E501


        :return: The ipv6_gateway of this OSConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_gateway

    @ipv6_gateway.setter
    def ipv6_gateway(self, ipv6_gateway):
        """Sets the ipv6_gateway of this OSConfigAllOf.


        :param ipv6_gateway: The ipv6_gateway of this OSConfigAllOf.  # noqa: E501
        :type: str
        """
        if ipv6_gateway is not None and len(ipv6_gateway) > 43:
            raise ValueError("Invalid value for `ipv6_gateway`, length must be less than or equal to `43`")  # noqa: E501
        if ipv6_gateway is not None and len(ipv6_gateway) < 6:
            raise ValueError("Invalid value for `ipv6_gateway`, length must be greater than or equal to `6`")  # noqa: E501

        self._ipv6_gateway = ipv6_gateway

    @property
    def reinstall(self):
        """Gets the reinstall of this OSConfigAllOf.  # noqa: E501


        :return: The reinstall of this OSConfigAllOf.  # noqa: E501
        :rtype: int
        """
        return self._reinstall

    @reinstall.setter
    def reinstall(self, reinstall):
        """Sets the reinstall of this OSConfigAllOf.


        :param reinstall: The reinstall of this OSConfigAllOf.  # noqa: E501
        :type: int
        """

        self._reinstall = reinstall

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
        if not isinstance(other, OSConfigAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
