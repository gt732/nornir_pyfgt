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
        scheme: Optional[str],
        port: Optional[str],
        timeout: Optional[int],
        verify: Optional[bool],
        vdom: Optional[str],
        ssh: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,
    ) -> None:
       parameters: Dict[str, Any] = {
            "host": hostname,
            "user": username,
            "password": password,
            "port": port,
            "ssh": ssh,
        }
       
       connection = FortigateAPI(**parameters)
       
       connection.login()
       
       self.connection = connection
       
    def close(self) -> None:
        self.connection.logout()