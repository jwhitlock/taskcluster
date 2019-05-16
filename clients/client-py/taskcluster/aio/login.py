# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .asyncclient import AsyncBaseClient
from .asyncclient import createApiClient
from .asyncclient import config
from .asyncclient import createTemporaryCredentials
from .asyncclient import createSession
_defaultConfig = config


class Login(AsyncBaseClient):
    """
    The Login service serves as the interface between external authentication
    systems and Taskcluster credentials.
    """

    classOptions = {
    }
    serviceName = 'login'
    apiVersion = 'v1'

    async def ping(self, *args, **kwargs):
        """
        Ping Server

        Respond without doing anything.
        This endpoint is used to check that the service is up.

        This method is ``stable``
        """

        return await self._makeApiCall(self.funcinfo["ping"], *args, **kwargs)

    async def oidcCredentials(self, *args, **kwargs):
        """
        Get Taskcluster credentials given a suitable `access_token`

        Given an OIDC `access_token` from a trusted OpenID provider, return a
        set of Taskcluster credentials for use on behalf of the identified
        user.

        This method is typically not called with a Taskcluster client library
        and does not accept Hawk credentials. The `access_token` should be
        given in an `Authorization` header:
        ```
        Authorization: Bearer abc.xyz
        ```

        The `access_token` is first verified against the named
        :provider, then passed to the provider's APIBuilder to retrieve a user
        profile. That profile is then used to generate Taskcluster credentials
        appropriate to the user. Note that the resulting credentials may or may
        not include a `certificate` property. Callers should be prepared for either
        alternative.

        The given credentials will expire in a relatively short time. Callers should
        monitor this expiration and refresh the credentials if necessary, by calling
        this endpoint again, if they have expired.

        This method is ``experimental``
        """

        return await self._makeApiCall(self.funcinfo["oidcCredentials"], *args, **kwargs)

    funcinfo = {
        "oidcCredentials": {
            'args': ['provider'],
            'method': 'get',
            'name': 'oidcCredentials',
            'output': 'v1/oidc-credentials-response.json#',
            'route': '/oidc-credentials/<provider>',
            'stability': 'experimental',
        },
        "ping": {
            'args': [],
            'method': 'get',
            'name': 'ping',
            'route': '/ping',
            'stability': 'stable',
        },
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'Login']
