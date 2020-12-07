rule piping_to_shell {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$a = /\|\s*(ba|z|fi)?sh/
		$b = /\|\s*sha\d+sum/
	condition:
		// https://github.com/VirusTotal/yara/issues/584
		// matching $a only if $b doesn't match
		for any i in (1..#a): (@a[i] != @b[i])
}

rule piping_from_download {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$a = /curl\s*\|/
		$b = /wget\s*\|/
	condition:
		any of them
}

rule python_exec {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$a = /python2?.*exec/
		$b = /python2?.*execute/
	condition:
		// https://github.com/VirusTotal/yara/issues/584
		// matching $a only if $b doesn't match
		for any i in (1..#a): (@a[i] != @b[i])
}
