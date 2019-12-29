#!/bin/bash
#for ubuntu

sudo apt install apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo add-apt-repository "deb https://apt.kubernetes.io/ kubernetes-$(lsb_release -cs) main"
sudo apt update
sudo apt install kubelet kubeadm kubectl kubernetes-cni
modprobe br_netfilter
echo '1' > /proc/sys/net/ipv4/ip_forward
sysctl -a
sysctl -p
sudo apt-get update && sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update && sudo apt-cache search docker-ce
sudo apt-get update && sudo apt-get install docker-ce
systemctl enable docker && systemctl start docker
kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

## Link
https://hiseon.me/linux/ubuntu/ubuntu-kubernetes-install/
https://github.com/weaveworks/weave/issues/2789
https://hiseon.me/linux/ubuntu/install-docker/


###
#kubectl run jenkins --image=launcher.gcr.io/google/jenkins2
#kubectl get pods
#kubectl get svc
#kubectl expose deployment jenkins-batch --type=LoadBalancer --name=jenkins-batch --port=8080

#python3 내장
#kubectl run jenkins01 --image=tgamauf/jenkins-python3
#kubectl delete pods deployment jenkins-pod

