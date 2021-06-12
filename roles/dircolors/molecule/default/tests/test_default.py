import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_exists(host):
    assert host.file("/root/.dir_colors").exists


@pytest.mark.parametrize("conf", [
    "BLK 40;33;01",
    ".jpg 00;35",
    ".ogg 00;36",
])
def test_config_option(host, conf):
    assert host.file("/root/.dir_colors").contains(conf)
