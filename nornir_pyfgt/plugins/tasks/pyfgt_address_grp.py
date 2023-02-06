from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_address_grp(
    task: Task
) -> Result:

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.address_group.get()
    
    return Result(host=task.host, result=result)