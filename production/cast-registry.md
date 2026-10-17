# Реестр эпизода — люди, места, объекты (`cast.json`)

> Фаза 2.95 (`production/new-episode.md`). Делает Claude сразу после утверждения `ru-script-final.txt`.
> Выход: `ep-N\02_characters\cast.json`. В ту же папку Nurlan кладёт найденные фото — по именам из реестра.

## Зачем

Один раз и глубоко выписать всё, что придётся показать: каждого человека, каждое место, каждый
объект с точной моделью и эпохой. Дальше из реестра питаются все: шот-лист и `characters.json`
(фаза 9), запросы `[НАЙТИ]` и карты `[КАРТА]` в VideoEditor_2.0, поиск фото Nurlan.

## Что делает Claude

1. **Проходит `ru-script-final.txt` целиком** и выписывает каждое упоминание: имена, роли без имени («директор ФБР» → кто именно), города, здания, базы, улицы, страны, технику, документы, логотипы и эмблемы.
2. **Копает по каждому пункту** (веб-поиск обязателен):
   - **Люди:** полное имя, роль, годы, возраст на момент событий. **Есть ли архивное изображение и где** — Wikimedia Commons, NARA, Library of Congress, президентские библиотеки, официальные фото ведомств, пресса. Если нашлось — точный источник или ссылка и рабочий запрос. Если нет — так и пишется: `"exists": false`.
   - **Места:** английское название, координаты (десятичные градусы, 4 знака), страна (`country` — обязательно, у каждого места), что там стояло в нужный год. Для зданий — как выглядели тогда, а не сейчас.
   - **Объекты:** точная модель и год (не «машина», а «1984 Chevrolet Caprice»; не «самолёт», а «Lockheed C-130D on skis»), где есть фото.
3. **Политика лица** по `production/visuals-guide.md` («Честность по лицам»): публичная фигура — только архив; малоизвестный — архив как референс для генерации; неизвестный — типаж или силуэт.
4. **Не меняет текст сценария.** Это не фактчек: расхождение, найденное попутно, — одной строкой Nurlan, решение за ним.
5. **Итог Nurlan — 2–3 строки:** сколько людей, мест и объектов, у скольких есть архивное фото, чего не нашлось.

## Схема `cast.json`

Ключи и названия — **по-английски** (так ждёт VideoEditor_2.0). Заметки (`note`) — по-русски.

```json
{
  "episode": "EP-08 · <title>",
  "slug": "ep-08-camp-century",
  "source": "ru-script-final.txt",
  "era": "1959–1967",

  "countries": {
    "Greenland": {"lang": "da", "words": ["greenland", "thule", "camp century"]}
  },

  "places": {
    "Camp Century": {
      "lat": 77.1797, "lon": -61.1097,
      "aliases": ["Project Iceworm base"],
      "country": "Greenland",
      "type": "military base",
      "years": "1959–1967",
      "map": "Camp Century(77.18, -61.11)",
      "archive": {"exists": true, "where": ["US Army film 'Camp Century: City Under the Ice' (1961)"], "query": "Camp Century 1960 trench"},
      "files": "camp_century_NN.jpg",
      "note": "Траншеи под снегом; современных фото нет — только архив 1959–66"
    }
  },

  "people": [
    {
      "id": "frank_camper",
      "name": "Frank Camper",
      "role": "owner of the Mercenary School, FBI informant",
      "years": "b. 1946",
      "age_at_event": 39,
      "fame": "obscure",
      "archive": {"exists": true, "where": ["AP photo 1986, arrest"], "query": "Frank Camper mercenary school 1985"},
      "face_policy": "reference",
      "appearance": "white American man, late 30s, lean, short military haircut",
      "wardrobe": "woodland camouflage, 1980s",
      "files": "frank_camper_NN.jpg",
      "note": ""
    }
  ],

  "objects": [
    {
      "id": "c130d_skis",
      "name": "Lockheed C-130D Hercules (ski-equipped)",
      "kind": "aircraft",
      "years": "1959",
      "archive": {"exists": true, "where": ["USAF Museum"], "query": "C-130D ski Greenland 1959"},
      "files": "c130d_skis_NN.jpg",
      "note": ""
    }
  ]
}
```

**Значения полей:**
- `fame`: `famous` (узнаваемое лицо) · `known` (публичный, но малоизвестный) · `obscure` · `generic` (типаж: «агенты ФБР», «сикхские курсанты»).
- `face_policy`: `archive_only` (никогда не генерировать) · `reference` (генерация только по архивному фото) · `allowed` (типаж) · `silhouette` (со спины, без лица).
- `archive.exists`: `true` · `false` · `"unknown"` (не удалось проверить — с пометкой почему).
- `kind` объекта: `building` · `vehicle` · `aircraft` · `ship` · `weapon` · `document` · `logo` · `other`.
- `places[].country` — **обязательно у каждого места**, английское название страны, как ключ в `countries` (и в `VideoEditor_2.0\data\countries.json`). По нему VideoEditor выбирает главную страну эпизода: побеждает страна с наибольшим числом мест; при равенстве выбирает Claude в VideoEditor, Nurlan подтверждает в паспорте. Каждая страна из `places` должна быть в блоке `countries`; спорные случаи (территории, сменившиеся границы) — в `note`.
- `files`: шаблон имени для фото, которые кладёт Nurlan: `<id>_01.jpg`, `<id>_02.jpg`… Плоско, в корне `02_characters\`.

## Совместимость с VideoEditor_2.0

- Блок `places` — **тот же формат, что `VideoEditor_2.0\data\places.json`** (`"Name": {lat, lon, aliases}`); лишние поля справочник игнорирует. Новые места переносятся туда целиком на шаге 0 VideoEditor.
- Блок `countries` — формат `data\countries.json` (`lang` + `words`).
- `map` — готовая точка для метки `[КАРТА: … | Name(lat, lon)]`.
- `people[].name + years` — контекст для запросов `[НАЙТИ]` («William Webster FBI 1985», а не «FBI director»).

## Связь с `characters.json` (фаза 9)

`shots\characters.json` строится **из `cast.json`**: берутся люди с `face_policy` ≠ `archive_only`, к ним добавляются описания под генерацию. Заново людей не искать.
