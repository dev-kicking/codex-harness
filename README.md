# Codex Harness

> **English** | [한국어](README.ko.md)

A friendly starting point for turning a blank or existing codebase into a repeatable **Codex development workflow**.

## What is this?

Codex Harness is **not an Android library** and it does not change your app just by being installed.

It is a reusable skill that helps Codex design project-specific instructions for work that repeats: architecture reviews, Compose UI work, Gradle troubleshooting, test planning, code review, release preparation, and more.

Think of it like this:

```text
codex-harness repository = the reusable blueprint
Your Android project       = the place where Codex creates project-specific rules
```

## The simple workflow

1. Start with a new or existing project.
2. Install Harness into that project's `.codex/skills/` directory.
3. Open Codex from the project root.
4. Ask Codex to use Harness for your project.
5. Review the generated project-specific skills and commit the ones you want to keep.

> Installing Harness only copies the reusable Harness skill. It does not automatically create a team or edit your Android code.

## Quick start for an Android project

### 1. Download this repository once

```bash
git clone https://github.com/dev-kicking/codex-harness.git ~/tools/codex-harness
```

### 2. Install it into your Android project

Replace `/path/to/MyAndroidApp` with your project folder.

```bash
cd ~/tools/codex-harness
python3 scripts/install_harness.py \
  --scope project \
  --target /path/to/MyAndroidApp
```

You can use the same command for a blank project or a project that already has code.

### 3. Open Codex in the Android project

```bash
cd /path/to/MyAndroidApp
```

Then open your normal Codex workflow from this folder.

### 4. Give Codex a clear first request

For an existing Android project:

```text
Use Harness to set up a reusable development workflow for this Android project.
First inspect the current codebase and Gradle configuration.
Then decide which reusable skills are actually needed for Kotlin, Compose, architecture, build tooling, and QA.
Create only the necessary files under .codex/skills/ and docs/harness/.
Keep parallel edits safe by assigning non-overlapping file ownership.
```

For a blank Android project, add your intended stack and goal:

```text
Use Harness to design a reusable workflow for a new Android app.
The stack will be Kotlin, Jetpack Compose, Hilt, Room, Retrofit, and Gradle.
The app will help users manage ...
Create the smallest useful set of skills and a team specification.
```

## What Codex may create

After reviewing your project, Codex may add only the artifacts that are useful:

```text
MyAndroidApp/
├── .codex/
│   └── skills/
│       ├── harness/                # installed shared blueprint
│       ├── android-orchestrator/   # project-specific workflow
│       ├── compose-ui/             # only when useful
│       ├── gradle-build/           # only when useful
│       └── android-qa/             # only when useful
├── docs/
│   └── harness/
│       └── android-development/
│           └── team-spec.md
└── AGENTS.md                       # only when concise repo-wide guidance helps
```

Review these files before committing. They are guidance for Codex, not application source code.

## Use it day to day

Once project-specific skills exist, ask Codex for work normally. Be specific about the outcome:

```text
Use the Android workflow to add offline caching for the user profile API.
Update the data layer, add tests, and have the QA step review error states.
```

Harness is most useful when a project has recurring work or needs clear review and handoff rules. For a small one-off edit, ask Codex directly instead.

## Update the shared Harness skill

To refresh only the installed shared Harness skill after this repository changes:

```bash
cd ~/tools/codex-harness
git pull
python3 scripts/install_harness.py \
  --scope project \
  --target /path/to/MyAndroidApp \
  --force
```

`--force` replaces only `.codex/skills/harness/`. Keep your project-specific skills outside that folder so they remain intact.

## Validate this repository

```bash
python3 scripts/validate.py
```

## License and attribution

Apache License 2.0. This repository is independently adapted from [revfactory/harness](https://github.com/revfactory/harness) and [SaehwanPark/meta-harness](https://github.com/SaehwanPark/meta-harness). See [NOTICE](NOTICE) for attribution.
