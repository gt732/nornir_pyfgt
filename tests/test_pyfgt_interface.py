from nornir_pyfgt.plugins.tasks import pyfgt_interface



def test_pyfgt_interface(nr):
    result = nr.run(task=pyfgt_interface)
    device_result = result['FW-01'][0].result
    assert result['FW-01'].failed is False
    assert device_result[0]['ip'] == '10.255.1.1 255.255.255.0'