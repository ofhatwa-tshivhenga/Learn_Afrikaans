import csv
import json
from pathlib import Path
from typing import Dict


import requests


CACHE_PATH = Path("word_pairs_cache.json")

def get_word_pairs(csv_url: str, use_cache: bool = True) -> Dict[str, str]:
    """
    Fetch English→Afrikaans word pairs from a CSV URL (Google Sheets publish link).
    Returns dict like {"english": "afrikaans"}. Also caches to JSON for offline use.
    """
    if use_cache and CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass # fall through to refetch

    try:
        resp = requests.get(csv_url, timeout=15)
        resp.raise_for_status()
        content = resp.content.decode("utf-8-sig") # handle BOM if present


        reader = csv.reader(content.splitlines())
        rows = list(reader)
        # Try to detect header
        if rows and ("english" in rows[0][0].lower() or "afrikaans" in ",".join(rows[0]).lower()):
            rows = rows[1:]

        pairs = {}
        for r in rows:
            if not r:
                continue

            # Accept either [english, afrikaans] or with extra cols
            english = (r[0] if len(r) > 0 else "").strip()
            afrikaans = (r[1] if len(r) > 1 else "").strip()
            if english and afrikaans:
                pairs[english] = afrikaans

        if not pairs:
            raise ValueError("No valid word pairs found in CSV")

        # Cache
        try:
            CACHE_PATH.write_text(json.dumps(pairs, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

        return pairs
    except Exception:
        # Fallback to cache if available
        if CACHE_PATH.exists():
            try:
                return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
            except Exception:
                pass
                # Nothing else we can do
        return {}