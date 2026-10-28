# Шпаргалка Nurlan — что за чем делать

> Коротко: что делаю я, что говорю Claude, где лежит результат.
> Подробности каждого шага — `production/new-episode.md`.
> Папка эпизода: `D:\YouTube-Studio\production\honest-lies\ep-N\`

---

## 1. Тема → угол (hl-script) — мой единственный стоп

- [ ] Новый чат, включить **Web search**
- [ ] «Новый эпизод: ep-N, тема …» (+ досье content successor) → Claude: ворота А, папка эпизода, Homer + Nolan, `00-script\brief.md`
- [ ] 🔒 **Выбираю угол подачи** — Claude приносит его одним сообщением вместе с черновиком упаковки (название, 3 слова на превью)

## 2. Дальше Claude сам, без моих апрувов

- [ ] Сценарий сразу на английском: Homer · Nolan · Ed · гуманизатор → `en-script-v1.txt` (снимок) = **`en-script-final.txt`**
- [ ] `02_characters\cast.json`, `sound-vo.md`, `clean-script.txt`, `udochka.md`
- [ ] В чат — итог: объём, что поправили помощники, прощание удочки (+ запасные)

**Хочу поправить текст** — правлю `en-script-final.txt` в Notepad++ и пишу «поправил final» → Claude проверит и пересоберёт файлы для озвучки.

## 3. Озвучка, кадры, монтаж (VideoEditor_2.0)

- [ ] Чат в VideoEditor_2.0: «Новый эпизод: ep-N» → дальше он ведёт сам (озвучка скиллом `elevenlabs-vo`, шоты, поиск кадров, монтаж)
- [ ] Сток — мои скрипты → `05_footage\`; гравюры и Veo → `03_generated\`; музыка Suno → `04_music\`
- [ ] Готовое видео → `09_final_assets\ep-NN-final.mp4`

## 4. Упаковка и публикация (video-wrapper)

- [ ] Чат в video-wrapper: «Упаковка ep-N» → он сам читает папку эпизода
- [ ] Рабочее — `07_thumbnail\`; финал к загрузке — `09_final_assets\` (варианты `v-1`, `v-2`…)
- [ ] Публикация

## 5. Закрытие (hl-script)

- [ ] «Закрываем эпизод» → Claude: разбор v1 → final, история канала, `CHANGELOG.md`, `MEMORY.md`
- [ ] Следующая тема → `episodes/next-idea/`
- [ ] Commit и push — **я сам**
- [ ] Через 30 дней — метрики в `CHANGELOG.md`
