## Python版TG代理 ##

>适配/amd64/arm64/armv7架构
>
>支持ipv4和ipv6
>
>默认开启混淆伪装和TLS加密
>
>支持TG频道推广（需要TG老号）

## 一键脚本
```
bash <(curl -sSL https://raw.githubusercontent.com/admin8800/mtprotoproxy/master/mtproxy.sh)
```
---

## Docker部署

### 下载项目(自行安装Git和Docker-compose)
```
git clone https://github.com/admin8800/mtprotoproxy.git
```
#### 修改`config.py`文件中的配置

#### 32位数密钥可在[这个网站在线生成](https://www.lzltool.com/Tools/RandomHex)

### 一键运行
```
cd mtprotoproxy
```
```
docker compose up -d
```

### 查看链接

```
docker logs mtp
```

#### 重启
```
docker restart mtp
```

#### 停止
```
docker stop mtp
```
#### 删除
```
docker rm -f mtp
```
