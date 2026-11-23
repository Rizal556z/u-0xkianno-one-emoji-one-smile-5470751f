# One Emoji, One Smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![make.fun · rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Rizal556z/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![make.fun · reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Rizal556z/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [make.fun bounty "One Emoji, One Smile"](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).

## What the program does

`main.py` (pure Python standard library, no network, no model calls)
writes exactly one emoji to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## The emoji

**🤗** (hugging face) — open arms offering a hug. It reads instantly as
kind, friendly and welcoming; a hug is understood the same way by a
stranger of any age or background; it is a deliberate pick rather than
the first smiley that comes to mind; and it is warm without intimacy,
flirtation or sarcasm, so it works coming from someone unknown.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/emoji-test python3 main.py
cat /tmp/emoji-test/entry.txt  # 🤗
```
