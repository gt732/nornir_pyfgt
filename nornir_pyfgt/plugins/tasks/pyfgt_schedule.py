from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_schedule(
    task: Task
) -> Result:
    """
    Retrieve firewall schedule configuration from a Fortinet device using the api path "api/v2/cmdb/firewall.schedule/onetime/"

    Arguments:
        task (Task): Nornir task object

    Returns:
        Result: Result object containing the result of the operation, with the firewall schedule information.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.schedule()
    
    return Result(host=task.host, result=result)