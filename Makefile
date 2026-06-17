.PHONY: validate

validate:
	./scripts/validate_docs.sh
	./scripts/validate_math_refs.sh
	./scripts/validate_agent_contracts.sh
