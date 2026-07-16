# bash completion for lyff
_lyff_projects() {
  lyff list 2>/dev/null | awk 'NR>2 {print $1}'
}

_lyff_docs() {
  local root
  root="$(lyff root 2>/dev/null)" || return
  compgen -W "$(ls "$root/docs"/*.md 2>/dev/null | xargs -n1 basename | sed 's/\.md$//')" -- "$1"
}

_lyff() {
  local cur prev
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"

  local cmds="status doctor list validate info path docs run foreach bundle registry root version help summary discover completion prep"

  if [[ ${COMP_CWORD} -eq 1 ]]; then
    COMPREPLY=( $(compgen -W "$cmds" -- "$cur") )
    return
  fi

  case "${COMP_WORDS[1]}" in
    info|path)
      COMPREPLY=( $(compgen -W "$(_lyff_projects)" -- "$cur") )
      ;;
    docs)
      COMPREPLY=( $(compgen -W "$(_lyff_docs "$cur")" -- "$cur") )
      ;;
    run)
      if [[ ${COMP_CWORD} -eq 2 ]]; then
        COMPREPLY=( $(compgen -W "$(_lyff_projects)" -- "$cur") )
      fi
      ;;
    completion)
      COMPREPLY=( $(compgen -W "bash zsh" -- "$cur") )
      ;;
    validate)
      COMPREPLY=( $(compgen -W "--schema" -- "$cur") )
      ;;
    status|list|summary)
      COMPREPLY=( $(compgen -W "--json" -- "$cur") )
      ;;
  esac
}
complete -F _lyff lyff
