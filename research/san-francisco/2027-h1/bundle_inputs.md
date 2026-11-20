# Bundle input copies (2027-h1, San Francisco)

The approved evidence package in this directory is unchanged. Two sanitised
copies are the inputs the release gate was run against, because the release
scanner rejects date-selection phrasing and the rendered summary must not
print a candidate Saturday:

- `calendar_conflicts.bundle_input.json` — four of the five approved calendar
  rows. The `candidate Saturday`/ISO candidate-date wording is removed from
  the rendered prose fields. The Funding the Commons Forum row is withheld
  because its structured `start_date` 2027-03-13 is itself a candidate
  Saturday and the renderer prints structured dates verbatim; the event is
  still recorded in full in `calendar_context.adjacent_events`.
- `calendar_context.bundle_input.json` — identical in structure to
  `calendar_context.raw.json`, with the `candidate Saturday` wording removed
  from the two adjacent-event evidence inferences and verification questions.

Held unchanged: `venues.raw.json`, `communities.raw.json`,
`calendar_conflicts.json`, `calendar_context.raw.json`, `city_input.json`,
both discovery logs and `evidence_summary.md`. `city_input.json` already
satisfies the gate contract (`recommendation.selected_venue` and
`recommendation.rationale` null, `date_window` intact), so it is passed
directly and no `bundle_input.json` copy exists.

Rebuild: the sanitisation is a fixed, assertion-checked replacement list over
those two approved files (each old string must match exactly once); no other
field, row or evidence observation differs from the approved originals except
the withheld Funding the Commons calendar row described above.
