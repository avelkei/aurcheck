rule url {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$url = /https?:\/\/([\w\.-]+)/ wide ascii
	condition:
		$url
}

rule dyndns {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = ".afraid.org"
		$ = ".dynu.com"

		// noip.com
		$ = ".noip.us"
		$ = ".noip.me"
		$ = ".no-ip.biz"
		$ = ".no-ip.info"
		$ = ".no-ip.org"
		$ = ".no-ip.ca"
		$ = ".no-ip.co.uk"
		$ = ".no-ip.net"
		$ = ".ddns.net"
		$ = ".ddnsking.com"
		$ = ".3utilities.com"
		$ = ".bounceme.net"
		$ = ".freedynamicdns.net"
		$ = ".freedynamicdns.org"
		$ = ".gotdns.ch"
		$ = ".hopto.org"
		$ = ".myddns.me"
		$ = ".myftp.biz"
		$ = ".myftp.org"
		$ = ".myvnc.com"
		$ = ".onthewifi.com"
		$ = ".redirectme.net"
		$ = ".servebeer.com"
		$ = ".serveblog.net"
		$ = ".servecounterstrike.com"
		$ = ".serveftp.com"
		$ = ".servegame.com"
		$ = ".servehalflife.com"
		$ = ".servehttp.com"
		$ = ".serveirc.com"
		$ = ".serveminecraft.net"
		$ = ".servemp3.com"
		$ = ".servepics.com"
		$ = ".servequake.com"
		$ = ".sytes.net"
		$ = ".viewdns.net"
		$ = ".webhop.me"
		$ = ".zapto.org"
		$ = ".access.ly"
		$ = ".blogsyte.com"
		$ = ".brasilia.me"
		$ = ".cable-modem.org"
		$ = ".ciscofreak.com"
		$ = ".collegefan.org"
		$ = ".couchpotatofries.org"
		$ = ".damnserver.com"
		$ = ".ddns.me"
		$ = ".ditchyourip.com"
		$ = ".dnsfor.me"
		$ = ".dnsiskinky.com"
		$ = ".dvrcam.info"
		$ = ".dynns.com"
		$ = ".eating-organic.net"
		$ = ".fantasyleague.cc"
		$ = ".geekgalaxy.com"
		$ = ".golffan.us"
		$ = ".health-carereform.com"
		$ = ".homesecuritymac.com"
		$ = ".homesecuritypc.com"
		$ = ".hosthampster.com"
		$ = ".hopto.me"
		$ = ".ilovecollege.info"
		$ = ".loginto.me"
		$ = ".mlbfan.org"
		$ = ".mmafan.biz"
		$ = ".myactivedirectory.com"
		$ = ".mydissent.net"
		$ = ".myeffect.net"
		$ = ".mymediapc.net"
		$ = ".mypsx.net"
		$ = ".mysecuritycamera.com"
		$ = ".mysecuritycamera.net"
		$ = ".mysecuritycamera.org"
		$ = ".net-freaks.com"
		$ = ".nflfan.org"
		$ = ".nhlfan.net"
		$ = ".pgafan.net"
		$ = ".point2this.com"
		$ = ".pointto.us"
		$ = ".privatizehealthinsurance.net"
		$ = ".quicksytes.com"
		$ = ".read-books.org"
		$ = ".securitytactics.com"
		$ = ".serveexchange.com"
		$ = ".servehumour.com"
		$ = ".servep2p.com"
		$ = ".servesarcasm.com"
		$ = ".stufftoread.com"
		$ = ".ufcfan.org"
		$ = ".unusualperson.com"
		$ = ".workisboring.com"

		// dyn.com
		$ = ".at-band-camp.net"
		$ = ".barrel-of-knowledge.info"
		$ = ".barrell-of-knowledge.info"
		$ = ".better-than.tv"
		$ = ".blogdns.com"
		$ = ".blogdns.net"
		$ = ".blogdns.org"
		$ = ".blogsite.org"
		$ = ".boldlygoingnowhere.org"
		$ = ".broke-it.net"
		$ = ".buyshouses.net"
		$ = ".cechire.com"
		$ = ".dnsalias.com"
		$ = ".dnsalias.net"
		$ = ".dnsalias.org"
		$ = ".dnsdojo.com"
		$ = ".dnsdojo.net"
		$ = ".dnsdojo.org"
		$ = ".does-it.net"
		$ = ".doesntexist.com"
		$ = ".doesntexist.org"
		$ = ".dontexist.com"
		$ = ".dontexist.net"
		$ = ".dontexist.org"
		$ = ".doomdns.com"
		$ = ".doomdns.org"
		$ = ".dvrdns.org"
		$ = ".dyn-o-saur.com"
		$ = ".dynalias.com"
		$ = ".dynalias.net"
		$ = ".dynalias.org"
		$ = ".dynathome.net"
		$ = ".dyndns-at-home.com"
		$ = ".dyndns-at-work.com"
		$ = ".dyndns-blog.com"
		$ = ".dyndns-free.com"
		$ = ".dyndns-home.com"
		$ = ".dyndns-ip.com"
		$ = ".dyndns-mail.com"
		$ = ".dyndns-office.com"
		$ = ".dyndns-pics.com"
		$ = ".dyndns-remote.com"
		$ = ".dyndns-server.com"
		$ = ".dyndns-web.com"
		$ = ".dyndns-wiki.com"
		$ = ".dyndns-work.com"
		$ = ".dyndns.biz"
		$ = ".dyndns.info"
		$ = ".dyndns.org"
		$ = ".dyndns.tv"
		$ = ".dyndns.ws"
		$ = ".endofinternet.net"
		$ = ".endofinternet.org"
		$ = ".endoftheinternet.org"
		$ = ".est-a-la-maison.com"
		$ = ".est-a-la-masion.com"
		$ = ".est-ie-patron.com"
		$ = ".est-mon-blogueur.com"
		$ = ".for-better.biz"
		$ = ".for-more.biz"
		$ = ".for-our.info"
		$ = ".for-some.biz"
		$ = ".for-the.biz"
		$ = ".forgot.her.name"
		$ = ".forgot.his.name"
		$ = ".from-ak.com"
		$ = ".from-al.com"
		$ = ".from-ar.com"
		$ = ".from-az.net"
		$ = ".from-ca.com"
		$ = ".from-co.net"
		$ = ".from-ct.com"
		$ = ".from-dc.com"
		$ = ".from-de.com"
		$ = ".from-fl.com"
		$ = ".from-ga.com"
		$ = ".from-hi.com"
		$ = ".from-ia.com"
		$ = ".from-id.com"
		$ = ".from-il.com"
		$ = ".from-in.com"
		$ = ".from-ks.com"
		$ = ".from-ky.com"
		$ = ".from-ia.net"
		$ = ".from-ma.com"
		$ = ".from-md.com"
		$ = ".from-me.org"
		$ = ".from-mi.com"
		$ = ".from-mn.com"
		$ = ".from-mo.com"
		$ = ".from-ms.com"
		$ = ".from-mt.com"
		$ = ".from-nc.com"
		$ = ".from-nd.com"
		$ = ".from-ne.com"
		$ = ".from-nh.com"
		$ = ".from-nj.com"
		$ = ".from-nm.com"
		$ = ".from-nv.com"
		$ = ".from-ny.net"
		$ = ".from-oh.com"
		$ = ".from-ok.com"
		$ = ".from-on.com"
		$ = ".from-pa.com"
		$ = ".from-pr.com"
		$ = ".from-ri.com"
		$ = ".from-sc.com"
		$ = ".from-sd.com"
		$ = ".from-tn.com"
		$ = ".from-tx.com"
		$ = ".from-ut.com"
		$ = ".from-va.com"
		$ = ".from-vt.com"
		$ = ".from-wa.com"
		$ = ".from-wi.com"
		$ = ".from-wv.com"
		$ = ".from-wy.com"
		$ = ".ftpaccess.cc"
		$ = ".fuettertdasnetz.de"
		$ = ".game-host.org"
		$ = ".game-server.cc"
		$ = ".getmyip.com"
		$ = ".gets-it.net"
		$ = ".go.dyndns.org"
		$ = ".gotdns.com"
		$ = ".gotdns.org"
		$ = ".groks-the.info"
		$ = ".groks-this.info"
		$ = ".ham-radio-op.net"
		$ = ".here-for-more.info"
		$ = ".hobby-site.com"
		$ = ".hobby-site.org"
		$ = ".home.dyndns.org"
		$ = ".homedns.org"
		$ = ".homeftp.net"
		$ = ".homeftp.org"
		$ = ".homeip.net"
		$ = ".homelinux.com"
		$ = ".homelinux.net"
		$ = ".homelinux.org"
		$ = ".homeunix.com"
		$ = ".homeunix.net"
		$ = ".homeunix.org"
		$ = ".iamallama.com"
		$ = ".in-the-band.net"
		$ = ".is-a-anarchist.com"
		$ = ".is-a-blogger.com"
		$ = ".is-a-bookkeeper.com"
		$ = ".is-a-bruinsfan.org"
		$ = ".is-a-bulls-fan.com"
		$ = ".is-a-candidate.org"
		$ = ".is-a-caterer.com"
		$ = ".is-a-celticsfan.org"
		$ = ".is-a-chef.com"
		$ = ".is-a-chef.net"
		$ = ".is-a-chef.org"
		$ = ".is-a-conservative.com"
		$ = ".is-a-cpa.com"
		$ = ".is-a-cubicle-slave.com"
		$ = ".is-a-democrat.com"
		$ = ".is-a-designer.com"
		$ = ".is-a-doctor.com"
		$ = ".is-a-financialadvisor.com"
		$ = ".is-a-geek.com"
		$ = ".is-a-geek.net"
		$ = ".is-a-geek.org"
		$ = ".is-a-green.com"
		$ = ".is-a-guru.com"
		$ = ".is-a-hard-worker.com"
		$ = ".is-a-hunter.com"
		$ = ".is-a-knight.org"
		$ = ".is-a-landscaper.com"
		$ = ".is-a-lawyer.com"
		$ = ".is-a-liberal.com"
		$ = ".is-a-libertarian.com"
		$ = ".is-a-linux-user.org"
		$ = ".is-a-llama.com"
		$ = ".is-a-musician.com"
		$ = ".is-a-nascarfan.com"
		$ = ".is-a-nurse.com"
		$ = ".is-a-painter.com"
		$ = ".is-a-patsfan.org"
		$ = ".is-a-personaltrainer.com"
		$ = ".is-a-photographer.com"
		$ = ".is-a-player.com"
		$ = ".is-a-republican.com"
		$ = ".is-a-rockstar.com"
		$ = ".is-a-socialist.com"
		$ = ".is-a-soxfan.org"
		$ = ".is-a-student.com"
		$ = ".is-a-teacher.com"
		$ = ".is-a-techie.com"
		$ = ".is-a-therapist.com"
		$ = ".is-an-accountant.com"
		$ = ".is-an-actor.com"
		$ = ".is-an-actress.com"
		$ = ".is-an-anarchist.com"
		$ = ".is-an-artist.com"
		$ = ".is-an-engineer.com"
		$ = ".is-an-entertainer.com"
		$ = ".is-by.us"
		$ = ".is-certified.com"
		$ = ".is-found.org"
		$ = ".is-gone.com"
		$ = ".is-into-anime.com"
		$ = ".is-into-cars.com"
		$ = ".is-into-cartoons.com"
		$ = ".is-into-games.com"
		$ = ".is-leet.com"
		$ = ".is-lost.org"
		$ = ".is-not-certified.com"
		$ = ".is-saved.org"
		$ = ".is-slick.com"
		$ = ".is-uberleet.com"
		$ = ".is-very-bad.org"
		$ = ".is-very-evil.org"
		$ = ".is-very-good.org"
		$ = ".is-very-nice.org"
		$ = ".is-very-sweet.org"
		$ = ".is-with-theband.com"
		$ = ".isa-geek.com"
		$ = ".isa-geek.net"
		$ = ".isa-geek.org"
		$ = ".isa-hockeynut.com"
		$ = ".issmarterthanyou.com"
		$ = ".isteingeek.de"
		$ = ".istmein.de"
		$ = ".kicks-ass.net"
		$ = ".kicks-ass.org"
		$ = ".knowsitall.info"
		$ = ".land-4-sale.us"
		$ = ".lebtimnetz.de"
		$ = ".leitungsen.de"
		$ = ".likes-pie.com"
		$ = ".likescandy.com"
		$ = ".merseine.com"
		$ = ".merseine.org"
		$ = ".mine.nu"
		$ = ".misconfused.org"
		$ = ".mypets.ws"
		$ = ".myphotos.cc"
		$ = ".neat-url.com"
		$ = ".office-on-the.net"
		$ = ".on-the-web.tv"
		$ = ".podzone.net"
		$ = ".podzone.org"
		$ = ".readmyblog.org"
		$ = ".remotecam.nu"
		$ = ".saves-the-whales.com"
		$ = ".scrapper-site.net"
		$ = ".scrapping.cc"
		$ = ".selflp.biz"
		$ = ".selflp.com"
		$ = ".selflp.info"
		$ = ".selflp.net"
		$ = ".selflp.org"
		$ = ".sells-for-less.com"
		$ = ".sells-for-u.com"
		$ = ".sells-it.net"
		$ = ".sellsyourhome.org"
		$ = ".servebbs.com"
		$ = ".servebbs.net"
		$ = ".servebbs.org"
		$ = ".serveftp.net"
		$ = ".serveftp.org"
		$ = ".servegame.org"
		$ = ".shacknet.biz"
		$ = ".shacknet.us"
		$ = ".shaqnet.nu"
		$ = ".simple-ufl.com"
		$ = ".space-to-rent.com"
		$ = ".stuff-4-sale.org"
		$ = ".stuff-4-sale.us"
		$ = ".teaches-yoga.com"
		$ = ".thruhere.net"
		$ = ".traeumtgerade.de"
		$ = ".webhop.biz"
		$ = ".webhop.info"
		$ = ".webhop.net"
		$ = ".webhop.org"
		$ = ".worse-than.tv"
		$ = ".writesthisblog.com"

		$ = ".dynip.com"
		$ = ".duckdns.org"

		// dyns.cx
		$ = ".dyns.cx"
		$ = ".dyns.net"
		$ = ".ma.cx"
		$ = ".metadns.cx"
	condition:
		any of them
}

rule code_hosting_sites {
	meta:
		author = "Adam Velkei <adam@avelkei.eu>"
	strings:
		$ = ".githubusercontent.com"
		$ = "pastebin.com"
		$ = "bpa.st"
		$ = "bpaste.net"
	condition:
		any of them
}
