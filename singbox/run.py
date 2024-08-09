import requests
import urllib3
import json
import os


def pc(urls, dir):
    os.makedirs(dir, exist_ok=True)
    for key, value in urls.items():
        response = requests.get(value, verify=False)
        if response.status_code == 200:
            res = response.json()
            with open(dir + "/" + key, "w") as file:
                json.dump(res, file)


def mobile(urls, dir):
    res = json.loads(
        '{"dns":{"servers":[{"tag":"google","address":"tls://8.8.8.8"},{"tag":"local","address":"223.5.5.5","detour":"direct"}],"rules":[{"outbound":"any","server":"local"}]},"inbounds":[{"type":"tun","inet4_address":"172.19.0.1/30","inet6_address":"fdfe:dcba:9876::1/126","auto_route":true,"sniff":true}],"outbounds":[{"type":"direct","tag":"direct"},{"type":"dns","tag":"dns-out"}],"route":{"rules":[{"protocol":"dns","outbound":"dns-out"},{"geoip":"private","outbound":"direct"}],"auto_detect_interface":true}}'
    )
    for key, value in urls.items():
        response = requests.get(value, verify=False)
        if response.status_code == 200:
            data = response.json()
            res["outbounds"] = data["outbounds"] + res["outbounds"]
            with open(dir + "/" + key, "w") as file:
                json.dump(res, file)


urls = {
    "config1.json": "https://www.gitlabip.xyz/Alvin9999/pac2/master/singbox/1/config.json",
    "config2.json": "https://gitlab.com/free9999/ipupdate/-/raw/master/singbox/config.json",
    "config3.json": "https://www.githubip.xyz/Alvin9999/pac2/master/singbox/config.json",
    "config4.json": "https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/singbox/config.json",
}
urllib3.disable_warnings()
pc(urls, "./singbox/pc")
mobile(urls, "./singbox/mobile")
