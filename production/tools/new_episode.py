"""Создать рабочую папку нового эпизода Honest Lies в production.

Использование:
    python production/tools/new_episode.py <N> <slug>

Пример:
    python production/tools/new_episode.py 8 camp-century

Создаёт D:/YouTube-Studio/production/honest-lies/ep-<N>/ :
    00-script/          ← всё сценарное: brief, en-script-v1/final, sound-vo, clean-script, udochka
    01_vo/  02_characters/  03_generated/  04_music/  05_footage/  06_montage/  07_thumbnail/  09_final_assets/
и кладёт в 00-script шаблоны из production/templates/.
Существующую папку не трогает — только досоздаёт недостающее, файлы не перезаписывает.
"""
import os
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

PRODUCTION = Path(os.environ.get("HL_PRODUCTION", "D:/YouTube-Studio/production/honest-lies"))
ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = [ROOT / "production" / "templates"]
MEDIA = ["01_vo", "02_characters", "03_generated", "04_music", "05_footage", "06_montage", "07_thumbnail", "09_final_assets"]


def main():
    if len(sys.argv) != 3 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    n, slug = int(sys.argv[1]), sys.argv[2]
    ep = PRODUCTION / f"ep-{n}"
    script = ep / "00-script"
    script.mkdir(parents=True, exist_ok=True)
    for d in MEDIA:
        (ep / d).mkdir(exist_ok=True)
    copied = []
    for tpl in TEMPLATES:
        for f in tpl.iterdir():
            dst = script / f.name
            if f.is_file() and not dst.exists():
                shutil.copy2(f, dst)
                copied.append(f.name)
    print(f"ok: {ep} ({slug})")
    print("  шаблоны:", ", ".join(copied) if copied else "уже были")


if __name__ == "__main__":
    main()
