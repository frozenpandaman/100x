# 100x.py

During Splatfests in _Splatoon 2_, records winners of all 100x battles (which occur at a rate of 1 every 10 minutes).

Upon running the program, you'll need to enter the following:
* Your `iksm_session` cookie (used to access SplatNet) – obtain using [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) or [mitmproxy](https://github.com/frozenpandaman/splatnet2statink/wiki/mitmproxy-instructions)
* The active Splatfest's `festival_id` (e.g. 4053) – check [here](https://splatoon2.ink/data/festivals.json)

## Usage

```
$ python 100x.py
```
or simply `./100x.py` if on Mac/Linux.

You can also pass in the arguments on the command line: `./100x.py iksm_session festival_id`

## Past recordings

https://elifessler.com/s2s/splatfest/
