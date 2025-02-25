---
layout: post
title: "Using static IPs in Linux"
date: 2020-01-05
---

It is often a requirement to assign static IP addresses to some important and permanent network interfaces. This is to avoid setting up a local DHCP server or relying on IP given by your network provider which may not be stable.  
  
This post shows steps to configure static IPs in Linux using Ubuntu 16.04 and Ubuntu 18.04 distros. We are considering two distros as network configuration has changed significantly in Ubuntu 18.04.  
  
There are two general steps to be followed:  
1\. Configure the network interface and assign a static IP.  
2\. Restart interface for the changes to take effect.  
  


###  Ubuntu 16.04

 The current interfaces on the system are as follows:  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1bNxjmcrN62XGG25I1wjYrtPgUZAYzta1ZLZFArXHRb3pjWDXVKBxapnHcOpA_bFRTaqGpft6K3u6lUUlIB2fIhSHukcVsf_lNduAHm9fpYlmaCPZhPdK3ZhdqJaQrACWb-8GPJgDFTQZ/s640/Screen+Shot+2020-04-30+at+11.58.21+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1bNxjmcrN62XGG25I1wjYrtPgUZAYzta1ZLZFArXHRb3pjWDXVKBxapnHcOpA_bFRTaqGpft6K3u6lUUlIB2fIhSHukcVsf_lNduAHm9fpYlmaCPZhPdK3ZhdqJaQrACWb-8GPJgDFTQZ/s1600/Screen+Shot+2020-04-30+at+11.58.21+PM.png)

  


  
As can be seen, enp0s8 interface does not have any IP. Let's assign a static IP to it. In case you already have an interface with a DHCP assigned IP, you just need to change that IP and make it static.  
  
Edit the /etc/network/interfaces file and add the following code block. Prefer using the IP address range available for private use (see [[1](https://en.wikipedia.org/wiki/Private_network)]) while deciding an IP. I want to add the server to the local 10.0.2.1/24 network. The word "static" at the end of second line indicates that this is a static IP.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq-BA3mPaeRpN0LfkUmmgjupHdS79Q5WAWmPYzwXWd-Jv4-8vRRdsrdKnKBUWAqu3WADwKGgQ5cE-ghaOjFQM3Zuh7Eu737uGGN-l2g8V39q_UDfjfPTEXz6Imh_TneBjqOXkkFeGi9EnR/s640/Screen+Shot+2020-05-01+at+12.02.50+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq-BA3mPaeRpN0LfkUmmgjupHdS79Q5WAWmPYzwXWd-Jv4-8vRRdsrdKnKBUWAqu3WADwKGgQ5cE-ghaOjFQM3Zuh7Eu737uGGN-l2g8V39q_UDfjfPTEXz6Imh_TneBjqOXkkFeGi9EnR/s1600/Screen+Shot+2020-05-01+at+12.02.50+AM.png)

  
Now restart the network interface with the following command:  


sudo ifdown enp0s8 && sudo ip add flush dev enp0s8 && sudo ifup --force enp0s8 

  
In case this doesn't work, try restarting the networking service:  


sudo systemctl restart networking.service 

  
While this has always worked for me, in case this doesn't work, check the configuration again and restart the server:  


sudo init 6 

OR  


sudo reboot 

Upon restart the interface should be configured with static IP.  
  
This is my ifconfig output:  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMMBVNwdnbzhi3p5UGszU-0wRlhrJfGDXWQH94XLbGoGi7awxAD2ihyphenhyphenHVXbyXKxa9qili1L_8LGxwJzCIf0Xlpg2MVDHu56PyoQ95x9rSFWGvV-_ihN7p59IfK7mrhb49Wb1Ku1hyFVdoa/s640/Screen+Shot+2020-05-01+at+12.04.28+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMMBVNwdnbzhi3p5UGszU-0wRlhrJfGDXWQH94XLbGoGi7awxAD2ihyphenhyphenHVXbyXKxa9qili1L_8LGxwJzCIf0Xlpg2MVDHu56PyoQ95x9rSFWGvV-_ihN7p59IfK7mrhb49Wb1Ku1hyFVdoa/s1600/Screen+Shot+2020-05-01+at+12.04.28+AM.png)

  
Let's see how to assign a static IP for Ubuntu 18.04 before testing.  


###   

###  Ubuntu 18.04

From Ubuntu 18.04, Ubuntu shifted to Netplan network configuration. This uses yaml based configuration setup. While the method of setup changes, the steps remain the same.  
  
The current interfaces on the system are as follows:  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioPpig9DbRjF2yCCA0AJY2K9WtG8v1AsVVkAS_xGdNA-MQyxU80ETyYePhxUyQtENiA_Hjyo4mMq3u5lP09jY6rKIbFXVDTSK88I44WSgVVH_Ny6d9V4r1-_QL0g9fQe_W1k0VlaLWLatU/s640/Screen+Shot+2020-05-01+at+12.20.46+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioPpig9DbRjF2yCCA0AJY2K9WtG8v1AsVVkAS_xGdNA-MQyxU80ETyYePhxUyQtENiA_Hjyo4mMq3u5lP09jY6rKIbFXVDTSK88I44WSgVVH_Ny6d9V4r1-_QL0g9fQe_W1k0VlaLWLatU/s1600/Screen+Shot+2020-05-01+at+12.20.46+AM.png)

  
Here also, enp0s8 interface does not have any IP.   
  
Edit the `/etc/netplan/50-cloud-init.yaml` file (NOTE: the file name may be different depending on system) and add the following code block. Here also, we will use an IP from the 10.0.2.0/24 network. The line "dhcp4: no" indicates that this is a static IP.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4F7SowhdG7DioxplW8e2BnawhwEjIVByEOxFZdmyqtlQtXH2HwLO_56z9UGRAUhP-kH5e5h-_yvTxhBYuBSE0voj_eQKyqYRno9gEmQsXFHjzllBUGagFCf3MyL8JhTZdRNmq5ddzLdBm/s640/Screen+Shot+2020-05-01+at+12.25.50+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4F7SowhdG7DioxplW8e2BnawhwEjIVByEOxFZdmyqtlQtXH2HwLO_56z9UGRAUhP-kH5e5h-_yvTxhBYuBSE0voj_eQKyqYRno9gEmQsXFHjzllBUGagFCf3MyL8JhTZdRNmq5ddzLdBm/s1600/Screen+Shot+2020-05-01+at+12.25.50+AM.png)

  
Apply the configuration using the following command:  


