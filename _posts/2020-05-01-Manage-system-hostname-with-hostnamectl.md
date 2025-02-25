---
layout: post
title: "Manage system hostname with hostnamectl"
date: 2020-05-01
---

This article explains the simplest method to set hostname and Fully Qualified Domain Name (FQDN/fqdn) of any given system using hostnamectl  
  
Check that hostnamectl is present on the system by typing it in a shell. You will see output similar to the one given below.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifOX8d7EeDMfZszNcD4Vk0tDVvxn6cBWVBak30XMI14pRmMXP3878S62thyphenhyphenyllKNoG8D8doFJFEp6jniCKcG_BgWYh7ORaj5jJwS7ynYNwYt9XCgZCQx-cH-9Lkw7Nos2CmoYQmp2ekS1l/s640/Screen+Shot+2020-05-01+at+3.35.01+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifOX8d7EeDMfZszNcD4Vk0tDVvxn6cBWVBak30XMI14pRmMXP3878S62thyphenhyphenyllKNoG8D8doFJFEp6jniCKcG_BgWYh7ORaj5jJwS7ynYNwYt9XCgZCQx-cH-9Lkw7Nos2CmoYQmp2ekS1l/s1600/Screen+Shot+2020-05-01+at+3.35.01+PM.png)

  
In case hostnamectl is not found, it is a good idea to install it.  
**sudo apt update**  
**sudo apt install systemd-services**  
  
Verify the static hostname given above using the following command:  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA-oDO67KKFjKlzJmkvgEhszFWBQ2k0UV0o9IMoc1IadnTLZgUNaJpjVK05mCzy2MDfqreeMG4LH1OGttHBBDut2LD9fKf4ZFoMZ9x4m5xrxGrwOQ2I_QJt4rLLj9oBVlPauFRGIVimwUJ/s400/Screen+Shot+2020-05-01+at+3.44.17+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA-oDO67KKFjKlzJmkvgEhszFWBQ2k0UV0o9IMoc1IadnTLZgUNaJpjVK05mCzy2MDfqreeMG4LH1OGttHBBDut2LD9fKf4ZFoMZ9x4m5xrxGrwOQ2I_QJt4rLLj9oBVlPauFRGIVimwUJ/s1600/Screen+Shot+2020-05-01+at+3.44.17+PM.png)

  
Also verify it by checking /etc/hostname file  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUOFf9cMB22O-7Kc7-GOy1ZnvJe1ju0nILQzwuyrwLShV5rUOxmugpiee9SQonuwvk_loIMPIss-q9m5VSgR8RuRUT2mfQzpDsWVWBP1KZoSHc-Vg8zdcebcyy5gJ9lD7I_xuKudHUhKtt/s400/Screen+Shot+2020-05-01+at+3.45.56+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUOFf9cMB22O-7Kc7-GOy1ZnvJe1ju0nILQzwuyrwLShV5rUOxmugpiee9SQonuwvk_loIMPIss-q9m5VSgR8RuRUT2mfQzpDsWVWBP1KZoSHc-Vg8zdcebcyy5gJ9lD7I_xuKudHUhKtt/s1600/Screen+Shot+2020-05-01+at+3.45.56+PM.png)

  
Change the hostname and set the desired hostname by running the following command and authenticating with the password.  
  
