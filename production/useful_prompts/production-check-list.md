# Шпаргалка Nurlan — что за чем делать

> Коротко: что делаю я, что говорю Claude, где лежит результат.
> Подробности каждого шага — `production/new-episode.md`.
> Папка эпизода: `D:\YouTube-Studio\production\honest-lies\ep-N\`

---

## 1. Тема → досье (hl-script)

- [ ] Новый чат, включить **Web search**
- [ ] «Новый эпизод: ep-N, тема …» → Claude проходит **ворота А** и создаёт папку эпизода
- [ ] Homer + Nolan собирают досье → `00-script\brief.md`
- [ ] 🔒 **Я утверждаю досье**
- [ ] Черновик упаковки (**ворота Б**): название, обложка, первые строки описания

## 2. Сценарий RU (hl-script)

- [ ] Обсуждаем → «пиши сценарий» → Claude пишет `00-script\ru-script-v1.txt` *(v1 больше не трогаем)*
- [ ] Homer проверяет факты v1 → правки в чат
- [ ] Копирую v1 → `ru-script-v2.txt`, правлю в Notepad++
- [ ] «Сделал правки, проверь в файле v2» → Claude даёт замечания в чат. Много правок — Claude соберёт v3 после моего «да»
- [ ] Повторяю, пока не доволен → сам называю файл **`ru-script-final.txt`**
- [ ] Claude сам: разбор v1 → final (учится на моих правках) + реестр `02_characters\cast.json`

## 3. Фото по реестру (я)

- [ ] Открываю `02_characters\cast.json` → ищу фото людей, мест, техники
- [ ] Кладу в `02_characters\` с именами `<id>_01.jpg`, `<id>_02.jpg`…

## 4. Сценарий EN → разметка голоса (hl-script)

- [ ] «Lingo, переводи» → `en-script-v1.md`
- [ ] «Ed, почисти язык» → «Nolan, разбери структуру» → правлю
- [ ] «Voicer, разметь» → `sound-vo.md`, **`11-labs-voice.txt`**, `clean-script.txt`
- [ ] 🔒 **Я утверждаю текст под запись**

## 5. Озвучка (я)

- [ ] `11-labs-voice.txt` → ElevenLabs **без изменений текста**, только паузы
- [ ] Готовый wav → `01_vo\Episode-NN.wav`
- [ ] «Озвучка записана» → Claude делает `vo-whisper.json` и сверяет `en-script-final.md`

## 6. Шот-листы и материал

- [ ] «Делай шот-листы» → `00-script\shots\` (архив, генерация, надписи)
- [ ] Сток — мои скрипты → `05_footage\`
- [ ] Гравюры (Gem HonestLiesIllustrator), хук в Veo → `03_generated\`
- [ ] Музыка (Suno) → `04_music\`

## 7. Монтаж (VideoEditor_2.0)

- [ ] Чат в VideoEditor_2.0: «Новый эпизод: ep-N» → дальше он ведёт сам
- [ ] Готовое видео → `06_montage\ep-N_vK.mp4`
- [ ] «Монтаж завершён» в hl-script

## 8. Упаковка и публикация (video-wrapper)

- [ ] Копирую в упаковщик 📦 3 файла: `brief.md` · `en-script-final.md` · `vo-whisper.json`
- [ ] Обложка → `07_thumbnail\`, название, описание, главы, теги — в video-wrapper
- [ ] Публикация

## 9. Закрытие (hl-script)

- [ ] «Закрываем эпизод» → Claude дописывает `ep-summary.md`, `CHANGELOG.md`, `MEMORY.md`
- [ ] Следующая тема → `episodes/next-idea/`
- [ ] Commit и push — **я сам**
- [ ] Через 30 дней — метрики в `CHANGELOG.md`
