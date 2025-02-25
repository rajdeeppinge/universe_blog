---
layout: post
title: "Virtualbox networking workarounds"
date: 2020-04-25
---

Virtualbox networking setup is a tedious task to understand and implement the very first time. This is mainly because of the multiple network options that it provides and the different locations used to setup those networks. Please follow this [virtualbox networking manual](https://www.virtualbox.org/manual/ch06.html) to learn about virtualbox networking options. This post builds on the above manual to demonstrate a custom case for setting up a local network of 4 virtual machines (VMs) with internet access and also give the host access to these machines.  
  
The specific networking requirement was not addressed by any of the network options provided by virtualbox. Let's understand it through the table provided in the above manual:  
  
**Mode**| **VM→Host** | **VM←Host** | **VM1↔VM2** | **VM→Net/LAN** | **VM←Net/LAN**  
---|---|---|---|---|---  
Host-only | **+** | **+** | **+** | – | –   
Internal | – | – | **+** | – | –   
Bridged | **+** | **+** | **+** | **+** | **+**  
NAT | **+** | Port forward | – | **+** | Port forward   
NATservice | **+** | Port forward | **+** | **+** | Port forward   
**Requirement** | **+** | **+** | **+** | **+** | **Port forward**  
  
As can be seen, the requirement is to have host access the VMs seamlessly but do not allow the outside network to access the VMs without port forwarding. A workaround to fulfill this requirement is to set up two networks that together satisfy the requirements. From the above table, two networks can be:   


  1. A host-only network and a NAT   
OR 
  2. A host-only network and a NAT service.

It was decided to setup a host-only network and a NAT service network. The setup is simple,  
  


####  Host-only network

  1. Navigate to File -> Host Network Manager (This path may change based on virtualbox version.)
  2. Create a new network
  3. Go to "properties" tab and edit the properties of the network adapter. Apply the properties.  
  
NOTE: Make sure the IPv4 address doesn't include network address  
For example, in the settings shown in the image, the IPv4 address should not be 10.0.1.0/24 but 10.0.1.1/24 otherwise it causes issues.  

  4. If you want DHCP managed IPs, tick the DHCP checkbox.
  5. Edit the DHCP server properties in the "DHCP server" tab. Apply the settings



[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9mwa5btzh_G6l2iM72RMWp805TSudVyyNq2gxfr4IYLROXEiSlvN84Q_47N7JA6Y8dlPUwF2ifB-HYXX6sH1WV77FMLysshyphenhyphenF1cJZsF4ALdrdw_J_OHU3csSuws5Tb0DPxlC50qQDOoQN/s640/Screen+Shot+2020-04-25+at+5.14.13+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9mwa5btzh_G6l2iM72RMWp805TSudVyyNq2gxfr4IYLROXEiSlvN84Q_47N7JA6Y8dlPUwF2ifB-HYXX6sH1WV77FMLysshyphenhyphenF1cJZsF4ALdrdw_J_OHU3csSuws5Tb0DPxlC50qQDOoQN/s1600/Screen+Shot+2020-04-25+at+5.14.13+PM.png)

  
Now edit the network settings for all the VMs and add a new adapter with host-only network as below.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH1OPxmSZSwuinKOI-WH5Vu_qxfLD5uaNCf6SB7LQMBUFCHkPKYNsHRXtLxN4oLDS8pfQ5Ncm2xxnvZu5gGA4KOw4_8P5sr2NRrMB3niKycxY9m12nterSxSRhHIx5V5OLyNb-fowDP0eK/s640/Screen+Shot+2020-04-25+at+5.21.56+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH1OPxmSZSwuinKOI-WH5Vu_qxfLD5uaNCf6SB7LQMBUFCHkPKYNsHRXtLxN4oLDS8pfQ5Ncm2xxnvZu5gGA4KOw4_8P5sr2NRrMB3niKycxY9m12nterSxSRhHIx5V5OLyNb-fowDP0eK/s1600/Screen+Shot+2020-04-25+at+5.21.56+PM.png)

  
   


####  NAT service network / NAT network

  1. To setup this network, navigate to Virtualbox -> preferences -> Network (This path may change based on virtualbox version.)
  2. Create a new network
  3. Navigate to preferences tab and configure necessary settings.  
  
In the image, the "Supports DHCP" checkbox is disabled. This is because the intention is to setup static IPs on all the VMs on the NAT network interface.



[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhG8T0-4-GE3q0d9Bz2VB7B7CQEHVGiFirOqY0xiYiJ-O-XLHb-cyIc_fd1cPj1VONqcvpetY9l9E4Kgu6ZTCEE7H2jJKmqK66-UOEpXZW1o2Re3BwTT_1oMx3bxux7jiuzPGJqJ7CX_Sqg/s640/Screen+Shot+2020-04-25+at+5.26.39+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhG8T0-4-GE3q0d9Bz2VB7B7CQEHVGiFirOqY0xiYiJ-O-XLHb-cyIc_fd1cPj1VONqcvpetY9l9E4Kgu6ZTCEE7H2jJKmqK66-UOEpXZW1o2Re3BwTT_1oMx3bxux7jiuzPGJqJ7CX_Sqg/s1600/Screen+Shot+2020-04-25+at+5.26.39+PM.png)

  
Again edit the network settings for all the VMs and add a new adapter with NAT network.  
  
  


###  Test 

(Re)start the VMs and check their network interfaces.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSJCbxPIrcBYEvpGbJi09wkuE4uXcgNtl5dO95km5rHIadSpWKbLBiYgVF9bDSWpAPS5athd5KpYmrlG7HAhq0vEENiJkeWo0zZnP5eLlnSbc4DCm0x-MBVHBxF2EPu3ou3vjbCzRkur_g/s640/Screen+Shot+2020-04-25+at+5.46.38+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSJCbxPIrcBYEvpGbJi09wkuE4uXcgNtl5dO95km5rHIadSpWKbLBiYgVF9bDSWpAPS5athd5KpYmrlG7HAhq0vEENiJkeWo0zZnP5eLlnSbc4DCm0x-MBVHBxF2EPu3ou3vjbCzRkur_g/s1600/Screen+Shot+2020-04-25+at+5.46.38+PM.png)

  
Apart from the loopback address, there are two other interfaces, enp0s3 on 10.0.1.1/24 host-only network and enp0s8 on 10.0.2.0/24 NAT network.  
  
  


###  Conclusion

Even though virtualbox network modes may not cover all the networking requirements, a combination of multiple networking modes can be used to set up-to 4 network interfaces on the VMs to achieve the desired configuration.

