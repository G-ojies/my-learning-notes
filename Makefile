# ChainSentry: Developer Experience (DevEx)
# Research Notes: Standardizing command execution for the repository.

.PHONY: help start test fuzz backup clean

help:
	@echo "🛡️ ChainSentry Developer Commands:"
	@echo "  make start   - Launch the FastAPI backend and Mempool Monitor"
	@echo "  make test    - Run the Pytest suite"
	@echo "  make fuzz    - Run the Chaos Fuzzer against the parsers"
	@echo "  make backup  - Create a safe snapshot of the SQLite database"
	@echo "  make clean   - Remove pycache and temporary test files"

start:
	python3 chainsentry_integration.py

test:
	pytest test_chainsentry.py -v

fuzz:
	python3 fuzz_mempool.py

backup:
	python3 db_backup_manager.py

clean:
	rm -rf __pycache__ .pytest_cache
	@echo "✅ Cleaned up temporary files."
