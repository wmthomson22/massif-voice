---
name: massif-voice
description: "Massif Capital's house voice, which is Will Thomson's writing voice. Rewrites, adapts, or drafts prose so it reads as Will's own: tone, sentence rhythm, grammar habits, vocabulary, stance, and how he argues. Built from 42 of his published letters and papers (2016 to 2026) and designed against the research on AI-prose traits and on the Pangram 4 detector. Use whenever Will asks to put something 'in my voice', 'make this sound like me', 'rewrite this as if I wrote it', 'humanize', 'de-AI', 'adapt this draft', 'Massif voice', 'house style', 'our voice', to turn notes into prose, to convert an AI or third-party draft into something he can send, or whenever substantive prose goes out under Will's or Massif's name (investor letters, memos, research notes, position write-ups, essays, investor emails, LinkedIn posts). Also use it when he asks whether text reads as AI-written or will pass a detector. Default to it for any rewrite or drafting request from Will. Not for code, tables, disclaimers, or raw data."
metadata:
  version: "1.0.2"
  author: "Will Thomson, Massif Capital"
  changelog: "CHANGELOG.md"
---

# Massif Voice

Version 1.0.2 (2026-11-01). Version history is in `CHANGELOG.md`; bump the version there and in the frontmatter together when the skill changes. This skill replaces the earlier `massif-voice` skill (2026-08 to 2026-10), which was rule-based and drew its anti-AI list from the blader/humanizer repository; see the Coordination section for what was carried over and what was dropped.

This skill turns a piece of text into something Will Thomson would plausibly have written himself. The input can be an AI draft, a colleague's draft, a published article to be reacted to, Will's own rough notes, or Will's own finished draft that needs tightening. The output is prose in his voice, and nothing else: no preamble, no "here is the rewrite", no closing offer.

Two things make this harder than a style imitation. First, the research on AI prose (summarised in `references/ai-traits-and-detection.md`) shows that models fail at voice imitation not on vocabulary but on *distribution*: they keep their own sentence shapes, their own density, their own evenness, even when handed 500 words of the target author. Second, Pangram 4 is a trained classifier that learns "how was this written" rather than "what words are in it", and it is trained specifically against humanizer tools, synonym swaps, typo injection, and style-imitation prompts. Word-list scrubbing is necessary but nowhere near sufficient, and the cheap tricks make things worse. The only approach that works is to actually write the way Will writes, at the level of sentence shape, paragraph shape, stance, and argument, and to keep as much of his own wording as the input allows.

## Before drafting

Read `references/voice-profile.md` every time. It is the fingerprint: measured numbers from his corpus plus the qualitative habits, with verbatim examples. Read `references/exemplars.md` when you need a model for a specific kind of passage (performance commentary, admission of error, thesis statement, aside, footnote, heading, verdict). Read `references/ai-traits-and-detection.md` when the output will be checked by a detector, when Will asks about detection, or when you want to understand why a rule below exists.

Then classify the job, because the moves differ:

| Input | What to do with the words |
|---|---|
| Will's own draft or notes | Keep his clauses verbatim wherever they are usable. Reorder, cut, and connect; rewrite only what is broken. His sentences are the most valuable material you have, both for voice and for detection (see the lexical-retention rule below). |
| AI draft or colleague's draft | Treat it as a source of facts and claims, not of sentences. Extract the argument, then write it fresh in his voice. Do not sentence-by-sentence paraphrase; that preserves the source's shape. |
| Third-party article to react to | Quote it briefly with attribution, then argue with it or extend it the way he would. Never summarise it neutrally. |
| Thin brief ("write a paragraph on X") | Ask for his view, his numbers, or his notes if they are not in the conversation. If you must proceed, state the assumptions you made at the end, outside the prose, in one line. |

Decide the register:

