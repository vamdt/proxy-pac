#!/usr/bin/env python

import urllib, re

GFWLIST_PAC_URL="https://raw.githubusercontent.com/clowwindy/gfwlist2pac/master/test/proxy.pac"
CUSTOM_START_COMMENT = "// custom -- start\n"
CUSTOM_END_COMMENT = "\n// custom -- end"

def main():
    pac_content = urllib.urlopen(GFWLIST_PAC_URL).read()
    repl = '\\n' + custom_domains() + '\\1'

    ret = re.sub(r'(\s.+: 1\n\};\n)', repl, pac_content, re.DOTALL)
    ret = ret.replace('1080', '15083')
    save(ret, 'proxy.pac')

def json_filed(field):
    return "  \"" +  field + "\": 1,"

def custom_domains():
    fp = open('./proxy_domains.txt', 'r')
    content = fp.read()
    domains = content.strip().split("\n")
    domains_format = '\n'.join(str(x) for x in map(json_filed, domains))
    return CUSTOM_START_COMMENT + domains_format + CUSTOM_END_COMMENT

def save(obj, name):
    file = open(name, 'w')
    file.write(str(obj))
    file.close



if __name__ == '__main__':
    main()
