# should-have-been-email

One line about a meeting that should have been an email.

[![make.fun](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![make.fun rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/nmlyz/should-have-been-email/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![make.fun reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/nmlyz/should-have-been-email/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

See the bounty page: https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9

## The line

> We all joined from different rooms in the same building, to say nothing to each other in high definition.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `/output`, or to `$MAKEFUN_OUTPUT_DIR` when set.
The program checks the line first (1-200 characters, a single line,
no leading or trailing whitespace, no control characters), writes it
with a trailing newline, then reads the file back and verifies the
bytes match.
