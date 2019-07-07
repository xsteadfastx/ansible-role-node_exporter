.PHONY: local-test

local-test:
	docker run --rm -ti --dns 192.168.10.1 -v $(CURDIR):/code/ansible-vwit-node_exporter -v /var/run/docker.sock:/var/run/docker.sock -w /code/ansible-vwit-node_exporter hub.ckc.de/vwit-infrastructure/ansible:latest molecule test
