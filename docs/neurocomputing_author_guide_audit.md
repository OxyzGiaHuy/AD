# Neurocomputing author-guide audit

Checked: 2026-07-22

Authoritative source: Elsevier/ScienceDirect, *Neurocomputing — Guide for
authors*:
`https://www.sciencedirect.com/journal/neurocomputing/publish/guide-for-authors`

Current requirements relevant to this repository:

- Peer review is single anonymized. Authors remain visible to reviewers.
- Editable LaTeX source is accepted. Double-column formatting is explicitly
  permitted for LaTeX submissions.
- The abstract must be concise, factual, stand alone, and at most 250 words.
- Supply 1--7 English keywords.
- Highlights are encouraged as a separate editable file: 3--5 items, each at
  most 85 characters including spaces.
- Number article sections and subsections; do not number the abstract.
- Use numbered references in order of appearance; consistent formatting is
  sufficient at initial submission, and DOI links are encouraged.
- CRediT contributions and a competing-interest declaration are required.
- The guide requests a biography of at most 100 words and a passport-type
  photograph for every author as separate editable/image files.
- Editable figures/tables and the underlying LaTeX sources must accompany the
  submission. Vector figures should be PDF or EPS with embedded fonts.
- Any generative-AI assistance must follow the current declaration policy and
  remain under author review and responsibility.

Repository consequences:

- `cas-dc` is acceptable; a forced switch back to single-column is unnecessary.
- The 250-word abstract gate remains valid.
- `highlights.txt` is the upload artifact; its text is mirrored in `main.tex`.
- An anonymous repository is not a journal requirement, but the code/data
  snapshot must remain reviewer-accessible and immutable.
- Author biographies, photographs, real metadata, and final approval of the AI
  disclosure remain author-supplied blockers.

Recheck this page on the actual submission date because Elsevier can update the
guide without changing the manuscript repository.
