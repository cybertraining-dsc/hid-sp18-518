# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ephemeral_disk_in_gb: int=None, vcpus: int=None, href: str=None, name: str=None, disk_in_gb: int=None, ram_in_mb: int=None, id: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param ephemeral_disk_in_gb: The ephemeral_disk_in_gb of this InlineResponse200.  # noqa: E501
        :type ephemeral_disk_in_gb: int
        :param vcpus: The vcpus of this InlineResponse200.  # noqa: E501
        :type vcpus: int
        :param href: The href of this InlineResponse200.  # noqa: E501
        :type href: str
        :param name: The name of this InlineResponse200.  # noqa: E501
        :type name: str
        :param disk_in_gb: The disk_in_gb of this InlineResponse200.  # noqa: E501
        :type disk_in_gb: int
        :param ram_in_mb: The ram_in_mb of this InlineResponse200.  # noqa: E501
        :type ram_in_mb: int
        :param id: The id of this InlineResponse200.  # noqa: E501
        :type id: str
        """
        self.swagger_types = {
            'ephemeral_disk_in_gb': int,
            'vcpus': int,
            'href': str,
            'name': str,
            'disk_in_gb': int,
            'ram_in_mb': int,
            'id': str
        }

        self.attribute_map = {
            'ephemeral_disk_in_gb': 'ephemeralDiskInGb',
            'vcpus': 'vcpus',
            'href': 'href',
            'name': 'name',
            'disk_in_gb': 'diskInGb',
            'ram_in_mb': 'ramInMb',
            'id': 'id'
        }

        self._ephemeral_disk_in_gb = ephemeral_disk_in_gb
        self._vcpus = vcpus
        self._href = href
        self._name = name
        self._disk_in_gb = disk_in_gb
        self._ram_in_mb = ram_in_mb
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ephemeral_disk_in_gb(self) -> int:
        """Gets the ephemeral_disk_in_gb of this InlineResponse200.

        VM ephemeral disk size in GB  # noqa: E501

        :return: The ephemeral_disk_in_gb of this InlineResponse200.
        :rtype: int
        """
        return self._ephemeral_disk_in_gb

    @ephemeral_disk_in_gb.setter
    def ephemeral_disk_in_gb(self, ephemeral_disk_in_gb: int):
        """Sets the ephemeral_disk_in_gb of this InlineResponse200.

        VM ephemeral disk size in GB  # noqa: E501

        :param ephemeral_disk_in_gb: The ephemeral_disk_in_gb of this InlineResponse200.
        :type ephemeral_disk_in_gb: int
        """

        self._ephemeral_disk_in_gb = ephemeral_disk_in_gb

    @property
    def vcpus(self) -> int:
        """Gets the vcpus of this InlineResponse200.

        Number of virtual CPUs  # noqa: E501

        :return: The vcpus of this InlineResponse200.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus: int):
        """Sets the vcpus of this InlineResponse200.

        Number of virtual CPUs  # noqa: E501

        :param vcpus: The vcpus of this InlineResponse200.
        :type vcpus: int
        """

        self._vcpus = vcpus

    @property
    def href(self) -> str:
        """Gets the href of this InlineResponse200.

        Url to a flavor  # noqa: E501

        :return: The href of this InlineResponse200.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this InlineResponse200.

        Url to a flavor  # noqa: E501

        :param href: The href of this InlineResponse200.
        :type href: str
        """

        self._href = href

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse200.

        Flavor name  # noqa: E501

        :return: The name of this InlineResponse200.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse200.

        Flavor name  # noqa: E501

        :param name: The name of this InlineResponse200.
        :type name: str
        """

        self._name = name

    @property
    def disk_in_gb(self) -> int:
        """Gets the disk_in_gb of this InlineResponse200.

        Disk size in GB  # noqa: E501

        :return: The disk_in_gb of this InlineResponse200.
        :rtype: int
        """
        return self._disk_in_gb

    @disk_in_gb.setter
    def disk_in_gb(self, disk_in_gb: int):
        """Sets the disk_in_gb of this InlineResponse200.

        Disk size in GB  # noqa: E501

        :param disk_in_gb: The disk_in_gb of this InlineResponse200.
        :type disk_in_gb: int
        """

        self._disk_in_gb = disk_in_gb

    @property
    def ram_in_mb(self) -> int:
        """Gets the ram_in_mb of this InlineResponse200.

        Memory size in MB  # noqa: E501

        :return: The ram_in_mb of this InlineResponse200.
        :rtype: int
        """
        return self._ram_in_mb

    @ram_in_mb.setter
    def ram_in_mb(self, ram_in_mb: int):
        """Sets the ram_in_mb of this InlineResponse200.

        Memory size in MB  # noqa: E501

        :param ram_in_mb: The ram_in_mb of this InlineResponse200.
        :type ram_in_mb: int
        """

        self._ram_in_mb = ram_in_mb

    @property
    def id(self) -> str:
        """Gets the id of this InlineResponse200.

        Flavor id  # noqa: E501

        :return: The id of this InlineResponse200.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this InlineResponse200.

        Flavor id  # noqa: E501

        :param id: The id of this InlineResponse200.
        :type id: str
        """

        self._id = id
