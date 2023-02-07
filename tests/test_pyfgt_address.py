from nornir_pyfgt.plugins.tasks import pyfgt_address



def test_pyfgt_address(nr):
    result = nr.run(task=pyfgt_address)
    device_result = result['FW-01'][0].result
    assert result['FW-01'].failed is False
    assert device_result[6]['start-ip'] == '10.212.134.200'