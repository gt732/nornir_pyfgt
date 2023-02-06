from typing import Any, Dict, List, Optional, AnyStr
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_delete(
    task: Task,
    url: AnyStr
) -> Result:

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.fgt.delete(url=url)
    
    return Result(host=task.host, result=result)