# lyff hub — offline orchestration
.PHONY: help status doctor list docs install uninstall test-cli bundle

LYFF := ./bin/lyff

help:
	@echo "lyff hub"
	@echo "  make install   install 'lyff' to ~/.local/bin"
	@echo "  make status    portfolio status (offline)"
	@echo "  make doctor    toolchain + paths"
	@echo "  make list      registry table"
	@echo "  make docs      print docs index"
	@echo "  make bundle    airplane tarball"
	@echo "  make test-cli  smoke the CLI"

status:
	$(LYFF) status

doctor:
	$(LYFF) doctor || true

list:
	$(LYFF) list

docs:
	$(LYFF) docs index

install:
	mkdir -p "$(HOME)/.local/bin"
	ln -sfn "$(CURDIR)/bin/lyff" "$(HOME)/.local/bin/lyff"
	@echo "Installed: $(HOME)/.local/bin/lyff"
	@echo "Ensure PATH contains ~/.local/bin"
	@command -v lyff >/dev/null && lyff help | head -3 || \
	  echo "Run: export PATH=\"\$$HOME/.local/bin:\$$PATH\""

uninstall:
	rm -f "$(HOME)/.local/bin/lyff"
	@echo "Removed ~/.local/bin/lyff"

bundle:
	$(LYFF) bundle

test-cli:
	$(LYFF) help >/dev/null
	$(LYFF) list
	$(LYFF) status
	$(LYFF) path bet
	$(LYFF) docs offline | head -5
	@echo "CLI smoke OK"
