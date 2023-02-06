from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_send_command(
    task: Task,
    command_string: str,
    **kwargs: Any
    
) -> Result:
    

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.ssh.send_command(command_string, **kwargs)
    
    return Result(host=task.host, result=result)