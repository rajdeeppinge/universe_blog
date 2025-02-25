---
layout: post
title: "Local domain name resolution using /etc/hosts"
date: 2020-05-01
---

The /etc/hosts file is a powerful mechanism for managing the information about hosts in the local network in the absence of a local DNS server.  


####  Setup

We have 4 VMs in the local /24 network. The following are the details:  
vm-1-ubuntu-16-04 - 10.0.1.11  
vm-2-ubuntu-16-04 - 10.0.1.12  
vm-1-ubuntu-18-04 - 10.0.1.21  
vm-2-ubuntu-18-04 - 10.0.1.22  
  
The VMs are reachable via their IP address but not by their hostnames.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjel1L0sI9HqYCZIFyl_9tJ5eRsaHi-Ed6hMddRMtpq7YFFwrDRcGQB0P6-yITRT3HO5-lkdt7AemCAVlMrKtSI8sTRkDp7yYkYIK0YFXffOuAZvoTwtA22xh1Izc_m6tDYKhYoEx-MmF_3/s640/Screen+Shot+2020-05-01+at+5.29.04+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjel1L0sI9HqYCZIFyl_9tJ5eRsaHi-Ed6hMddRMtpq7YFFwrDRcGQB0P6-yITRT3HO5-lkdt7AemCAVlMrKtSI8sTRkDp7yYkYIK0YFXffOuAZvoTwtA22xh1Izc_m6tDYKhYoEx-MmF_3/s1600/Screen+Shot+2020-05-01+at+5.29.04+PM.png)

  
This is problematic because we have to remember their IP addresses everytime we want to access these hosts. It is would be much simpler to remember and access the servers by their hostnames. For that we need some sort of mapping between the IP addresses and their corresponding host names. There are 3 common ways of achieving this mapping.  


  1. Setup a DNS server which handles resolution for your local network.
  2. Use an existing DNS server of the local Internet Service Provider (ISP) or any other higher level ISP. Note that a public static IP address is required for this setup.
  3. Handle the name resolution on every host on the local network via the /etc/hosts file.

The first option is the best and least expensive. However, it is not always feasible to setup a local DNS server. First of all, it needs to be setup and maintained. Secondly, it may be a huge overhead for a local network containing a very small number of hosts as is our case.  
  
Since we have only 4 hosts in the network, we'll go for the third option. Let's add entries for all the hosts in the /etc/hosts file on every server.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggUi1kGseBNrAxzQRsDwZB4LpmUrCxoWnf3ll32R9FYvsVzymjqKUUHmG26dqaQ3yJ0yB-IZykuywIODQEgtjMA6_99hKLF1qHSjN_VEXhV_fbtt9HCt-o2QpCA7Yj6qFD6zkN2lgz3MQ4/s640/Screen+Shot+2020-05-01+at+5.32.05+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggUi1kGseBNrAxzQRsDwZB4LpmUrCxoWnf3ll32R9FYvsVzymjqKUUHmG26dqaQ3yJ0yB-IZykuywIODQEgtjMA6_99hKLF1qHSjN_VEXhV_fbtt9HCt-o2QpCA7Yj6qFD6zkN2lgz3MQ4/s1600/Screen+Shot+2020-05-01+at+5.32.05+PM.png)

  
Test ping and try connecting via the hostname now.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVJwfdkd8SFEayCEJAZG0ZK0FzZ_OXmY2p4Y2Gg4N8EfrYimw-MscZzMUGSTnaDkUU-jMAdoNFHZCvT2toiX5n2S3tAEPcbP-yt9HU_2B2q3nh1iXAiEjDniQqbJTqsXym0ClJJCFiCdQT/s640/Screen+Shot+2020-05-01+at+5.34.26+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVJwfdkd8SFEayCEJAZG0ZK0FzZ_OXmY2p4Y2Gg4N8EfrYimw-MscZzMUGSTnaDkUU-jMAdoNFHZCvT2toiX5n2S3tAEPcbP-yt9HU_2B2q3nh1iXAiEjDniQqbJTqsXym0ClJJCFiCdQT/s1600/Screen+Shot+2020-05-01+at+5.34.26+PM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRR5rePzN4KA_vK-9PqNR7NEX1cpkYsMzXieDWdCGlrtZ5pJRUU-3t24PhM8sh_e5VTz23QV1PnOEffHsRArmzRqeyjy643-FX9mTzXtDdRsm8gWvc9_Glti1GcAC2H-qHkWyP9i_ByqQv/s640/Screen+Shot+2020-05-01+at+5.34.37+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRR5rePzN4KA_vK-9PqNR7NEX1cpkYsMzXieDWdCGlrtZ5pJRUU-3t24PhM8sh_e5VTz23QV1PnOEffHsRArmzRqeyjy643-FX9mTzXtDdRsm8gWvc9_Glti1GcAC2H-qHkWyP9i_ByqQv/s1600/Screen+Shot+2020-05-01+at+5.34.37+PM.png)

  
And there you have it! Connected via the hostname.  


####  Use cases

  1. To identify hosts on a local network by their hostnames.
  2. For testing a production setup  
At my work, we run our company website on a public domain name. When there is a new feature development, we need to test it first in a staging environment before adding it to production. We load the updated code on a test server and update our local /etc/hosts file to point the company website URL to the IP address of the test server which is reachable from the local machine. This way the local browser resolves the website domain to the IP specified in the /etc/hosts file and we can easily test the new features.

  
Modifying the /etc/hosts file is one of the simplest ways of overriding or substituting the DNS name resolution for local network.  
  
_Have you used any innovative ways of resolving local domain names? Let me know in the comments._

