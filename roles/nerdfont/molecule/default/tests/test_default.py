import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("font", [
    "DejaVu Sans Mono Nerd Font Complete",
    "DejaVu Sans Mono Nerd Font Complete Mono",
])
def test_font_files_exist(host, font):
    assert host.file(f"/root/.fonts/{font}.ttf").exists
