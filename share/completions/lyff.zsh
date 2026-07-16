#compdef lyff

_lyff() {
  local -a cmds projects docs
  cmds=(
    'status:Nested repo status'
    'doctor:Toolchain + registry health'
    'list:Registry table'
    'validate:Validate registry'
    'info:JSON project details'
    'path:Absolute path'
    'docs:Print documentation'
    'run:Run project command'
    'foreach:Shell in every project'
    'bundle:Airplane tarball'
    'summary:One-screen portfolio dashboard'
    'discover:Find unregistered git dirs'
    'prep:Offline dependency checklist'
    'completion:Shell completion script'
    'registry:Registry path'
    'root:Hub root'
    'version:CLI version'
    'help:Help'
  )

  if (( CURRENT == 2 )); then
    _describe 'command' cmds
    return
  fi

  case $words[2] in
    info|path|run)
      projects=(${(f)"$(lyff list 2>/dev/null | awk 'NR>2 {print $1}')"})
      _describe 'project' projects
      ;;
    docs)
      local root
      root=$(lyff root 2>/dev/null) || return
      docs=(${(f)"$(ls $root/docs/*.md 2>/dev/null | xargs -n1 basename | sed 's/\.md$//')"})
      _describe 'topic' docs
      ;;
    completion)
      _values 'shell' bash zsh
      ;;
    status|list|summary)
      _values 'flags' --json
      ;;
    validate)
      _values 'flags' --schema
      ;;
  esac
}

compdef _lyff lyff
