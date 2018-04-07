# FIRST PGP Keys

FIRST PGP Public Key Checker.

## A problem I have

I realized that there are so many public keys on `https://www.first.org/members/teams/*` which are expired. It means that I cannnot contact these teams by PGP.

For example, National Cyber Security Centre's key is expired at 2016-08-26 15:20:41 (on 2018/04/08). This is the problem IMO.

So I made a simple script which collects and checks a status of the public keys on `https://www.first.org/members/teams/*`.

## How to run

```bash
$pip install -r requirements.txt
$python main.py
```

## Stas

FIRST has 414 teams and 40 teams' keys are expired on 2018/04/08.

Here is a list of expired PGP public keys.

- https://gist.github.com/ninoseki/7ca950c99601b5f96573434be065a924

