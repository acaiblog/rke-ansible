# 环境信息
节点信息

| 节点名称  | IP地址            | 角色         |
|-------|-----------------|------------|
| rke01 | 192.168.234.132 | k8s master |
| rke02 | 192.168.234.130 | k8s worker |
| rke02 | 192.168.234.131 | k8s worker |
软件版本

| 名称     | 版本                 |
|--------|--------------------|
| 操作系统   | CentOS7.5.1804_x86 |
| Docker |  20.10.9                  |
| RKE    | v1.3.20                   |
| k8s | v1.21.14-rancher1-1 |
| rancher | 2.6.6 |

# 环境部署
安装ansible
```bash
yum install python3-pip
pip3 install --upgrade pip
pip3 install setuptools_rust
pip3 install ansible==4.10.0
```
下载部署脚本
```bash
git clone https://gitee.com/acaiblog/rke-ansible.git
```
编辑`rke-ansible/inventory/hosts`添加部署节点
```
[k8s-master]
192.168.234.132 hostname=rke01

[k8s-worker]
192.168.234.130 hostname=rke02
192.168.234.131 hostname=rke03

[k8s:children]
k8s-master
k8s-worker

[all:vars]
ansible_ssh_user=root
ansible_ssh_pass=1
ansible_ssh_port=22
```
编辑`rke-ansible/group_vars/all.yml`修改如下内容
```yaml
---
api_interface: ens33
keepalived_vip: "192.168.234.251"
keepalived_route_id: 85
rke_user: apps
docker_version: 20.10.9
rke_version: v1.3.20
k8s_version: v1.21.14-rancher1-1
rancher_domain: rancher.acaiblog.top
rancher_version: 2.6.6
```
执行部署脚本
```bash
cd rke-ansible
python deploy.py --action deploy
```