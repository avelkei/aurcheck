rule crypto_mining_domains {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = "coinhive.com"
		$ = "coin-hive.com"
	condition:
		any of them
}
