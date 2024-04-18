import requests
import json
import os


def singbox(dir):
    pc = dir + "/pc"
    mobile = dir + "/mobile"

    default = '{"dns":{"servers":[{"tag":"google","address":"tls://8.8.8.8"},{"tag":"local","address":"223.5.5.5","detour":"direct"}],"rules":[{"outbound":"any","server":"local"}]},"inbounds":[{"type":"tun","inet4_address":"172.19.0.1/30","inet6_address":"fdfe:dcba:9876::1/126","auto_route":true,"sniff":true}],"outbounds":[{"type":"direct","tag":"direct"},{"type":"dns","tag":"dns-out"}],"route":{"rules":[{"protocol":"dns","outbound":"dns-out"},{"geoip":"private","outbound":"direct"}],"auto_detect_interface":true}}'
    map = {
        "config1": "https://www.gitlabip.xyz/Alvin9999/pac2/master/singbox/1/config.json",
        "config2": "https://gitlab.com/free9999/ipupdate/-/raw/master/singbox/config.json",
        "config3": "https://www.githubip.xyz/Alvin9999/pac2/master/singbox/config.json",
        "config4": "https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/singbox/config.json",
    }

    config = json.loads(default)
    outbounds = config["outbounds"]
    os.makedirs(pc, exist_ok=True)
    os.makedirs(mobile, exist_ok=True)
    for key, value in map.items():
        response = requests.get(value, verify=False)
        if response.status_code == 200:
            data = response.json()
            with open(pc + "/" + key + ".json", "w") as file:
                json.dump(data, file)

            config["outbounds"] = data["outbounds"] + outbounds
            with open(mobile + "/" + key + ".json", "w") as file:
                json.dump(config, file)


singbox("./singbox")
