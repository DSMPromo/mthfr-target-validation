#!/usr/bin/env python3
"""
MTHFR Target Validation — Language Compliance Scanner
======================================================
Scans all project documents for overclaiming, promotional, or
non-defensible language. Run this before every commit or publication.

Usage:  python validate_language.py
        python validate_language.py --fix  (auto-fix known patterns)

Author: Igor Mihaljko / DSM.Promo
License: CC BY-NC-SA 4.0
"""
import re, sys, os
from pathlib import Path
from datetime import datetime

# Files to scan
SCAN_FILES = [
    "README.md",
    "docs/RESEARCH_PAPER_DRAFT.md",
    "CONTRIBUTING.md",
    "DISCLAIMER.md",
    "outreach/email_template.md",
    "outreach/target_researchers.md",
    "alphafold/jobs/submission_plan.md",
    "analysis/analysis_workflow.md",
    "analyze.py",
    "generate_figures.py",
    "MTHFR_AlphaFold_Analyzer.ipynb",
]

# ============================================================
# RULES: Each rule has a pattern, description, severity,
# suggested replacement, and context exclusions
# ============================================================
RULES = [
    # --- CRITICAL: Brand/Title ---
    {
        "id": "C01",
        "pattern": r"Gene Therapy Platform",
        "severity": "CRITICAL",
        "description": "Project is a Target Validation Program, not a therapy platform",
        "suggestion": "Target Validation Program",
        "exclude_context": [],
    },
    {
        "id": "C02",
        "pattern": r"Billions of Lives",
        "severity": "CRITICAL",
        "description": "Promotional language inappropriate for validation program",
        "suggestion": "Remove or replace with population carrier statistics",
        "exclude_context": [],
    },
    {
        "id": "C03",
        "pattern": r"mthfr-gene-therapy-project",
        "severity": "CRITICAL",
        "description": "Old repository name — should be mthfr-target-validation",
        "suggestion": "mthfr-target-validation",
        "exclude_context": [],
    },

    # --- HIGH: Causal overclaiming ---
    {
        "id": "H01",
        "pattern": r"\bproves\b",
        "severity": "HIGH",
        "description": "Computational predictions cannot prove — use 'supports' or 'is consistent with'",
        "suggestion": "supports / is consistent with / demonstrates (for other companies' data only)",
        "exclude_context": ["not proof", "cannot prove", 'not "proves"', "not \"proves\"", "-- not"],
    },
    {
        "id": "H02",
        "pattern": r"\bconfirms\b",
        "severity": "HIGH",
        "description": "Our predictions do not confirm — use 'supports' or 'is consistent with'",
        "suggestion": "supports / is consistent with",
        "exclude_context": ["experimentally confirmed", "literature confirms", 'not "proves"', "not \"confirms\"", "-- not"],
    },
    {
        "id": "H03",
        "pattern": r"\bdemonstrates\b",
        "severity": "HIGH",
        "description": "Too strong for computational predictions — use 'suggests' or 'is consistent with'",
        "suggestion": "suggests / is consistent with",
        "exclude_context": ["VERVE", "PCSK9", "Beam", "Casgevy", "YOLT", "Luxturna", "literature demonstrates", 'not "proves"', "not \"demonstrates\"", "-- not"],
    },
    {
        "id": "H04",
        "pattern": r"root cause",
        "severity": "HIGH",
        "description": "Presupposes causation — use 'candidate upstream factor' or 'genetic variant'",
        "suggestion": "candidate upstream factor / genetic variant",
        "exclude_context": [],
    },
    {
        "id": "H05",
        "pattern": r"clinical implications?\b",
        "severity": "HIGH",
        "description": "Too strong for computational work — use 'experimental indication hypothesis'",
        "suggestion": "experimental indication hypothesis",
        "exclude_context": ["wide-ranging"],  # OK when quoting published review
    },
    {
        "id": "H06",
        "pattern": r"clinical target",
        "severity": "HIGH",
        "description": "Presumes clinical relevance — use 'candidate disease pathway' or 'experimental indication'",
        "suggestion": "candidate disease pathway / experimental indication hypothesis",
        "exclude_context": [],
    },
    {
        "id": "H07",
        "pattern": r"\bexplains\b.*treatment.resistant",
        "severity": "HIGH",
        "description": "Cannot explain treatment resistance from structural modeling",
        "suggestion": "may be relevant in / warrants investigation in defined subgroups",
        "exclude_context": [],
    },
    {
        "id": "H08",
        "pattern": r"blindness reversed|complete blindness",
        "severity": "HIGH",
        "description": "Overstates case report — use 'case report: visual recovery associated with'",
        "suggestion": "case report: metabolic correction associated with visual recovery",
        "exclude_context": [],
    },
    {
        "id": "H09",
        "pattern": r"\bbroken enzyme\b|\bbroken\b.*enzyme",
        "severity": "HIGH",
        "description": "Too judgmental — use 'variant enzyme' or 'enzyme carrying variant alleles'",
        "suggestion": "variant enzyme",
        "exclude_context": [],
    },

    # --- MEDIUM: Presumptive/promotional ---
    {
        "id": "M01",
        "pattern": r"\bwill restore\b|\bwill address\b|\bwill correct\b",
        "severity": "MEDIUM",
        "description": "Presumptive future — use 'may' or 'could potentially'",
        "suggestion": "may / could potentially / contingent on experimental validation",
        "exclude_context": [],
    },
    {
        "id": "M02",
        "pattern": r"Fully reversible",
        "severity": "MEDIUM",
        "description": "Too absolute — biological reversibility is context-dependent",
        "suggestion": "Potentially reversible",
        "exclude_context": [],
    },
    {
        "id": "M03",
        "pattern": r"change lives|save lives|help billions",
        "severity": "MEDIUM",
        "description": "Promotional language — reframe as hypothesis-generating research",
        "suggestion": "Remove or reframe as research contribution",
        "exclude_context": [],
    },
    {
        "id": "M04",
        "pattern": r"breaks? this cycle permanently",
        "severity": "MEDIUM",
        "description": "Too definitive about therapeutic outcome",
        "suggestion": "could potentially interrupt this cycle",
        "exclude_context": [],
    },
    {
        "id": "M05",
        "pattern": r"\baffected\b.*(?:population|billion|million)",
        "severity": "MEDIUM",
        "description": "'Affected' presupposes disease — use 'carrying these variants' or 'reported associations'",
        "suggestion": "carrying these variants / populations with reported associations",
        "exclude_context": ["WHO", "CDC"],  # OK when citing WHO/CDC disease burden stats
    },
    {
        "id": "M06",
        "pattern": r"\bplatform\b",
        "severity": "MEDIUM",
        "description": "'Platform' implies tested reusable system — use 'program' or 'design' for our work",
        "suggestion": "program / design / approach",
        "exclude_context": ["delivery platform", "gene editing platform", "LNP platform",
                           "validated gene editing platforms", "open-source platform"],
    },
    {
        "id": "M07",
        "pattern": r"ancestral.*healthy|healthy.*sequence",
        "severity": "MEDIUM",
        "description": "Presupposes WT = healthy — use 'reference allele' or 'majority allele'",
        "suggestion": "reference allele sequence / majority allele",
        "exclude_context": [],
    },
    {
        "id": "M08",
        "pattern": r"\bcure\b",
        "severity": "MEDIUM",
        "description": "Too definitive — this is a validation program, not a therapy",
        "suggestion": "correction / modulation",
        "exclude_context": ["primary hyperoxaluria"],  # OK when citing other papers
    },
    {
        "id": "M09",
        "pattern": r"suffer\b|suffering\b|preventable symptoms",
        "severity": "MEDIUM",
        "description": "Emotional appeal — use neutral scientific language",
        "suggestion": "Remove or reframe neutrally",
        "exclude_context": [],
    },
]


