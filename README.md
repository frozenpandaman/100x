# 100x.py

During Splatfests in *Splatoon 2*, records winners of all 100x battles ~~(which occur at a rate of 1 every 10 minutes)~~\*.


Upon running the program, you'll need to enter the following:
* Your `iksm_session` cookie (used to access SplatNet) – obtain using [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) or [mitmproxy](https://github.com/frozenpandaman/splatnet2statink/wiki/mitmproxy-instructions)
* The active Splatfest's `festival_id` (e.g. 4053) – check [here](https://splatoon2.ink/data/festivals.json)
* The refresh interval you want to use, in seconds

\* Update – July 2019: Starting with Final Fest, 100x battles were advertised as changing to occur at 100x the previous frequency, i.e. 10 per minute. Data shows the actual rate is slightly higher. Recording *all* battles is now untenable due to the sheer number of requests, sustained over a lengthy period of time, that this would cause to be made on Nintendo's servers.

## Usage

```
$ python 100x.py
```
or simply `./100x.py` if on Mac/Linux.

You can also pass in the arguments on the command line: `./100x.py iksm_session festival_id refresh_interval`

## Past recordings

https://elifessler.com/s2s/splatfest/

### Disclaimer
You use this script at your own risk. None of the creators or contributors are responsible for anything that happens to your account as a result of running this script to make automated web requests. *[(modified from the s2s docs)](https://github.com/frozenpandaman/splatnet2statink/wiki/api-docs#disclaimer)*