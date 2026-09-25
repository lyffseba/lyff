# Stack

**Reviewed:** 2026-09-25

Toolchain for the lyff hub tip: what this repository actually runs, the latest stable upstream release for each tool, and where the repo has drifted from those releases.

`lyff docs stack` prints this page. Nested products keep their own dependency pins.

## Pin rules

A pin is the newest **final** release the upstream project ships for general use, with the official docs for that release.

These upstream lines were current on the review date and stay off the pin table until they ship as stable:

| Upcoming | Status on 2026-09-25 |
|----------|----------------------|
| Python 3.15 | Prerelease. Final release planned 2026-10-01 ([PEP 790](https://peps.python.org/pep-0790/)). |
| Git 2.56.0-rc1 | Release candidate, announced 2026-09-16. |
| Node.js 26.10.0 | Current channel. The production pin is Active LTS. |
| GNU Make 4.4.90 | Development snapshot on the Make git tip. |

Node.js is pinned to **Active LTS**. npm is pinned to the copy bundled in that Node release (`deps/npm/package.json` on the tag), which is the npm `lyff doctor` and `lyff prep` invoke.

CI selectors stay in `.github/workflows/ci.yml`. A docs review updates the drift table; a version bump is its own change.

## Two tiers

| Tier | Required to | What "missing" means |
|------|-------------|----------------------|
| Hub runtime | `./bin/lyff`, `make test`, CI | Hub commands or CI fail. |
| Portfolio probes | Nothing in the hub itself | `lyff doctor` says "not found". Its header is "presence only; missing tools are fine if unused". `lyff prep` only prints the checklist. |

## Hub runtime

These are invoked by `bin/lyff`, the Makefile, `share/`, tests, or CI.

| Tool | Stable pin | Released | Official docs |
|------|------------|----------|---------------|
| Python | **3.14.7** | 2026-08-05 | [docs.python.org/3.14](https://docs.python.org/3.14/) · [release](https://www.python.org/downloads/release/python-3147/) · [status](https://devguide.python.org/versions/) |
| PyYAML | **6.0.3** | 2025-09-25 | [PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation) · [PyPI](https://pypi.org/project/PyYAML/6.0.3/) · [changelog](https://github.com/yaml/pyyaml/blob/6.0.3/CHANGES) |
| pip | **26.2.1** | 2026-08-04 | [pip.pypa.io](https://pip.pypa.io/en/stable/) · [news](https://pip.pypa.io/en/stable/news/) |
| Git | **2.55.0** | 2026-06-29 | [git-scm.com/docs](https://git-scm.com/docs) · [site](https://git-scm.com/) |
| GNU Make | **4.4.1** | 2023-02-26 | [manual](https://www.gnu.org/software/make/manual/) · [tarball](https://ftp.gnu.org/gnu/make/make-4.4.1.tar.gz) |
| Bash | **5.3 patch 15** | 5.3 on 2025-07-30; patch 15 on 2026-06-09 | [manual](https://www.gnu.org/software/bash/manual/) · [status](https://tiswww.case.edu/php/chet/bash/bashtop.html) · [bash53-015](https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-015) |
| actions/checkout | **v7.0.1** | 2026-07-17 | [README](https://github.com/actions/checkout/blob/v7.0.1/README.md) · [releases](https://github.com/actions/checkout/releases) |
| actions/setup-python | **v7.0.0** | 2026-07-20 | [README](https://github.com/actions/setup-python/blob/v7.0.0/README.md) · [releases](https://github.com/actions/setup-python/releases) |
| GitHub-hosted Ubuntu | **24.04** via `ubuntu-latest` today | 26.04 image GA 2026-09-17 | [runner images](https://github.com/actions/runner-images#available-images) · [migration note](https://github.blog/changelog/2026-09-17-ubuntu-26-generally-available-and-latest-migration/) |

### Python

`bin/lyff` is `#!/usr/bin/env python3`. CI asks for `3.12` (see drift). `make test` runs `python3 -m unittest`.

The CLI stays on the standard library except for an optional PyYAML import. Library pages to re-read when the Python pin moves:

| Module | Used for |
|--------|----------|
| `json` | `--json`, registry cache, bundle `MANIFEST.json` |
| `pathlib` | Hub root, project paths, docs lookup |
| `subprocess` | `git`, doctor probes, `lyff run` |
| `tarfile` | `lyff bundle` |
| `unittest`, `tempfile` | `tests/test_lyff_cli.py` |
| `importlib` | Tests load `bin/lyff` (no `.py` suffix) |

`typing`, `os`, `sys`, and `time` are also imported. There is no `requirements.txt` and no pinned interpreter file (no `.python-version`).

3.14 is in bugfix until 2030-10 ([PEP 745](https://peps.python.org/pep-0745/)). 3.13 is also in bugfix (latest patch 3.13.15, 2026-08-05). 3.12 is security-only until 2028-10; its newest patch is 3.12.14 (2026-08-12).

### PyYAML

`load_raw_registry()` calls `yaml.safe_load`. On any import or parse failure it falls back to a line parser, then to `.lyff/registry.json` if that cache exists. CI installs it with `pip install pyyaml` and no version specifier.

6.0.3 declares Python `>=3.8` and is the release that added 3.14 support. PyYAML's safe loader implements YAML 1.1 ([spec](https://yaml.org/spec/1.1/)).

### pip

CI is the only hub call to pip (`pip install pyyaml`). `lyff prep` also prints a pip line for ents, run inside that project's venv, not the hub.

### Git

`bin/lyff` shells out to `git -C <dir>` for status, branch, and `HEAD` subject. It does not fetch. `lyff doctor` runs `git --version`. Nested checkouts are separate repositories, not submodules.

### GNU Make

The hub Makefile is GNU Make (`:=`, `$(CURDIR)`, `.PHONY`). `lyff doctor` runs `make --version`. `lyff prep` for project `43` is `make -C libft bonus`. 4.4.1 is still the newest stable tarball; the 2023 date is the upstream release date.

### Bash

`lyff run` executes registry commands and `lyff run <id> -- …` through `bash -lc`. `share/lyff.sh` is written for bash and zsh. Completion lives in `share/completions/lyff.bash`.

Patch 15 is `bash53-015` on the GNU patch series. `bash --version` on a patched build reports `5.3.15`.

### GitHub Actions

`.github/workflows/ci.yml` runs on `ubuntu-latest` for `push` and `pull_request` to `main`. The job checks out the repo, sets up Python, installs PyYAML, runs unittest, then smokes `./bin/lyff`.

`ubuntu-latest` is Ubuntu 24.04 on this review date. Ubuntu 26.04 is generally available, and GitHub will move the `ubuntu-latest` label to 26.04 between **2026-10-19** and **2026-11-19**. Until that window finishes, a workflow that says `ubuntu-latest` still lands on 24.04. Pinning `ubuntu-24.04` is what keeps the image stable through the migration; pinning `ubuntu-26.04` is what opts in early. This docs change leaves the workflow label as it is.

## Optional shell

| Tool | Stable pin | Released | Where the tip uses it | Docs |
|------|------------|----------|------------------------|------|
| zsh | **5.9.2** | 2026-07-12 | `share/lyff.sh` and `share/completions/lyff.zsh` when `ZSH_VERSION` is set | [releases](https://zsh.sourceforge.io/releases.html) · [tarball](https://www.zsh.org/pub/zsh-5.9.2.tar.xz) |

Hub commands and CI run without zsh.

## Portfolio probes

`lyff doctor` runs the version command and treats a non-zero exit as "not found". `lyff prep` prints these steps and does not run them. Nothing in the hub pins their versions.

| Tool | Stable pin | Released | Doctor argv | Prep / registry use | Docs |
|------|------------|----------|-------------|---------------------|------|
| Node.js LTS | **24.21.0** | 2026-09-08 | `node -v` | Projects `44` and the prep line for `rugs` install via npm | [v24 API](https://nodejs.org/docs/latest-v24.x/api/) · [release](https://nodejs.org/en/blog/release/v24.21.0) |
| npm | **11.19.0** | bundled in Node 24.21.0 | `npm -v` | prep: `npm install` for `rugs` and `44`. Registry `44` commands: `npm run dev`, `npm run install-cli` | [docs.npmjs.com](https://docs.npmjs.com/) · [tag's package.json](https://github.com/nodejs/node/blob/v24.21.0/deps/npm/package.json) |
| Rust / Cargo | **1.98.1** | 2026-09-03 | `cargo -V` | prep: `cargo fetch && cargo build --release`. Registry `bet`: `cargo build --release`, `cargo run --release` | [Rust book](https://doc.rust-lang.org/stable/book/) · [Cargo book](https://doc.rust-lang.org/cargo/) · [1.98.1](https://blog.rust-lang.org/2026/09/03/Rust-1.98.1/) |
| Go | **1.27.1** | 2026-08-28 | `go version` | prep: `go mod download && make build` for `witness`. Registry test is `make test` | [go.dev/doc](https://go.dev/doc/) · [go1.27 notes](https://go.dev/doc/go1.27) · [dl](https://go.dev/dl/) |
| pixi | **0.81.0** | 2026-09-15 | `pixi --version` | prep: `pixi install && pixi run test`. Registry `maxi` test: `pixi run test` | [pixi.prefix.dev/latest](https://pixi.prefix.dev/latest/) · [v0.81.0](https://github.com/prefix-dev/pixi/releases/tag/v0.81.0) |
| GCC as `cc` | **16.2** | 2026-08-07 | `cc --version` | Doctor only. C projects `43` and `421` build with `make` | [gcc.gnu.org](https://gcc.gnu.org/) · [GCC 16 changes](https://gcc.gnu.org/gcc-16/changes.html) |

`cc` is whatever the system puts on `PATH`. The reference compiler for this pin is GCC 16.2, the newest maintained GCC release series (regression fixes only as of 2026-08-07).

`lyff prep` still prints a `rugs` npm step. `registry.yaml` has no `rugs` entry. That checklist line is unchanged by this page.

## Registry labels

`registry.yaml` `stack:` values name nested projects. Hub commands reach them only through the tool in the last column:

| Label | Projects | How the hub meets them |
|-------|----------|------------------------|
| `c` | `43`, `421` | `make` in prep and registry commands. `cc` is a doctor probe only. |
| `php` | `421` | No hub command. |
| `python` | `421`, `ents` | Hub interpreter, plus the ents prep venv. |
| `node` | `44` | `npm` probe and prep. |
| `three` | `44` | A library `npm install` would fetch inside `44`. |
| `rust` | `bet` | `cargo`. |
| `mojo`, `jax` | `ents` | No hub command. Ents prep installs Python packages into `.venv`. |
| `mojo`, `max` | `maxi` | `pixi run test`. |

## Drift

Repo record versus the pins above, on 2026-09-25. "Behind" means the committed selector tracks an older release line. "Unpinned" means the tip invokes the tool and commits no version. "Floating" means a label whose meaning upstream changes without a commit here.

| Tool | Repo record | File | Versus stable pin |
|------|-------------|------|-------------------|
| Python | `python-version: "3.12"` | `.github/workflows/ci.yml` | **Behind.** `3.12` installs the newest 3.12 patch (3.12.14, security-only). Stable pin is 3.14.7. |
| PyYAML | `pip install pyyaml` | `.github/workflows/ci.yml` | **Unpinned.** Latest stable is 6.0.3. |
| pip | `pip install` with no `pip==` | `.github/workflows/ci.yml` | **Unpinned.** Latest stable is 26.2.1. |
| actions/checkout | `actions/checkout@v4` | `.github/workflows/ci.yml` | **Behind.** `@v4` tracks v4 (newest v4.4.0, 2026-07-16). Current major is v7.0.1. |
| actions/setup-python | `actions/setup-python@v5` | `.github/workflows/ci.yml` | **Behind.** `@v5` tracks v5 (newest v5.6.0, 2026-04-24). Current major is v7.0.0. |
| Ubuntu runner | `runs-on: ubuntu-latest` | `.github/workflows/ci.yml` | **Floating.** Today that label is Ubuntu 24.04. It moves to 26.04 between 2026-10-19 and 2026-11-19. |
| Git, Make, Bash | no version | `bin/lyff`, `Makefile`, `share/` | **Unpinned.** Doctor and the shell use `PATH`. |
| zsh | no version | `share/lyff.sh`, `share/completions/lyff.zsh` | **Unpinned.** |
| Node.js, npm, Cargo, Go, pixi, `cc` | no version | `bin/lyff` doctor and prep | **Unpinned.** Presence checks only. |

The columns above quote committed selectors. A machine's `python3 --version` sits outside this table.

## Keeping this page current

Update this file in the same change that adds or removes a tool from `bin/lyff` doctor, `lyff prep`, the Makefile, `share/`, or `.github/workflows/ci.yml`. Otherwise re-review at least once a quarter, and again when one of the dated events below lands:

- Python 3.15 final (planned 2026-10-01)
- `ubuntu-latest` migration window (2026-10-19 through 2026-11-19)
- Git 2.56.0 final (2.56.0-rc1 exists)

Checklist:

1. Open each URL in the tables above and the [status pages](#pin-rules).
2. Replace a pin only when the new release is a final stable (Active LTS for Node.js). Record the release date from the upstream page.
3. Rebuild the drift table from the files named there. Quote the selector the file actually contains.
4. Set **Reviewed** at the top to the review date.
5. Leave CI selectors alone in a docs-only pass.

`lyff doctor` remains the offline check that the tools exist. It does not compare versions to this page.
