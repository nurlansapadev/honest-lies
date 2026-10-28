# Реестр эпизода — люди, места, объекты (`cast.json`)

> Фаза 4 (`production/new-episode.md`). Делает Claude сразу после сохранения `en-script-final.txt`, без вопроса.
> Выход: `ep-N\02_characters\cast.json`.

## Зачем

Один раз и точно описать всё, что придётся показать: каждого человека, каждое место, каждый
объект с моделью и эпохой. Из реестра питаются VideoEditor_2.0 (паспорт эпизода, запросы `[НАЙТИ]`, карты `[КАРТА]`, генерация) и Video-Wrapper (лица для обложки).

## Что делает Claude

> **Только описание, без поиска материалов.** Где искать фото и есть ли архив — дело VideoEditor. Поле `archive` не заполняется, веб-поиск по фото не ведётся.

1. **Проходит `en-script-final.txt` целиком** и выписывает каждое упоминание: имена, роли без имени («директор ФБР» → кто именно), города, здания, базы, улицы, страны, технику, документы, логотипы и эмблемы.
2. **Описывает каждый пункт:**
   - **Люди:** полное имя, роль, годы, возраст на момент событий, `fame`, `face_policy`, внешность и одежда эпохи.
   - **Места:** английское название, координаты (десятичные градусы, 4 знака), страна (`country` — обязательно, у каждого места), что там стояло в нужный год. Для зданий — как выглядели тогда, а не сейчас.
   - **Объекты:** точная модель и год (не «машина», а «1984 Chevrolet Caprice»; не «самолёт», а «Lockheed C-130D on skis»). Анахронизмы и запреты (нет фото, копирайт) — одной строкой в `note`.
3. **Политика лица** (честность по лицам — принцип бренда): публичная фигура — только архив; малоизвестный — архив как референс для генерации; неизвестный — типаж или силуэт.
4. **Не меняет текст сценария.** Это не фактчек: расхождение, найденное попутно, — одной строкой Nurlan, решение за ним.
5. **Итог Nurlan — 2–3 строки:** сколько людей, мест и объектов, что спорно (анахронизм, копирайт, расхождение с фактами разведки).

## Схема `cast.json`

Ключи и названия — **по-английски** (так ждёт VideoEditor_2.0). Заметки (`note`) — по-русски.

```json
{
  "episode": "EP-NN · <title>",
  "slug": "ep-08-camp-century",
  "source": "en-script-final.txt",
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
- `kind` объекта: `building` · `vehicle` · `aircraft` · `ship` · `weapon` · `document` · `logo` · `other`.
- `places[].country` — **обязательно у каждого места**, английское название страны, как ключ в `countries` (и в `VideoEditor_2.0\data\countries.json`). По нему VideoEditor выбирает главную страну эпизода: побеждает страна с наибольшим числом мест; при равенстве выбирает Claude в VideoEditor, Nurlan подтверждает в паспорте. Каждая страна из `places` должна быть в блоке `countries`; спорные случаи (территории, сменившиеся границы) — в `note`.
- `files`: шаблон имени для фото в `02_characters\`: `<id>_01.jpg`, `<id>_02.jpg`…

## Совместимость с VideoEditor_2.0

- Блок `places` — **тот же формат, что `VideoEditor_2.0\data\places.json`** (`"Name": {lat, lon, aliases}`); лишние поля справочник игнорирует. Новые места переносятся туда целиком на шаге 0 VideoEditor.
- Блок `countries` — формат `data\countries.json` (`lang` + `words`).
- `map` — готовая точка для метки `[КАРТА: … | Name(lat, lon)]`.
- `people[].name + years` — контекст для запросов `[НАЙТИ]` («William Webster FBI 1985», а не «FBI director»).

## Кто читает `cast.json`

VideoEditor_2.0: паспорт эпизода, места и страны для карт, поиск и генерация кадров (`face_policy`). Video-Wrapper: лица для обложки. Заново людей не искать.
