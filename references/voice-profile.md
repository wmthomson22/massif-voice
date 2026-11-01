# Will Thomson: voice profile

Source: 42 published Massif Capital pieces, Q4 2016 to Q2 2026 (37 quarterly letters, 4 working papers / investment reports), 210,798 words and 9,122 sentences after stripping tables, headings, footers and disclaimers. Measured 2026-11-01 with `scripts/style_check.py --corpus`. Two files in the same folder are third-party source articles (FT, Foreign Affairs) and were excluded.

Use this file as the fingerprint. Section 1 is the measured distribution; sections 2 to 6 are the habits that produce it, with verbatim examples. Quotations are exact, including the odd typo, so you can see what his unedited prose actually looks like.

## 1. Measured profile

### Sentence length (words)

| Statistic | Will | Typical instruction-tuned model draft |
|---|---|---|
| Mean | 23.7 | 20 to 24 |
| Median | 22 | similar |
| Standard deviation | 12.4 | 6 to 9 |
| Deciles | 10, 13, 16, 19, 22, 25, 28, 32, 39 | compressed toward the middle |
| Share of sentences of 8 words or fewer | 7.4% | 1 to 3% |
| Share of 40 words or more | 9.7% | 2 to 5% |
| Share of 50 words or more | 3.5% | under 1% |
| Mean within-paragraph SD of sentence length (paragraphs of 3+ sentences) | 9.2 | 4 to 6 |

The mean is unremarkable. The spread is the signature. The sentences at both tails are what a model does not produce unprompted.

### Paragraph length (sentences)

| Sentences per paragraph | Share |
|---|---|
| 1 | 11% |
| 2 | 16% |
| 3 | 20% |
| 4 | 19% |
| 5 | 15% |
| 6 | 8% |
| 7 or more | 11% |

Mean 3.9, median 4. A paragraph of one sentence is used for a verdict, a pivot, or a plain statement of fact after a long passage. Paragraphs of seven or more occur when he is walking evidence and does not stop.

### Punctuation and mechanics (share of sentences containing)

| Feature | Will |
|---|---|
| Semicolon | 5.9% |
| Colon | 5.3% |
| Parenthetical "( ... )" | 8.9% |
| Em-dash or en-dash | 0.0% (zero instances) |
| Exclamation mark | 0.0% |
| Question mark | 1.3% |
| Single-quoted phrase | 1.9% |
| Double-quoted phrase | 0.6% |
| Contraction (n't, it's, we've, we're, that's, let's and the like; possessives excluded) | 1.7% |
| Any digit | 31.8% |
| Percentage figure | 13.4% |
| Dollar figure | 4.5% |
| "etc." | 0.3% |
| "i.e." or "e.g." | 0.1% |

Contractions are a near-absence worth noting: fewer than one sentence in fifty. He writes "it is", "do not", "we have", "cannot". The exceptions ("it's simply far from clear", "we've made that mistake", "until it isn't", "when they can't sleep") are casual asides or quoted speech. A draft that contracts freely reads as an imitation of informality rather than as him.

The dash finding is absolute: in 210,000 words there is not one em-dash or en-dash. Spaced hyphens " - " appear in 0.6% of sentences, mostly in ranges ("1998 - 2013") and a few heading subtitles. When a model would write a dash he writes a comma, a semicolon, a colon, or a parenthesis.

### Stance and person (share of sentences containing)

| Marker | Will |
|---|---|
| we / our / us | 33.2% |
| I / my / me | 3.1% (concentrated in 2016 to 2017 letters, before the firm voice became "we") |
| you / your | 2.5% |
| "we believe" | 1.8% |
| "we expect" | 0.7% |
| "we think" | 0.6% |
| "in our opinion / view / estimation" | 0.5% |
| "we find" | 0.4% |
| "we suspect" | 0.2% |
| "seems / seem" | 1.3% |
| "likely / unlikely" | 2.4% |
| "perhaps" | 0.6% |
| "frankly / admittedly" | 0.3% (admittedly 24 uses) |
| "unfortunately" / "fortunately" | 43 uses each |
| "roughly" | 305 uses (vs. "approximately" 57) |
| "one" as impersonal pronoun ("one might", "one can") | 35 uses |
| Rhetorical question (sentence ends in "?") | 1.2% |