def scan_file(filepath, rules):
    """Scan a file against all rules. Returns list of violations."""
    violations = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except (FileNotFoundError, UnicodeDecodeError):
        return violations

    for line_num, line in enumerate(lines, 1):
        for rule in rules:
            matches = list(re.finditer(rule["pattern"], line, re.IGNORECASE))
            for match in matches:
                # Check exclusions
                excluded = False
                for exc in rule.get("exclude_context", []):
                    if exc.lower() in line.lower():
                        excluded = True
                        break
                if not excluded:
                    violations.append({
                        "file": str(filepath),
                        "line": line_num,
                        "rule_id": rule["id"],
                        "severity": rule["severity"],
                        "description": rule["description"],
                        "match": match.group(),
                        "context": line.strip()[:120],
                        "suggestion": rule["suggestion"],
                    })
    return violations


def main():
    print("=" * 70)
    print("MTHFR Target Validation — Language Compliance Scanner")
    print(f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)
    print()

    project_root = Path(".")
    all_violations = []

    for filepath in SCAN_FILES:
        fp = project_root / filepath
        if fp.exists():
            violations = scan_file(fp, RULES)
            all_violations.extend(violations)

    # Sort by severity
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2}
    all_violations.sort(key=lambda v: (severity_order.get(v["severity"], 3), v["file"], v["line"]))

    if not all_violations:
        print("ALL CLEAR — No language violations found.")
        print()
        print("Checked:")
        for f in SCAN_FILES:
            status = "OK" if (project_root / f).exists() else "MISSING"
            print(f"  [{status}] {f}")
        print()
        print(f"Rules checked: {len(RULES)}")
        print("Result: PASS — Ready for publication")
        return 0

    # Print violations
    critical = [v for v in all_violations if v["severity"] == "CRITICAL"]
    high = [v for v in all_violations if v["severity"] == "HIGH"]
    medium = [v for v in all_violations if v["severity"] == "MEDIUM"]

    print(f"VIOLATIONS FOUND: {len(all_violations)}")
    print(f"  CRITICAL: {len(critical)}")
    print(f"  HIGH:     {len(high)}")
    print(f"  MEDIUM:   {len(medium)}")
    print()

    for v in all_violations:
        icon = {"CRITICAL": "!!!", "HIGH": " ! ", "MEDIUM": " ~ "}[v["severity"]]
        print(f"[{icon}] {v['severity']} | {v['rule_id']} | {v['file']}:{v['line']}")
        print(f"      Match: \"{v['match']}\"")
        print(f"      Context: {v['context']}")
        print(f"      Issue: {v['description']}")
        print(f"      Suggestion: {v['suggestion']}")
        print()

    print("-" * 70)
    print(f"RESULT: {'FAIL' if critical or high else 'WARN'}")
    if critical or high:
        print("Fix CRITICAL and HIGH issues before publication.")
    else:
        print("Only MEDIUM issues remain. Review manually — some may be acceptable in context.")
    print("-" * 70)

    return 1 if critical or high else 0


if __name__ == "__main__":
    sys.exit(main())
