rule firefox_profile_data {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = ".mozilla/firefox"
		$ = "cookies.sqlite"
		$ = "formhistory.sqlite"
		$ = "logins.json"
		$ = "places.sqlite"
		$ = "webappsstore.sqlite"
		$ = "bookmarkbackups"
	condition:
		any of them
}

rule chrome_profile_data {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = "Default/Cookies"
		$ = "Default/History"
		$ = "Default/Login Data"
		$ = "Default/Web Data"
	condition:
		any of them
}

rule ssh {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = ".ssh"
		$ = "authorized_keys"
		$ = "id_rsa"
		$ = "id_rsa.pub"
		$ = "known_hosts"
	condition:
		any of them
}
