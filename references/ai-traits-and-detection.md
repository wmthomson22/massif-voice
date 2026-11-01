# What the research says about AI prose, and how Pangram 4 detects it

Two sources, read in full on 2026-11-01:

1. "How AI Writes: A Critical Literature Review of Linguistic and Stylistic Traits" (narrative review covering Herbold et al. 2023 *Scientific Reports*; Reinhart et al. 2025 *PNAS*; Zamaraeva et al. 2025 arXiv:2506.01407; Kendro, Maloney and Jarvis 2026 *IJAL*; Doshi and Hauser 2024 *Science Advances*; the PubMed excess-vocabulary study 2025 *Science Advances*).
2. Glickenhaus, Thai, Russell, Masrour, Han, Spero and Emi, "Pangram 4 Technical Report" (Pangram Labs / University of Maryland, 2026).

This file records what they actually found, what it implies for writing in Will's voice, and where the honest limits are.

## Part A. How AI prose differs from human prose

### A1. The difference is regularity, not error

The review's headline: AI text is distinguished "less by grammatical errors than by regularity: recurring vocabulary preferences, favored grammatical structures, and a narrower range of stylistic choices." Fluency is not the problem. Sameness is. Any method that only fixes words leaves the sameness in place.

### A2. Vocabulary: distinctive preferences carried into the wrong context

Reinhart et al. found GPT-4o used "tapestry" in 23% of outputs and "amidst" in 27%, with "camaraderie", "intricate", "palpable" similarly overused relative to matched human text. The PubMed study found "delves", "underscores", "showcasing" at roughly 28x, 13.8x and 10.7x their projected 2024 frequencies. The review's point is not that these words are artificial; it is that models use them "across contexts in which human writers would be more selective". A word fine in fiction becomes conspicuous in an investor letter.

Implication: the word list matters, but the test is contextual appropriateness. Will's corpus shows what is appropriate in his context (see voice-profile section 4). Replace a flagged word with the plain word he would use, not with a rarer one.

### A3. Syntax: noun-heavy density and a few favoured constructions

Herbold et al.: GPT essays had more nominalisations and more complex sentence structure than the human comparison set. Reinhart et al.: GPT-4o used nominalisations at 2.1x the human rate and present participial clauses at 5.3x the human rate, producing "a dense, elaborated style" through phrasal coordination. Zamaraeva et al.: lower *diversity* of syntactic constructions in model news text even where sentences were complex.

The review's key distinction: "syntactic complexity and syntactic diversity are different. An output can contain elaborate sentences while repeatedly relying on the same construction types."

Implication: Will's prose is not simple, but it is varied. He writes 55-word sentences and 4-word sentences; he uses parentheses, semicolons, colons, comma splices, rhetorical questions, and "one"-pronoun generalisations. The target is construction variety, not shorter sentences. Watch especially for the trailing participle (", highlighting", ", reflecting", ", underscoring") which runs at a fraction of the model rate in his corpus.

### A4. Stance: models take fewer explicit positions

Herbold et al.: students used more modal and epistemic expressions ("I think", "in my opinion") than the models, whose essays "leaned toward nominalized, more impersonal formulations." The review: "presenting several sides of an issue is not the same as expressing an identifiable authorial position."

Implication: this is the single largest gap between model prose and Will's prose. A third of his sentences contain "we/our" and "we believe" alone appears in nearly 2% of sentences, because he states judgments as his own and takes responsibility for them. That is stance, not hedging: the claim is made in the first person and then left to stand. Real hedges ("admittedly", "it is far from clear to us") are occasional, about one per section. Put him in the sentence as the one making the claim; do not pile qualifiers around the claim, and never use "we may be early", which he has retired.

### A5. Imitation fails at depth, not at the surface

Reinhart et al. gave models roughly 500 words of a human author and asked for a continuation in the same style, tone and diction. Instruction-tuned models "retained distinctive grammatical and lexical preferences" across every genre tested. The review: "matching topic and tone does not guarantee matching a genre's deeper conventions. A model may produce a plausible-looking continuation while maintaining a default density, vocabulary, or sentence pattern that is atypical of the original context." Base models diverged less from human patterns than instruction-tuned ones, implicating post-training.

