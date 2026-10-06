# Storytelling

[![Validate skill](https://github.com/nonomnonom/storytelling/actions/workflows/validate.yml/badge.svg)](https://github.com/nonomnonom/storytelling/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Story development, writing, and revision across media.

Storytelling gives writing agents a practical repertoire for developing ideas, shaping scenes, diagnosing narrative problems, and producing revisions. It works with the story's existing voice, characters, facts, and intended experience.

## Capabilities

- Develop premises, characters, relationships, scenes, dialogue, and endings.
- Diagnose problems with viewpoint, pacing, structure, continuity, and motivation.
- Revise a draft while preserving the choices that matter to the work.
- Adapt stories for prose, screen, stage, comics, audio, oral performance, and interactive media.
- Research factual context and unfamiliar storytelling traditions.

The references bring together structural models, drafting methods, and approaches to narrative craft. Each approach includes guidance on when it fits and where its limits matter. Method selection follows the story and its purpose.

## Installation

Install with the [Skills CLI](https://github.com/vercel-labs/skills) using Node.js and npm:

```bash
npx skills add nonomnonom/storytelling
```

The CLI supports Claude Code, Codex, Cursor, OpenCode, and other agents listed in its documentation. Use `--agent` to select target agents and `--global` for a personal installation across projects.

For manual installation, clone or download the repository:

```bash
git clone https://github.com/nonomnonom/storytelling.git
```

Place the complete `storytelling` folder in the skills directory documented by your agent. Keep `SKILL.md` and `references/` together so the supporting guides remain accessible.

## Compatibility

The package uses the open [Agent Skills format](https://agentskills.io/specification). Its core instructions are Markdown with YAML metadata and have no model-provider dependency. `agents/openai.yaml` supplies optional interface metadata for hosts that use it.

Discovery, installation paths, and invocation syntax depend on the host. For an agent without native skill support, provide `SKILL.md` as instructions and make the referenced files accessible through its context or file tools.

## Usage

Ask your agent to use the storytelling skill with a draft, an idea, or a specific narrative problem. Include the medium and any choices the revision should preserve. If your host offers a skill picker or explicit invocation command, use its supported mechanism.

```text
Use the storytelling skill to diagnose and revise this scene.
Preserve the limited viewpoint, the ending, and the narrator's informal voice.
```

```text
Use the storytelling skill to adapt this story into six silent comic panels.
Keep the central relationship and make the turning point readable through action.
```

Prompts and output can use the language of the project. In hosts that support automatic skill selection, the package can also be selected from its description.

## Reference library

| Guide | Focus |
| --- | --- |
| [Methods](references/methods.md) | Selecting and applying storytelling approaches |
| [Craft](references/craft.md) | Character, scene, dialogue, viewpoint, voice, and endings |
| [Media and purposes](references/media-and-purposes.md) | Medium-specific writing, factual narratives, and interactive stories |
| [Diagnosis and revision](references/diagnosis-and-revision.md) | Connecting narrative symptoms to causes and concrete repairs |
| [Research and traditions](references/research-and-traditions.md) | Sources, cultural context, factual integrity, and originality |
| [Examples and evaluation](references/examples-and-evaluation.md) | Worked examples and scenarios for evaluating behavior |

[SKILL.md](SKILL.md) contains the working instructions and routes to the references relevant to each task.

## Development

Writing guidance requires no Python dependencies. To validate package changes, use Python 3.12 or later and run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

GitHub Actions runs these checks for pushes and pull requests. They cover metadata, local links, reference navigation, and validator behavior. Narrative quality and audience response require evaluation of the actual work.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

Original repository content is available under the [MIT License](LICENSE). Referenced books, articles, and other third-party materials retain their own rights and terms. Sources are linked from the relevant guides.
