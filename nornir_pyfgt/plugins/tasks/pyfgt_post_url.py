from typing import Any, Dict, List, Optional, AnyStr
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_post_url(
    task: Task,
    url: AnyStr,
    data: Dict
) -> Result:
    """
    Create a new object on the Fortinet device using the REST API.

    Arguments:
    task (Task): Nornir task object
    url (AnyStr): REST API URL of the object to create
    data (Dict): Data of the object to be created

    Returns:
    Result: Result object containing the result of the operation, with the host information.
    The result will be a Response object from the session, with a 200 status code indicating a successful creation or an already existing object,
    or a 500 status code indicating that the object already exists in the Fortinet device.
    
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.fgt.post(url=url, data=data)
    
    return Result(host=task.host, result=result)