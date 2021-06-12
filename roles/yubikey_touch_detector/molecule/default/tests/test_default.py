import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_conf(host):
    f = host.file("/root/.config/yubikey-touch-detector/service.conf")
    assert f.exists
    assert f.contains("YUBIKEY_TOUCH_DETECTOR_VERBOSE=false")
    assert f.contains("YUBIKEY_TOUCH_DETECTOR_LIBNOTIFY=true")
