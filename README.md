# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/asfel307/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/asfel307/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

## The World Today — Monday, 23 November 2026

A single front-page newspaper infographic summing up the world's news for
Monday, 23 November 2026. One lead story on the collapse of the COP31
climate talks, plus five more stories: an Iranian strike in Bahrain, a
Russian drone attack near Kyiv, a rising death toll from a factory fire in
Indonesia, Russian missiles confirmed in Poland, and a South Korean
minister resigning over AI exam cheating.

The image is drawn entirely in code with Pillow: warm cream paper, dark
slate ink, dark-teal and gold accents, a big serif masthead, and a small
pictogram for every story — a globe, a tanker, a drone, a factory, a
missile, and a pencil over an exam paper. No photos, no downloaded assets,
no network calls anywhere in the build.

## The six stories

The front page is dated Monday, 23 November 2026 and was compiled in the
early hours of that day (UTC). The events themselves took place on 21–22
November, with fresh developments reported on 23 November — casualty
updates, forensic confirmations, and the search resuming on Monday
morning. Each story was checked against wire reporting before it was drawn.

1. **Lead — COP31 ends without a deal.** After about 44 hours of
   overtime, the COP31 climate talks in Antalya ended on Sunday with no
   agreement. The EU and other countries rejected a final draft that made
   no mention of fossil fuels. COP president Murat Kurum conceded there
   was no consensus. It was the longest COP in history.
   Sources: AP / NPR.
   https://www.wcbe.org/npr-news/2026-11-22/international-climate-talks-end-in-disappointment
2. **The Gulf.** An Iranian attack on a civilian industrial facility in
   Bahrain wounded two people, one critically. Two tankers were hit in
   the Strait of Hormuz, and a Saudi-led coalition intercepted Houthi
   drones bound for Riyadh. Iran's foreign minister still spoke of a deal.
   Sources: La Post; Jawawa.
   https://www.lapost.com/content/bahrain-says-iranian-attack-hits-industrial-facility-causes-fire
   https://jawawa.id/newsitem/deadly-combo-iran-linked-forces-target-saudi-arabia-and-bahrain-strike-two-tankers-1795395065
3. **Ukraine war.** A Russian drone collapsed part of a five-storey
   apartment block in Dymer, near Kyiv: 14 people were missing (later
   revised to 15) and one body was found. A missile strike on Kryvyi Rih
   killed two people, including a child.
   Sources: Political.org.
   https://political.org/2026/11/22/at-least-14-people-missing-after-russian-drone-strike-collapses-part-of-apartment-building-in-kyiv-region/
4. **Disaster.** Rescuers had pulled 24 body bags from the burnt candy
   factory of PT Fonusa Agung Mulia in Cikande by Sunday evening. At least
   3 deaths were confirmed and 37 people remained missing as the search
   resumed on Monday morning, 23 November.
   Sources: Daily Fox News; Northland News Radio.
   https://dailyfoxnews.com/news/3095/dozens-feared-dead-after-massive-blaze-engulfs-candy-factory
   https://northlandnewsradio.com/2026/11/21/indonesia-rescuers-search-for-36-missing-after-factory-fire-kills-3/
   Note: casualty and missing counts were still moving between outlets
   (7 vs 24 body bags, 36–50 missing); the image uses the latest Sunday
   evening figures (24 body bags, 37 missing) with the cautious wording
   "at least 3 confirmed dead".
5. **Poland.** Prosecutors in Lublin confirmed that all three objects
   that fell in Poland on Friday were Russian Kh-101 cruise missiles
   (built in Q4 2026, in Dubna). No one was hurt; NATO will discuss the
   incident.
   Sources: SRN News.
   https://srnnews.com/three-russian-missiles-flew-into-poland-friday-prosecutors-say/
6. **South Korea.** Education Minister Choi Kyo-jin resigned after
   last-minute anti-cheating rules for the college entrance exam (CSAT)
   sowed confusion. President Lee accepted the resignation; 111 cheating
   cases were caught during the test.
   Sources: 97.9 WEVE; TBS News.
   https://979weve.com/2026/11/22/south-koreas-education-minister-quits-over-exam-cheating-chaos/
   https://www.tbsnews.net/worldbiz/asia/south-korea-education-minister-resigns-after-ai-assisted-exam-cheating-scandal-1610146

## How to run

Requirements: Python 3 and Pillow 10.2.0. The DejaVu fonts bundled with the
system are used (`/usr/share/fonts/truetype/dejavu/`).

```sh
# Render the front page (writes entry.png, 1024x1024, under 1 MiB)
python3 render.py

# Copy the pre-rendered image to the output directory
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` uses only the Python standard library. It copies the
pre-rendered `entry.png` beside it into `$MAKEFUN_OUTPUT_DIR/entry.png`
(falling back to `/output`), with no network access. The copy is a
byte-for-byte copy, so repeated runs produce identical output.

## Files

- `render.py` — draws `entry.png` from scratch with Pillow.
- `main.py` — copies `entry.png` to the output directory.
- `entry.png` — the finished front page, 1024x1024.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet for this entry.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=8htny0qp&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
