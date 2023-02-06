from typing import Any, Dict, List, Optional, AnyStr
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_get_url(
    task: Task,
    url: AnyStr
) -> Result:
    """
    Get information of the specified object from the Fortinet device using the api.

    Arguments:
        task (Task): Nornir task object
        url (AnyStr): REST API URL of the object to retrieve information from

    Returns:
        Result: Result object containing the result of the operation, with the host information.
            The result will be a list of dictionaries representing the objects data, or an empty list if the operation is not successful.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.fgt.get(url=url)
    
    return Result(host=task.host, result=result)