### Connectives (share of sentences containing)

| Marker | Will |
|---|---|
| Sentence-initial "Furthermore" | 87 instances (about 1%) |
| "Thus" | 1.0% |
| "As such" | 0.8% |
| "However" | 0.7% |
| "Moreover / Furthermore" (any position) | 1.0% |
| "In short" | 0.4% |
| "Put another way / put differently" | 14 uses |
| "After all" | 28 uses |
| "Rather than" | 1.5% |
| "Not X but Y" | 0.6% |
| Sentence-initial And / But / So / Yet | 0.7% |
| "Importantly" | 0.2%; "Notably" 0.1%; "Indeed" 0.1% |

### Features associated with machine prose

| Feature | Will |
|---|---|
| Trailing "-ing" clause closing the sentence (", highlighting the risk.") | 4.1% |
| Sentence beginning with a participle | 3.6% |
| Agentive passive ("was driven by") | 0.9% |
| Sentences containing a word from the AI vocabulary list (delve, crucial, pivotal, tapestry, underscore, showcase, foster, holistic, intricate, testament, interplay, multifaceted, nuanced, seamless, "evolving landscape") | 0.4% |
| Type-token ratio, first 50,000 words | 0.109 |

Top content words, in order: market, capital, price, portfolio, investment, value, position, energy, quarter, prices, supply, management, demand, gold, years, risk, only, commodity, global, return, roughly, company, short, growth, significant, copper, business. "Significant" (282) and "very" (262) are both common; he does not avoid plain intensifiers.

Top adverbs: roughly, likely, currently, early, especially, highly, particularly, significantly, increasingly, recently, approximately, specifically, unfortunately, globally, fully, explicitly, historically, relatively, independently, primarily.

## 2. Sentence habits

**The two-tail rhythm.** A long evidentiary sentence, then a short declarative. Not a staccato run of fragments; one short sentence closing or opening a thought.

> "The portfolio gained 10.9% in April on a gross basis. Materials contributed 9.8% to the return, and industrials another 1.9%. Energy was effectively flat at minus six basis points, the product of a violent intra-month round trip in crude as US-Iran ceasefire talk gave way to direct escalation by the end of the month." (Q1 2026)

> "Enovix was the single worst performer, dragging the portfolio down 2.4% due to stale fundamentals and a thinning tape. It costs more on its own than all the shorts combined. The thesis depends on commercial validation that has yet to arrive." (Q1 2026)

> "The Fed cut, and the long end sold off. The expectations channel said yields should fall; the term-premium channel overwhelmed it." (Cartography of the Risk-Free Rate, 2026)

> "The commodity shock and the rate shock are not two stories. They are one." (Cartography of the Risk-Free Rate, 2026)

**Long sentences that keep going.** He is comfortable with 50 to 70 word sentences full of qualifications, parentheses, and the occasional comma splice. They are not elegant; they are how he thinks on the page.

> "Timing is a tricky issue, and we were hesitant to even mention the word in our letter, after all, no one knows how to time the market, although some people seem to be good at it (Warren Buffett, despite his protests, has the best timing of any investor we have ever seen, Stanley Druckenmiller also comes to mind)." (Q2 2019)

> "While we do invest in US stocks (~75% of the portfolio is invested in our 10 largest positions, of which three are US listed, but one is an ADR and one is a duel listed US/Canadia stock) but most derive the majority of revenue, earnings, and cash flow from assets outside the US, so our operational risk (as opposed to systemic market risk) is outside the US." (Q3 2025)

