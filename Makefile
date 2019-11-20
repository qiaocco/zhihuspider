lint: ## check style with flake8
	@echo "--> Linting python"
	black .
	@echo ""

sort: # sort import with isort
	@echo "--> Sort python imort"
	isort -rc .
	@echo ""