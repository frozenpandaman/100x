#!/usr/bin/env python

# eli fessler
import time, json, requests, sys, datetime, time

app_head = {
	'Host': 'app.splatoon2.nintendo.net',
	'x-unique-id': "32449507786579989234",
	'x-requested-with': 'XMLHttpRequest',
	'x-timezone-offset': str(int(time.timezone/60)),
	'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Pixel Build/NJH47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Accept': '*/*',
	'Referer': 'https://app.splatoon2.nintendo.net/home',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US'
}

iksm_cookie = input("Enter your iksm_session cookie: ")
fest_id = input("Enter the Splatfest ID: ")

last_json = {}

def fetch_json():
	url = "https://app.splatoon2.nintendo.net/api/festivals/{}/events".format(fest_id)
	events_list = requests.get(url, headers=app_head, cookies=dict(iksm_session=iksm_cookie))
	events = json.loads(events_list.text)
	if events["events"][1]["event_type"]["key"] == "100_x_match":
		return events["events"][1]
	elif events["events"][0]["event_type"]["key"] == "100_x_match":
		return events["events"][0]

# def save_to_file(events):
# 	filename = "{}.json".format(int(time.time()))
# 	with open(filename, 'w') as outfile:
# 		json.dump(events, outfile, indent=4, sort_keys=True, separators=(',', ': '))
# 	print("Wrote {}".format(filename))

def ordered(obj): # https://stackoverflow.com/a/25851972
	if isinstance(obj, dict):
		return sorted((k, ordered(v)) for k, v in obj.items())
	if isinstance(obj, list):
		return sorted(ordered(x) for x in obj)
	else:
		return obj

def record_winners(events):
	filename = "winners.txt"
	with open(filename, 'a') as outfile:
		outfile.write("{}:\n".format(datetime.datetime.fromtimestamp(events["updated_time"]).strftime('%b %d, %Y @ %I:%M:%S %p')))
		if events["another_name"] != "":
			outfile.write("{}\n".format(events["another_name"]))
		for i in range(4):
			outfile.write("- {} ({})\n".format(events["members"][i]["name"], events["members"][i]["weapon"]["name"]))
		outfile.write("\n")
	print("Updated winners file.")

def main():
	# save on boot
	events = fetch_json()
	record_winners(events)
	last_json = events

	while True:
		# sleep
		for i in range(600, -1, -1):
			sys.stdout.write("Sleeping... {} ".format(i))
			sys.stdout.flush()
			time.sleep(1)
			sys.stdout.write("\r")

		events = fetch_json()
		if ordered(events) != ordered(last_json):
			print("Changes detected at {}!".format(datetime.datetime.fromtimestamp(events["updated_time"]).strftime('%I:%M %p')))
			record_winners(events)
			events = last_json
		else:
			# print("No changes detected...")
			pass

if __name__ == "__main__":
	main()