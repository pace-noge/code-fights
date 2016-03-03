def htmlToLuna(html):
    html = html.split("><")
    tag = ""
    for i in range(len(html)):
        print html[i]
        if html[i].startswith("<"):
            tag += html[i].replace("<", "").upper() + "(["
        elif html[i].startswith("/") and html[i].endswith(">"):
            tag += "])"
        elif html[i].startswith("/"):
            tag += html[i].replace("/", "").replace(">", "")
        elif html[i].startswith("img"):
            tag += html[i].replace(" /", "").upper() + "({})"
        else:
            tag += html[i].upper() + "(["
    print tag


html = "<div><p></p><p></p><p></p></div>"
htmlToLuna(html)
