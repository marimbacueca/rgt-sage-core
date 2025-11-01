import hashlib, json, re
from pathlib import Path

manifest = Path("RGT_Sage_v3.6.1_MANIFEST.json")
data = manifest.read_text(encoding="utf-8")
m = json.loads(data)

def compute_sha256_excluding_hashline(p: Path) -> str:
    t = p.read_text(encoding="utf-8")
    # remove the first line that starts with "SHA256"
    t_nohash = re.sub(r"^SHA256 .*?\n", "", t, count=1, flags=re.M)
    return hashlib.sha256(t_nohash.encode("utf-8")).hexdigest()

ok = True
for f in m["files"]:
    p = Path(f["name"])
    h = compute_sha256_excluding_hashline(p)
    if h != f["sha256"]:
        print("MISMATCH:", p, h, "!=", f["sha256"])
        ok = False
print("OK" if ok else "FAIL")