> "Admittedly, some incremental value would be created by new mines, the market is unlikely to recognize that value, in our opinion, and there is an option on a potential second world-class copper asset; it is such an early stage deposit that we were not comfortable valuing it."

**Semicolons to butt clauses together.**

> "We like volatility; it creates opportunity even if it creates heartburn." (Q2 2019)

> "Investing is an art; it is not a science." (Q4 2023)

> "If you produce a better battery, there will be consumers; that is not in question."

> "This was not a unique insight though; others understood the value of the project."

**Parentheses that carry a full thought.**

> "From my perspective, this is a new wrinkle/risk (I can't decide which it is) for active investment managers." (Q2 2017)

> "The Commodity Purity Index (CPI, an unfortunate acrynom) is a framework developed to measure, on a rolling basis, the extent to which the underlying commodity drives a commodity producer's stock price behavior." (You're Not Long Copper, 2026)

> "We take no issue with investors choosing to avoid sectors based on a lack of opportunities or not being interested in spending the time to bring a company into their circle of competence (there is after all only so much time in the day), but we found the ratio sufficiently skewed to ask most attendees we spoke with why they choose to avoid mining." (Q2 2019)

**Colons into a list or a question.**

> "Variance decomposition answers the question a trader asks at two in the morning when they can't sleep: why is my position moving?" (You're Not Long Copper, 2026)

> "It seems prudent to ask a relatively unasked question: why would foreigners want to own this dollar?"

**Single quotes for scare-quotes and short quoted phrases.** 'long energy', 'bullish on copper', 'commodity' driven, 'risk', 'unequivocally'. Double quotes are reserved for longer direct quotations with attribution.

**"Roughly" everywhere a number is approximate.** "roughly 25 people", "roughly $450 billion", "roughly 40% of the world's population", "roughly 1% per annum". Not "approximately", not "around", not "some".

## 3. Stance habits

**Views stated in the first person, then left alone.** "We believe", "we think", "in our opinion" are how he states a judgment. They are the verb of the claim, not a softener in front of it, and the sentence does not then add a second qualifier.

> "We do not claim to have the ability to forecast commodity prices, nor are we familiar with anyone who does, but we also don't see it as a key to successful mining investing" (Q2 2019)

> "We disagree with this particular aspect of the work; it undersells the significance, but the qualitative work is sound." (From Geology to Geography, 2026)

**Hedges are rare and earned.** About one per section. "Admittedly", "it is far from clear to us", "we are not certain" appear where a real limitation exists, never as a reflex after a claim, and never two in succession. Will has asked (November 2026) that the skill keep hedging sparse, and that the construction "we may be early, but we are not wrong", which appeared in several of his pieces, not be used again in any form, either half of it. Do not quote it, do not paraphrase it ("early is not the same as wrong" is the same tic). Where the thought is needed, state the test that would prove the view wrong.

> "Put another way, every variable in the equation is an assumption open to debate, but the tools we have are the tools we use." (Q3 2025)

> "such forward-looking prognostications are opinions strongly stated but loosely held" (Q3 2024)

> "We see a link between market momentum and an industries capital cycle, to the best of our knowledge this a new claim." (Q2 2019)

**Plain admissions, then process.**

> "We were optimistic and wrong."

> "Sitting on a quick unrealized gain, we got caught playing with house money and made a bad call."

> "This performance is not up to our standards, and we make no excuses for that." (Q3 2023)

> "Our understanding of the business, having spoken with management dozens of times over the years and visited most of the firm's mines, did not yield much value this year. You would have received the same return by simply owning a gold ETF. We think this will change going forward." (Q3 2025)

> "No Massif Capital letter would be complete without examining something that is not working or that we got wrong."

> "The company read was accurate, but our read on the market concern or lack thereof for fundamentals in the short to medium term was wrong." (Q4 2023)

> "Investment managers with tunnel vision on high earnings in a cyclical industry have been wrong-footed before (we've made that mistake)." (Q3 2021)

**Steelmanning by stating the objection plainly.**

> "We do not claim that geology no longer has importance, far from it. Ore grades will still decline; marginal costs still matter. We do claim that the marginal-cost variable has been demoted" (From Geology to Geography, 2026)

> "We recognize that our ongoing discussion of changes, adjustments, and lessons learned may unsettle some investors who perhaps thought they were investing with a firm and in a portfolio supported by a portfolio manager with unwavering commitment in his proven process." (Q4 2023)

**Pride stated without inflation.**

> "Overall, we believe this is a respectable result."

> "We are pleased but not satisfied with our 2024 performance." (Q4 2024)

> "We take more pride in that than in absolute returns, after all, the easiest way to benefit from compounding is not to lose money." (Q3 2025)

**Dry wit, by juxtaposition, unannounced.**

> "While academics will tell you what risk is with a straight face, we cannot." (Q3 2025)

> "Although we sympathize with this position, after all, Wall Street Hedge Fund managers are usually depicted as masters of the universe, but we would suggest that image is fiction." (Q4 2023)

> "It seems worthwhile to highlight that while the software is supposedly eating the world, at least according to Marc Anderson, in the real world, it is China, not software, that is eating the world." (Q3 2024)

> "Linear beta, the output of our multifactor model, is a serviceable approximation of sensitivity, until it isn't, and in commodity equities, it fails precisely when it matters most." (2026)

> "Most recently here, here and here, We're a bit hoarse from trying to get this point across. Why the shouting? Two reasons:" (Q3 2021)

> "the producers we own are generating cash at $80 Brent and gushing at $115." (Q1 2026)

Colloquialisms that appear inside formal argument: heartburn, hoarse, putters along, gushing, rickety, a dash of carry or convexity, balance-sheet spice, the stuff itself, hold my nose, just what the doctor ordered, bottom-ticked, house money, wrong-footed, blasphemy, purgatory, topic du jour, a pretty remunerative torque, shelling out.

## 4. Vocabulary habits

**Technical terms used without translation**: EBITDA, AISC, NSR, IRR, capex, free-cash-flow yield, term premium, basis differential, netback, offtake, orderbook-to-fleet ratio, time-charter equivalent, beta, alpha, Sortino, variance decomposition, convexity, residual. Where a term is genuinely obscure he adds a short parenthetical or a footnote, not a sentence of explanation.

**House frames**: real assets, the capital cycle, margin of safety, probability-weighted intrinsic value, stock-picking alpha versus factor exposure, capital intensity, underinvestment, the real-asset ecosystem, geography-first versus geology-first, dispersion not direction, the cleared price, structural versus cyclical.

**Compound analytical adjectives in attributive position**: capital-intensive, price-insensitive, balance-sheet-focused, long-dated, pre-production, policy-driven, geography-first, high-fixed-cost, fundamentals-driven, event-driven, duration-heavy. Keep these; they are his. Do not hyphenate in predicate position ("the business is capital intensive").

**Words he leans on that look generic but are his**: significant, very, roughly, likely, prudent, sensible, interesting, respectable, remunerative, meaningful, modest, durable, telling, odd/oddity, fuzziness, plainly, frankly, admittedly, unfortunately.

**Words he almost never uses** (whole-corpus counts in brackets): delve (1), pivotal (2), underscore (2), navigate (3), intricate (0), tapestry (0), testament (0), showcase (0), foster (0), seamless (0), holistic (1), multifaceted, realm, bolster, garner, journey, unlock, empower, elevate.

**Words on AI lists that he does use**, so do not scrub them to zero: robust (43; "robust balance sheet", "robust demand", "a robust $5.50 CAD"), comprehensive (39), landscape (25; "energy landscape", "macroeconomic landscape", "corporate landscape"), leverage (67, almost all in the financial sense), crucial (8), nuanced (8). The rate is roughly one per letter. Two in a paragraph is not him.

## 5. Structural habits

**Letters open with the number.** "During the first quarter of 2026, the Massif Capital Real Assets Strategy advanced 16.0% net of fees." "The core portfolio of Massif Capital returned -0.8% during the second quarter of 2019, bringing the year-to-date performance to 3.5%." Then attribution by position with contributions in percentage points, then the self-assessment, then the essay sections, then the portfolio review by position (ticker in parentheses after the name), then footnotes and disclosures.

**Essay sections open with the claim.** "Commodity pricing has shifted from a geology-first regime to a geography-first regime." "The interest rate is the price of sovereign money, and that price is increasingly being set by geography rather than by the policy rate." "Every investment is a wager on what might be, not what is."

**Evidence is walked, often chronologically.** "The case for regime change is best made by walking it." Six regimes, each with dates, each with the cleared price at the start and the end.

**Sections close on a verdict.** "The implication for the real-asset investor is dispersion, not direction." "The thesis is unchanged." "Either answer means the position gets cut." "Rates are high, companies are cash-rich, and the order-to-fleet ratio is bottoming. This is a unique situation, perhaps unprecedented."

**Headings.** Plain nouns for routine sections (Portfolio Review, Oil Markets, Attribution, Mining Investments, Siemens Energy (ENR), New Position: Short Deere & Co). For essay sections, either a declarative ("The Frequency Separation: Why Commodity is Noise and Residuals are Signal", "What Could Be Wrong, and the Call") or a question with a joke in it ("Great Results, What Have You Done For Me Lately?", "Where Do We Go From Here?? I Don't Know…Call China", "Value Investors - Avoiding Mining at All Costs, But Why?", "Capital Cycle Analysis - Seeing the Forest Before the Tree").

**Footnotes carry content.** Some are one line ("We use 4.2% at the current time."). Some are a paragraph of definition or history (Market Internals; the Achnacarry Agreement; Section 232). Some are a recommendation ("If you are an investor in Massif Capital and have not yet read this book, please contact us and we will send you a copy."). He will put a secondary argument in a footnote rather than cut it.

**Lists.** Numbered "1) 2) 3)" with semicolons at line ends when enumerating concerns or questions ("1) Mining was too volatile; 2) Mining was too technical, and; 3) Many felt uncomfortable forecasting commodity prices."). Bullets are rare in argument. Catalogues of names run inline with commas and a final "etc." if he is bored of the list.

**Addressing the reader.** "Dear Friends and Investors," as the salutation. "As investors in the fund and regular readers of our letters know". "Many of you have invested with other funds". "As a reminder,". "Hopefully, this review has provided you with some context". He talks to a specific room.

## 6. What he does not do

- No dashes, no exclamation marks.
- No scene-setting openings, no dates-and-podiums, no "In recent years".
- No announcing structure ("In this section we will"). The one exception is the deliberately plain "A Brief Note About What Follows" heading, used once.
- No aphoristic one-liners for their own sake in letters; the short line is a verdict on the paragraph above it.
- No translating jargon for the reader.
- No impersonal hedging ("it is important to consider"). The little hedging there is belongs to him ("we are not certain", "it is far from clear to us"), and there is little of it: one per section, not one per paragraph, and never stacked.
- No "we may be early", in any wording. Retired at Will's request.
- No forced triplets, no "not only... but also" as a reflex, no false ranges.
- No uniform paragraphs. If every paragraph is four sentences it is not him.
- No tidy closings that restate the piece. The last sentence is a position, often with what would change it.
- No rhetorical gadgets: no reveal clauses (", and it has a date on it"), no commentary on his own sentences ("that is a conditional sentence"), no echo constructions, no negative-definition zingers ("is not what a cheap asset looks like"), no two quips joined by a semicolon, no one-line paragraph for drama. Will flagged each of these in test drafts as obviously machine-written. His wit is in the facts, not in the sentence shape.
- In personal register (LinkedIn, email) he is plainer and more casual than in the letters: short sentences, short paragraphs, talking rather than arguing. Do not write a letter paragraph and call it a post.
