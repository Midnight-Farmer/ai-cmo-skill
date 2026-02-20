# Workflow Cadences

How the AI-CMO system operates on a weekly and monthly rhythm.

## Your First Week (New Users)

Just finished onboarding? Here's how to get rolling:

**Days 1-2: Review your plans**
- Read through your monthly brief and weekly plan in `outputs/`
- These are strategy documents for *you* — they tell you what to create, not the final copy
- Pick the 1-2 easiest content pieces from your weekly plan to start with

**Days 2-3: Create your first content**
- Use the weekly plan as direction — it gives you the topic, hook, format, and key message
- Film, write, or design the piece. It doesn't need to be perfect — getting something out matters more.

**Days 3-5: Publish and log**
- Post your content on the recommended platform
- Log it: `log content for [client]` — this takes about 1 minute per piece

**End of week: Check in**
- After a few days, log metrics for your published content: `log performance for [client]`
- Get next week's plan: `weekly plan for [client]`

**After your first month:**
- Run `analyze performance for [client]` to see what's working
- Run `update whats working for [client]` to capture insights
- Run `monthly plan for [client]` to get next month's strategy
- From here, you're in the regular weekly/monthly rhythm described below

---

## Weekly Workflow

| Day | Task | Time |
|-----|------|------|
| Monday | Review last week's performance, generate weekly plan | 30-45 min |
| Tuesday-Thursday | Log content as it's scheduled/published | 5 min per piece |
| Friday | Quick check on week's metrics, note any standouts | 10 min |

### Monday Workflow Detail

1. **Performance Review (15 min):**
   - Check metrics from last week's content
   - Log performance data for any content that's hit the 7-day mark
   - Note what performed above or below expectations

2. **Weekly Planning (15-30 min):**
   - Run `weekly plan for [client]` (or `generate week` for Typefully-integrated clients)
   - Review the generated plan
   - Adjust based on any real-time considerations (trends, events, client updates)
   - If using Typefully, review and schedule drafts

---

## Monthly Workflow

| When | Task | Time |
|------|------|------|
| Last week of month | Monthly performance review | 30 min |
| Last week of month | Update what's working | 15 min |
| First 2-3 days of month | Generate monthly plan | 30 min |

### Month-End Review Detail

1. **Data Gathering (10 min):**
   - Ensure all content is logged in `content-log.csv`
   - Ensure all performance data is captured in `performance.csv`
   - Update any lead/revenue attribution data

2. **Pattern Analysis (10 min):**
   - Run `analyze performance for [client]`
   - Review the analysis for new insights

3. **Update Insights (5 min):**
   - Run `update whats working for [client]`
   - Review proposed changes and approve

4. **Goal Check (5 min):**
   - Compare current metrics against 90-day goals in `goals-and-benchmarks.md`
   - Note whether on track, ahead, or behind

5. **Next Month Planning:**
   - Run `monthly plan for [client]`
   - The new monthly plan should reflect learnings from the review

---

## Quarterly Workflow

Every 90 days:
1. Review the full quarter's performance
2. Assess progress against 90-day goals
3. Set new 90-day goals (update `goals-and-benchmarks.md`)
4. Major update to `whats-working.md`
5. Consider strategy pivots based on cumulative data
6. Generate revenue report if tracking leads

---

## Multi-Client Management

When managing multiple clients:
- Stagger monthly reviews so they don't all fall on the same day
- Keep a running note of which clients need attention this week
- Prioritize performance reviews for clients with active campaigns or testing
- Cross-pollinate insights: patterns that work for one client in a similar industry might work for another (but always validate against the specific client's data)
