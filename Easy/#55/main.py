"""
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""

from typing import Dict

alphanum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class UrlShortener:
	urlToShort: Dict[str, str]
	shortToUrl: Dict[str, str]

	def __init__(self):
		self.urlToShort = dict()
		self.shortToUrl = dict()

	def newShort(self) -> str:
		short = ""
		n = len(self.urlToShort)

		while len(short) < 6:
			short = alphanum[n % len(alphanum)] + short
			n = n // len(alphanum)

		return short

	def shorten(self, url: str) -> str:
		if url in self.urlToShort:
			return self.urlToShort[url]

		short = self.newShort()
		self.urlToShort[url] = short
		self.shortToUrl[short] = url
		return short

	def restore(self, short: str) -> str:
		return self.shortToUrl.get(short)


urlShortener = UrlShortener()

url1 = "https://www.test.com/"
shorten1 = urlShortener.shorten(url1)
restore1 = urlShortener.restore(shorten1)

url2 = "https://www.foo.fr/"
shorten2 = urlShortener.shorten(url2)
restore2 = urlShortener.restore(shorten2)

url3 = "https://www.bar.jp/"
shorten3 = urlShortener.shorten(url3)
restore3 = urlShortener.restore(shorten3)

print(f"urlShortener.shorten({url1}) = {shorten1}")
print(f"urlShortener.restore({shorten1}) = {restore1}")
print(
    f"urlShortener.(re)shorten({restore1}) = {urlShortener.shorten(restore1)}")

print(f"urlShortener.shorten({url2}) = {shorten2}")
print(f"urlShortener.restore({shorten2}) = {restore2}")
print(
    f"urlShortener.(re)shorten({restore2}) = {urlShortener.shorten(restore2)}")

print(f"urlShortener.shorten({url3}) = {shorten3}")
print(f"urlShortener.restore({shorten3}) = {restore3}")
print(
    f"urlShortener.(re)shorten({restore3}) = {urlShortener.shorten(restore3)}")

print(f"urlShortener.restore('0NONE0') = {urlShortener.restore('0NONE0')}")
