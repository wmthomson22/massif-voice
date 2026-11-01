# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
style_check.py: measure a draft against Will Thomson's writing profile.

Usage:
    uv run style_check.py DRAFT.md            # compare one draft to the stored targets
    uv run style_check.py DRAFT.md --verbose  # also list the offending sentences
    uv run style_check.py --corpus DIR        # recompute targets from a folder of his *.md pieces
    python style_check.py DRAFT.md            # works without uv as well

The targets were measured on 42 published pieces (2016 to 2026). They describe his
distribution; they are a diagnostic for a draft, not a score to optimise. If a draft
is flagged for low sentence-length variance, rewrite sentences; do not splice fragments.
"""
import re
import sys
import glob
import os
import statistics as st
from collections import Counter

# ---------------------------------------------------------------- targets
# (name, target, low_ok, high_ok, unit) measured 2026-11-01 on the Massif corpus.
TARGETS = {
    "sent_mean":        ("Mean sentence length (words)",            23.7, 19.0, 29.0, "w"),
    "sent_sd":          ("Sentence length SD",                      12.4, 9.5,  99.0, "w"),
    "short_share":      ("Sentences of 8 words or fewer",           7.4,  4.0,  14.0, "%"),
    "long_share":       ("Sentences of 40 words or more",           9.7,  5.0,  16.0, "%"),
    "para_sd":          ("Within-paragraph sentence-length SD",     9.2,  6.5,  99.0, "w"),
    "para_mean":        ("Mean sentences per paragraph",            3.9,  2.5,  5.5,  "s"),
    "para_1_share":     ("One-sentence paragraphs",                 11.0, 3.0,  25.0, "%"),
    "para_7_share":     ("Paragraphs of 7+ sentences",              11.0, 0.0,  25.0, "%"),
    "semicolon":        ("Sentences with a semicolon",              5.9,  2.5,  11.0, "%"),
    "colon":            ("Sentences with a colon",                  5.3,  2.0,  10.0, "%"),
    "paren":            ("Sentences with a parenthetical",          8.9,  4.0,  16.0, "%"),
    "dash":             ("Em/en-dashes (count)",                    0.0,  0.0,  0.0,  "n"),
    "exclaim":          ("Exclamation marks (count)",               0.0,  0.0,  0.0,  "n"),
    "question":         ("Sentences ending in ?",                   1.3,  0.0,  4.0,  "%"),
    "contraction":      ("Sentences with a contraction",            1.7,  0.0,  6.0,  "%"),
    "digit":            ("Sentences containing a digit",            31.8, 15.0, 60.0, "%"),
    "we":               ("Sentences with we/our/us",                33.2, 18.0, 60.0, "%"),
    "claim_verb":       ("Sentences with a first-person claim verb (we believe/think/expect, in our opinion)", 3.5, 1.0, 8.0, "%"),
    "stance":           ("Sentences with an explicit hedge (admittedly, we may be wrong, far from clear...)", 1.5, 0.0, 3.5, "%"),
    "retired":          ("Retired 'may be early / not wrong' (count)", 0.0, 0.0, 0.0, "n"),
    "gadget":           ("Rhetorical gadgets (reveal clause, self-commentary, zinger templates)", 0.0, 0.0, 0.0, "n"),
    "roughly":          ("'roughly' per 1000 words",                1.4,  0.3,  4.0,  "n"),
    "approx_ratio":     ("'approximately'/'around' vs 'roughly'",   0.2,  0.0,  1.0,  "x"),
    "ing_tail":         ("Sentences closing with an -ing clause",   4.1,  0.0,  8.0,  "%"),
    "participle_start": ("Sentences opening with a participle",     3.6,  0.0,  7.0,  "%"),
    "ai_vocab":         ("Sentences with AI-list vocabulary",       0.4,  0.0,  1.5,  "%"),
    "nominal":          ("Sentences with 2+ -tion/-ment/-ness/-ity nouns", 20.0, 0.0, 32.0, "%"),
    "triplet":          ("Sentences with an 'X, Y, and Z' triplet",  6.0,  0.0,  11.0, "%"),
    "notonly":          ("'not only/not just ... but' (count)",     0.0,  0.0,  2.0,  "n"),
    "copula_avoid":     ("'serves as/stands as/represents/boasts'", 0.0,  0.0,  2.0,  "n"),
    "signpost":         ("Impersonal signposts (count)",            0.0,  0.0,  1.0,  "n"),
    "len_run":          ("Longest run of similar-length sentences", 4.0,  0.0,  6.0,  "n"),
}

AI_VOCAB = r"\b(delv(e|es|ing)|crucial(ly)?|pivotal|intricate|intricacies|tapestry|testament|underscor(e|es|ing)|showcas(e|es|ing)|foster(s|ing|ed)?|holistic|interplay|multifaceted|nuanced|seamless(ly)?|garner(s|ed)?|bolster(s|ed|ing)?|realm|navigat(e|es|ing) (the|a|an|this|these|those|complex|uncertain)|(evolving|shifting|changing|complex) landscape|leverag(e|es|ing) (the|a|an|our|its|their|this) (power|strength|expertise|capabilit|insight|relationship|position))\b"
SIGNPOST = r"\b(it is (important|worth|crucial|essential) to (note|mention|consider|remember|highlight|recognize|recognise|understand)|it should be noted|the real question is|at its core|in today's|in recent years|as we navigate|in an era of|in the ever|the bottom line is|at the end of the day|let's (dive|explore|unpack)|here's the thing|in summary|in conclusion|to summarize|i hope this helps|let me know)\b"
CLAIM_VERB = r"\b(we believe|we think|we expect|we find|we suspect|we would (argue|suggest|counter|note)|in (our|my) (opinion|view|estimation)|our (read|view) is|i believe|i think|i suspect)\b"
STANCE = r"\b(admittedly|frankly|candidly|to the best of our knowledge|it is far from clear|far from clear to us|we (are|am) not (certain|convinced|sure)|i am not (certain|convinced|sure)|we may be (wrong|mistaken|premature)|i may be (wrong|mistaken)|we could be wrong|we (do not|don't) know (for sure|whether|if)|we (cannot|can't) be (sure|certain)|it may be too (soon|early)|we concede|we acknowledge|we recognize that we)\b"
GADGET = r"(, and it has an? \w+ (on|to|in|attached to) it\b|\bthat is an? \w+ (sentence|clause|statement|question|claim)\b|\bin one (sentence|line|word)\b|\bis not what an? [\w -]+ looks like\b|\b(does|did|do) not change the (arithmetic|math|maths)\b|\bthat is not an? \w+, it is an? \w+\b|\bthe \w+ is the (problem|point|story|tell)\b|, and (we|i) (are|am) not going to \w+ (one|it|that)\b|\bcalling (it|the result|that) \w+\b|\bis not the same (thing )?as \w+\b|\bthe \w+ has a name for (this|that)\b|\bread that (sentence|line) again\b|\bthat is the (whole|entire) (argument|point|story|thesis)\b|\bnot a \w+ but a \w+\b)"
RETIRED = r"\b(may be early|may be premature|too (soon|early) to (say|call)|(we are|we're|i am|i'm) not wrong|(don't|do not) think (we are|we're|i am|i'm) wrong|early (is not|isn't) (the same as )?wrong)\b"
HEDGE_COPULA = r"\b(serves as|stands as|represents a|represent a|boasts|features a)\b"
NOTONLY = r"\bnot (only|just|simply|merely)\b[^.;]{2,80}\bbut\b"


def clean(text: str) -> str:
    """Strip frontmatter, tables, headings, images, bullets, footers, disclaimers."""
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    keep = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            keep.append("")
            continue
        if s.startswith(("|", "#", "- ", "* ", "> ", "!", "[", "EXHIBIT", "Figure", "Table", "*Data", "^Data")):
            continue
        if re.match(r"^\d+[\).]\s", s) or len(s) < 30:
            continue
        if re.search(r"(Opinions expressed herein|not an investment recommendation|Consulting a qualified)", s):
            continue
        keep.append(s)
    return "\n".join(keep)


def split_sentences(p: str):
    p = re.sub(r"\s+", " ", p).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", p)
    return [s.strip() for s in parts if len(s.strip().split()) >= 3]


def analyse(text: str):
    text = clean(text)
    paras = [split_sentences(p) for p in re.split(r"\n\s*\n|\n", text)]
    paras = [p for p in paras if p]
    sents = [s for p in paras for s in p]
    if len(sents) < 5:
        sys.exit("Not enough prose to measure (need at least 5 sentences after stripping tables/headings).")
    words = [re.findall(r"[A-Za-z][A-Za-z'\-]*", s) for s in sents]
    lens = [len(w) for w in words]
    nwords = sum(lens)
    N = len(sents)
    pct = lambda n: 100.0 * n / N
    has = lambda pat, flags=re.I: sum(1 for s in sents if re.search(pat, s, flags))

    psd = [st.pstdev([len(x.split()) for x in p]) for p in paras if len(p) >= 3]
    plen = [len(p) for p in paras]

    # longest run of consecutive sentences within +/-4 words of each other
    run, best = 1, 1
    for a, b in zip(lens, lens[1:]):
        run = run + 1 if abs(a - b) <= 4 else 1
        best = max(best, run)

    lower = text.lower()
    roughly = len(re.findall(r"\broughly\b", lower))
    approx = len(re.findall(r"\b(approximately|around)\b(?=\s*\$?\d|\s+(a|an|one|two|three|half|a third|a quarter))", lower))

    m = {
        "sent_mean": st.mean(lens),
        "sent_sd": st.pstdev(lens),
        "short_share": pct(sum(1 for x in lens if x <= 8)),
        "long_share": pct(sum(1 for x in lens if x >= 40)),
        "para_sd": st.mean(psd) if psd else 0.0,
        "para_mean": st.mean(plen),
        "para_1_share": 100.0 * plen.count(1) / len(plen),
        "para_7_share": 100.0 * sum(1 for x in plen if x >= 7) / len(plen),
        "semicolon": pct(has(r";")),
        "colon": pct(has(r":")),
        "paren": pct(has(r"\([^)]{3,}\)")),
        "dash": len(re.findall(r"[—–]|(?<=\w)--(?=\w)| -- ", text)),
        "exclaim": text.count("!"),
        "question": pct(has(r"\?$", 0)),
        "contraction": pct(has(r"\b(\w+n't|it's|that's|there's|here's|what's|let's|who's|we're|we've|we'll|we'd|they're|they've|they'll|you're|you've|you'll|i'm|i've|i'll|i'd|he's|she's)\b")),
        "digit": pct(has(r"\d")),
        "we": pct(has(r"\b(we|our|us|ours)\b")),
        "claim_verb": pct(has(CLAIM_VERB)),
        "stance": pct(has(STANCE)),
        "retired": len(re.findall(RETIRED, text, re.I)),
        "gadget": len(re.findall(GADGET, text, re.I)),
        "roughly": 1000.0 * roughly / max(nwords, 1),
        "approx_ratio": approx / max(roughly, 1) if (approx or roughly) else 0.0,
        "ing_tail": pct(has(r",\s(\w+ing)\s[^,;:]{4,}[.?]$")),
        "participle_start": pct(has(r"^[A-Z]\w+ing\b(?!\s+(is|are|was|were))", 0)),
        "ai_vocab": pct(has(AI_VOCAB)),
        "nominal": pct(sum(1 for w in words if sum(1 for x in w if re.search(r"(tion|sion|ment|ness|ity)$", x.lower()) and len(x) > 6) >= 2)),
        "triplet": pct(has(r"\b\w+(?: \w+)?, \w+(?: \w+)?,? (and|or) \w+")),
        "notonly": has(NOTONLY),
        "copula_avoid": has(HEDGE_COPULA),
        "signpost": has(SIGNPOST),
        "len_run": best,
    }
    details = {
        "retired": [s for s in sents if re.search(RETIRED, s, re.I)],
        "gadget": [s for s in sents if re.search(GADGET, s, re.I)],
        "stance": [s for s in sents if re.search(STANCE, s, re.I)],
        "dash": [s for s in sents if re.search(r"[—–]|--", s)],
        "ai_vocab": [s for s in sents if re.search(AI_VOCAB, s, re.I)],
        "signpost": [s for s in sents if re.search(SIGNPOST, s, re.I)],
        "ing_tail": [s for s in sents if re.search(r",\s(\w+ing)\s[^,;:]{4,}[.?]$", s)],
        "copula_avoid": [s for s in sents if re.search(HEDGE_COPULA, s, re.I)],
        "notonly": [s for s in sents if re.search(NOTONLY, s, re.I)],
        "triplet": [s for s in sents if re.search(r"\b\w+(?: \w+)?, \w+(?: \w+)?,? (and|or) \w+", s)],
    }
    return m, details, N, nwords, lens


def report(m, details, N, nwords, lens, verbose=False):
    print(f"\n{N} sentences, {nwords} words, {len(lens)} measured")
    if N < 40:
        print("Short text: percentage metrics are unreliable below about 40 sentences. Read the flags as hints, and trust the dash, vocabulary, signpost and tail checks over the rates.")
    print()
    print(f"{'Metric':52s} {'draft':>8s} {'Will':>8s}  band")
    print("-" * 84)
    flags = []
    for key, (label, target, lo, hi, unit) in TARGETS.items():
        v = m[key]
        fmt = "{:8.1f}" if unit != "n" else "{:8.0f}"
        ok = lo <= v <= hi
        mark = "" if ok else "  <-- outside"
        print(f"{label:52s} {fmt.format(v)} {fmt.format(target)}  {lo:g}-{hi:g}{mark}")
        if not ok:
            flags.append((key, label, v))
    print()
    deciles = st.quantiles(lens, n=10) if len(lens) >= 10 else []
    if deciles:
        print("Sentence-length deciles  draft:", [round(q) for q in deciles])
        print("                         Will: ", [10, 13, 16, 19, 22, 25, 28, 32, 39])
    print()
    if not flags:
        print("No metric outside Will's band. Read it once more as him anyway.")
    else:
        print(f"{len(flags)} metric(s) outside the band:")
        for key, label, v in flags:
            print(f"  - {label}")
            if key in ("sent_sd", "para_sd", "len_run", "short_share", "long_share"):
                print("      Variance problem. Rewrite sentences; do not splice in fragments or bolt clauses on.")
            if key == "stance":
                print("      Too many hedges. He concedes once per section and then commits. Cut the qualifiers; keep the claim verbs.")
            if key == "retired":
                print("      'We may be early, but we are not wrong' is retired at Will's request, both halves. Say what would prove the view wrong instead.")
            if key == "gadget":
                print("      Manufactured cleverness (SKILL.md section). Delete the sentence; if something is lost, state it plainly.")
            if key == "claim_verb":
                print("      Judgments should be stated as his ('we believe', 'in our opinion'), or if high, some of these are padding.")
            if key == "we":
                print("      Too impersonal (or, if high, too chatty for a paper section). Check who is making the claims.")
            if key == "dash":
                print("      He has never published a dash. Comma, semicolon, colon, or parentheses.")
    if verbose:
        for key in ("retired", "gadget", "stance", "dash", "ai_vocab", "signpost", "copula_avoid", "notonly", "ing_tail"):
            if details.get(key):
                print(f"\n[{key}]")
                for s in details[key][:12]:
                    print("  *", s)
    return flags


def recompute_from_corpus(folder: str):
    files = sorted(f for f in glob.glob(os.path.join(folder, "*.md")) if "SOURCE" not in os.path.basename(f))
    text = "\n\n".join(open(f, encoding="utf-8", errors="ignore").read() for f in files)
    m, details, N, nwords, lens = analyse(text)
    print(f"Corpus: {len(files)} files")
    report(m, details, N, nwords, lens)
    print("\nPaste these into TARGETS if the corpus has changed materially:")
    for key in TARGETS:
        print(f"  {key:18s} {m[key]:.2f}")


PERSONAL_OVERRIDES = {
    # Emails and posts: shorter, plainer, more one-line paragraphs; keep every hard check.
    "sent_mean": 13.0, "sent_sd": 8.0, "long_share": 0.0, "short_share": 40.0, "para_sd": 4.0, "para_mean": 1.5,
    "para_1_share": 70.0, "we": 0.0, "digit": 10.0, "claim_verb": 0.0, "roughly": 0.0, "semicolon": 0.0, "colon": 0.0, "paren": 0.0,
}

def apply_register(register):
    if register != "personal":
        return
    for key, val in PERSONAL_OVERRIDES.items():
        label, target, lo, hi, unit = TARGETS[key]
        if key in ("sent_mean", "sent_sd", "para_sd", "para_mean"):
            TARGETS[key] = (label + " [personal]", target, val, hi, unit)
        elif key in ("short_share", "para_1_share"):
            TARGETS[key] = (label + " [personal]", target, lo, val, unit)
        elif key == "claim_verb":
            TARGETS[key] = (label + " [personal]", target, 0.0, 15.0, unit)
        else:
            TARGETS[key] = (label + " [personal]", target, val, hi, unit)


if __name__ == "__main__":
    if "--register" in sys.argv:
        i = sys.argv.index("--register"); reg = sys.argv[i + 1] if i + 1 < len(sys.argv) else "letter"
        sys.argv = sys.argv[:i] + sys.argv[i + 2:]
        apply_register(reg)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--corpus" in sys.argv:
        recompute_from_corpus(args[0])
        sys.exit(0)
    if not args:
        print(__doc__)
        sys.exit(1)
    draft = open(args[0], encoding="utf-8", errors="ignore").read()
    m, details, N, nwords, lens = analyse(draft)
    flags = report(m, details, N, nwords, lens, verbose="--verbose" in sys.argv)
    sys.exit(0)
