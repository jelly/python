# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.31
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1FieldSelectorRequirement(object):
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
        'key': 'str',
        'operator': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, key=None, operator=None, values=None, local_vars_configuration=None):  # noqa: E501
        """V1FieldSelectorRequirement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._operator = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.operator = operator
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this V1FieldSelectorRequirement.  # noqa: E501

        key is the field selector key that the requirement applies to.  # noqa: E501

        :return: The key of this V1FieldSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1FieldSelectorRequirement.

        key is the field selector key that the requirement applies to.  # noqa: E501

        :param key: The key of this V1FieldSelectorRequirement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def operator(self):
        """Gets the operator of this V1FieldSelectorRequirement.  # noqa: E501

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future.  # noqa: E501

        :return: The operator of this V1FieldSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this V1FieldSelectorRequirement.

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future.  # noqa: E501

        :param operator: The operator of this V1FieldSelectorRequirement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def values(self):
        """Gets the values of this V1FieldSelectorRequirement.  # noqa: E501

        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty.  # noqa: E501

        :return: The values of this V1FieldSelectorRequirement.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1FieldSelectorRequirement.

        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty.  # noqa: E501

        :param values: The values of this V1FieldSelectorRequirement.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if not isinstance(other, V1FieldSelectorRequirement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1FieldSelectorRequirement):
            return True

        return self.to_dict() != other.to_dict()