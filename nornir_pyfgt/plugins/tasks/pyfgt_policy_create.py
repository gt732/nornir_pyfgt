from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_policy_create(
    task: Task,
    data: Dict
) -> Result:
    """
    Creates fortigate-object policy in the Fortigate

    Arguments:
        task (Task): Nornir task object
        data: Data of the fortigate-object
        Returns:
        Result: Result response 200 or 500.
        *<Response [200]>* Object successfully created or already exists
        *<Response [500]>* Object already exist in the Fortigate
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    
    result = fgt_conn.policy.create(data)
    
    return Result(host=task.host, result=result)