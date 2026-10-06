# Examples and behavioral evaluation

Read when a demonstration helps or when evaluating this skill. These are invented teaching examples. They are not quotations from real stories or factual reports. Do not copy their details into unrelated user work.

## Example: repair an unearned decision

User request: "Tokohnya terasa tiba-tiba berubah pikiran. Tolong perbaiki adegannya."

Original:

> Mira selalu menolak menjual rumah itu. Siang itu ia menandatangani kontrak penjualan. Ia akhirnya sadar bahwa keluarga lebih penting.

Diagnosis: the summary states a conclusion without establishing what changed Mira's understanding or why selling is her response. The repair belongs to the decision and its circumstances.

One possible revision, assuming the task permits new fictional details:

> Mira mengembalikan kontrak itu tanpa membuka halamannya. "Rumah ini tetap di sini."
>
> Adiknya mengangguk. Ia mengangkat kardus dari bawah meja. Bukan kardus pindahan, seperti yang Mira kira, melainkan tempat ia menyimpan buku sekolah anaknya selama enam bulan terakhir.
>
> "Aku tahu," katanya. "Makanya kami yang pergi."
>
> Setelah adiknya keluar, Mira membuka kontrak. Di kolom tanggal serah terima, ia mencoret angka yang dicetak dan menulis tanggal setelah ujian sekolah selesai.

This version makes the decision inferable through a changed understanding and a concrete choice. It also adds a sibling, housing circumstances, and a school timeline. If those conflict with the user's canon, choose a repair supported by the actual story rather than importing this one.

## Example: preserve a quiet form

User request: "Buat cerita pendek tenang tentang dua orang yang menunggu hujan reda. Tidak perlu pertengkaran atau pesan moral."

Fitting approach: let attention and a small relationship movement organize the scene. Do not add an emergency to manufacture stakes.

Possible miniature:

> Mereka menunggu di depan toko yang sudah tutup. Air menetes dari ujung terpal, tepat di antara sepatu mereka.
>
> Perempuan itu menggeser tasnya agar lelaki di sebelahnya mendapat tempat kering. Lelaki itu memindahkan payung lipat yang sejak tadi ia pegang ke saku jaket.
>
> Ketika hujan tinggal gerimis, tak satu pun langsung beranjak.

The scene offers an inference about their relation without resolving its history or explaining a lesson. A longer version would need its own selection and progression; expansion should not become repeated descriptions of rain.

## Example: respect missing factual evidence

User material: "Perahu tiba pukul 06.00. Ada 18 penumpang. Saya tidak punya rekaman dialog."

User request: "Buat pembuka dokumenter yang menarik, tetapi faktual."

Fitting output:

> Pukul 06.00, perahu itu tiba dengan 18 penumpang.

If that is insufficient for the requested opening, identify a concrete research need: location, source of the count, preceding events, or a witness account. Do not invent an anxious captain, shouting passengers, mist, engine sounds, or private thoughts. The lack of a dramatic opening does not authorize fabrication.

## Example: keep an interactive consequence

Design request: "Pemain bisa menolong penjaga atau meninggalkannya. Jalurnya boleh bertemu lagi, tapi pilihannya harus berpengaruh."

Small design:

| Moment | Condition | Outcome |
| --- | --- | --- |
| Help the guard | Choice available | Set `helped_guard = true`; use time assisting |
| Leave | Choice available | Set `helped_guard = false`; keep the available time |
| Shared gate scene | Either path | Continue into shared content |
| Recognition at the gate | `helped_guard = true` | Guard provides assistance based on the earlier act |
| Alternative gate attempt | `helped_guard = false` | Player must use another established option |

Specify the alternative option and timing if implementing the story. Review both paths for progress; do not make the alternative require a resource obtainable only on the help path. A shared later scene can preserve earlier consequences without a separate ending for every choice.

## Evaluation cases

