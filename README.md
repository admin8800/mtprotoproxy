## Python版TG代理 ##

>适配/amd64/arm64/arm/v7架构
>
>支持ipv4和ipv6
>
>自带TLS伪装
>
>支持TG频道推广（需要TG老号）

### 安装git和docker-compose

### 下载项目
```
git clone https://github.com/admin8800/mtprotoproxy.git
```
### 修改`config.py`文件中的配置

32位数密钥可在[这个网站在线生成](https://www.lzltool.com/Tools/RandomHex)

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
