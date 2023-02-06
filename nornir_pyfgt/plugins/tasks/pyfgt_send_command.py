from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_send_command(
    task: Task,
    command: str,
    **kwargs: Any
    
) -> Result:
    """
    Sends a SSH command to the Fortigate device using Nornir.
    
    Arguments:
        task (Task): Nornir task object.
        command_string (str): The command to be sent.
        **kwargs (Any): Additional parameters to be passed to the `send_command` method.
    
    Returns:
        Result: Nornir result object containing the result of the command.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    
    result = fgt_conn.ssh.send_command(command, **kwargs)
    
    return Result(host=task.host, result=result)