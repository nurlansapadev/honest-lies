# Honest Lies

YouTube channel about the mechanics of deception — espionage, industrial and
ideological theft, propaganda, information warfare, patent schemes.

Every episode lives in the gap between the official version and what actually
happened. The spine is not a country or an era — it's the **mechanism of the lie**.

- **Format:** 20–30 min documentary, voiceover only, faceless channel
- **Audience:** US/UK, 50–75, educated, done with self-congratulation
- **Voice:** Arny — a retired American who loves his country enough to want the truth
- **Channel:** youtube.com/@HonestLiesSpy

> "I tell you how the machinery of deception works — in the voice of an American
> off a New York pier who reads the primary sources, not the headlines."

---

## Как читать этот репозиторий

Репозиторий — не код, а рабочая база канала: правила, роли, воркфлоу и досье
эпизодов. Порядок чтения в новой сессии:

1. **`CLAUDE.md`** — что за проект, нарратор, подниша, помощники, структура папок
2. **`MEMORY.md`** — принятые решения и правила «больше не делаем»
3. **`CHANGELOG.md`** — история эпизодов, метрики, маркер сползания ниши
4. **`production/new-episode.md`** — воркфлоу эпизода: 16 фаз и карта файлов проекта

`AGENTS.md` — указатель на `CLAUDE.md`, не копия.

## Что где лежит

| Папка | Что там |
|---|---|
| `channel/` | Нарратор, подниша, ключи, стиль (`style/`), помощники (`staff/`) |
| `production/` | Воркфлоу, голос и звук, видеоряд, музыка, промпты |
| `episodes/` | Рабочие папки эпизодов (**не в git**) и заготовки тем в `next-idea/` |
| `deliverables/` | Финальные документы эпизодов — в git, как контекст для новых чатов |
| `artifacts/` | Ссылки и заметки на медиа; сами файлы — в `D:\YouTube-Studio\` |

**Медиафайлы в репозиторий не попадают.** Исходники, проекты монтажа и рендеры
живут локально в `D:\YouTube-Studio\[ep-folder]\`, здесь — только ссылки и заметки.

## Скиллы

Скиллы HyperFrames ставятся отдельно и в git не идут (`.agents/`, `.claude/skills/`).
Версии пинит `skills-lock.json`.

```
npx skills add heygen-com/hyperframes
```
