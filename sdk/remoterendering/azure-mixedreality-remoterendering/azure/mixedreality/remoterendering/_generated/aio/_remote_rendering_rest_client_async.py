# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import RemoteRenderingRestClientConfiguration
from .operations_async import RemoteRenderingOperations
from .. import models


class RemoteRenderingRestClient(object):
    """Describing the `Azure Remote Rendering <https://docs.microsoft.com/azure/remote-rendering/>`_ REST API for rendering sessions and asset conversions. 

All requests to these APIs must be authenticated using the Secure Token Service as described in the `Azure Remote rendering documentation chapter about authentication <https://docs.microsoft.com/azure/remote-rendering/how-tos/tokens>`_.

    :ivar remote_rendering: RemoteRenderingOperations operations
    :vartype remote_rendering: azure.mixedreality.remoterendering._generated.aio.operations_async.RemoteRenderingOperations
    :param endpoint: The endpoint to use e.g. https://remoterendering.eastus.mixedreality.azure.com. A list can be found at https://docs.microsoft.com/azure/remote-rendering/reference/regions.
    :type endpoint: str
    """

    def __init__(
        self,
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{endpoint}'
        self._config = RemoteRenderingRestClientConfiguration(endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.remote_rendering = RemoteRenderingOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "RemoteRenderingRestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
