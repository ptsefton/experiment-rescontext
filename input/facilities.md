title: Facilities
menu-position: 3
---
Facilities page


{%
for page in pages:
	if page.typeOf == "@facility":
		print "* <a href='%s'>%s</a>\n\n" % (page.url, page.title)
		

%}
