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


class ResourceAddModel(object):
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
        'user_desc': 'str',
        'service_uuid': 'str',
        'location_uuid': 'str',
        'price_plan_uuid': 'str',
        'pay_day': 'int',
        'demo': 'bool'
    }

    attribute_map = {
        'user_desc': 'user_desc',
        'service_uuid': 'service_uuid',
        'location_uuid': 'location_uuid',
        'price_plan_uuid': 'price_plan_uuid',
        'pay_day': 'pay_day',
        'demo': 'demo'
    }

    def __init__(self, user_desc=None, service_uuid=None, location_uuid=None, price_plan_uuid=None, pay_day=None, demo=None):  # noqa: E501
        """ResourceAddModel - a model defined in OpenAPI"""  # noqa: E501

        self._user_desc = None
        self._service_uuid = None
        self._location_uuid = None
        self._price_plan_uuid = None
        self._pay_day = None
        self._demo = None
        self.discriminator = None

        if user_desc is not None:
            self.user_desc = user_desc
        self.service_uuid = service_uuid
        self.location_uuid = location_uuid
        self.price_plan_uuid = price_plan_uuid
        if pay_day is not None:
            self.pay_day = pay_day
        if demo is not None:
            self.demo = demo

    @property
    def user_desc(self):
        """Gets the user_desc of this ResourceAddModel.  # noqa: E501


        :return: The user_desc of this ResourceAddModel.  # noqa: E501
        :rtype: str
        """
        return self._user_desc

    @user_desc.setter
    def user_desc(self, user_desc):
        """Sets the user_desc of this ResourceAddModel.


        :param user_desc: The user_desc of this ResourceAddModel.  # noqa: E501
        :type: str
        """

        self._user_desc = user_desc

    @property
    def service_uuid(self):
        """Gets the service_uuid of this ResourceAddModel.  # noqa: E501


        :return: The service_uuid of this ResourceAddModel.  # noqa: E501
        :rtype: str
        """
        return self._service_uuid

    @service_uuid.setter
    def service_uuid(self, service_uuid):
        """Sets the service_uuid of this ResourceAddModel.


        :param service_uuid: The service_uuid of this ResourceAddModel.  # noqa: E501
        :type: str
        """
        if service_uuid is None:
            raise ValueError("Invalid value for `service_uuid`, must not be `None`")  # noqa: E501
        if service_uuid is not None and len(service_uuid) > 36:
            raise ValueError("Invalid value for `service_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if service_uuid is not None and len(service_uuid) < 36:
            raise ValueError("Invalid value for `service_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._service_uuid = service_uuid

    @property
    def location_uuid(self):
        """Gets the location_uuid of this ResourceAddModel.  # noqa: E501


        :return: The location_uuid of this ResourceAddModel.  # noqa: E501
        :rtype: str
        """
        return self._location_uuid

    @location_uuid.setter
    def location_uuid(self, location_uuid):
        """Sets the location_uuid of this ResourceAddModel.


        :param location_uuid: The location_uuid of this ResourceAddModel.  # noqa: E501
        :type: str
        """
        if location_uuid is None:
            raise ValueError("Invalid value for `location_uuid`, must not be `None`")  # noqa: E501
        if location_uuid is not None and len(location_uuid) > 36:
            raise ValueError("Invalid value for `location_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if location_uuid is not None and len(location_uuid) < 36:
            raise ValueError("Invalid value for `location_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._location_uuid = location_uuid

    @property
    def price_plan_uuid(self):
        """Gets the price_plan_uuid of this ResourceAddModel.  # noqa: E501


        :return: The price_plan_uuid of this ResourceAddModel.  # noqa: E501
        :rtype: str
        """
        return self._price_plan_uuid

    @price_plan_uuid.setter
    def price_plan_uuid(self, price_plan_uuid):
        """Sets the price_plan_uuid of this ResourceAddModel.


        :param price_plan_uuid: The price_plan_uuid of this ResourceAddModel.  # noqa: E501
        :type: str
        """
        if price_plan_uuid is None:
            raise ValueError("Invalid value for `price_plan_uuid`, must not be `None`")  # noqa: E501
        if price_plan_uuid is not None and len(price_plan_uuid) > 36:
            raise ValueError("Invalid value for `price_plan_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if price_plan_uuid is not None and len(price_plan_uuid) < 36:
            raise ValueError("Invalid value for `price_plan_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._price_plan_uuid = price_plan_uuid

    @property
    def pay_day(self):
        """Gets the pay_day of this ResourceAddModel.  # noqa: E501


        :return: The pay_day of this ResourceAddModel.  # noqa: E501
        :rtype: int
        """
        return self._pay_day

    @pay_day.setter
    def pay_day(self, pay_day):
        """Sets the pay_day of this ResourceAddModel.


        :param pay_day: The pay_day of this ResourceAddModel.  # noqa: E501
        :type: int
        """

        self._pay_day = pay_day

    @property
    def demo(self):
        """Gets the demo of this ResourceAddModel.  # noqa: E501


        :return: The demo of this ResourceAddModel.  # noqa: E501
        :rtype: bool
        """
        return self._demo

    @demo.setter
    def demo(self, demo):
        """Sets the demo of this ResourceAddModel.


        :param demo: The demo of this ResourceAddModel.  # noqa: E501
        :type: bool
        """

        self._demo = demo

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
        if not isinstance(other, ResourceAddModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
