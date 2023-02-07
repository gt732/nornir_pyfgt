from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_virtual_ip(
    task: Task
) -> Result:
    """
    Retrieve virtual ip configuration from a Fortinet device using the api path "api/v2/cmdb/firewall/vip/"

    Arguments:
        task (Task): Nornir task object

    Returns:
        Result: Result object containing the result of the operation, with the virtual ip information.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.virtual_ip.get()
    
    return Result(host=task.host, result=result)