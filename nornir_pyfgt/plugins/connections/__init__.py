from typing import Any, Dict, Optional

from fortigate_api import FortigateAPI

from nornir.core.configuration import Config

CONNECTION_NAME = "pyfgt"


class Pyfgt:
    def open(
        self,
        hostname: Optional[str],
        username: Optional[str],
        password: Optional[str],
        platform: Optional[str],
        port: Optional[str] = 22,
        scheme: Optional[str] = 'http',
        timeout: Optional[int] = 15,
        verify: Optional[bool] = False,
        vdom: Optional[str] = 'root',
        ssh: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,
        extras: Optional[Dict[str, Any]] = None,
    ) -> None:
       parameters: Dict[str, Any] = {
            "host": hostname,
            "username": username,
            "password": password,
            "port": port,
            "ssh": ssh,
            "scheme:": scheme,
            "timeout": timeout,
            "verify": verify,
            "vdom": vdom,
        }
       
       connection = FortigateAPI(**parameters)
       
       self.connection = connection
       
    def close(self) -> None:
        self.connection.logout()