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

if len(sys.argv) == 4:
	iksm_cookie = sys.argv[1]
	fest_id = sys.argv[2]
	refresh_interval = sys.argv[3]
else:
	iksm_cookie = input("Enter your iksm_session cookie: ")
	fest_id = input("Enter the Splatfest ID: ")
	refresh_interval = input("Enter refresh interval (sec): ")

last_json = {}

def fetch_json():
	url = "https://app.splatoon2.nintendo.net/api/festivals/{}/events".format(fest_id)
	events_list = requests.get(url, headers=app_head, cookies=dict(iksm_session=iksm_cookie))
	events = json.loads(events_list.text)
	try:
		if events["events"][1]["event_type"]["key"] == "100_x_match":
			return events["events"][1]
	except:
		pass
	try:
		if events["events"][0]["event_type"]["key"] == "100_x_match":
			return events["events"][0]
	except:
		print("Splatfest ID #{} is not currently active!".format(fest_id))
		exit()

def record_winners(events):
	filename = "100x_winners_{}.txt".format(fest_id)
	with open(filename, 'a') as outfile:
		outfile.write("{}:\n".format(datetime.datetime.fromtimestamp(events["updated_time"]).strftime('%b %d, %Y @ %I:%M:%S %p')))
		if events["another_name"] != "":
			outfile.write("{}\n".format(events["another_name"]))
		for i in range(4):
			outfile.write("- {} ({})\n".format(events["members"][i]["name"], events["members"][i]["weapon"]["name"]))
		outfile.write("\n")
	print("Updated winners file.")

def is_dupe(events, last_json):
	one_same   = True if events["members"][0]["name"] == last_json["members"][0]["name"] else False
	two_same   = True if events["members"][1]["name"] == last_json["members"][1]["name"] else False
	three_same = True if events["members"][2]["name"] == last_json["members"][2]["name"] else False
	four_same  = True if events["members"][3]["name"] == last_json["members"][3]["name"] else False
	return one_same and two_same and three_same and four_same

def main():
	# save on boot
	events = fetch_json()
	record_winners(events)
	last_json = events

	while True:
		# sleep
		for i in range(int(refresh_interval), -1, -1):
			sys.stdout.write("Sleeping... {} ".format(i))
			sys.stdout.flush()
			time.sleep(1)
			sys.stdout.write("\r")

		events = fetch_json()
		if not is_dupe(events, last_json):
			print("Changes detected at {}!".format(datetime.datetime.fromtimestamp(events["updated_time"]).strftime('%I:%M:%S %p')))
			record_winners(events)
		else:
			pass
		last_json = events

if __name__ == "__main__":
	main()
