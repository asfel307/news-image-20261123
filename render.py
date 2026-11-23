#!/usr/bin/env python3
"""Render the front page of 'The World Today' for Monday, 23 November 2026.

Draws a 1024x1024 newspaper front page with Pillow: a serif masthead,
one lead story and five more world stories, each with a small pictogram
drawn in code. No photos, no downloaded assets, no network calls.

Stories (all checked against wire reporting, 23 Nov 2026):
  1. COP31 climate talks collapse with no deal (lead)
  2. Gulf: Iranian strike wounds two in Bahrain; tankers hit
  3. Ukraine: drone collapses apartment block near Kyiv, 14 missing
  4. Indonesia: factory fire in Cikande, 24 body bags, search resumes
  5. Poland: prosecutors confirm three Russian Kh-101 missiles
  6. South Korea: education minister resigns over AI exam cheating
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

W, H = 1024, 1024
MARGIN = 40
RIGHT = W - MARGIN

PAPER = (247, 242, 231)
INK = (28, 32, 40)
TEAL = (14, 79, 79)
RED = (139, 30, 30)
GOLD = (176, 141, 46)
GREY = (96, 92, 82)
RULE = (196, 186, 158)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit in max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw wrapped paragraph; return y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def hline(draw, x0, x1, y, width=1, color=INK):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


# ---------------------------------------------------------------- pictograms

def pic_globe(d, cx, cy, r, color=TEAL):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    d.ellipse([cx - int(r * 0.45), cy - r, cx + int(r * 0.45), cy + r],
              outline=color, width=3)
    d.ellipse([cx - r, cy - int(r * 0.45), cx + r, cy + int(r * 0.45)],
              outline=color, width=3)
    for frac in (-0.55, 0.55):
        yy = cy + int(r * frac)
        half = int(math.sqrt(max(r * r - (r * frac) ** 2, 0)))
        d.line([(cx - half, yy), (cx + half, yy)], fill=color, width=2)
    d.line([(cx, cy - r), (cx, cy + r)], fill=color, width=2)


def pic_tanker(d, cx, cy, s, color=TEAL):
    # hull
    d.polygon([(cx - s, cy - 8), (cx + s, cy - 8), (cx + s - 14, cy + 16),
               (cx - s + 14, cy + 16)], fill=color)
    # deck + funnel
    d.rectangle([cx - s + 18, cy - 30, cx - s + 44, cy - 8], fill=color)
    d.rectangle([cx + s - 52, cy - 44, cx + s - 30, cy - 8], fill=GOLD)
    d.rectangle([cx - s + 8, cy - 20, cx + s - 8, cy - 8], fill=INK)
    # waves
    for k, yy in enumerate((cy + 26, cy + 38)):
        d.arc([cx - s + k * 12, yy - 8, cx - s + 34 + k * 12, yy + 8],
              180, 360, fill=color, width=3)
        d.arc([cx + 6 + k * 10, yy - 8, cx + 40 + k * 10, yy + 8],
              180, 360, fill=color, width=3)


def pic_drone(d, cx, cy, s, color=TEAL):
    d.ellipse([cx - 12, cy - 10, cx + 12, cy + 10], outline=color, width=4)
    d.ellipse([cx - 4, cy - 3, cx + 4, cy + 3], fill=color)
    for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        ex, ey = cx + sx * s, cy + sy * int(s * 0.6)
        d.line([(cx, cy), (ex, ey)], fill=color, width=4)
        d.ellipse([ex - 13, ey - 4, ex + 13, ey + 4], outline=color, width=3)
        d.line([(ex - 16, ey), (ex + 16, ey)], fill=color, width=2)


def pic_factory(d, cx, cy, s, color=TEAL):
    # chimney with smoke (kept short so it stays below the kicker)
    d.rectangle([cx + s - 26, cy - s + 12, cx + s - 8, cy + 20], fill=color)
    for ox, oy, rr in ((4, -s + 2, 7), (12, -s - 10, 9),
                       (22, -s - 20, 11)):
        d.ellipse([cx + s - 26 + ox - rr, cy + oy - rr,
                   cx + s - 26 + ox + rr, cy + oy + rr],
                  outline=GREY, width=2)
    # sawtooth-roof building
    d.polygon([(cx - s, cy + 20), (cx - s, cy - 6),
               (cx - s + 26, cy - 26), (cx - s + 26, cy - 6),
               (cx - s + 52, cy - 26), (cx - s + 52, cy - 6),
               (cx + s - 30, cy - 6), (cx + s - 30, cy + 20)],
              fill=color)
    # flame in two windows
    d.polygon([(cx - 22, cy + 18), (cx - 14, cy - 6), (cx - 6, cy + 18)],
              fill=GOLD)
    d.polygon([(cx + 2, cy + 18), (cx + 10, cy - 2), (cx + 18, cy + 18)],
              fill=RED)


def pic_missile(d, cx, cy, s, color=TEAL):
    d.rounded_rectangle([cx - s, cy - 10, cx + s - 26, cy + 10],
                        radius=10, fill=color)
    d.polygon([(cx + s - 26, cy - 10), (cx + s + 6, cy),
               (cx + s - 26, cy + 10)], fill=color)
    d.polygon([(cx - s + 22, cy - 10), (cx - s + 34, cy - 28),
               (cx - s + 48, cy - 10)], fill=color)
    d.polygon([(cx - s + 22, cy + 10), (cx - s + 34, cy + 28),
               (cx - s + 48, cy + 10)], fill=color)
    # exhaust
    d.line([(cx - s - 4, cy - 4), (cx - s - 26, cy - 4)], fill=GOLD, width=3)
    d.line([(cx - s - 4, cy), (cx - s - 32, cy)], fill=RED, width=3)
    d.line([(cx - s - 4, cy + 4), (cx - s - 26, cy + 4)], fill=GOLD, width=3)


def pic_exam(d, cx, cy, s, color=TEAL):
    # sheet of paper
    d.rectangle([cx - s + 6, cy - s, cx + s - 22, cy + s],
                fill=(255, 255, 255), outline=color, width=3)
    for i in range(3):
        yy = cy - s + 22 + i * 18
        d.line([(cx - s + 16, yy), (cx + s - 32, yy)], fill=GREY, width=2)
    # pencil, diagonal across the sheet
    d.polygon([(cx - 6, cy + s + 6), (cx + s + 2, cy - s + 14),
               (cx + s + 12, cy - s + 26), (cx + 4, cy + s + 16)],
              fill=GOLD)
    d.polygon([(cx - 6, cy + s + 6), (cx + 4, cy + s + 16),
               (cx - 2, cy + s + 24)], fill=INK)
    d.line([(cx + s - 6, cy - s + 30), (cx + s + 2, cy - s + 40)],
           fill=RED, width=3)


# ---------------------------------------------------------------- page

def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header ----
    hline(d, MARGIN, RIGHT, 30, 2)
    d.text((MARGIN, 40), "MONDAY, 23 NOVEMBER 2026", font=SANS_B(18), fill=INK)
    right_tag = "WORLD EDITION  •  No. 327"
    d.text((RIGHT - d.textlength(right_tag, font=SANS_B(16)), 42),
           right_tag, font=SANS_B(16), fill=GREY)

    mast = "The World Today"
    mw = d.textlength(mast, font=SERIF_B(88))
    d.text(((W - mw) / 2, 66), mast, font=SERIF_B(88), fill=INK)

    sub = "S I X   S T O R I E S   F R O M   A R O U N D   T H E   G L O B E"
    sw = d.textlength(sub, font=SANS_B(15))
    d.text(((W - sw) / 2, 164), sub, font=SANS_B(15), fill=TEAL)

    hline(d, MARGIN, RIGHT, 192, 3)
    hline(d, MARGIN, RIGHT, 198, 1)

    # ---- lead story ----
    y = 214
    d.text((MARGIN, y), "LEAD STORY  —  CLIMATE", font=SANS_B(17), fill=RED)
    y += 30
    lead_head = ["COP31 ends in disarray:",
                 "no deal after 44 hours"]
    for line in lead_head:
        d.text((MARGIN, y), line, font=SERIF_B(37), fill=INK)
        y += 45
    y += 4
    lead_body = ("After about 44 hours of overtime, the climate talks in "
                 "Antalya closed on Sunday with no agreement. The EU and "
                 "others rejected a final draft that made no mention of "
                 "fossil fuels. It was the longest COP in history.")
    y = para(d, MARGIN, y, lead_body, SANS(19), 610, 25)
    pic_globe(d, 852, 316, 82)

    hline(d, MARGIN, RIGHT, 446, 2, RULE)

    # ---- grid: four stories, two columns x two rows ----
    stories = [
        ("THE GULF", "Iran strike wounds two in Bahrain",
         "Tehran hit a civilian plant in Bahrain and two tankers in the "
         "Strait of Hormuz, as Saudi defences downed Houthi drones. "
         "Iran's foreign minister still spoke of a deal.",
         pic_tanker, (44, 40, 46)),
        ("UKRAINE", "Drone flattens block near Kyiv",
         "A Russian drone collapsed part of a five-storey block in Dymer; "
         "14 people are missing and one body was found. A missile on "
         "Kryvyi Rih killed two, including a child.",
         pic_drone, (38, 44, 34)),
        ("DISASTER", "Factory fire toll rises in Java",
         "Rescuers had pulled 24 body bags from the burnt candy factory "
         "in Cikande by Sunday evening. At least 3 are confirmed dead; "
         "37 remain missing as the search resumes.",
         pic_factory, (44, 96, 42)),
        ("POLAND", "Missiles were Russian, Warsaw says",
         "Prosecutors confirmed all three objects that fell in Poland on "
         "Friday were Russian Kh-101 cruise missiles. No one was hurt; "
         "NATO will discuss the incident.",
         pic_missile, (56, 40, 38)),
    ]
    col_w = 457
    col_x = [MARGIN, MARGIN + col_w + 30]
    row_y = [462, 652]
    for i, (kick, head, body, pic, (px, py, ps)) in enumerate(stories):
        x = col_x[i % 2]
        yy = row_y[i // 2]
        d.text((x, yy), kick, font=SANS_B(15), fill=RED)
        yy += 24
        pic(d, x + px, yy + py, ps)
        tx = x + 104
        for line in wrap(d, head, SERIF_B(23), col_w - 104):
            d.text((tx, yy), line, font=SERIF_B(23), fill=INK)
            yy += 28
        yy += 6
        para(d, tx, yy, body, SANS(16), col_w - 104, 21)
        if i % 2 == 0:
            d.line([(x + col_w + 15, row_y[i // 2] - 4),
                    (x + col_w + 15, row_y[i // 2] + 176)],
                   fill=RULE, width=1)
    hline(d, MARGIN, RIGHT, 640, 1, RULE)

    # ---- bottom strip: South Korea ----
    y = 856
    hline(d, MARGIN, RIGHT, 844, 2, RULE)
    pic_exam(d, MARGIN + 46, y + 52, 48)
    tx = MARGIN + 112
    d.text((tx, y), "SOUTH KOREA", font=SANS_B(15), fill=RED)
    d.text((tx, y + 24), "Minister quits over AI exam cheating",
           font=SERIF_B(27), fill=INK)
    para(d, tx, y + 62,
         "Education Minister Choi Kyo-jin resigned after last-minute "
         "anti-cheating rules for the college entrance exam sowed "
         "confusion. President Lee accepted it; 111 cheating cases "
         "were caught during the test.",
         SANS(16), RIGHT - tx, 21)

    # ---- footer ----
    hline(d, MARGIN, RIGHT, 986, 1)
    d.text((MARGIN, 996),
           "Sources: Reuters  •  AP  •  NPR  •  Korea JoongAng Daily  •  The National",
           font=SANS(13), fill=GREY)
    foot_r = "Compiled early Monday, 23 November 2026 (UTC)"
    d.text((RIGHT - d.textlength(foot_r, font=SANS(13)), 996),
           foot_r, font=SANS(13), fill=GREY)

    return img


def main():
    img = build()
    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, img.size,
          os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
