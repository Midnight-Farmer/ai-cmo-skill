#!/usr/bin/env python3
"""
Initialize a new AI-CMO client folder structure.

Usage:
    init-client.py <client-name> --path <base-path>

Example:
    init-client.py acme-corp --path clients/

Creates the full client directory structure with template files:
    clients/acme-corp/
    ├── .claude/CLAUDE.md
    ├── knowledge/
    │   ├── 00-client-overview.md
    │   ├── voice-guidelines.md
    │   ├── personas-storybrand.md
    │   ├── goals-and-benchmarks.md
    │   └── whats-working.md
    ├── tracking/
    │   ├── content-log.csv
    │   ├── performance.csv
    │   └── revenue-attribution.csv
    ├── content/our-content/
    ├── content/competitors/
    ├── transcripts/
    └── outputs/
        ├── monthly-briefs/
        └── weekly-briefs/
"""

import sys
import shutil
from pathlib import Path


def find_templates_dir():
    """Find the templates directory relative to this script."""
    script_dir = Path(__file__).resolve().parent
    # Templates are in assets/templates/ within the skill directory
    templates_dir = script_dir.parent / "assets" / "templates"
    if templates_dir.exists():
        return templates_dir
    # Fallback: check the old _templates location
    workspace_root = script_dir.parent.parent
    old_templates = workspace_root / "_templates"
    if old_templates.exists():
        return old_templates
    return None


def init_client(client_name, base_path):
    """Create client folder structure and copy templates."""
    client_dir = Path(base_path).resolve() / client_name

    if client_dir.exists():
        print(f"Error: Client directory already exists: {client_dir}")
        return False

    templates_dir = find_templates_dir()

    # Create directory structure
    dirs = [
        ".claude",
        "knowledge",
        "tracking",
        "content/our-content",
        "content/competitors",
        "transcripts",
        "outputs/monthly-briefs",
        "outputs/weekly-briefs",
    ]

    for d in dirs:
        (client_dir / d).mkdir(parents=True, exist_ok=True)
        print(f"  Created {d}/")

    # Map template files to destinations
    template_map = {
        # Knowledge files
        "00-client-overview.md": "knowledge/00-client-overview.md",
        "voice-guidelines.md": "knowledge/voice-guidelines.md",
        "personas-storybrand.md": "knowledge/personas-storybrand.md",
        "goals-and-benchmarks.md": "knowledge/goals-and-benchmarks.md",
        "whats-working.md": "knowledge/whats-working.md",
        # Tracking files
        "content-log.csv": "tracking/content-log.csv",
        "performance.csv": "tracking/performance.csv",
        "revenue-attribution.csv": "tracking/revenue-attribution.csv",
        # Client CLAUDE.md
        "CLIENT-CLAUDE.md": ".claude/CLAUDE.md",
    }

    if templates_dir:
        for src_name, dest_path in template_map.items():
            src = templates_dir / src_name
            dest = client_dir / dest_path
            if src.exists():
                shutil.copy2(src, dest)
                print(f"  Copied {src_name} -> {dest_path}")
            else:
                print(f"  Warning: Template not found: {src_name}")
    else:
        print("  Warning: Templates directory not found. Creating empty files.")
        for dest_path in template_map.values():
            dest = client_dir / dest_path
            if dest_path.endswith(".csv"):
                # Create CSV headers
                if "content-log" in dest_path:
                    dest.write_text("content_id,date_published,platform,format,title_description,content_url,theme_topic,hook_used,cta_type,created_by,status,notes\n")
                elif "performance" in dest_path:
                    dest.write_text("content_id,date_measured,views,reach,likes,comments,shares,saves,link_clicks,follows,engagement_rate,performance_score,notes\n")
                elif "revenue" in dest_path:
                    dest.write_text("lead_id,lead_date,lead_name,lead_source,platform,content_id,first_touch,last_touch,lead_status,close_date,project_type,revenue,notes\n")
            else:
                dest.write_text(f"# {dest_path.split('/')[-1].replace('.md', '').replace('-', ' ').title()}\n\n[To be completed during onboarding]\n")

    # Replace placeholder in CLAUDE.md
    claude_md = client_dir / ".claude" / "CLAUDE.md"
    if claude_md.exists():
        content = claude_md.read_text()
        display_name = client_name.replace("-", " ").title()
        content = content.replace("[Client Name]", display_name)
        content = content.replace("[client-name]", client_name)
        claude_md.write_text(content)

    print(f"\nClient '{client_name}' initialized at {client_dir}")
    print("\nNext: Run through the onboarding interview to populate knowledge files.")
    return True


def main():
    if len(sys.argv) < 4 or sys.argv[2] != "--path":
        print("Usage: init-client.py <client-name> --path <base-path>")
        print("\nExample:")
        print("  init-client.py acme-corp --path clients/")
        sys.exit(1)

    client_name = sys.argv[1]
    base_path = sys.argv[3]

    print(f"Initializing client: {client_name}")
    print(f"Location: {base_path}\n")

    if init_client(client_name, base_path):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
