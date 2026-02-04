import json
from pathlib import Path

PREF_FILE = Path("data/user_prefs.json")

def load_preferences():
    if PREF_FILE.exists():
        return json.loads(PREF_FILE.read_text())
    return {"categories": ["Technology"], "summary_type": "short"}

def save_preferences(prefs):
    PREF_FILE.parent.mkdir(exist_ok=True)
    PREF_FILE.write_text(json.dumps(prefs, indent=2))
