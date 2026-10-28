# Honest Lies

YouTube channel about the mechanics of deception — espionage, industrial and
ideological theft, propaganda, information warfare, patent schemes.

Every episode lives in the gap between the official version and what actually
happened. The spine is not a country or an era — it's the **mechanism of the lie**.

- **Format:** 28–33 min documentary, voiceover only, faceless channel
- **Audience:** US/UK, 50–75, educated, done with self-congratulation
- **Voice:** Arny — a retired New Yorker who loves his country enough to want the truth
- **Channel:** youtube.com/@HonestLiesSpy

> "I tell you how the machinery of deception works — in the voice of an American
> off a New York pier who reads the primary sources, not the headlines."

---

## Как читать репозиторий

Это штаб сценария (hl-script): правила, роли, воркфлоу, память и план тем. Порядок чтения в новой сессии:

1. **`CLAUDE.md`** — проект, нарратор, подниша, помощники, структура папок
2. **`MEMORY.md`** — действующие решения
3. **`channel/history/INDEX.md`** — что уже рассказано
4. **`production/new-episode.md`** — воркфлоу эпизода и карта файлов

## Что где лежит

| Папка | Что там |
|---|---|
| `channel/` | Кто и о чём: ниша, ключи, история канала (`history/`), стиль (`style/`), нарратор и помощники (`staff/`) |
| `episodes/` | Что дальше: `content-plan.md`, карточки тем (`next-idea-cards/`), отработанные карточки (`completed/`) |
| `production/` | Как делаем: воркфлоу, голос, видеоряд, музыка, реестр, шаблоны, `new_episode.py`, LUT, промпты |

Артефакты эпизодов в репозиторий не попадают — они в `D:\YouTube-Studio\production\honest-lies\ep-N\`.

## Скиллы

Скиллы HyperFrames ставятся отдельно и в git не идут (`.agents/`, `.claude/skills/`); версии — `skills-lock.json`.

```
npx skills add heygen-com/hyperframes
```
