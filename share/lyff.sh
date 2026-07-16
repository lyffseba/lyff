# Optional shell helpers — source from ~/.bashrc or ~/.zshrc:
#   source ~/lyff/share/lyff.sh
#
# Provides:
#   lyffcd <id>   cd into a project
#   lyff          passthrough if on PATH, else hub bin

_lyff_bin() {
  if command -v lyff >/dev/null 2>&1; then
    command lyff "$@"
  elif [ -x "${LYFF_ROOT:-$HOME/lyff}/bin/lyff" ]; then
    "${LYFF_ROOT:-$HOME/lyff}/bin/lyff" "$@"
  else
    echo "lyff not found; run: make -C ~/lyff install" >&2
    return 127
  fi
}

lyffcd() {
  local p
  p="$(_lyff_bin path "$1")" || return 1
  cd "$p" || return 1
  pwd
}

# Enable completion if available
if [ -n "${BASH_VERSION:-}" ] && [ -f "${LYFF_ROOT:-$HOME/lyff}/share/completions/lyff.bash" ]; then
  # shellcheck source=/dev/null
  . "${LYFF_ROOT:-$HOME/lyff}/share/completions/lyff.bash"
elif [ -n "${ZSH_VERSION:-}" ] && [ -f "${LYFF_ROOT:-$HOME/lyff}/share/completions/lyff.zsh" ]; then
  # shellcheck source=/dev/null
  fpath=("${LYFF_ROOT:-$HOME/lyff}/share/completions" $fpath)
  autoload -Uz compinit 2>/dev/null && compinit -C 2>/dev/null
  # shellcheck source=/dev/null
  . "${LYFF_ROOT:-$HOME/lyff}/share/completions/lyff.zsh" 2>/dev/null
fi
