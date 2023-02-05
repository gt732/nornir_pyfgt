from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_send_command(
    task: Task,
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    result = device.facts
    return Result(host=task.host, result=result)