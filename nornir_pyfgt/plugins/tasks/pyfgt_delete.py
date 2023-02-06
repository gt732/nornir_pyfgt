from typing import Any, Dict, List, Optional, AnyStr
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_delete(
    task: Task,
    url: AnyStr
) -> Result:
    """
    Delete an object from the Fortinet device using the fortigate api.

    Arguments:
        task (Task): Nornir task object
        url (AnyStr): REST API URL of the object to be deleted

    Returns:
        Result: Result object containing the result of the operation, with the host information.
            The operation returns a 'Response [200]' if the object is successfully deleted, or 'Response [404]' if the object is absent in the Fortinet device.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.fgt.delete(url=url)
    
    return Result(host=task.host, result=result)