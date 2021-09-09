# CloudflareDDNS

Cloudflare DDNS python3 script.

## Usage

### Get API token

* Login your Cloudflare account, create an API token at [this page](https://dash.cloudflare.com/profile/api-tokens)
* Use "Edit zone DNS" template.
* Choose an specific zone at "Zone Resource"
* Get token

### Get zone ID

* Get "Zone ID" from your zone page
 
### Install requirements

```bash
pip3 install -r requirements.txt
```

### Run it

```bash
python3 cfdns.py <token> <zone_id> <dns_name>
```

## 用法

### 获取API token

* 登录Cloudflare账号，在[这里](https://dash.cloudflare.com/profile/api-tokens)创建API token
* 使用"编辑区域DNS"模板
* 在"区域资源"选择一个指定的区域
* 获取token

### 获取zone ID

* 在区域页面找到Zone ID

### 安装依赖

```bash
pip3 install -r requirements.txt
```

### 运行之

```bash
python3 cfdns.py <token> <zone_id> <dns_name>
```
