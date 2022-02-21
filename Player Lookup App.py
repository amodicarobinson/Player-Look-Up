from http.client import CONTINUE
import sys
import webbrowser


while True:
	player, name = input("Enter A Players name: ").split()
	try:
		from googlesearch import search
	except ImportError:
		print("No module named 'google' found")

	# to search
	query = player + name + "stats"

	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		print(j)
	
	urL=input("Paste the URL you would like to go to: ")
	chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
	webbrowser.get('chrome').open_new_tab(urL)

	while True:
		answer = str(input("Run again? (y/n): "))
		if answer in ('y', 'n'):
			break
		print("invalid input.")
	if answer == 'y':
		CONTINUE
	else:
		print("Goodbye")
		sys.exit()