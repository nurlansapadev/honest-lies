# Фонетические замены — EP-NUR-01
> Вставлять в ELEVENLABS-строки вместо оригинала. Проверять на 1–2 дублях перед финальной записью.

## Имена людей

| Оригинал | Замена для движка | Произношение |
|----------|------------------|--------------|
| Gene Wheaton | Gene Wheaton | обычное, ок |
| Richard Secord | Richard Secord | обычное, ок |
| George Bush | George Bush | обычное, ок |
| Richard Helms | Richard Helms | обычное, ок |
| Bob Woodward | Bob Woodward | обычное, ок |
| Donald Smith | Donald Smith | обычное, ок |
| Robert Krongard | Robert KRON-gard | ударение на KRON |
| William Cottrell Jr. | William COT-trel Junior | движок может съесть «Jr.» |
| Rockwell | Rockwell | обычное, ок |

## Места

| Оригинал | Замена для движка | Произношение |
|----------|------------------|--------------|
| Tehran | Teh-RAN | ударение на второй слог, «а» как в ran |
| Vosough Square | Voh-SOOG Square | «gh» не читается, ударение на SOOG |
| Doshan Tappeh | Doh-SHAHN Tah-PEH | два слова, оба с ударением на последний слог |
| Langley | Langley | обычное, ок |
| Iran | ih-RAN | не «EYE-ran» — американский вариант ih-RAN |
| Iranian | ih-RAY-nee-an | обычное, но проверить |

## Аббревиатуры

| Оригинал | Замена для движка | Как должно звучать |
|----------|------------------|-------------------|
| CIA | C-I-A | побуквенно — движок обычно знает |
| NSA | N-S-A | побуквенно — проверить |
| IBEX | EYE-becks | как слово, не побуквенно |
| SAVAK | SAH-vak | как слово, ударение на первый слог |
| MAAG | M-A-A-G | побуквенно (Military Assistance Advisory Group) |
| CID | C-I-D | побуквенно |
| WaPo | Washington Post | не сокращать — движок может прочитать странно |

## Цифры и даты

| Оригинал | Замена для движка | Как должно звучать |
|----------|------------------|-------------------|
| 1976 | nineteen seventy-six | прописью — движок иногда читает как «one thousand» |
| 1974 | nineteen seventy-four | прописью |
| 1979 | nineteen seventy-nine | прописью |
| August 28th | August twenty-eighth | прописью безопаснее |
| 7 AM / 6:50 AM | six fifty in the morning | не цифры — читает неровно |
| $500 million | five hundred million dollars | прописью + слово dollars |
| $2 billion | two billion dollars | прописью |
| 80 F-14s | eighty F-14s | число прописью, «F-14» движок знает |
| 18,000 | eighteen thousand | прописью |
| 52 hostages | fifty-two hostages | прописью |

## Спорные слова (проверить отдельно)

| Слово | Риск | Что делать |
|-------|------|-----------|
| Mojahedin | мoh-jah-heh-DEEN | персидское — проверить, при необходимости: «moh-jah-heh-DEEN» |
| Shah | SHAH | обычно знает, но проверить — не «shay» |
| Ayatollahs | ay-ah-TOL-ahs | движок обычно знает |
| Watergate | Watergate | обычное, ок |

## Правило проверки
1. Прогони каждое сложное имя **отдельной строкой** в движке перед основной записью.
2. Если коверкает — вставь фонетику из этой таблицы.
3. Если фонетика тоже не работает — разбей слово дефисом: `Voh-SOOG`.
4. Заглавные буквы в фонетике = ударение.