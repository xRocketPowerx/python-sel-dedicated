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


class ResourceOrderedModel(object):
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
        'info': 'str',
        'created': 'int',
        'primary_uuid': 'str',
        'is_single_prolonged': 'bool',
        'state': 'str',
        'service_price': 'float',
        'service_uuid': 'str',
        'quantity': 'int',
        'service_type': 'str',
        'paid_till': 'int',
        'billing': 'BillingModel'
    }

    attribute_map = {
        'uuid': 'uuid',
        'info': 'info',
        'created': 'created',
        'primary_uuid': 'primary_uuid',
        'is_single_prolonged': 'is_single_prolonged',
        'state': 'state',
        'service_price': 'service_price',
        'service_uuid': 'service_uuid',
        'quantity': 'quantity',
        'service_type': 'service_type',
        'paid_till': 'paid_till',
        'billing': 'billing'
    }

    def __init__(self, uuid=None, info=None, created=None, primary_uuid=None, is_single_prolonged=None, state=None, service_price=None, service_uuid=None, quantity=None, service_type=None, paid_till=None, billing=None):  # noqa: E501
        """ResourceOrderedModel - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._info = None
        self._created = None
        self._primary_uuid = None
        self._is_single_prolonged = None
        self._state = None
        self._service_price = None
        self._service_uuid = None
        self._quantity = None
        self._service_type = None
        self._paid_till = None
        self._billing = None
        self.discriminator = None

        self.uuid = uuid
        if info is not None:
            self.info = info
        if created is not None:
            self.created = created
        if primary_uuid is not None:
            self.primary_uuid = primary_uuid
        self.is_single_prolonged = is_single_prolonged
        self.state = state
        self.service_price = service_price
        self.service_uuid = service_uuid
        self.quantity = quantity
        self.service_type = service_type
        self.paid_till = paid_till
        self.billing = billing

    @property
    def uuid(self):
        """Gets the uuid of this ResourceOrderedModel.  # noqa: E501


        :return: The uuid of this ResourceOrderedModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ResourceOrderedModel.


        :param uuid: The uuid of this ResourceOrderedModel.  # noqa: E501
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
    def info(self):
        """Gets the info of this ResourceOrderedModel.  # noqa: E501


        :return: The info of this ResourceOrderedModel.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ResourceOrderedModel.


        :param info: The info of this ResourceOrderedModel.  # noqa: E501
        :type: str
        """

        self._info = info

    @property
    def created(self):
        """Gets the created of this ResourceOrderedModel.  # noqa: E501


        :return: The created of this ResourceOrderedModel.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResourceOrderedModel.


        :param created: The created of this ResourceOrderedModel.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def primary_uuid(self):
        """Gets the primary_uuid of this ResourceOrderedModel.  # noqa: E501


        :return: The primary_uuid of this ResourceOrderedModel.  # noqa: E501
        :rtype: str
        """
        return self._primary_uuid

    @primary_uuid.setter
    def primary_uuid(self, primary_uuid):
        """Sets the primary_uuid of this ResourceOrderedModel.


        :param primary_uuid: The primary_uuid of this ResourceOrderedModel.  # noqa: E501
        :type: str
        """
        if primary_uuid is not None and len(primary_uuid) > 36:
            raise ValueError("Invalid value for `primary_uuid`, length must be less than or equal to `36`")  # noqa: E501
        if primary_uuid is not None and len(primary_uuid) < 36:
            raise ValueError("Invalid value for `primary_uuid`, length must be greater than or equal to `36`")  # noqa: E501

        self._primary_uuid = primary_uuid

    @property
    def is_single_prolonged(self):
        """Gets the is_single_prolonged of this ResourceOrderedModel.  # noqa: E501


        :return: The is_single_prolonged of this ResourceOrderedModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_single_prolonged

    @is_single_prolonged.setter
    def is_single_prolonged(self, is_single_prolonged):
        """Sets the is_single_prolonged of this ResourceOrderedModel.


        :param is_single_prolonged: The is_single_prolonged of this ResourceOrderedModel.  # noqa: E501
        :type: bool
        """
        if is_single_prolonged is None:
            raise ValueError("Invalid value for `is_single_prolonged`, must not be `None`")  # noqa: E501

        self._is_single_prolonged = is_single_prolonged

    @property
    def state(self):
        """Gets the state of this ResourceOrderedModel.  # noqa: E501


        :return: The state of this ResourceOrderedModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ResourceOrderedModel.


        :param state: The state of this ResourceOrderedModel.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["pending", "processing", "prolong", "paid", "deploy", "active", "expiring", "ending", "cancelling", "unpaid", "blocked", "provided", "cancel", "deleted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def service_price(self):
        """Gets the service_price of this ResourceOrderedModel.  # noqa: E501


        :return: The service_price of this ResourceOrderedModel.  # noqa: E501
        :rtype: float
        """
        return self._service_price

    @service_price.setter
    def service_price(self, service_price):
        """Sets the service_price of this ResourceOrderedModel.


        :param service_price: The service_price of this ResourceOrderedModel.  # noqa: E501
        :type: float
        """
        if service_price is None:
            raise ValueError("Invalid value for `service_price`, must not be `None`")  # noqa: E501

        self._service_price = service_price

    @property
    def service_uuid(self):
        """Gets the service_uuid of this ResourceOrderedModel.  # noqa: E501


        :return: The service_uuid of this ResourceOrderedModel.  # noqa: E501
        :rtype: str
        """
        return self._service_uuid

    @service_uuid.setter
    def service_uuid(self, service_uuid):
        """Sets the service_uuid of this ResourceOrderedModel.


        :param service_uuid: The service_uuid of this ResourceOrderedModel.  # noqa: E501
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
    def quantity(self):
        """Gets the quantity of this ResourceOrderedModel.  # noqa: E501


        :return: The quantity of this ResourceOrderedModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ResourceOrderedModel.


        :param quantity: The quantity of this ResourceOrderedModel.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def service_type(self):
        """Gets the service_type of this ResourceOrderedModel.  # noqa: E501


        :return: The service_type of this ResourceOrderedModel.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ResourceOrderedModel.


        :param service_type: The service_type of this ResourceOrderedModel.  # noqa: E501
        :type: str
        """
        if service_type is None:
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501

        self._service_type = service_type

    @property
    def paid_till(self):
        """Gets the paid_till of this ResourceOrderedModel.  # noqa: E501

        Start order date from resource  # noqa: E501

        :return: The paid_till of this ResourceOrderedModel.  # noqa: E501
        :rtype: int
        """
        return self._paid_till

    @paid_till.setter
    def paid_till(self, paid_till):
        """Sets the paid_till of this ResourceOrderedModel.

        Start order date from resource  # noqa: E501

        :param paid_till: The paid_till of this ResourceOrderedModel.  # noqa: E501
        :type: int
        """
        if paid_till is None:
            raise ValueError("Invalid value for `paid_till`, must not be `None`")  # noqa: E501

        self._paid_till = paid_till

    @property
    def billing(self):
        """Gets the billing of this ResourceOrderedModel.  # noqa: E501


        :return: The billing of this ResourceOrderedModel.  # noqa: E501
        :rtype: BillingModel
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this ResourceOrderedModel.


        :param billing: The billing of this ResourceOrderedModel.  # noqa: E501
        :type: BillingModel
        """
        if billing is None:
            raise ValueError("Invalid value for `billing`, must not be `None`")  # noqa: E501

        self._billing = billing

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
        if not isinstance(other, ResourceOrderedModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
