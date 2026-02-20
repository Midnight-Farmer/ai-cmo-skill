# Planning Procedures

Detailed procedures for generating monthly and weekly content plans.

## Monthly Plan

### When to Create
Last week of the previous month, or first 2-3 days of the new month. Monthly plans set the strategic direction that weekly plans execute against.

### Process

1. **Read client context:**
   - Client's `.claude/CLAUDE.md`
   - All knowledge files in `knowledge/`

2. **Review recent performance:**
   - Read `knowledge/whats-working.md` for current patterns
   - Check `knowledge/goals-and-benchmarks.md` for 90-day goals and current priorities
   - If `tracking/performance.csv` has recent data, analyze last 30 days for trends

3. **Check for an existing monthly plan:**
   - Look in `outputs/monthly-briefs/` for the current month
   - If one exists, you're updating — note what's changed since it was written

4. **Generate the plan using the Monthly Plan Template** (see `output-formats.md` for the full template):
   - Set a monthly theme aligned with the 90-day goal
   - Define 2-3 strategic objectives
   - Break into 4 weekly themes with content types and topics
   - Include a hypothesis to test each week
   - Define production planning (shoot days, assets needed, B-roll gaps)
   - Set metrics targets with current baselines
   - Propose 2 tests to run with clear success criteria
   - Align key messages with messaging pillars from `voice-guidelines.md`

5. **Save the plan:**
   - Markdown: `outputs/monthly-briefs/YYYY-MM-monthly-plan.md`
   - If client has a Google Drive path configured, also save DOCX or Google Doc there

### Planning Principles for Monthly Plans

- Anchor everything to the 90-day goal. If a content piece doesn't advance a strategic objective, question whether it belongs.
- Balance what's proven (from `whats-working.md`) with what needs testing. Roughly 70% proven approaches, 30% experiments.
- Think about production efficiency — group similar content types for batch filming days.
- Be specific about what "success" looks like for each test. "More engagement" is not a success metric. "15%+ engagement rate on educational Reels" is.

---

## Weekly Plan

### When to Create
Monday morning (or end of previous week). Weekly plans are the tactical execution layer of the monthly strategy.

### Process

1. **Read client context:**
   - Client's `.claude/CLAUDE.md`

2. **Check for a current monthly plan:**
   - Look in `outputs/monthly-briefs/` for this month's plan
   - If one exists, identify which week you're in and align with that week's theme and content types
   - If no monthly plan exists, generate the weekly plan independently based on knowledge files

3. **Review what's working:**
   - Read `knowledge/whats-working.md` for hook patterns, best times, top content types
   - Check `knowledge/goals-and-benchmarks.md` for current campaign focus

4. **If performance data exists**, review last week's performance:
   - Read recent entries in `tracking/performance.csv`
   - Note what performed well and what underperformed
   - Adjust this week's approach based on learnings

5. **Generate the plan using the Weekly Plan Template** (see `output-formats.md` for the full template):
   - Set a weekly focus aligned with the monthly theme (or standalone if no monthly plan)
   - Create 3-7 content pieces (varies by client's posting cadence)
   - For each piece: platform, format, topic, hook, key message, CTA, and a "why this works" note referencing `whats-working.md`
   - Write video scripts for any video content (hook/setup/value/CTA structure)
   - Create a combined production shot list for efficient filming
   - Write caption starting points (hook line + direction)
   - List key messages aligned with messaging pillars
   - Identify specific metrics to watch this week

6. **Save the plan:**
   - Markdown: `outputs/weekly-briefs/YYYY-MM-DD-weekly-plan.md`
   - If client has alternate output formats configured (Google Sheets, DOCX, etc.), follow those instructions from client `.claude/CLAUDE.md`

### Planning Principles for Weekly Plans

- Every content piece needs a clear "why" — connect it to what's working or what you're testing.
- Hooks are the most important element. Reference proven hook patterns from `whats-working.md`.
- Scripts should be concise and action-oriented. The human team will adapt them during filming.
- Shot lists should optimize for efficiency — group similar setups together for batch filming.
- Caption starting points give direction without being final copy. The hook line matters most.
