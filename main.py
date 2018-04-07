from requests_html import HTMLSession
import pgpy


def links():
    URL = "https://www.first.org/members/teams/"
    session = HTMLSession()
    r = session.get(URL)

    links = []
    rows = r.html.find("tr")
    for row in rows:
        td = row.find("td", first=True)
        if td:
            a = td.find("a", first=True)
            links.append(a.attrs.get("href"))
    return links


def public_key_block(link):
    session = HTMLSession()
    r = session.get("https://www.first.org" + link)
    td = r.html.find(".property-pgp-key", first=True)
    if td:
        code = td.find("code", first=True)
        return code.html.replace("<code>", "").replace("</code>", "")
    return None


def check(link):
    block = public_key_block(link)
    if block:
        try:
            key, _ = pgpy.PGPKey.from_blob(block)
            if key.is_expired:
                print(",".join([link, str(key.expires_at)]))
            else:
                print(",".join([link, "not_expired"]))
        except Exception as err:
            print(",".join([link, str(err)]))
    else:
        print(",".join([link, "there_is_no_key"]))

if __name__ == "__main__":
    for link in links():
        check(link)