sudo netplan apply 

Use --debug flag for debugging purposes   
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_GyTsnKMB3bHP5RGiJI8i42gLHY33_x_8f2JNFUb7BKahuMPBl98DpJOKq1h_sNwWSCcXfEc4m-N3gZ74oHcK9OtwOljAbp8RCCrQfSc5yjz0TR1Y6v5WyxzhT2Aq4gRewmhzphtfz3a7/s640/Screen+Shot+2020-05-01+at+12.26.52+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_GyTsnKMB3bHP5RGiJI8i42gLHY33_x_8f2JNFUb7BKahuMPBl98DpJOKq1h_sNwWSCcXfEc4m-N3gZ74oHcK9OtwOljAbp8RCCrQfSc5yjz0TR1Y6v5WyxzhT2Aq4gRewmhzphtfz3a7/s1600/Screen+Shot+2020-05-01+at+12.26.52+AM.png)

  
It can be seen in the above screenshot that the new config has been merged in the existing config. Let's check our interface with ifconfig,   
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1C8kjI3um_sTAYOm6VJyMguKghaW6u2WAlA2EMJ6fN2FBWHGVUsdI8d0jz54qOctTx_269V407BHyI0tvBVDCoee5sy7eG9hdz-9umI8nJrp5ej8FCEtL9d-gOqHBtjtVp1QD1TLjnIlm/s640/Screen+Shot+2020-05-01+at+12.29.36+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1C8kjI3um_sTAYOm6VJyMguKghaW6u2WAlA2EMJ6fN2FBWHGVUsdI8d0jz54qOctTx_269V407BHyI0tvBVDCoee5sy7eG9hdz-9umI8nJrp5ej8FCEtL9d-gOqHBtjtVp1QD1TLjnIlm/s1600/Screen+Shot+2020-05-01+at+12.29.36+AM.png)

  
The IP has been assigned successfully.  
  


