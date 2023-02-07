from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_policy_delete(
    task: Task,
    **kwargs
) -> Result:
    """
    Deletes the fortigate-object from the Fortigate

    Arguments:
        task (Task): Nornir task object
        str uid: Identifier of the fortigate-object. Used to delete a single object
        :param list filter: Filters fortigate-objects by one or multiple conditions: equals "==",
            not equals "!=", contains "=@". Used to delete multiple objects
        :return: Session response
            *<Response [200]>* Object successfully deleted
            *<Response [404]>* Object absent in the Fortigate
    Returns:
        Result: Response 200 or 404.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    
    result = fgt_conn.policy.delete(**kwargs)
    
    return Result(host=task.host, result=result)