# massif-voice

A Claude Code skill that rewrites, adapts, or drafts prose so it reads as Will Thomson's own writing, which is Massif Capital's house voice. It was built from 42 of his published letters and papers, measured rather than described, and designed against the research on how AI prose differs from human prose and on how the Pangram 4 detector works.

Current version: see `CHANGELOG.md` and `metadata.version` in `SKILL.md`.

## Install

Clone into the Claude Code skills folder so the directory is named `massif-voice`:

```
git clone https://github.com/wmthomson22/massif-voice.git ~/.claude/skills/massif-voice
```

On Windows the folder is `C:\Users\<you>\.claude\skills\massif-voice`. Claude Code picks the skill up on the next session. If an older `massif-voice` is also installed (for example a synced copy from claude.ai), remove it so only one skill carries the name.

The measurement script needs Python 3.10 or later. It has no third-party dependencies and runs with `uv run scripts/style_check.py <draft.md>` or plain `python`.

## What is in the box

| Path | Purpose |
|---|---|
| `SKILL.md` | The skill: workflow, registers, the rules that matter, what to strip, detection guidance |
| `references/voice-profile.md` | The measured fingerprint of the corpus with verbatim examples |
| `references/ai-traits-and-detection.md` | What the literature review and the Pangram 4 report found, and the implications |
| `references/exemplars.md` | Verbatim passages grouped by the job they do |
| `scripts/style_check.py` | Compares a draft to the corpus profile and flags what is outside Will's band |
| `evals/` | Test cases in `claude plugin eval` layout |
| `CHANGELOG.md` | Version history and the review decisions behind each change |

## How the copies relate

The Claude app is the distribution channel. The `.skill` package built from this repo is uploaded there and the app syncs it to each machine's `~/.claude/skills/synced/` folder, where Claude Code loads it. This repo is the development clone and should not itself sit inside `~/.claude/skills` on a machine that also receives the synced copy, or the skill will load twice. The `massif-house-style` plugin in `wmthomson22/massif-claude-plugins` carries a copy of the same files for plugin installs; update it from this repo when a version ships.

Release steps: bump `metadata.version` in `SKILL.md`, add the entry to `CHANGELOG.md`, commit, tag `vX.Y.Z`, push with tags, build the `.skill` package (everything except `.git`, `evals/` and `.gitignore`, zipped under a `massif-voice/` root), upload it in the Claude app, and copy the skill files into the plugin repo.

## Updating the profile

If the corpus folder grows, recompute the targets and paste them into `TARGETS` in the script:

```
uv run scripts/style_check.py --corpus "<folder of his *.md pieces>"
```

Then bump the version in `SKILL.md` and `CHANGELOG.md`, commit, tag `vX.Y.Z`, and push with tags.

## Running the tests

From the skill directory, with Claude Code 2.1.269 or later:

```
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

The three cases are real, billed model runs.
