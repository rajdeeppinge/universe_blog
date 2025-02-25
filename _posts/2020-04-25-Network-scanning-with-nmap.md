---
layout: post
title: "Network scanning with nmap"
date: 2020-04-25
---

nmap or network mapper is a great open-source tool for network scanning and port discovery. The detailed description of nmap is available on its [official website](https://nmap.org/). An interesting fact about nmap and its wide ranging applications from the website :p "...It was even featured in [twelve movies](https://nmap.org/movies/), including [The Matrix Reloaded](https://nmap.org/movies/#matrix), [Die Hard 4](https://nmap.org/movies/#diehard4), [Girl With the Dragon Tattoo](https://nmap.org/movies/#gwtdt), and [The Bourne Ultimatum](https://nmap.org/movies/#bourne)."  
  
Hoping that this has generated enough curiosity in you, lets focus on the very basic use of nmap in network subnet scanning. Network scanning is useful to detect hosts in the network that are reachable from the server on which nmap is run. It is also useful in security auditing of the servers exposed to internet.  
  
We have a setup of 4 VMs on a local network with each having an IP address. The local network subnet is defined as 10.0.1.1/24 and the IPs in the below images verify this fact.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBqBtRdr1X4kse8yVROw-0l_BgtKPDP9rQD5kDoEcgiiaabMN7O3pz9RKyiajGDX8OcNMOV9ulM83dQxQqtNFyKdD88JRDwHgc5-QncOrgTkcB8JMi1irWKmCDQAmrjBo57e8voV4YvYrw/s640/Screen+Shot+2020-04-25+at+6.48.10+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBqBtRdr1X4kse8yVROw-0l_BgtKPDP9rQD5kDoEcgiiaabMN7O3pz9RKyiajGDX8OcNMOV9ulM83dQxQqtNFyKdD88JRDwHgc5-QncOrgTkcB8JMi1irWKmCDQAmrjBo57e8voV4YvYrw/s1600/Screen+Shot+2020-04-25+at+6.48.10+PM.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA4m9z2XhgvxecEf3SeUHmm5sOCKncJWYXUvdhfnjvaxzW4USDqjt1WD5Qi6IBNuh8tFXcsqFLr18-A7DzAgxM7OutldA7aDwgiStElyTGzf4f6p1jBAhHdnt_1bENf6911dSJ1TVllSgw/s640/Screen+Shot+2020-04-25+at+7.01.51+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA4m9z2XhgvxecEf3SeUHmm5sOCKncJWYXUvdhfnjvaxzW4USDqjt1WD5Qi6IBNuh8tFXcsqFLr18-A7DzAgxM7OutldA7aDwgiStElyTGzf4f6p1jBAhHdnt_1bENf6911dSJ1TVllSgw/s1600/Screen+Shot+2020-04-25+at+7.01.51+PM.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijJE3UyJZgvF91KLbbtjuc0Vkylauc7Q0FllWSYGi8setM08NACtWaty6DLLlTSk2O_KzJ3ruAkSXGUOizecsNBOUfGPom0r82sUIeu2TZUOXDiQGUc0Q8KUN5hVZS8-NeOsakt4Xu3Vo9/s640/Screen+Shot+2020-04-25+at+7.01.59+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijJE3UyJZgvF91KLbbtjuc0Vkylauc7Q0FllWSYGi8setM08NACtWaty6DLLlTSk2O_KzJ3ruAkSXGUOizecsNBOUfGPom0r82sUIeu2TZUOXDiQGUc0Q8KUN5hVZS8-NeOsakt4Xu3Vo9/s1600/Screen+Shot+2020-04-25+at+7.01.59+PM.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibdcxQ7s-Z9OQ941gLO5apMVFEeTnM7NBVQQE01Cjg2T4fb550GpoX45wAc8ueVL-sNvlSd32vFb2pCdU5ITPzIfalIdS1F8ZnF5FxkDus03qZbxW8By7En5CUNGKNMighPYeKvR53OV_l/s640/Screen+Shot+2020-04-25+at+7.02.11+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibdcxQ7s-Z9OQ941gLO5apMVFEeTnM7NBVQQE01Cjg2T4fb550GpoX45wAc8ueVL-sNvlSd32vFb2pCdU5ITPzIfalIdS1F8ZnF5FxkDus03qZbxW8By7En5CUNGKNMighPYeKvR53OV_l/s1600/Screen+Shot+2020-04-25+at+7.02.11+PM.png)

  
The goal is to verify that nmap is able to detect all the hosts in the local subnet 10.0.1.1/24. Execute the following command to scan the subnet:  
`nmap <subnet.ip>`  
  
It returns a list of hosts present on the subnet. nmap also performs a port scan on the live hosts and returns a list of ports that are open on those hosts.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBzqg0NkYB-XBFoOggIjWR9IOs3fSCA0BOjiWwHH52V8_eNkOG5IrdKfHs5CDLjMo6j8BiGEpGtwEd-mwtC2gmNyG9MHemA_UXfxi2u-OHsJI-CtEgmrtLnrF5t1VdLQ3s5WU22YJ4Ysbh/s640/Screen+Shot+2020-04-25+at+7.09.30+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBzqg0NkYB-XBFoOggIjWR9IOs3fSCA0BOjiWwHH52V8_eNkOG5IrdKfHs5CDLjMo6j8BiGEpGtwEd-mwtC2gmNyG9MHemA_UXfxi2u-OHsJI-CtEgmrtLnrF5t1VdLQ3s5WU22YJ4Ysbh/s1600/Screen+Shot+2020-04-25+at+7.09.30+PM.png)

  
nmap scanned 256 IP addresses i.e. the whole /24 subnet and found 4 hosts. It also scanned for ports on all hosts and found port 22 open which is the standard port running ssh service.  
  
  
There are many uses for network scanning. I have used nmap for the following two cases:  


  1. To find IP addresses of servers that are dynamically assigned IP addresses by DHCP.
  2. To detect all the running servers in a legacy infrastructure of hundreds of servers.

  
In conclusion, nmap is a simple yet powerful tool to scan subnets for running servers. It is also an important tool in security auditing. It gives information about all the open ports which can make servers vulnerable to various cyber-attacks. Use it wisely and make your systems more secure.

