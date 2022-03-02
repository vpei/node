# -*- coding: utf-8 -*-

from base64 import urlsafe_b64encode, urlsafe_b64decode

from ssrspeed.config_parser import TrojanParser

if __name__ == "__main__":
	links = "trojan://66666666@helloworld.xyz:440?allowinsecure=0&tfo=1#%E4%BD%A0%E5%A5%BD"

	raw = urlsafe_b64encode(links.encode("utf8"))
	tropar = TrojanParser()
	for link in urlsafe_b64decode(raw).decode("utf8").split("\n"):
		if link:
			print(tropar.parse_single_link(link))
