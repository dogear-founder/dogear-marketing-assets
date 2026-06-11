"""Founder's Rating row renderer — CD-ported glyphs (icons.jsx), app colors.
Usage: build_rating_row(label, kind, value, value_str) -> RGBA 760x86
Kinds: 'star' (#E0B547), 'pepper' (#BB5038), 'tear' (#5E86A0).
Fills are ink-area based. Requires cd_glyphs.pkl alongside + EB Garamond fonts.
Glyph source: design_handoff_rating_flow/reference/icons.jsx (verbatim paths,
pepper scaled 1.34x about center per ICON_TF). Hairline rgba(color,0.45) on dark bg.
See Dogear marketing chat 2026-06-11 for full provenance."""
# (full renderer code archived in chat; re-paste from transcript when needed)
