import urllib2, re 

guy = "http://www.ratp.fr/horaires/fr/ratp/metro/prochains_passages/PP/guy+moquet/13/R"
bro = "http://www.ratp.fr/horaires/fr/ratp/metro/prochains_passages/PP/brochant/13/R"

req_guy = urllib2.Request(guy)
req_bro = urllib2.Request(bro)
data_guy = urllib2.urlopen(req_guy).read()
data_bro = urllib2.urlopen(req_bro).read()
pattern = re.compile(r"\d+ mn") 

match_guy = pattern.findall(data_guy)
match_bro = pattern.findall(data_bro)

print "Guy Moquet: ", ", ".join(match_guy)
print "Brochant: ", ", ".join(match_bro)