# Changelog

All notable changes to the massif-voice skill. Versions follow semantic versioning: patch for wording and calibration fixes, minor for new rules or reference material, major for a change in how the skill is meant to be used. The version lives in two places that must agree: `metadata.version` in `SKILL.md` frontmatter and the top entry here.

## 1.0.2 (2026-11-01)

- The style-check invocation in SKILL.md no longer hardcodes a machine path. It names the skill folder generically and gives the plugin location (`${CLAUDE_PLUGIN_ROOT}/skills/massif-voice`) so the same file works as a direct install, as a Claude app upload, and inside the massif-house-style plugin.

## 1.0.1 (2026-11-01)

- Shortened the frontmatter description to under 1,024 characters so the skill packages for the Claude app (claude.ai), which enforces that limit. Triggers unchanged.

## 1.0.0 (2026-11-01)

First release of the corpus-built skill, replacing the rule-based massif-voice skill of 2026-08 to 2026-10.

Built from 42 published Massif Capital pieces (37 quarterly letters Q4 2016 to Q2 2026, 4 working papers and investment reports from 2026; 210,798 words, 9,122 sentences). Informed by "How AI Writes: A Critical Literature Review of Linguistic and Stylistic Traits" and the Pangram 4 Technical Report (Glickenhaus et al., 2026).

Contents:

- `SKILL.md`: workflow, input classification, three registers (letter, paper, personal), ten rules that most separate Will's prose from machine prose, a "Manufactured cleverness" section, the strip list, detection guidance, coordination notes.
- `references/voice-profile.md`: measured distribution (sentence length deciles, paragraph lengths, punctuation and stance rates) and the habits behind them, with verbatim examples.
- `references/ai-traits-and-detection.md`: what the literature review and the Pangram 4 report found, and what each finding implies.
- `references/exemplars.md`: verbatim passages by job (performance opening, admission of error, thesis opening, verdict, footnote, heading).
- `scripts/style_check.py`: measures a draft against the corpus profile; `--register personal` for posts and emails; `--corpus DIR` to recompute targets.
- `evals/`: three test cases in `claude plugin eval` layout (AI copper draft rewrite, Will's Enovix notes to a letter section, LinkedIn reaction to an FT article).

Decisions taken during review (three evaluation rounds, 2026-11-01):

- Hedging is sparse by design: first-person claim verbs ("we believe") stay, explicit hedges are capped at about one per section. Will's review: "I dont like that many personal hedges."
- The construction "we may be early, but we are not wrong" is retired in all forms and paraphrases at Will's request, although it appears in his past letters.
- Rhetorical gadgets (reveal clauses, self-commenting sentences, echo constructions, negative-definition zingers, semicolon-joined quips, dramatic one-line paragraphs) are struck on sight; each was flagged by Will in a test draft as obviously machine-written.
- Personal register (LinkedIn, email) is casual and plain, not a letter paragraph.
- Contraction target corrected from 12.4% to 1.7% of sentences after the first measurement was found to count possessives.
- "robust", "landscape", "comprehensive", "crucial" and "nuanced" removed from the strike list because Will uses them at roughly one per letter.

Dropped from the earlier skill: the opt-in Commentary Register (Grant toolkit) and the blader/humanizer-derived word list as a primary mechanism.
