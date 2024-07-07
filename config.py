# 连接端口
PORT = 8443

# 密钥（32个十六进制字符）
USERS = {
    "tg":  "bc6dddb180509c5b18cb51d17d849455",
    # "tg2": "fa33e8ed3523ce760c241129c66153b6",
}

MODES = {
    # 经典模式，容易被检测
    "classic": False,

    # TLS伪装加密
    # 可能与非常旧的客户端不兼容
    "secure": True,

    # 使代理更难被检测到
    # 可能与旧客户端不兼容
    "tls": True
}

# 伪装域名
TLS_DOMAIN = "www.swift.com"

# 广告标签，可从 @MTProxybot 获取
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

