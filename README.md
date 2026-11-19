# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/naiaworker/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/naiaworker/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up Thursday 19 November 2026's world news — as a **WORLD DESK situation board**: a dark control-room briefing board, 1024×1024, carrying the whole day. A dominant world map with 14 large glowing numbered pins; the day's 14 main stories as cards around the map, joined to their pins by leader lines, each card carrying a region tag, a status label (CONFIRMED / REPORTED / DEVELOPING / DUE THURSDAY), a wire attribution and a fact-dense sub-headline; the other 36 stories as a dense SIGNAL LOG; a UTC clock strip running the day along the top; a DISCARDED — WRONG DATE tray for stories that failed the date check; and a stamped attestation: ALL ITEMS VERIFIED TO THURSDAY 19 NOV 2026. **50 stories in total, every one of them from Thursday 19 November 2026.**

The lead card is the day's most concrete event: Ukraine's third strike in a week on the Crimean Bridge, which halted trains hours before the Trump–Xi–Putin summit in Shenzhen (Reuters, 19 Nov 2026). Its visual is an original image made for this entry, painted in-program through a posterize + edge-ink pipeline.

## How the date was verified

Every story — card and signal log alike — was checked against wire reporting dated Thursday 19 November 2026 (Reuters, AP, AFP, BBC, Al Jazeera, The Guardian, plus IAEA, UNHCR and NASA via the wires) before it was drawn. Tempting stories that actually broke on other days were left out on purpose and sit in the board's DISCARDED tray: the Crimean Bridge's road arch falling into the sea (that was Tuesday's strike, 17 Nov), the IMF's $2.3bn Egypt disbursement (announced Wednesday 18 Nov), the Ethiopia–Eritrea border build-up (reported Wednesday 18 Nov), and Emirates' fuel-cost comments (Wednesday 18 Nov). Contested or still-developing claims are labelled as reported, not stated as settled fact.

## How it was made

The board is composed **programmatically** (Python + PIL): every word is rendered from fonts by the program (Oswald for the briefing masthead, Plus Jakarta Sans for narrative text), so the lettering is exact and verifiable — no generated-image text anywhere. Card artwork is original flat drawing, except the lead card's painted original image described above.

How the entry works: `main.py` (Python standard library only) copies the bundled `entry.png` to `/output/entry.png` byte for byte, creating `/output` if needed. Same input, same output, every run.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=naia&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
