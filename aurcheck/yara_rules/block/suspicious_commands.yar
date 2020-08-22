rule piping_to_shell {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$a = /\|\s*(ba|z|fi)?sh/
		$b = /\|\s*sha\d+sum/
	condition:
		// https://github.com/VirusTotal/yara/issues/584
		for any i in (1..#a): (@a[i] != @b[i])
}

rule python_exec {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$a = /python2?.*exec/
		$b = /python2?.*execute/
	condition:
		for any i in (1..#a): (@a[i] != @b[i])
}
