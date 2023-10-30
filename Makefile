.PHONY: build
build:
	docker build -f ./docker/Dockerfile.model -t fernapi/fern-go-model .
	docker build -f ./docker/Dockerfile.sdk -t fernapi/fern-go-sdk .
	docker build -f ./docker/Dockerfile.fiber -t fernapi/fern-go-fiber .
	docker tag fernapi/fern-go-sdk fernapi/fern-go-sdk:0.0.0

.PHONY: generate
generate: install
	cd internal/fern; fern-go-model ir_config.json

.PHONY: install
install:
	go install ./cmd/...

.PHONY: test
test: install
	go test ./...
	npm install -g @fern-api/seed-cli@0.15.0-rc47
	seed test --workspace sdk --fixture response-property
	seed test --workspace sdk --fixture file-upload

.PHONY: fixtures
fixtures: install
	@./scripts/update-fixtures.sh