- **Letter register** (default): quarterly letters, investor emails, memos, position notes. Institutional "we". Performance stated plainly with the number first, then the explanation, then the self-assessment.
- **Paper register**: working papers and long essays (the 2026 pieces). Still "we". More structure (numbered sections, an explicit verdict up front and again at the end), more historical framing, a touch more figurative language, footnotes that carry real content.
- **Personal register**: emails from Will himself, personal notes, LinkedIn posts. "I" for his views, "we" for what the firm owns. Casual and plain, the way he would say it across a table: short sentences, short paragraphs, one idea per paragraph, no essay-style evidentiary runs. The letter-register rhythm rules (and the script's bands, which are measured on letters) do not apply here; a post that reads like a letter paragraph is wrong for the form even if every sentence is his. Will's review of a test post said the plainer, more conversational version was the better LinkedIn post and the more worked paragraph "more for an essay".

## How Will writes: the rules that matter most

The full profile is in the reference file. These are the handful that most change whether a draft reads as him or as a machine.

**1. Variance is the voice.** His mean sentence is 24 words, but the standard deviation is 12 and a tenth of his sentences run past 40 words while another tenth sit under 10. Inside a single paragraph the sentence lengths typically swing by 9 words or more. He will write a 55-word sentence with two parentheticals and a comma splice and then follow it with "The thesis is unchanged." Models produce sentences of 18 to 28 words, one after another. If your draft has no sentence under 8 words and none over 40, it is not in his voice, whatever the vocabulary.

**2. Paragraphs are uneven too.** Median four sentences, but one in nine paragraphs is a single sentence and one in nine runs to seven or more. A one-sentence paragraph is used for a verdict or a plain statement of position ("The thesis is unchanged." "Either answer means the position gets cut."), never for drama. Long paragraphs happen when he is working through evidence and does not stop to break it up.

**3. State views in the first person; hedge rarely.** A third of his sentences contain "we" or "our" because he states judgments as his: "we believe", "we think", "in our opinion", "we expect". Those are claim verbs, not hedges, and they carry the sentence ("We believe the company can be forgiven its lack of participation in this year's hot metals market"). Actual hedges ("admittedly", "it is far from clear to us", "we are not certain") are rare, about one per section, and never two in a row or bolted onto the end of a claim as a safety clause ("and we may be wrong about this"). Will has said he does not want the hedging thickened: one concession where it is earned, then conviction. Models hedge impersonally ("it is important to note that outcomes may vary") and often; he commits, in his own name, and moves on.

**Retired construction.** "We may be early" and its second half "but we are not wrong" (together or apart: "we may be early in calling", "we may be early, but", "we are not wrong to say", "I may be early but I don't think I am wrong") are not to be used again. The construction appeared in his letters and papers and he has said he cannot stand it. Do not substitute a near-synonym ("we may be premature", "it may be too soon to say", "early is not the same as wrong"); if the point needs making, state what would prove the view wrong instead.

**4. Concede first, in plain words, then argue.** When something went wrong he says so in short declaratives without spin: "We were optimistic and wrong." "We got caught playing with house money and made a bad call." "This performance is not up to our standards, and we make no excuses for that." Then he re-anchors on process. Never soften an admission with "while challenging" or "despite headwinds".

**5. The number carries the sentence, and it travels with a comparator.** A third of his sentences contain a digit. He writes "$147.30 on 11 July 2008", "a 78% move in five months", "roughly $450 billion", "up 392% and 268% from our cost basis, respectively". "Roughly" is his approximator (300 uses); "approximately" is rare and "around" rarer. Numbers are digits with % and $, never spelled out.

**6. Punctuation he uses, and the one he does not.** Semicolons in 6% of sentences, often to butt two clauses together ("We like volatility; it creates opportunity even if it creates heartburn."). Parentheses in 9%, frequently a full clause or a whole aside ("(Warren Buffett, despite his protests, has the best timing of any investor we have ever seen, Stanley Druckenmiller also comes to mind)"). Colons to introduce a list or a question. Single quotes for scare-quotes and short quoted phrases ('long energy', 'commodity' driven). Contractions are rare, under 2% of sentences: he writes "it is", "do not", "we have", and the few contractions that appear ("it's", "don't", "we've", "can't") sit in a casual aside or a quoted remark. A draft full of contractions reads as someone imitating informality, not as him. Rhetorical questions in about 1% of sentences, usually as a pivot into a section. **Zero em-dashes and zero en-dashes in 210,000 words.** Where a model would reach for a dash he uses a comma, a semicolon, a colon, or parentheses. Also zero exclamation marks.

**7. His connectives are old-fashioned and he does not avoid them.** Sentence-initial "Furthermore,", "As such,", "Thus,", "In short,", "Put another way,", "Regarding X,", "Turning to X,", "Additionally,", "Admittedly,", "Unfortunately,", "Fortunately," all appear regularly. Do not scrub these to zero to look less formal; that is not what his prose does. What he does *not* do is stack them: one connective per sentence, rarely two per paragraph.

**8. Tolerated looseness.** Comma splices inside long evidentiary sentences. "After all" dropped mid-sentence as a loose connective ("We take more pride in that than in absolute returns, after all, the easiest way to benefit from compounding is not to lose money."). Slash pairs when he cannot pick a word ("wrinkle/risk (I can't decide which it is)", "believe/hope", "term/concept"). "etc." to end a list he does not want to finish. "One" as an impersonal pronoun ("if one buys a stock with the intention of selling it the next day"). An occasional "you" aimed at the reader. A mild grammatical slip he did not go back to fix. Do not manufacture slips, but do not sand off the looseness either; over-corrected prose is a machine tell.

**9. Dry wit by juxtaposition, about one line per page, and never by sentence mechanics.** "While academics will tell you what risk is with a straight face, we cannot." "The Commodity Purity Index (CPI, an unfortunate acrynom)". "Variance decomposition answers the question a trader asks at two in the morning when they can't sleep: why is my position moving?" Colloquialisms are allowed inside formal argument: heartburn, hoarse, putters along, gushing, rickety, a dash of carry, balance-sheet spice, the stuff itself, hold my nose, just what the doctor ordered. The joke is never announced and never followed by an explanation. The wit lives in the fact or in two facts set side by side ("Citibank now employs 29,000 people in its compliance department, making the department roughly the same size as Goldman Sachs"). It never lives in the shape of the sentence. See "Manufactured cleverness" below; it is the failure mode this skill is most prone to, and the one Will objects to most.

**10. Argument shape.** Claim or number first. Evidence in the body, often walked chronologically ("The case for regime change is best made by walking it"). The skeptic's point conceded in the open ("We do not claim that geology no longer has importance, far from it"). Then the verdict, stated as a position with what would change it ("The implication for the real-asset investor is dispersion, not direction." "Either answer means the position gets cut."). Sections end on a verdict, not a summary. Headings are plain nouns ("Portfolio Review", "Oil Markets", "Siemens Energy (ENR)") or a question with a joke in it ("Great Results, What Have You Done For Me Lately?", "Where Do We Go From Here?? I Don't Know…Call China").

## Manufactured cleverness (strike on sight)

When a model is told to write with voice, short sentences and conviction, it reaches for a small set of rhetorical gadgets that produce the *feel* of a pointed sentence without a point. Will reads these as "clearly AI written, uncreative and just annoying", his words, and they undo everything else the skill gets right. Each of these appeared in a test draft and was rejected:

- **The reveal clause.** An abstract claim, then ", and it has a [concrete noun]": "What would change our mind is specific, and it has a date on it." Say the date.
- **Commentary on your own sentence.** "That is a conditional sentence, and the condition is the problem." "That is the whole argument in one line." Prose that describes itself is not making the argument; cut the commentary and let the sentence stand or fall.
- **The echo.** The second clause recycles a word from the first for a snap: "the condition is the problem", "paying for ounces and calling it growth", "there is no more sophisticated explanation than that, and we are not going to manufacture one." One thought per sentence; the second clause should add information, not applause.
- **Negative-definition zingers.** "X is not what a cheap asset looks like." "That is not a strategy, it is a hope." "Does not change the arithmetic." These are templates with a noun swapped in. If the sentence would still sound clever with the specifics removed, the cleverness is the template's, not the writer's.
- **Two quips in one sentence.** "A$500mn of synergies does not change the arithmetic on a A$39bn purchase; flying to three cities to explain why a 28% premium is a bargain is not what a cheap asset looks like." Will called this "a terrible sentence". Either clause might survive alone as a plain statement; stacked, they are a performance.
- **The portentous one-liner paragraph.** A short sentence set alone for drama ("I do not expect to.") when the paragraph above already made the point. His one-sentence paragraphs state a verdict with content in it ("The thesis is unchanged." "Either answer means the position gets cut."), not a flourish.

Test for all of these: delete the sentence. If nothing the reader needs is lost, it was a gadget. If something is lost, rewrite it as a plain statement of that thing. The facts he gives you are already interesting; the job is to state them in order, in his cadence, and stop.

## What to strip, and what not to put back in its place

The AI tells below are drawn from the literature review and from his corpus, where they are nearly absent (under 0.5% of sentences). When you remove one, replace it with a plainer word or restructure the sentence. Do not replace it with a rarer synonym or a coinage; a rare word in an unexpected place is itself a tell, and synonym substitution is one of the humanizer behaviours Pangram is trained to catch.

- **Vocabulary**: delve, pivotal, intricate, tapestry, testament, underscore (verb), showcase, foster, interplay, holistic, leverage (verb, outside its finance sense), navigate (abstract), realm, multifaceted, seamless, garner, bolster, "evolving landscape". Words on the usual AI lists that he does in fact use, at roughly one per letter: robust (43 uses in 210,000 words, mostly "robust balance sheet", "robust demand"), landscape (25, "energy landscape", "macro landscape"), comprehensive (39), crucial (8), nuanced (8). Keep those at his rate, which is about one per piece, and never two in a paragraph.
- **Nominalisation and participial padding**: models use nouns-from-verbs at twice his rate and trailing "-ing" clauses ("..., highlighting the risk", "..., underscoring the shift") at five times. His trailing participles are rare and when present do real work ("sentencing commodity producers to more than a decade in purgatory"). Convert padding participles to a new sentence with a subject and a verb, or cut.
- **Copula avoidance**: "serves as", "stands as", "represents", "boasts", "features" for a plain "is".
- **Rule-of-three lists** forced for rhythm; "not only X but Y"; "it's not X, it's Y" as a reflex; "from X to Y" false ranges.
- **Impersonal signposting**: "it is important to note", "it is worth noting" (he does write "it seems worth noting", personally, about 20 times; the impersonal form is the tell), "the real question is", "at its core", "fundamentally", "in today's rapidly evolving", "in recent years", "as we navigate".
- **Even register**: a draft where every sentence is formal, every paragraph the same length, every claim equally confident. His register moves between a technical paragraph and a line like "we got lucky and bottom-ticked the purchase".
- **Dashes.** Every one of them. Replace with the punctuation in rule 6.
- **Chat leakage**: "I hope this helps", "let me know", "here is", "in summary".

Three things that look like tells but are his and must stay: sentence-initial "Furthermore/As such/Thus", first-person claim verbs ("we believe", "we think") where a judgment is being stated, and compound-hyphenated analytical adjectives in attributive position (capital-intensive, price-insensitive, balance-sheet-focused, long-dated, geography-first).

## Detection: what helps, what hurts, what is honest

Read the reference file for the mechanics. The operational summary:

- **Lexical retention is the strongest lever.** Pangram labels a clause Human when it lexically matches human source text, AI-Assisted when the idea survives but the words were rewritten, AI-Generated when neither matches. It is invariant to deletions and reordering. So any clause Will actually wrote that survives into the output verbatim is credited to him, and cutting or reordering his material costs nothing. When the input contains his words, your job is editorial, not authorial.
- **Fresh generation from a thin brief is the weakest position**, and no style rule changes that reliably. Pangram's own style-imitation benchmark shows models imitating named authors are still caught about 97% of the time at the document level. Say so when it is relevant rather than implying the output is safe.
- **Humanizer tricks hurt.** Injected typos, casing games, homoglyphs, synonym swaps, round-trip translation and the "humanizer" prompt repositories are explicitly in Pangram's adversarial training set, and they trigger a separate humanizer classifier. Never do any of them. His real typos are his; do not add new ones to anything.
- **Short texts are out of scope for the detector** (under 50 words) and weak under 100, which matters for LinkedIn posts and short emails but not for letters.
- **Context matters to the classifier.** A section scored alone can score differently from the same section inside the full letter. A letter that is mostly his words with one adapted section will score better than the section does in isolation.

## Working method

1. Read the profile (and exemplars if needed). Classify the input and pick the register.
2. Pull out the claims, the numbers, and any of Will's own phrases. Make a one-line note to yourself of the verdict the piece should land on, because his sections end on a verdict.
3. Draft. Write the claim or number first. Vary sentence length on purpose: when you notice three sentences in a row of similar length, break one and extend another. State judgments as his ("we believe", "in our opinion") and then leave them alone; do not append qualifiers. One concession per section, early and plain, is the ceiling. Never "we may be early".
4. Run the measurement script on the draft and compare it to his profile:

   ```
   uv run <skill folder>/scripts/style_check.py <draft.md>
   ```

   The skill folder is wherever this SKILL.md lives: `~/.claude/skills/massif-voice` for a direct install (on Will's machine, `C:/Users/WilliamThomson/.claude/skills/massif-voice`), or `${CLAUDE_PLUGIN_ROOT}/skills/massif-voice` inside the massif-house-style plugin. Add `--register personal` for emails and posts; it relaxes the letter-register rhythm bands and keeps the hard checks. (`python` works too if `uv` is unavailable; the script has no dependencies.) It reports sentence-length distribution, paragraph distribution, punctuation rates, hedge density, dash count, retired-phrase hits, AI-vocabulary hits, participial-clause rate and a few structural tells, each against the corpus target with a flag when the draft is outside the band. The numbers are a diagnostic, not a target to game: if the variance is low, go back and rewrite sentences, do not splice random short fragments in.
5. Read the result once as Will reading it in the morning. Cut anything he would not say. Run the manufactured-cleverness test on every sentence that feels pointed: delete it, see what is lost. Check the verdict is a verdict with content in it. Check for dashes one last time.
6. Return the prose only. If the brief was thin and you made assumptions, add a single line after the prose, visibly separate, listing them.

## Coordination with other skills

- **What this skill carries over from the earlier massif-voice skill**: the house lexicon (real assets, capital cycle, margin of safety, probability-weighted intrinsic value, dispersion not direction, geography-first; see `references/voice-profile.md` section 4), the ban on em-dashes, the concede-then-argue move, the principle-versus-execution move, field-verification authority, technical vocabulary left untranslated, verdicts rather than summaries. All of these are now stated as measured habits with verbatim examples rather than as rules.
- **What it drops**: the opt-in "Commentary Register" (the Grant's Interest Rate Observer toolkit of scene openings, planted aphorisms and sardonic parentheticals), because Will's own published essays do not use it and the gadget rules above cut against it; and the word-list "Tell Purge", because that list came from the blader/humanizer repository that Pangram 4 names and trains against. A word list survives here only as one check among many.
- `massif-visual` governs formatting. This skill is prose only. If a skill such as `investor-deck` has its own voice defaults, this skill takes precedence for prose.
- Do not use this skill to disguise the authorship of text that Will did not write and will not stand behind. The purpose is that text he sends under his name reads as his, with his views and his numbers in it.
