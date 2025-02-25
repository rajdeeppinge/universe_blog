---
layout: post
title: "Simple HTTP Server in Python"
date: 2020-01-05
---

Have you ever come across a need to share a file over a local network to a number of machines? Have you ever felt the need to share output of a task in text files available at a web-endpoint? Often, there is a requirement to quickly setup a light-weight web-server for such requirements. Python provides the easiest way to setup a simple HTTP server for such use cases with a single command.  
  
Python comes pre-installed with Linux as many of the linux libraries use python in background. Therefore there is no extra overhead of installing python. With support for python2 getting stopped in April 2020, many of the newer versions of linux distros come with default python3. Therefore this post will focus on setting up an HTTP server using both python2 and python3. We will be using Ubuntu 16.04, however it will work for majority of the linux systems where python comes pre-installed.  
  


###  Preparation

Steps to follow before starting the server:  


  1. Make sure you are in the directory which you want to share via server. If you aren't, navigate to an existing location or create a new directory.
  2. Create or move the files and subdirectories that you want to share in the parent directory on which the server will run.

Once all the files and directories to be shared over web-server are in one place and you are in that parent directory, we are good to go ahead and start the server.  
  
For the purposes of this post, I have setup httpserver_demo directory in my /root directory which contains following files and subdirectories:  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCmADoucJEdjCJZLhs4AYpWgGGUgNkZfWNvOWlplnpEt6sYAtMQkbUgckRUKNXtu0itMTvuyniKDdsz74O6DYyh3y51XcAqxb7ENbP8MriteCQQ78xaFS9W0r88s0S7E0-SgtIxppeh1BN/s640/Screen+Shot+2020-01-05+at+6.40.58+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCmADoucJEdjCJZLhs4AYpWgGGUgNkZfWNvOWlplnpEt6sYAtMQkbUgckRUKNXtu0itMTvuyniKDdsz74O6DYyh3y51XcAqxb7ENbP8MriteCQQ78xaFS9W0r88s0S7E0-SgtIxppeh1BN/s1600/Screen+Shot+2020-01-05+at+6.40.58+PM.png)

  
  


###  Python 2

Execute the following python2 command to start a server on port 23456.  


python -m SimpleHTTPServer 23456 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmycSqns-6R7148AFGOw7zsHsvjC3HZg7ky26_VNrlGjF8upgV4Lp8M-hTJj-miuAhnjiGLFOBzaFbmfA8iNeaGSryL8HmiwMroQchDUbXR1lpxgbXQicAf_r6CBiXfmtJLSw19Pik6fjt/s640/Screen+Shot+2020-01-05+at+6.53.42+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmycSqns-6R7148AFGOw7zsHsvjC3HZg7ky26_VNrlGjF8upgV4Lp8M-hTJj-miuAhnjiGLFOBzaFbmfA8iNeaGSryL8HmiwMroQchDUbXR1lpxgbXQicAf_r6CBiXfmtJLSw19Pik6fjt/s1600/Screen+Shot+2020-01-05+at+6.53.42+PM.png)

  
Of course you can choose a port of your choice between 0 and 65536 but make sure not to use any of the reserved ports or ports in use.  
  
I have setup my server on a virtualbox VM. The following is the output when I hit the port from web-browser on my host machine:  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO9o0l8bfXw0j9YW6Hz9RdXs16defHEE5XJHIgZf2-56RY-owuIY74UZefgq49EFOBPoVCbLJOqcw28xA15rvHb6Jj3OYo089X0eSYF46SCUv6nd3LuhzO6DqqewnDzFxKsJ_4HDk4ocss/s640/Screen+Shot+2020-01-05+at+6.48.41+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO9o0l8bfXw0j9YW6Hz9RdXs16defHEE5XJHIgZf2-56RY-owuIY74UZefgq49EFOBPoVCbLJOqcw28xA15rvHb6Jj3OYo089X0eSYF46SCUv6nd3LuhzO6DqqewnDzFxKsJ_4HDk4ocss/s1600/Screen+Shot+2020-01-05+at+6.48.41+PM.png)

###  Python 3

Let's start this server on the same host but on a different port, say 65432. Execute following command for python3  


python3 -m http.server 65432 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFBZIMv7PtfW-tHnvPvy5390ZAej5z_s-ERWEwRTzjWxB7sPtkpQFwd_tnKbV3swedPpvebPAWgQc2g1-WytuIvP_8pba-1oVfZE2TYv2HLtcKwAtvnNbZ8H8NVZnZQl9_Yv89biHlt5LP/s640/Screen+Shot+2020-01-05+at+6.56.37+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFBZIMv7PtfW-tHnvPvy5390ZAej5z_s-ERWEwRTzjWxB7sPtkpQFwd_tnKbV3swedPpvebPAWgQc2g1-WytuIvP_8pba-1oVfZE2TYv2HLtcKwAtvnNbZ8H8NVZnZQl9_Yv89biHlt5LP/s1600/Screen+Shot+2020-01-05+at+6.56.37+PM.png)

  
Following is the browser output for directory python_files:  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJRGlciXtqRmzzuUbs5BAvy4fljjIOoaTri5uIuov4dfmzqzv_iY0aXdR5_lmXtDICyNME50WPTiBxRQF4h_Qcs5bPOXYWoUgkAKfmGT_8qXP9tRPlhyZeeyE59Z0EPcSAI0xcgusAhejy/s640/Screen+Shot+2020-01-05+at+6.57.56+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJRGlciXtqRmzzuUbs5BAvy4fljjIOoaTri5uIuov4dfmzqzv_iY0aXdR5_lmXtDICyNME50WPTiBxRQF4h_Qcs5bPOXYWoUgkAKfmGT_8qXP9tRPlhyZeeyE59Z0EPcSAI0xcgusAhejy/s1600/Screen+Shot+2020-01-05+at+6.57.56+PM.png)

  


###  Permanent Setup

While the server is working, you might have noticed that the server process is started in the foreground i.e. the shell in which you have started the server doesn't give back the shell prompt after executing the command. It keeps on showing you the access logs of the server. This is problematic if you need to keep the server on even after you log out of the system or your ssh connection to the remote host (if you are working on a remote system) breaks. In such cases, to prevent the web-server from terminating, the web-server must be started in a background process or an alternative process detached from your shell session.  


####  Starting the process in background

This is the simplest solution. Just append an "&" at the end of the above commands and it will start the web-server in a background process.   


####  Starting the server in a screen or tmux session

This is the solution that you may use if you want to keep all the access logs in one place and want to check them later by connecting back to the process in the future. However, the details are out of the scope of this post.  
  


###  Practical Uses

Python http server has come in handy many times in my day-to-day requirements. When I was conducting lab sessions for one of the courses in my university as a teaching assistant, python http server was my primary tool to share big files and starter code with all the students. And it was the fastest way considering the file transfers happened over internal network. I also used this option to publish daily reports about code differences between code on version control system and code in production during my job. These reports were further used to alert users using an alerting service. There are many such possible uses of this simple light-weight web-server.  
  
_Do give it a try and let me know your experience._

