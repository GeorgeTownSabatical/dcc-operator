.PHONY: validate
.PHONY: reports

validate:
	./scripts/validate_docs.sh
	./scripts/validate_math_refs.sh
	./scripts/validate_agent_contracts.sh
	python3 scripts/validate_operational_manifests.py
	python3 scripts/generate_readiness_report.py --check

reports:
	python3 scripts/generate_readiness_report.py
