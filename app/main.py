from requests import Session
from requests.exceptions import RequestException
from random import randint
from os import path, makedirs
from itertools import batched
from base64 import b64encode, b64decode

v2ray_addresses = [
    'https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/BeVpn.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt',
    'https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray',
    'https://raw.githubusercontent.com/ts-sf/fly/main/v2', #b64
    'https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/BeVpn.txt', #b64
    'https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/app/sub.txt', #b64
    'https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt', #b64
    'https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt', #b64
    'https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt', #b64
    'https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt', #b64
    'https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed', #b64
    'https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/mix',
    'https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/mixed_iran.txt',
    'https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html',
    'https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt',
    'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt',
    'https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt',
    'https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt',
    'https://raw.githubusercontent.com/code3-dev/v-data/refs/heads/main/vip',
    'https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub', #b64
    'https://raw.githubusercontent.com/MrAbolfazlNorouzi/iran-configs/refs/heads/main/configs/working-configs.txt',
    'https://www.v2nodes.com/subscriptions/country/all/', #b64
    'https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt',
    'https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt',
]


proxy_addresses = {
    'socks5': [
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/socks5.txt',
        'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/refs/heads/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/hookzof/socks5_list/refs/heads/master/proxy.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks5.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks5/data.txt',
        'https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks5_proxies.txt',
        'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/socks5.txt',
        'https://raw.githubusercontent.com/elliottophellia/proxylist/refs/heads/master/results/socks5/global/socks5_checked.txt',
        'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/socks5.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/SOCKS5_RAW.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/socks5_proxies.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks5.txt',
    ],
    'socks4': [
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks4/data.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/socks4_proxies.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/socks4.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks4.txt',
        'https://proxyspace.pro/socks4.txt'
    ],
    'http': [
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/http.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/http_proxies.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt',
        'https://api.openproxylist.xyz/http.txt',
        'https://rootjazz.com/proxies/proxies.txt',
        'https://proxy-spider.com/api/proxies.example.txt',
        'https://multiproxy.org/txt_all/proxy.txt',
        'https://proxyspace.pro/http.txt'
    ],
    'https': [
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt',
        'https://raw.githubusercontent.com/claude89757/free_https_proxies/refs/heads/main/https_proxies.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt',
        'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/https.txt',
        'https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/https.txt',
        'https://proxyspace.pro/https.txt'
    ]
}

metadata_title = "#profile-title: base64:"
metadata_headers = """
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/firmfox/Proxify
#profile-web-page-url: https://github.com/firmfox/Proxify
"""

#-----------------------------------------

def check_existence(address):
    if not path.exists(address):
        makedirs(address)

def generate_protocols():

    check_existence('v2ray_configs/separated_by_protocol')

    protocol_map = {
        'mixed': [],
        'vmess': [],
        'vless': [],
        'trojan': [],
        'shadowsocks': [],
        'wireguard': [],
        'warp': [],
        'reality': [],
        'other': []
    }

    mixed_data = set()

    session = Session()

    try:

        for address in v2ray_addresses:

            try:

                response = session.get(address, timeout=15)
                response.raise_for_status()

                raw_text = response.text.strip()

                try:
                    raw_text = b64decode(raw_text).decode('utf-8')
                except Exception:
                    pass

                for config in raw_text.splitlines():

                    config = config.strip()

                    if config.startswith((
                        'vless://',
                        'vmess://',
                        'ss://',
                        'shadowsocks://',
                        'wg://',
                        'wireguard://',
                        'hysteria2://',
                        'trojan://'
                    )):

                        config = (
                            config.split('#')[0]
                            + f'#[🛜] @Firmfox [{randint(10,100)}-{randint(1000,10000)}]'
                        )

                        mixed_data.add(config)

            except RequestException as e:
                print(f'[ERROR] {address}: {e}')

    finally:
        session.close()

    protocol_map['mixed'] = list(mixed_data)

    for config in protocol_map['mixed']:

        if config.startswith('vmess://'):
            protocol_map['vmess'].append(config)

        elif config.startswith('vless://'):
            protocol_map['vless'].append(config)

        elif config.startswith('trojan://'):
            protocol_map['trojan'].append(config)

        elif config.startswith(('ss://', 'shadowsocks://')):
            protocol_map['shadowsocks'].append(config)

        elif config.startswith(('wg://', 'wireguard://')):
            protocol_map['wireguard'].append(config)

        elif config.startswith('warp://'):
            protocol_map['warp'].append(config)

        elif config.startswith('reality://'):
            protocol_map['reality'].append(config)

        else:
            protocol_map['other'].append(config)

    for protocol, configs in protocol_map.items():

        profile_name = f'{protocol} - @Firmfox'

        content = (
            metadata_title
            + b64encode(profile_name.encode()).decode()
            + metadata_headers
            + '\n'.join(configs)
        )

        with open(
            f'v2ray_configs/separated_by_protocol/{protocol}.txt',
            'w',
            encoding='utf-8'
        ) as protocol_file:
            protocol_file.write(content)

def generate_subscriptions():

    check_existence('v2ray_configs/subscriptions')

    with open(
        'v2ray_configs/separated_by_protocol/mixed.txt',
        'r',
        encoding='utf-8'
    ) as mixed_file:

        batches = list(batched(mixed_file.readlines(), 100))

    for batch_id, batch in enumerate(batches, start=1):

        profile_name = f'SUB-{batch_id} - @Firmfox'

        content = (
            metadata_title
            + b64encode(profile_name.encode()).decode()
            + metadata_headers
            + ''.join(batch)
        )

        with open(
            f'v2ray_configs/subscriptions/subscription-{batch_id}.txt',
            'w',
            encoding='utf-8'
        ) as subscription:

            subscription.write(content)

#-----------------------------------------

def generate_proxylists():

    check_existence('proxy')

    session = Session()

    try:
        for proxy_protocol, addresses in proxy_addresses.items():

            proxy_list = set()

            for address in addresses:

                try:
                    response = session.get(address, timeout=10)
                    response.raise_for_status()

                    for proxy_data in response.text.splitlines():

                        proxy_data = proxy_data.strip()

                        if not proxy_data:
                            continue

                        if '://' in proxy_data:
                            proxy_data = proxy_data.split('://', 1)[1]

                        proxy_list.add(proxy_data)

                except RequestException as e:
                    print(f'[ERROR] {address}: {e}')

            with open(f'proxy/{proxy_protocol}.txt', 'w', encoding='utf-8') as proxy_file:
                proxy_file.write('\n'.join(sorted(proxy_list)))

    finally:
        session.close()


generate_protocols()
generate_subscriptions()
generate_proxylists()
