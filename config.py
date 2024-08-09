# 连接端口
PORT = 8443

# 密钥（32个十六进制字符）
USERS = {
    "TG链接":  "bc6dddb180509c5b18cb51d17d849455",
    #"TG链接二": "fa33e8ed3523ce760c241129c66153b6",
}

MODES = {
    # 经典模式，容易被墙
    "classic": False,

    # 流量混淆
    "secure": True,

    # TLS加密
    "tls": True
}

# 伪装域名
TLS_DOMAIN = "www.swift.com"

#广告标签，可从 @MTProxybot 获取
#AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

