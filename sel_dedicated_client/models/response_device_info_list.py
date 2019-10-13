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


class ResponseDeviceInfoList(object):
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
        'task_id': 'str',
        'status': 'str',
        'progress': 'int',
        'page': 'int',
        'limit': 'int',
        'item_count': 'int',
        'execution_time': 'float',
        'result': 'list[DeviceInfo]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'progress': 'progress',
        'page': 'page',
        'limit': 'limit',
        'item_count': 'item_count',
        'execution_time': 'execution_time',
        'result': 'result'
    }

    def __init__(self, task_id=None, status=None, progress=None, page=None, limit=None, item_count=None, execution_time=None, result=None):  # noqa: E501
        """ResponseDeviceInfoList - a model defined in OpenAPI"""  # noqa: E501

        self._task_id = None
        self._status = None
        self._progress = None
        self._page = None
        self._limit = None
        self._item_count = None
        self._execution_time = None
        self._result = None
        self.discriminator = None

        self.task_id = task_id
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if page is not None:
            self.page = page
        if limit is not None:
            self.limit = limit
        if item_count is not None:
            self.item_count = item_count
        if execution_time is not None:
            self.execution_time = execution_time
        if result is not None:
            self.result = result

    @property
    def task_id(self):
        """Gets the task_id of this ResponseDeviceInfoList.  # noqa: E501

        Unique task UUID v4  # noqa: E501

        :return: The task_id of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ResponseDeviceInfoList.

        Unique task UUID v4  # noqa: E501

        :param task_id: The task_id of this ResponseDeviceInfoList.  # noqa: E501
        :type: str
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501
        if task_id is not None and len(task_id) > 36:
            raise ValueError("Invalid value for `task_id`, length must be less than or equal to `36`")  # noqa: E501
        if task_id is not None and len(task_id) < 36:
            raise ValueError("Invalid value for `task_id`, length must be greater than or equal to `36`")  # noqa: E501

        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this ResponseDeviceInfoList.  # noqa: E501


        :return: The status of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseDeviceInfoList.


        :param status: The status of this ResponseDeviceInfoList.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this ResponseDeviceInfoList.  # noqa: E501


        :return: The progress of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ResponseDeviceInfoList.


        :param progress: The progress of this ResponseDeviceInfoList.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def page(self):
        """Gets the page of this ResponseDeviceInfoList.  # noqa: E501


        :return: The page of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ResponseDeviceInfoList.


        :param page: The page of this ResponseDeviceInfoList.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def limit(self):
        """Gets the limit of this ResponseDeviceInfoList.  # noqa: E501


        :return: The limit of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ResponseDeviceInfoList.


        :param limit: The limit of this ResponseDeviceInfoList.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def item_count(self):
        """Gets the item_count of this ResponseDeviceInfoList.  # noqa: E501


        :return: The item_count of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this ResponseDeviceInfoList.


        :param item_count: The item_count of this ResponseDeviceInfoList.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

    @property
    def execution_time(self):
        """Gets the execution_time of this ResponseDeviceInfoList.  # noqa: E501


        :return: The execution_time of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: float
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this ResponseDeviceInfoList.


        :param execution_time: The execution_time of this ResponseDeviceInfoList.  # noqa: E501
        :type: float
        """

        self._execution_time = execution_time

    @property
    def result(self):
        """Gets the result of this ResponseDeviceInfoList.  # noqa: E501


        :return: The result of this ResponseDeviceInfoList.  # noqa: E501
        :rtype: list[DeviceInfo]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ResponseDeviceInfoList.


        :param result: The result of this ResponseDeviceInfoList.  # noqa: E501
        :type: list[DeviceInfo]
        """

        self._result = result

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
        if not isinstance(other, ResponseDeviceInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