**hostnamectl set-hostname <hostname>**  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRX4xWFaNLqWhhf7tlORAicLJlPsL4m5dTMqTX8V9srd_2vM6patvHQB88L8lTtzw3a2DTlzmfjGCW4m-oHz6-GfK1xSvnsqwt1boXdqFJpK4MbHKJmpnZZvTehb7s_boXkY62yoSc8dRV/s640/Screen+Shot+2020-05-01+at+3.50.25+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRX4xWFaNLqWhhf7tlORAicLJlPsL4m5dTMqTX8V9srd_2vM6patvHQB88L8lTtzw3a2DTlzmfjGCW4m-oHz6-GfK1xSvnsqwt1boXdqFJpK4MbHKJmpnZZvTehb7s_boXkY62yoSc8dRV/s1600/Screen+Shot+2020-05-01+at+3.50.25+PM.png)

  
Start a new shell session or reconnect to the server to see the change in the hostname  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2If6UloZrvQEfqFE1a3P-XpxUDkRYtOm3hgfZOFvzDTwPOXFpU5T9es5nuQ51JxWvQlT0D96WNXOm2NGWLnPD10mTRm_voZPaQbonUe0srqWcJA5uh0Ve0Fa7tMrpOKOe7Bzs-gtaoxFW/s400/Screen+Shot+2020-05-01+at+3.53.43+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2If6UloZrvQEfqFE1a3P-XpxUDkRYtOm3hgfZOFvzDTwPOXFpU5T9es5nuQ51JxWvQlT0D96WNXOm2NGWLnPD10mTRm_voZPaQbonUe0srqWcJA5uh0Ve0Fa7tMrpOKOe7Bzs-gtaoxFW/s1600/Screen+Shot+2020-05-01+at+3.53.43+PM.png)

  
Again run above steps to verify that hostname has been changed correctly.  


####  Configure FQDN

While the above process may suffice to identify the host in the local network, it is not enough when the host is to be identifies uniquely over the internet.  
  
For example, here we have setup the hostname as "vm-3". However there may be many such "vm-3" on the internet. Then how to identify our "vm-3" uniquely? For that we need to also add the domain and the top-level-domain (tld), if any, of the network in which the server resides.  
  
**FQDN = [hostname].[domain].[tld]**   
  
For demo purposes, we are using domain as "shodh" and tld as "demo".  
  
Therefore, the FQDN of the demo server is _**vm-3.shodh.demo**_  
  
Let's add this FQDN to the server._****_  
  


Edit the /etc/hosts file and add FQDN in front of hostname as shown below.  
**FORMAT: <ip> <fqdn> <hostname>**  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRBnWa-4HGCM8uFlQfVTYVxBQcY3ZxuhJT8DpHzmbzx9DGTgoB9rMrNREPkCNBGcd0zzMXjPgj1eMM2QNP0v1Yb3ZeTtmZCtFXs7R3DWuE4x4uwX5Z6aqoO1YmQ-dBM1b3psLbCWB1_C7i/s640/Screen+Shot+2020-05-01+at+4.23.37+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRBnWa-4HGCM8uFlQfVTYVxBQcY3ZxuhJT8DpHzmbzx9DGTgoB9rMrNREPkCNBGcd0zzMXjPgj1eMM2QNP0v1Yb3ZeTtmZCtFXs7R3DWuE4x4uwX5Z6aqoO1YmQ-dBM1b3psLbCWB1_C7i/s1600/Screen+Shot+2020-05-01+at+4.23.37+PM.png)

  


Test the FQDN setup as follows:  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3z1SMKkl_XI6wVXSBFP-dOzVYbVCf_tJC4o40teVSwZzG9DTdlmpa_xrye8yYSpW0M2PJY6ieCWzkRRmS4Dkx0QgE3utTN8S6VgrI9QyiqQwoUEF1bM2Sicvj0J4y6iLrPAlY-yFRP-Nb/s400/Screen+Shot+2020-05-01+at+4.25.38+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3z1SMKkl_XI6wVXSBFP-dOzVYbVCf_tJC4o40teVSwZzG9DTdlmpa_xrye8yYSpW0M2PJY6ieCWzkRRmS4Dkx0QgE3utTN8S6VgrI9QyiqQwoUEF1bM2Sicvj0J4y6iLrPAlY-yFRP-Nb/s1600/Screen+Shot+2020-05-01+at+4.25.38+PM.png)

  


That's it folks! We have successfully setup the hostname and the FQDN for our server.

