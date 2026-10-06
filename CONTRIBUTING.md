# Contributing

Contributions should help an agent make better storytelling decisions or solve a demonstrated writing problem. Keep the skill broad enough to respect different media, traditions, and user intentions.

## Propose a change

For a behavior problem, include the user request, the smallest relevant material, what the agent did, and what failed. Identify the actual effect on the story or user task. Remove private or sensitive material before sharing it.

For a method or tradition, provide an appropriate source and explain its purpose, context, limitations, and relevance to an agent's decisions. Distinguish a structural model, drafting process, analytical theory, genre convention, and performance tradition.

Do not copy copyrighted manuals or source passages into the repository. Write original summaries and link to sources. Only contribute material you have the right to distribute under the repository's MIT license. Linked third-party material retains its own terms.

## Make the change

1. Put shared workflow and routing in `SKILL.md`; put substantial conditional guidance in the relevant reference.
2. Preserve the user's scope, voice, factual integrity, and current stage. Do not add a universal rule for a single stylistic preference.
3. Keep every reference discoverable from the entrypoint or another reachable reference.
4. Update documentation when usage, structure, or validation changes.
5. Run the validation commands in the [README](README.md).

Avoid creating scripts, dependencies, or files without a concrete recurring purpose. The instructions should remain usable without development tools.

## Show evidence

For instruction changes, use a relevant brief from [Examples and evaluation](references/examples-and-evaluation.md), or provide a more suitable one. Include the actual draft, revision, diagnosis, or path trace needed to assess the result.

When possible, evaluate the skill on a fresh agent context without supplying the desired answer. Report whether evidence came from packaging checks, manual review, independent agent execution, reader feedback, or an executed playtest. Do not describe a test brief as a completed test.

For validator changes, add a focused test of the affected packaging invariant and run the suite. External source availability is a separate research concern; do not make offline validation depend on network access.

## Open a pull request

Explain the problem, resulting behavior, and validation performed. List material limitations or unavailable checks. Keep a change focused enough that a reviewer can assess its effect.
