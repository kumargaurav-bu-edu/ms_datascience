# AGENTS.md

Personal data-science MS learning/practice repo (Boston University, Semester 3). Plain Python 3 + Jupyter notebooks: no build system, no tests, no CI, no package manifest, no third-party deps. This is study material, not a software product — the recurring tasks are notebook annotation and quiz JSON generation.

## Layout

- `week_MMDDYYYY/<COURSECODE>/` — one folder per week and course. Courses seen here: `DX701O1`, `DX702O1`, `DX799O1`. A new week = a new `week_<MMDDYYYY>/` root folder.
  - `w<N>_<course>_objective.md` — the week's learning objectives (course-provided). Source of truth for what homework/annotations must cover.
  - `imp_urls.md` — the student's curated links and mnemonics; freeform notes.
  - `homework/kumar_gaurav_week<N>_dx799O1.ipynb` — homework notebooks, named `lastname_firstname_week<N>_dx<NNN>O<N>.ipynb`.
- `data/` — CSV datasets used by notebooks, but **gitignored** (`*.csv` rule in `.gitignore`). They exist locally; never assume they exist in a fresh clone or reference them as git-tracked.
- `generic_quiz.py` — stdlib-only interactive quiz runner (`python3 generic_quiz.py <path>/quiz_questions.json`).

## Quiz generation (the main recurring task)

- Quiz JSON must conform to the spec in `whatisexpected.md`, which also drives the grader: 25–35 questions, levels 1–3 only, 8 allowed `question_type`s, one section per learning objective with the coverage table, 4–6 concrete keywords for open-ended questions, "concrete not abstract" answers, 3-part explanations. Generate `quiz_questions.json` in the relevant week/course folder.
- Run any quiz with `python3 generic_quiz.py <week_folder>/<course>/quiz_questions.json`.
- The old `week_08282026/DX799O1/quiz.json` predates the spec (all level 2, MCQ-only) — do not use it as a format template.

## Notebook annotation

- `markp_ins.md` defines the required per-cell Markdown format for notebooks ("Cell X — <title>" with why/what/how, alternatives, key concepts, issues, connection to next step, and result interpretation including H₀/H₁). Notebooks are meant to be self-contained study guides, not just code.
- Do not rewrite working code just to add explanations — that is an explicit rule in `markp_ins.md`.

## Git

- Work on the current personal branch (`semester3-home`). Sibling branches belong to other collaborators (`semester3-pan`, `main`, `dev`, `home-dev`, `pan-dev`) — don't commit to them.
- No CI or enforced conventions; commits are made per week.