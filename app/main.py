import os
import requests
from base64 import b64decode
from concurrent.futures import ThreadPoolExecutor
import time
import shutil

MT_PROTO_LINKS = [
    'https://mtpro.xyz/api/?type=mtproto',
    'https://mtpro.xyz/api/?type=socks'
]

V2RAY_LINKS = [
    "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/BeVpn.txt",
    "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
    "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt",
    "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks",
    "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
    "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
    "https://mrpooya.top/SuperApi/BE.php",
    "https://v2.alicivil.workers.dev",
    "https://gist.githubusercontent.com/WLget/aeb222e378a8dcbd74e06413dbacf400/raw/base64.txt",
    "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/BeVpn.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/app/sub.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/mix",
    "https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
    "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
    "https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt",
    "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
    "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/normal/mix",
    "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged",
    "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUBSCRIPTION_LINK/main/v2rayconfigs.txt",
    "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
    "https://raw.githubusercontent.com/C4ssif3r/V2ray-sub/main/all.txt",
    "https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt",
    "https://raw.githubusercontent.com/code3-dev/v-data/refs/heads/main/vip",
    'https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub',
    'https://raw.githubusercontent.com/shabane/kamaji/master/hub/b64/merged.txt',
    "https://raw.githubusercontent.com/MrAbolfazlNorouzi/iran-configs/refs/heads/main/configs/working-configs.txt",
    'https://www.v2nodes.com/subscriptions/country/all/',
    "https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt"
]

PROXY_LINKS = {
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
        'https://alexa.lr2b.com/proxylist.txt',
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
    ],
    'mtproto': [
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-proxies-collector/refs/heads/main/proxies'
    ]
}

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def fetch_url(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        return None

def clean_proxy_line(line):
    line = line.strip()
    prefixes = ['socks5://', 'socks4://', 'http://', 'https://']
    for prefix in prefixes:
        if line.startswith(prefix):
            line = line[len(prefix):]
            break
    return line

def get_metadata_headers():
    return """#profile-title: base64:8J+GkyBHaXQ6IEBGaXJtZm94IOKbk++4j+KAjfCfkqU=
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/firmfox/Proxify
#profile-web-page-url: https://github.com/firmfox/Proxify\n"""

def organize_configs(configs):
    protocol_map = {
        'vmess': [],
        'vless': [],
        'trojan': [],
        'shadowsocks': [],
        'wireguard': [],
        'warp': [],
        'reality': [],
        'other': []
    }
    
    for config in configs:
        if not config.strip():
            continue
            
        config_lower = config.lower()
        if 'vmess://' in config_lower:
            protocol_map['vmess'].append(config)
        elif 'vless://' in config_lower:
            protocol_map['vless'].append(config)
        elif 'trojan://' in config_lower:
            protocol_map['trojan'].append(config)
        elif 'ss://' in config_lower or 'shadowsocks://' in config_lower:
            protocol_map['shadowsocks'].append(config)
        elif 'wireguard' in config_lower or 'wg://' in config_lower:
            protocol_map['wireguard'].append(config)
        elif 'warp' in config_lower:
            protocol_map['warp'].append(config)
        elif 'reality' in config_lower:
            protocol_map['reality'].append(config)
        else:
            protocol_map['other'].append(config)
    
    return protocol_map

def save_protocol_files(protocol_map):
    ensure_directory_exists('v2ray_configs/seperated_by_protocol')
    metadata = get_metadata_headers()
    
    for protocol, configs in protocol_map.items():
        if configs:
            with open(f'v2ray_configs/seperated_by_protocol/{protocol}.txt', 'w') as f:
                f.write(metadata)
                f.write('\n'.join(configs) + '\n')

def save_subscription_files(configs, chunk_size=500):
    ensure_directory_exists('v2ray_configs/mixed')
    metadata = get_metadata_headers()
    
    for i in range(0, len(configs), chunk_size):
        chunk = configs[i:i + chunk_size]
        with open(f'v2ray_configs/mixed/subscription-{i//chunk_size + 1}.txt', 'w') as f:
            f.write(metadata)
            f.write('\n'.join(chunk) + '\n')

def get_proxy(proxy_type):
    proxies = set()
    
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(fetch_url, url): url for url in PROXY_LINKS[proxy_type]}
        
        for future in futures:
            data = future.result()
            if data:
                for line in data.splitlines():
                    cleaned = clean_proxy_line(line)
                    if cleaned:
                        proxies.add(cleaned)
    
    if proxies:
        ensure_directory_exists('proxies')
        with open(f'proxies/{proxy_type}.txt', 'w') as f:
            f.write('\n'.join(proxies) + '\n')

def get_v2ray():
    configs = set()
    
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(fetch_url, url): url for url in V2RAY_LINKS}
        
        for future in futures:
            data = future.result()
            if data:
                try:
                    decoded = b64decode(data).decode('utf-8')
                    configs.update(line.strip() for line in decoded.splitlines() if line.strip())
                except:
                    configs.update(line.strip() for line in data.splitlines() if line.strip())
    
    if configs:
        configs = list(configs)
        protocol_map = organize_configs(configs)
        save_protocol_files(protocol_map)
        save_subscription_files(configs)

def get_mtproto(link_index):
    try:
        response = requests.get(MT_PROTO_LINKS[link_index], timeout=20)
        response.raise_for_status()
        data = response.json()
        
        ensure_directory_exists('telegram_proxies')
        
        if link_index == 0:
            filename = 'telegram_proxies/mtproto.txt'
            with open(filename, 'w') as f:
                if isinstance(data, list):
                    for proxy in data:
                        f.write(f"https://t.me/proxy?server={proxy['host']}&port={proxy['port']}&secret={proxy['secret']}\n")
                elif isinstance(data, dict):
                    f.write(f"https://t.me/proxy?server={data['host']}&port={data['port']}&secret={data['secret']}\n")
        else:
            filename = 'telegram_proxies/socks5.txt'
            with open(filename, 'w') as f:
                if isinstance(data, list):
                    for proxy in data:
                        host = proxy.get('ip', proxy.get('host', ''))
                        f.write(f"https://t.me/proxy?server={host}&port={proxy['port']}\n")
                elif isinstance(data, dict):
                    host = data.get('ip', data.get('host', ''))
                    f.write(f"https://t.me/proxy?server={host}&port={data['port']}\n")
    except Exception as e:
        print(f"Error in get_mtproto: {e}")

def cleanup_old_files():
    for dir_path in ['Seperated_by_protocol', 'proxy', 'telegram_proxy', 'mix']:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

def main():
    if os.path.basename(os.getcwd()) == 'app':
        os.chdir('..')
    start_time = time.time()
    cleanup_old_files()
    
    ensure_directory_exists('telegram_proxies')
    ensure_directory_exists('proxies')
    ensure_directory_exists('v2ray_configs/mixed')
    ensure_directory_exists('v2ray_configs/seperated_by_protocol')
    
    with ThreadPoolExecutor(max_workers=7) as executor:
        executor.submit(get_proxy, 'socks4')
        executor.submit(get_proxy, 'socks5')
        executor.submit(get_proxy, 'http')
        executor.submit(get_proxy, 'https')
        executor.submit(get_mtproto, 0)
        executor.submit(get_mtproto, 1)
        executor.submit(get_v2ray)
    
    print(f"Execution completed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