Implication: this is why the skill measures distribution (`scripts/style_check.py`) rather than trusting the feel of a draft. The default density and evenness come back silently.

### A6. Lexical diversity is not the lever

Herbold et al. found GPT-3.5 less lexically diverse than students but GPT-4 more. Kendro et al. found all four ChatGPT models differed from humans on six diversity dimensions, with newer models not necessarily closer. The review: "sophistication, variety within a text, and variation across texts are separate properties. AI writing may look lexically rich while remaining unusually regular in how it distributes vocabulary."

Implication: do not try to sound human by using more varied or more sophisticated words. Will's type-token ratio is modest (0.109 over 50,000 words); he repeats "roughly", "significant", "very", "likely", "we believe" without embarrassment. Reaching for variety is a tell.

### A7. Quality is not the issue

Teachers rated GPT essays above the human comparison set. The review's caution: "characteristics that make model writing statistically distinctive can coexist with strong evaluations of organization and language mastery." A draft can be well organised and well written and still be obviously machine prose. Do not confuse polish with voice.

### A8. Homogenisation across outputs

Doshi and Hauser: AI-assisted stories were individually better but collectively more similar to each other, and anchored on the AI's suggestions. Implication for a body of letters: if every adapted section lands on the same paragraph shape and the same verdict cadence, the letters converge on each other. Vary the moves across pieces as well as within them.

### A9. Limits the review itself states

Findings are model-, genre-, comparator- and workflow-dependent; classifiers that work on one corpus degrade on another; the studies explain distributions, not individual authorship. Treat the rules in this skill as describing tendencies to steer against, not as a checklist that guarantees anything.

## Part B. How Pangram 4 works

### B1. What it is

A fine-tuned open-weight mixture-of-experts language model with LoRA adapters and linear classification heads. It is trained on human text from many domains (professional and finance is 4.9% of the human training data; creative writing 22.2%, scientific 18%, consumer reviews 15.9%) and on AI text generated in-house by "synthetic mirroring": take a human document, extract its topic, ask an LLM to write on that topic, keep the pair. The stated aim is to learn "How was this text written?" rather than "What is this text about?". So it is topic-invariant by design and it is not a word-list or perplexity detector. Stylistic regularity of the kind in Part A is exactly what it learns.

Reported performance: AUROC 0.9916; false positive rate 0.0041% (one human text in roughly 24,000 flagged); false negative rate 0.34% over 520,000 AI outputs from 26 models. Anthropic models have the lowest FNR of any family at 0.195% (Claude Fable 5: 0.255%; Opus 5: 0.195%; Sonnet 5: 0.140%). Fresh Claude output is, on these numbers, the easiest thing it detects.

### B2. How it reads a document

- Context window 512 tokens, slid with a stride of 256, so every token is seen in two overlapping windows and each window is repeated twice ("Repeat2") so early tokens see the whole window.
- Three heads: a 15-bucket estimate of the AI fraction of each window; a per-token three-class label (human / AI-assisted / AI-generated); a binary "is this window mixed" head. A fourth probe head detects humanization.
- Outputs are combined by a linear-chain CRF, then snapped to sentence boundaries by majority vote, then short runs are merged into neighbours. The product therefore reports at sentence resolution.
- Document verdict: Human if at least 90% of characters are labelled human; AI if at least 80% are AI; Mixed otherwise. For their own metrics a Mixed verdict on human text counts as a false positive.

### B3. How it defines and labels authorship (this is the part that matters most)

Pangram defines AI-generated text as "original, substantial natural-language prose generated by an LLM in response to an open-ended writing task." Three consequences they state explicitly:

1. Summarisation and deletion do not count. "We must consider the output to be human if the AI does not add any original tokens of its own." The labeler "is invariant to both deletions in the target and rearrangements of clauses." Reordering a human's sentences without rewriting them is human.
2. Training labels for mixed text come from a clause-level "soft n-grams" procedure: for each clause in the edited text, if there is an exact or near-exact lexical match in the human source it is labelled **Human**; if there is only a semantic match (the idea survives, the words changed) it is **AI-Assisted**; if neither, **AI-Generated**. The document's AI fraction is (AI-generated characters + half the AI-assisted characters) / total.
3. Texts under 50 words are out of scope. Error rates are highest in the 50 to 99 word bucket and fall with length.