###  Testing

Make sure you are on the server which is in the same network as the network of static IPs for testing purposes. Here we will use the two servers that we have set the static IP for.  


####  PING test:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjN79aBFohCinaYvbuICTvNLcDV9yvvdavEqSL5HeLk_PInigJw9R3xMC0OtT0vJKjmiyBTxuyxixFum7blZWYFh4LHYbdrBmFlaAqmULBoU7Z3px-slgdsD6ml0pj8s-RnT5nt2exCi7yE/s640/Screen+Shot+2020-05-01+at+12.34.24+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjN79aBFohCinaYvbuICTvNLcDV9yvvdavEqSL5HeLk_PInigJw9R3xMC0OtT0vJKjmiyBTxuyxixFum7blZWYFh4LHYbdrBmFlaAqmULBoU7Z3px-slgdsD6ml0pj8s-RnT5nt2exCi7yE/s1600/Screen+Shot+2020-05-01+at+12.34.24+AM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiO6FNGzbpTnRWhxufQL-Myg9NSxQHRKhFWnWsjsGpg55FKA0Ve4VNKd17Uui9fQGJ52A8Za74OjLSUQ8t12Vh0qGdxJSYuipnQb2y_s4lfodwsY-zJK2aoQcgwIPUyXllJEDQRSbN_tJAA/s640/Screen+Shot+2020-05-01+at+12.34.31+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiO6FNGzbpTnRWhxufQL-Myg9NSxQHRKhFWnWsjsGpg55FKA0Ve4VNKd17Uui9fQGJ52A8Za74OjLSUQ8t12Vh0qGdxJSYuipnQb2y_s4lfodwsY-zJK2aoQcgwIPUyXllJEDQRSbN_tJAA/s1600/Screen+Shot+2020-05-01+at+12.34.31+AM.png)

####  SSH test

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxhXtLb4qbzfP2LAhEbncK12UAF2F-LxoAPuVU3BSECBIKPK28jDUS9q8dWPigfOERF9PxVg38aHCyqOnIZxCGNAi7pREWhXAwHuYzo4E28JMMwq3D7LTGfu_BJ00HCwkVpXH_FGUuz86s/s640/Screen+Shot+2020-05-01+at+12.36.10+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxhXtLb4qbzfP2LAhEbncK12UAF2F-LxoAPuVU3BSECBIKPK28jDUS9q8dWPigfOERF9PxVg38aHCyqOnIZxCGNAi7pREWhXAwHuYzo4E28JMMwq3D7LTGfu_BJ00HCwkVpXH_FGUuz86s/s1600/Screen+Shot+2020-05-01+at+12.36.10+AM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibzQQUXEPDhaF80poYX3P1PvDNNduvKgWIGHLJxEm15xfYSXuuv1Me5Q1siSoZ0r5BZ5Pl4BULPyLAQaLNf8mtZMpTlx2rnaRYGt86qCAtrQn6GA4Bb1n9Uh1kxdEo-L_7F2rygzZxP_jj/s640/Screen+Shot+2020-05-01+at+12.36.30+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibzQQUXEPDhaF80poYX3P1PvDNNduvKgWIGHLJxEm15xfYSXuuv1Me5Q1siSoZ0r5BZ5Pl4BULPyLAQaLNf8mtZMpTlx2rnaRYGt86qCAtrQn6GA4Bb1n9Uh1kxdEo-L_7F2rygzZxP_jj/s1600/Screen+Shot+2020-05-01+at+12.36.30+AM.png)

####   

####  Use Cases: 

Static IPs are useful when:  


  1. The DHCP server is unstable or insufficient to manage a large number of servers. 
  2. Another possible issue is that the static IP lease expires frequently and takes time to reestablish causing frequent outages.

  
_Have you faced any such issues with your DHCP server? Have you used any innovative strategies for static IP assignment? Let me know in the comments._  
_  
_  


####  References:

####  [1] <https://en.wikipedia.org/wiki/Private_network> 

