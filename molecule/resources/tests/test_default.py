import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_remove_node_exporter_dist_package(host):
    assert host.package("prometheus-node-exporter").is_installed is False


def test_install_deps(host):
    assert host.package("tar").is_installed is True


def test_installed_node_exporter(host):
    node_exporter_binary = host.file("/usr/local/bin/node_exporter")

    assert node_exporter_binary.exists is True
    assert node_exporter_binary.is_file is True


def test_node_exporter_version(host):
    cmd = host.run("/usr/local/bin/node_exporter --version")

    assert "0.18.1" in cmd.stderr


def test_remove_install_files(host):
    assert host.file("/tmp/node_exporter-0.18.1.linux-amd64").exists is False


def test_service(host):
    service = host.service("node_exporter")

    assert service.is_running is True
    assert service.is_enabled is True
