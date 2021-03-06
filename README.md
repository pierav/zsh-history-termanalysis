# zsh-history-termanalysis

Cool visualization of Zsh history.

## Fast start

zsh-history-termanalysis is started by running the following command in your terminal.

```sh
$ python -c "$(wget https://raw.githubusercontent.com/PIRXrav/zsh-history-termanalysis/master/analyze.py -O -)"
```

## Demo

```
$ python analyze.py
Analyse /home/pirx/.zsh_history
Frequencies:
+------+------------------------+------+-------+------+------------+
|      |          hour          |      |  day  |      |   month    |
+------+------------------------+------+-------+------+------------+
|  821 |           █            | 1902 | █     | 1719 |█           |
|  730 |           █  █         | 1691 | █ █   | 1528 |█           |
|  639 |           ██ ██        | 1479 | █ █   | 1337 |██          |
|  547 |           ██ ███       | 1268 | █ █   | 1146 |██          |
|  456 |        ██████████      | 1057 |██ ██ █|  955 |██ █        |
|  365 |       █████████████    |  845 |█████ █|  764 |████      ██|
|  273 |       ████████████████ |  634 |███████|  573 |████      ██|
|  182 |       ████████████████ |  422 |███████|  382 |████ █    ██|
|   91 |       ████████████████ |  211 |███████|  191 |██████    ██|
|    0 |      ██████████████████|    0 |███████|    0 |███████ ████|
+------+------------------------+------+-------+------+------------+
|      |012345678901012345678901|      |MTWTFSS|      |JFMAMJJASOND|
+------+------------------------+------+-------+------+------------+

Top commands:
     vim   935 ( 9.3%) |    echo   212 ( 2.1%) |      ls   119 ( 1.2%) |
      cd   515 ( 5.1%) |     pip   184 ( 1.8%) |    grep   106 ( 1.1%) |
      rm   435 ( 4.3%) |    file   170 ( 1.7%) |    find   104 ( 1.0%) |
    sudo   368 ( 3.7%) |     man   165 ( 1.6%) |    icat    97 ( 1.0%) |
    make   334 ( 3.3%) |     git   152 ( 1.5%) |    wget    96 ( 1.0%) |
     yay   276 ( 2.8%) |     xxd   135 ( 1.3%) | openssl    78 ( 0.8%) |
      mv   267 ( 2.7%) |       l   129 ( 1.3%) |   mkdir    74 ( 0.7%) |
  python   244 ( 2.4%) |     ima   125 ( 1.2%) |   chmod    63 ( 0.6%) |
     gcc   243 ( 2.4%) | objdump   122 ( 1.2%) |    perf    63 ( 0.6%) |
     cat   231 ( 2.3%) |     ssh   120 ( 1.2%) |    time    59 ( 0.6%) |
```

## Notes

Inspired by https://github.com/bamos/zsh-history-analysis
