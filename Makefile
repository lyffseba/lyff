# lyff hub — offline orchestration
.PHONY: help status doctor list docs install uninstall test test-cli validate bundle

LYFF := ./bin/lyff
PYTHON ?= python3

help:
	@echo "lyff hub"
	@echo "  make install    install 'lyff' to ~/.local/bin"
	@echo "  make status     portfolio status (offline)"
	@echo "  make doctor     toolchain + paths + registry"
	@echo "  make validate   registry validation only"
	@echo "  make list       registry table"
	@echo "  make docs       print docs index"
	@echo "  make test       unit tests (offline)"
	@echo "  make bundle     airplane tarball"
	@echo "  make test-cli   smoke the CLI"

status:
	$(LYFF) status

doctor:
	-$(LYFF) doctor

validate:
	$(LYFF) validate

list:
	$(LYFF) list

docs:
	$(LYFF) docs index

install:
	mkdir -p "$(HOME)/.local/bin"
	ln -sfn "$(CURDIR)/bin/lyff" "$(HOME)/.local/bin/lyff"
	@echo "Installed: $(HOME)/.local/bin/lyff"
	@command -v lyff >/dev/null && lyff version || \
	  echo "Run: export PATH=\"\$$HOME/.local/bin:\$$PATH\""

uninstall:
	rm -f "$(HOME)/.local/bin/lyff"
	@echo "Removed ~/.local/bin/lyff"

test:
	$(PYTHON) -m unittest discover -s tests -v

bundle:
	$(LYFF) bundle

test-cli: test
	$(LYFF) help >/dev/null
	$(LYFF) version
	$(LYFF) validate
	$(LYFF) list
	$(LYFF) status
	$(LYFF) path bet
	$(LYFF) docs offline | head -5
	@echo "CLI smoke OK"
