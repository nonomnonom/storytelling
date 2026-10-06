# Storytelling

[![Validate skill](https://github.com/nonomnonom/storytelling/actions/workflows/validate.yml/badge.svg)](https://github.com/nonomnonom/storytelling/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An AI agent skill for developing, writing, diagnosing, adapting, and revising stories across media and traditions.

The skill helps an agent solve the user's actual narrative problem: find the cause, choose a fitting approach, and produce a usable draft or revision. It preserves the user's voice, established facts, and intended experience.

## What it covers

- Ideas, premises, characters, relationships, scenes, dialogue, viewpoint, pacing, and endings.
- Prose, film, television, animation, theatre, comics, audio, oral performance, interactive fiction, and games.
- Documentary, journalism, memoir, biography, historical narratives, and persuasive communication.
- Dramatic and journey structures, development methods, alternative organizing principles, and research into cultural traditions.
- Concrete diagnosis and revision, factual integrity, continuity, and meaningful interactive consequences.

The library includes approaches associated with Aristotle, Freytag, Syd Field, Campbell, Vogler, Harmon, Save the Cat!, Dan Wells, Hauge, Truby, Snowflake, MICE, Story Grid, kishotenketsu, jo-ha-kyu, Le Guin, and Propp. Sources and limitations accompany the summaries. Some formal methods require consulting their full sources when a detailed application is requested.

This is a broad working repertoire, not an exhaustive catalogue of every storytelling tradition. The agent is instructed to research unfamiliar methods when needed and to avoid forcing every story into one formula.

## Install

The repository root is the complete skill folder. Install the whole folder so its references remain available.

For a Codex personal skill, clone into your skills directory:

```bash
git clone https://github.com/nonomnonom/storytelling.git ~/.codex/skills/storytelling
```

On Windows PowerShell:

```powershell
git clone https://github.com/nonomnonom/storytelling.git "$env:USERPROFILE\.codex\skills\storytelling"
```

If your skills directory is configured elsewhere, use that location. For another agent, use its documented skill-loading mechanism or provide `SKILL.md` and the relevant reference files as context. This repository does not install an application, browser connector, or writing engine.

No Python dependency is required to use the writing instructions. Python and PyYAML are needed only for repository validation.

## Use

Invoke `$storytelling` in a host that supports named skills. The skill can also be discovered automatically through its description when the host supports that behavior.

```text
Use $storytelling to diagnose this scene and rewrite it.
Preserve the limited viewpoint, the ending, and my informal voice.
```

```text
Gunakan $storytelling untuk membantu memperbaiki bagian tengah cerita ini.
Pertahankan tokoh dan akhir yang sudah ada. Berikan revisi konkret.
```

```text
Use $storytelling to adapt this story into six silent comic panels.
```

```text
Use $storytelling to design a branching story where earlier choices
affect later scenes, even when the paths reconverge.
```

Supply the material and any constraints that matter: audience, medium, language, length, factual status, existing canon, and what should be preserved. The agent should ask only for consequential missing information and start at the current stage of the work.

## How the skill works

The entrypoint establishes the working brief, selects the relevant references, and guides writing and review. References are loaded as needed rather than all at once.

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent entrypoint, task selection, workflow, and delivery checks |
| [Methods](references/methods.md) | Method selection, application, sources, and limits |
| [Craft](references/craft.md) | Character, scene, dialogue, viewpoint, information, voice, and endings |
| [Media and purposes](references/media-and-purposes.md) | Writing for different media, factual work, interactive stories, and communication |
| [Diagnosis and revision](references/diagnosis-and-revision.md) | Symptoms, causes, repairs, and downstream consistency |
| [Research and traditions](references/research-and-traditions.md) | Evidence, cultural context, source use, and originality |
| [Examples and evaluation](references/examples-and-evaluation.md) | Invented demonstrations and behavioral test briefs |
| [Agent metadata](agents/openai.yaml) | Display name, short description, and example invocation |

## Validate changes

Use Python 3.12 or later. From the repository root:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

The validator checks the skill frontmatter, optional UI metadata, local Markdown links, and discoverability of the reference files. GitHub Actions runs the same commands for pushes and pull requests.

These checks verify packaging and navigation. They do not prove literary quality, reader response, completeness of cultural coverage, or the availability of external source URLs. Behavioral evaluation briefs are provided; their presence does not mean an independent agent evaluation has been performed.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include demonstrated fixes to agent behavior, better source-backed guidance, and additional methods with a clear purpose and scope.

## License and sources

The original repository content is licensed under [MIT](LICENSE). Linked books, articles, studies, and cultural materials remain governed by their own rights and terms. They are referenced, not bundled or relicensed by this repository.
