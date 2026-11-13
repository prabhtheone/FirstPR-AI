"""Single source of truth for FirstPR AI's five agent skills."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SKILLS_DIR = PROJECT_ROOT / "skills"

SKILL_FOLDERS = {
    "Issue Analyzer": "issue-analyzer",
    "Codebase Explorer": "codebase-explorer",
    "Test Planner": "test-planner",
    "PR Mentor": "pr-mentor",
    "Contribution Safety Checker": "contribution-safety-checker",
}


def load_skill(skill_name):
    """Load a skill's Markdown instructions and return (content, error)."""
    if not isinstance(skill_name, str):
        return None, "Unknown skill selected. Please select a valid skill."

    folder = SKILL_FOLDERS.get(skill_name)
    if folder is None:
        return None, "Unknown skill selected. Please select a valid skill."

    skill_path = SKILLS_DIR / folder / "SKILL.md"
    try:
        content = skill_path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return None, f"Skill file not found: {skill_path}"
    except OSError as error:
        return None, f"Could not read the skill file: {error}"

    if content.startswith("---"):
        _, separator, remainder = content.partition("---")
        if separator:
            _, separator, content = remainder.partition("---")
            if not separator:
                return None, f"Invalid YAML frontmatter in skill file: {skill_path}"
            content = content.strip()

    if not content:
        return None, f"The skill file is empty: {skill_path}"

    return content, None
