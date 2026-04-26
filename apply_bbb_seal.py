"""
Atlas Roofing — BBB Seal Patch
================================
Replaces the existing "BBB A+ Rated" text trust-item with the official
BBB-hosted seal image (with link to your BBB profile) sitewide.

USAGE:
    1. Place this file in the ROOT of your local repo (next to index.html)
    2. Open a terminal/PowerShell IN that folder
    3. Run:  python apply_bbb_seal.py

It will scan all .html files and report what got changed.
Safe to run multiple times — it's idempotent (won't double-apply).
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

BBB_LINK_HREF = "https://www.bbb.org/us/oh/beachwood/profile/roofing-contractors/atlas-roofing-restoration-0312-92057214/#sealclick"
BBB_IMG_SRC = "https://seal-cleveland.bbb.org/seals/blue-seal-250-52-bbb-92057214.png"

SUBPAGE_SEAL = (
    '<div class="trust-item trust-item-seal">'
    f'<a href="{BBB_LINK_HREF}" target="_blank" rel="nofollow" '
    'aria-label="Atlas Roofing &amp; Restoration BBB A+ Accredited Business Profile">'
    f'<img src="{BBB_IMG_SRC}" '
    'alt="Atlas Roofing &amp; Restoration BBB Business Review — A+ Rated" '
    'loading="lazy" style="display:block;height:50px;width:auto;border:0;">'
    '</a></div>'
)

HOMEPAGE_SEAL = (
    '<div class="tb-item tb-item-seal">'
    f'<a href="{BBB_LINK_HREF}" target="_blank" rel="nofollow" '
    'aria-label="Atlas Roofing &amp; Restoration BBB A+ Accredited Business Profile">'
    f'<img src="{BBB_IMG_SRC}" '
    'alt="Atlas Roofing &amp; Restoration BBB Business Review — A+ Rated" '
    'loading="lazy" style="display:block;height:50px;width:auto;border:0;">'
    '</a></div>'
)

# Patterns we replace in subpages (two known variants)
SUBPAGE_VARIANTS = [
    '<div class="trust-item"><span class="trust-icon green">★</span> BBB A+ Rated</div>',
    '<div class="trust-item"><span>&#9733;</span> BBB A+ Rated</div>',
    '<div class="trust-item"><span>★</span> BBB A+ Rated</div>',
]

# Homepage uses .tb-item with inline SVG star icon — regex match
HOMEPAGE_PATTERN = re.compile(
    r'<div class="tb-item">'
    r'<div class="tb-icon green">'
    r'<svg viewBox="0 0 24 24"><path d="M12 2L15\.09 8\.26L22 9\.27L17 14\.14L18\.18 21\.02L12 17\.77L5\.82 21\.02L7 14\.14L2 9\.27L8\.91 8\.26L12 2Z"/></svg>'
    r'</div>'
    r'BBB A\+ Rated</div>'
)


def patch_file(path):
    """Patch a single HTML file. Returns (patched: bool, hits: int)."""
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, OSError):
        return False, 0

    if "seal-cleveland.bbb.org" in content:
        return False, 0  # already patched

    original = content
    hits = 0

    # Homepage pattern (inline SVG)
    new_content, n = HOMEPAGE_PATTERN.subn(HOMEPAGE_SEAL, content)
    if n:
        content = new_content
        hits += n

    # Subpage variants
    for variant in SUBPAGE_VARIANTS:
        if variant in content:
            n = content.count(variant)
            content = content.replace(variant, SUBPAGE_SEAL)
            hits += n

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True, hits
    return False, 0


def patch_generator(path):
    """Patch generate_pages.py so future page generations include the seal."""
    if not os.path.exists(path):
        return False
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if "seal-cleveland.bbb.org" in content:
        return False
    old = '<div class="trust-item"><span class="trust-icon green">★</span> BBB A+ Rated</div>'
    if old not in content:
        return False
    new = content.replace(old, SUBPAGE_SEAL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    return True


def main():
    print("Atlas Roofing — BBB Seal Patch\n" + "=" * 40)
    print(f"Scanning: {REPO_ROOT}\n")

    files_changed = 0
    total_hits = 0
    files_scanned = 0

    for root, _, files in os.walk(REPO_ROOT):
        # skip .git directory if present
        if ".git" in root.split(os.sep):
            continue
        for fname in files:
            if fname.endswith(".html"):
                path = os.path.join(root, fname)
                files_scanned += 1
                changed, hits = patch_file(path)
                if changed:
                    files_changed += 1
                    total_hits += hits

    # Patch generator
    gen_path = os.path.join(REPO_ROOT, "generate_pages.py")
    gen_patched = patch_generator(gen_path)

    print("--- Summary ---")
    print(f"HTML files scanned:    {files_scanned:,}")
    print(f"HTML files updated:    {files_changed:,}")
    print(f"Total replacements:    {total_hits:,}")
    print(f"generate_pages.py:     {'updated' if gen_patched else 'no change needed'}")
    print()
    if files_changed:
        print("✓ Done. Review changes in GitHub Desktop, then commit and push.")
    else:
        print("→ No changes needed (already patched).")


if __name__ == "__main__":
    main()