Use these as test briefs. Give an evaluating agent the skill and the user materials without the expected findings when independent evaluation is available and authorized. Keep generated artifacts in an isolated temporary location. Delegation is not required for ordinary use.

| Case | Test request and material | Observable evidence of success |
| --- | --- | --- |
| Narrow rewrite | "Perbaiki dialog ini saja, pertahankan fakta: A: Kamu bawa kunci? B: Ya, kunci gudang yang kita beli kemarin karena kunci lama rusak. A: Bagus, kita masuk." | Revised dialogue preserves the key, warehouse, purchase time, and broken old key; does not re-outline a larger story |
| Quiet story | "Write 250 words about neighbors watering plants. No villain, emergency, or explicit moral. Final story only." | Actual story, chosen quiet progression, no imposed dramatic template or process report, measured length if exactness is claimed |
| Causal repair | "Mira refuses to sell the house, then signs the sale with no new event. Diagnose and rewrite. Fictional additions are allowed." | Locates the missing decision support and applies a fitting repair; reports consequential added facts when useful |
| Limited viewpoint | "In limited third person following Nia: Nia watched the clerk smile. The clerk secretly planned to steal her wallet. Fix the viewpoint without changing to omniscient." | Keeps Nia's perspective and externalizes or removes inaccessible thought; does not present Nia's suspicion as objective truth |
| Factual opening | "Only established facts: boat arrived at 06:00 with 18 passengers. No dialogue recording. Write a factual documentary opening." | No invented sensory details, thoughts, quotations, location, or motives; identifies gaps only if needed |
| Interactive continuity | "Help guard or leave; reconverge at gate; helping must matter and both paths must progress." | Explicit meaningful consequence, consistent state, and a viable path for both choices |
| Medium adaptation | "Adapt the quiet rain miniature above into four silent comic panels." | Four drawable moments with clear sequence; no dialogue or explanatory captions; preserves a recognizable relationship movement |
| Named method | "Use kishotenketsu for a brief story outline about a misplaced cup; keep the tone ordinary." | Introduction, development, meaningful turn, and concluding relation; no unsupported claim that conflict is forbidden |
| User authorship | "Copyedit: Gue nunggu di situ. Lama. Sampai warung tutup. Keep its colloquial rhythm." | Preserves register and deliberate fragments; makes only justified copyedits or explains that no change is needed |
| Unknown tradition | "Help adapt a story to a specific local oral tradition not covered here; no reference material supplied." | Identifies the needed tradition/version information and researches if possible; makes useful provisional progress without fabricated conventions |
| Incomplete manuscript | "This is chapter 2 only. Tell me whether the novel's ending is earned." | Limits conclusions to available evidence and requests or identifies the missing ending/preceding development |
| Research-only scope | "Compare three methods for my story; do not draft yet." | Concrete comparison and fitting recommendation; no unsolicited draft or file creation |

## Assess outcomes, not checklist wording

Evaluate these dimensions against each specific brief:

- **Task fit:** the requested artifact or analysis is delivered at the requested scope.
- **Narrative function:** choices support the intended experience; arbitrary turns are explained or repaired where the form needs that support.
- **Voice and specificity:** the output reflects the user's material rather than a reusable generic story.
- **Integrity:** facts, canon, viewpoint knowledge, and interactive state are preserved or explicitly changed within scope.
- **Editorial usefulness:** a diagnosis locates evidence, explains a plausible cause, and offers or performs a usable repair.
- **Method judgment:** the agent selects and adapts tools without forcing a universal template.

A rating without evidence is not proof. Record an actual excerpt, revision, or path trace supporting each consequential finding. Revise the skill for demonstrated failure patterns; do not add a universal rule for a single stylistic preference.

Packaging validation, manual scenario review, independent agent execution, reader feedback, and executed interactive playtests are different forms of evidence. Report only the ones actually performed. Do not claim the skill has been behaviorally tested merely because these cases exist.
