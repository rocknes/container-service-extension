# container-service-extension
# Copyright (c) 2020 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

"""Utility methods to help interaction with defined entities framework."""

from container_service_extension.cloudapi.cloudapi_client import CloudApiClient
import container_service_extension.def_.constants as def_constants
import container_service_extension.exceptions as excptn


def raise_error_if_def_not_supported(cloudapi_client: CloudApiClient):
    """Raise DefNotSupportedException if defined entities are not supported.

    :param cloudapi_client CloudApiClient
    """
    if float(cloudapi_client.get_api_version()) < \
            def_constants.DEF_API_MIN_VERSION:
        raise excptn.DefNotSupportedException("Defined entity framework is not"
                                              " supported for {cloudapi_client.get_api_version()}")  # noqa: E501


def get_registered_def_interface():
    """Fetch the native cluster interface loaded during server startup."""
    from container_service_extension.service import Service
    return Service().get_kubernetes_interface()


def get_registered_def_entity_type():
    """Fetch the native cluster entity type loaded during server startup."""
    from container_service_extension.service import Service
    return Service().get_native_cluster_entity_type()


def generate_interface_id(vendor, nss, version):
    """Generate defined entity interface id.

    By no means, id generation in this method, guarantees the actual
    entity type registration with vCD.

    :param vendor (str)
    :param nss (str)
    :param version (str)

    :rtype str
    """
    return f"{def_constants.DEF_INTERFACE_ID_PREFIX}:{vendor}:{nss}:{version}"


def generate_entity_type_id(vendor, nss, version):
    """Generate defined entity type id.

    By no means, id generation in this method, guarantees the actual
    interface registration with vCD.

    :param vendor (str)
    :param nss (str)
    :param version (str)

    :rtype str
    """
    return f"{def_constants.DEF_ENTITY_TYPE_ID_PREFIX}:{vendor}:{nss}:{version}"  # noqa: E501
