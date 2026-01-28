
import sys
from urllib.parse import quote_plus


def generate_qr(link, filename="qr.png", scale=10):

	try:
		import segno

		segno.make(link).save(filename, scale=scale)
		print(f"Saved {filename} using segno")
		return filename
	except Exception:
		pass

	try:
		import qrcode

		img = qrcode.make(link)
		img.save(filename)
		print(f"Saved {filename} using qrcode")
		return filename
	except Exception:
		pass

	try:
		import requests

		size = 500
		url = f"https://chart.googleapis.com/chart?cht=qr&chs={size}x{size}&chl={quote_plus(link)}"
		r = requests.get(url, timeout=10)
		r.raise_for_status()
		with open(filename, "wb") as f:
			f.write(r.content)
		print(f"Saved {filename} by downloading Google Charts image")
		return filename
	except Exception:
		data_url = f"https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl={quote_plus(link)}"
		print("Could not generate locally; use this URL to fetch the QR image:")
		print(data_url)
		raise RuntimeError("Failed to generate QR code (install 'segno' or 'qrcode' or 'requests')")


if __name__ == "__main__":
	
	default_link = "https://www.maiinji.com"
	link = default_link
	out = "qr.png"
	if len(sys.argv) > 1:
		link = sys.argv[1]
	if len(sys.argv) > 2:
		out = sys.argv[2]
generate_qr(link, out)

