rule piping_to_shell {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = /\|\s*(ba|z|fi)?sh/
	condition:
		any of them
}

rule python_exec {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = /python2?.*exec/
	condition:
		any of them
}
