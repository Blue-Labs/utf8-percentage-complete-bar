utf8-percentage-complete-bar
============================

Draw a simple text percentage complete bar with high granularity using utf8 gylphs and ANSI
coloring.


Python dependencies
  - none

Environment
  - terminal (and font) that supports utf8 glyphs 0x2588 - 0x258f


Example output:

(shown with ANSI for local rendering)

```
[david@Scott]$ python completion-status-bar.py
[1;37;47m             [0m   0 status line #0
[1;37;47m▌            [0m   1 status line #1
[1;37;47m██▋          [0m  18 status line #2
[1;37;47m███████▌     [0m  57 status line #3
[1;37;47m████████████▉[0m 100 status line #4
```

(shown without ANSI for github - no two-tone color for the bars)

```
[david@Scott]$ python completion-status-bar.py
                0 status line #0
▌               1 status line #1
██▋            18 status line #2
███████▌       57 status line #3
████████████▉ 100 status line #4
```