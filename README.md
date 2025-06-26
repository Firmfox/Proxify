# Proxify 🔄🔗

Automated proxy and V2Ray configuration scraper that collects fresh SOCKS4, SOCKS5, HTTP/HTTPS proxies, MTProto (Telegram), and V2Ray configs from various public sources.

![GitHub last commit](https://img.shields.io/github/last-commit/74647/proxify)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

## Features ✨

- **Multi-protocol support**: SOCKS4, SOCKS5, HTTP, HTTPS, MTProto, and V2Ray
- **Automatic updates**: Regularly refreshed proxy lists
- **Organization**: V2Ray configs sorted by protocol (VMess, VLESS, Trojan, etc.)
- **Ready-to-use**: Formatted proxy lists for immediate use

## Subscription URLs 📡

Proxify automatically generates and maintains these subscription URLs containing fresh proxies:

### V2Ray Configuration Files

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-1.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-2.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-3.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-4.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-5.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-6.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-7.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-8.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-9.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-10.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-11.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-12.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-13.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-14.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-15.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-16.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-17.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-18.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-19.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/mixed/subscription-20.txt
```

### Protocol-Specific Configs

```bash
  https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/seperated_by_protocol/vmess.txt
```

```bash
  https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/seperated_by_protocol/vless.txt
```

```bash
  https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/seperated_by_protocol/trojan.txt
```

```bash
  https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/seperated_by_protocol/shadowsocks.txt
```

```bash
  https://raw.githubusercontent.com/74647/proxify/main/v2ray_configs/seperated_by_protocol/other.txt
```

### Telegram Proxy Links

```bash
https://raw.githubusercontent.com/74647/proxify/main/telegram_proxies/mtproto.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/telegram_proxies/socks5.txt
```
 
### Other Proxy Links

```bash
https://raw.githubusercontent.com/74647/proxify/main/proxies/socks4.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/proxies/socks5.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/proxies/http.txt
```

```bash
https://raw.githubusercontent.com/74647/proxify/main/proxies/https.txt
```
## 🛠️ How to Use Proxify

### 📲 V2Ray Clients Setup

#### Recommended Clients by Platform:

| Platform  | Recommended Clients |
|-----------|---------------------|
| Windows   | [v2rayN](https://github.com/2dust/v2rayN), [Nekoray](https://github.com/MatsuriDayo/nekoray), [Hiddify](https://github.com/hiddify/hiddify-app) |
| macOS     | [V2RayX](https://github.com/Cenmrev/V2RayX), [v2rayN](https://github.com/2dust/v2rayN), [Hiddify](https://github.com/hiddify/hiddify-app) |
| Linux     | [Qv2ray](https://github.com/Qv2ray/Qv2ray), [Nekoray](https://github.com/MatsuriDayo/nekoray), [Hiddify](https://github.com/hiddify/hiddify-app) |
| Android   | [v2rayNG](https://github.com/2dust/v2rayNG), [Hiddify](https://github.com/hiddify/hiddify-app), [NapsternetV](https://play.google.com/store/apps/details?id=com.napsternetlabs.napsternetv) |
| iOS       | [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118), [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690), [NapsternetV](https://apps.apple.com/us/app/npv-tunnel/id1629465476) |

#### Importing Subscriptions:
1. Copy a subscription URL from Proxify's `v2ray_configs/mixed/` folder
2. In your client:
   - v2rayN: `Subscription` > `Add Subscription` > Paste URL > `Update`
   - v2rayNG: `Groups` > `+` > Paste URL > `OK` > `Update`
   - Shadowrocket: `Add Subscription` > Paste URL > `Download`
3. Select a working server from the updated list
4. Connect and verify your IP has changed

### 🔌 Proxy Configuration Guide

#### Desktop Setup:

**Browser Configuration:**
1. Install:
   - [FoxyProxy](https://getfoxyproxy.org/) (Firefox/Chrome)
2. Add proxies from Proxify's `proxies/` folder
3. Configure pattern-based automatic switching

**System-Wide Proxy:**
- Windows:
  Settings > Network & Internet > Proxy
Set "Use a proxy server" and enter details
text

- macOS:
  System Preferences > Network > Advanced > Proxies
Check SOCKS/HTTP proxy and enter details
text

- Linux (GNOME):
  Settings > Network > Network Proxy > Manual
Enter proxy details for each protocol
text


#### Mobile Setup:

**Android:**
1. Recommended apps:
 - [SocksDroid](https://www.socksdroid.com/)
2. Configuration:
 - Import proxy list from `proxies/` folder
 - Enable VPN mode for system-wide proxy
 - Set up per-app proxy rules if needed

**iOS:**
1. Recommended apps:
 - [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)
 - [Potatso](https://apps.apple.com/us/app/potatso-lite/id1239860606)
2. Configuration:
 - Manual proxy entry with IP:Port
 - Import proxy lists via URL or file sharing
 - Enable in iOS Settings > VPN

## Contribution 🤝

Contributions are welcome! Feel free to:

- **Add** new reliable proxy sources

- **Optimize** performance

## Disclaimer ⚠️

This tool is for educational purposes only. The maintainers are not responsible for how these proxies are used. Always respect terms of service of services you access.

## License 📜

![License](https://img.shields.io/github/license/74647/Proxify)
