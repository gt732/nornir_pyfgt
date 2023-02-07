from typing import Any, Dict, List, Optional, AnyStr
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_put_url(
    task: Task,
    url: AnyStr,
    data: Dict
) -> Result:
    """
    Update information for the specified object on the Fortinet device using the API.

    Arguments:
    task (Task): Nornir task object
    url (AnyStr): REST API URL of the object to update
    data (Dict): Data to update the object with

    Returns:
    Result: Result object containing the result of the operation, with the host information.
    The result will be a dictionary representing the updated object data, or an empty dictionary if the operation is not successful.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.fgt.put(url=url, data=data)
    
    return Result(host=task.host, result=result)