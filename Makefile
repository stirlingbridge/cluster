# Setup dev environment
dev:
	@echo Please run this command: source scripts/dev-setup.sh

build:  ./build/cluster

./build/machine:
	./sh/build-package.sh

lint:
	flake8

