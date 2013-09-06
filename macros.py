#TODO - use the JSON-LD way of doing this
types = {
"@facility" : "http://vivoweb.org/ontology/core#CoreLaboratory",
"@experiment" : "http://purl.org/some/experiment"


}

page = {
"typeOf" : None,
"description" : "",
"code" : "",
"lat" : "",
"long" : "",
"full_name" : ""
}

facilityHeaderBlock = """
<h1 property="dc:title">%(full_name)s</h1>
%(description)s
<table>
<tr><th>Code</th><td>%(code)s</td></tr>
<tr><th>Location</th><td><span property="http://www.w3.org/2003/01/geo/wgs84_pos#lat" content="%(lat)s"%(lat)s</span>(%(lat)s</span>,<span property="http://www.w3.org/2003/01/geo/wgs84_pos#long" content="%(long)s">%(long)s</span>)</td></tr>

</table>

"""

experimentHeaderBlock = """
<h1 property="dc:title">%(full_name)s</h1>
%(description)s
<table>
<tr><th>Code</th><td>%(code)s</td></tr>

</table>

"""


def typeOf(p):
	if p.has_key("typeOf"):
		return p.typeOf
	else:
		return None 

#			
def hook_preconvert_semantics():
	for p in pages:
		if p.typeOf == "@facility":
			p.source = facilityHeaderBlock % p + p.source
		


def hook_postconvert_semantics():
    for p in pages:
    	if p.typeOf <> None:
       		p.html = "\n\n<section resource='%s' typeof='%s'>\n\n%s\n\n</section>\n\n" % (p.url, types[p.typeOf], p.html)
    for p in pages:
	ptype = typeOf(p)
	if ptype == "@facility":
		p.html += "<section><h1>Experiments associated with facility: %s</h1>" % p.full_name
		for e in pages:
			etype = typeOf(e)
			
			if etype == "@experiment" and e.associatedWithFacility == p.code:
				p.html += e.html
		p.html += "</section>"
	
		
