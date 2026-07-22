import re
from pathlib import Path
from urllib.parse import urlparse

_ROOT = Path(__file__).resolve().parent.parent
_CONFIG = _ROOT / "properdocs.yml"


def _read_site_url():
    text = _CONFIG.read_text(encoding="utf-8")
    match = re.search(r'^\s*site_url:\s*["\']?([^"\'\s]+)', text, re.MULTILINE)
    if not match:
        raise RuntimeError(f"Could not find 'site_url:' in {_CONFIG}")
    return match.group(1)


SITE_URL = _read_site_url().rstrip("/") + "/"
PATH_PREFIX = urlparse(SITE_URL).path or "/"