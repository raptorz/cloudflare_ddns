#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fire
import requests


class CloudflareDNS:
    def __init__(self, token, zone_id):
        self.token = token
        self.url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    def __call__(self, method, dns_id=None, **kwargs):
        url = (self.url + "/" + dns_id) if dns_id else self.url
        fn = getattr(requests, method)
        if not fn:
            raise ValueError(f"Invalid method: {method}")
        params = dict(params=kwargs) if method in ['get', 'delete'] else dict(json=kwargs)
        headers = {"Authorization": f"Bearer {self.token}",
                   "Content-Type": "application/json"}
        res = fn(url, headers=headers, **params)
        res.raise_for_status()
        return res.json()

    def get_dns_id(self, hostname, type='A'):
        res = self('get', name=hostname, type=type)
        return res['result'][0]['id']

    def get_dns_info(self, dns_id):
        res = self('get', dns_id)
        return res['result']

    def set_dns_ip(self, dns_id, ip):
        res = self("patch", dns_id, content=ip)
        return res['result']


def cloudflare_ddns(token, zone_id, dns_name, dns_ip="", dns_type="A"):
    """
    Cloudflare DDNS tool
    :param token: Cloudflare API token
    :param zone_id: Cloudflare zone ID
    :param dns_name: DNS host name
    :param dns_ip: DNS IP address
    :param dns_type: DNS record type, default is 'A'
    :return:
    """
    if not dns_ip:
        res = requests.get("https://httpbin.org/ip")
        res.raise_for_status()
        dns_ip = res.json()['origin']
    api = CloudflareDNS(token, zone_id)
    dns_id = api.get_dns_id(dns_name, type=dns_type)
    if not dns_id:
        print(f"Invalid dns_name: {dns_name}")
        return
    info = api.get_dns_info(dns_id)
    if info['content'] == dns_ip:
        return
    api.set_dns_ip(dns_id, dns_ip)


if __name__ == "__main__":
    fire.Fire(cloudflare_ddns)