Implications:

- **Will's own clauses, kept verbatim, are labelled his.** This is the strongest lever available. When adapting his notes or his draft, preserve his wording wherever it is usable. Cutting, reordering and connecting his material is free.
- **Paraphrasing his idea into new words is the worst of both worlds**: it loses the lexical match (now AI-Assisted at best) while adding nothing. If a clause of his is awkward, leave it awkward or ask him.
- **Writing fresh prose from a brief is open generation**, which is what the detector is built for. Style rules reduce the signal but do not remove it. Pangram's results on the Epoch AI "Style Imitation" benchmark (594 AI passages, half prompted to imitate named authors) were a 2.86% document-level false negative rate, so imitation of a known author got through about 1 time in 35, and that benchmark was among their weakest results, not their strongest.

### B4. What they trained against (do not do these)

The humanizer head is trained to recognise "deliberate typo injection, casing changes, synonym substitution, homoglyph attacks, and transformations produced by services that advertise humanization or AI-detector evasion." Incidental artefacts (PDF extraction errors, OCR, encoding) are explicitly *not* classified as humanization, which is why injecting fake ones does not help: the classifier has seen both.

Results on 13 commercial humanizers: humanized text detected as AI 97.7% of the time, as AI or Mixed 98.8%. The humanizer head identifies the text as humanized with 91.5% to 99.4% per-system true positive rate. The blader/humanizer GitHub repository (32,000 stars; the source of the "AI-Writing Tell Purge" list in the earlier massif-voice skill that this one replaced) is named and evaluated: text humanised with its instructions by GPT-5.5, Opus 4.8 and Sonnet 4.6 had a 0.43% false negative rate. In other words, following that checklist alone leaves the text about as detectable as raw output.

Their automated red-team agent (GPT-5.6, 24 hours of API access) tried "imitating specific human voices and styles, using different operational and professional registers, imitating a notetaker, using much terser vocabulary, conditioning its output on detailed source writing, aggregating multiple AI documents together, reformatting data as PDFs, putting the text through multiple rounds of translation". The only bypass found was terse clinical dictation, which they deemed out of scope. Round-trip translation, terse vocabulary, and voice imitation are therefore known to the model.

Synonym substitution, homoglyphs, whitespace and zero-width tricks, number perturbation, and case flips each had a per-attack detection rate of 99.96% to 100%.

### B5. What they are weak at (this is the realistic opening)

- **Light edits on a human base barely register.** AI-polished human text ("fix spelling", "lightly polish for readability") is called AI 0.01% of the time and Mixed 0.54%.
- **Heavy edits on a human base are under-called.** On the OpAI-Bench editing trajectory, a "style rewrite" with a true AI character fraction of 46% was predicted at 13.6% mean (median 0%); "compress" at 50% true was predicted 5.5%; only once the true fraction passed roughly 70% did predictions rise above half. The model systematically under-estimates AI involvement when a genuine human document is the substrate.
- **Deletion and rearrangement are invisible to it** by construction.
- **Short texts** are out of scope under 50 words and weakest under 100.
- **Context dependence.** "A section of a paper run in isolation may receive a different prediction than it does within the full context of the paper." A mostly-human letter carries an adapted section better than the section carries itself.
- **Stated limitation**: "Pangram 4 does not account for people who intentionally write like LLMs or who have absorbed elements of LLM style into their writing." The converse is the opening: an LLM that genuinely writes in the distribution of a specific human is the data-drift problem they say they have not solved. That is a hope, not a guarantee, and the style-imitation benchmark says it mostly does not work yet.

### B6. The honest summary for Will

- If the input contains Will's words, keep them. Edit, do not rewrite. This is both better voice and the only lever with a measured effect.
- If the input is an AI draft or a brief, the output is open generation. Writing in his distribution (variance, stance, punctuation, argument shape) is the right thing to do for the reader and reduces the obvious signal, but it should not be sold as passing the detector. Say so if asked.
- Never use the humanizer bag of tricks. They are counterproductive and they put a second, specific flag on the text.
- The best workflow for a letter is Will drafting or dictating the substance in his own words, however rough, and the skill doing editorial work on top. The worst workflow is a one-line brief and a request to "make it sound like me".
