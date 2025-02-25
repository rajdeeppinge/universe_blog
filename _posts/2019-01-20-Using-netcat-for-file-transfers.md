---
layout: post
title: "Using netcat for file transfers"
date: 2019-01-20
---

Netcat is an efficient tool to transfer files between two servers in the same network. It works across all the platforms (Linux, Mac OS X and Windows). For this post, we will demo a file transfer between Ubuntu linux distro and Mac OS X.   
  
Let's first create a large file using dd tool. If you are not familiar with dd, please go through this [post](https://shodhfortruth.blogspot.com/2019/01/generate-large-files-in-linux-using-dd.html).  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl6641PdMIuXqyhHN3vGxPBxnwlMrgMFWuJYKFQ58pNG988UGE3I3qmyc-YfTQbyCh6FKt1YRh_P1jsnGMqsOkcnPuFOVjh7QWG4RgQck0qvRrucVZg3dyPAIjhtm0rJ7E-3nvbTG5rpEc/s640/Screen+Shot+2019-10-27+at+6.15.44+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl6641PdMIuXqyhHN3vGxPBxnwlMrgMFWuJYKFQ58pNG988UGE3I3qmyc-YfTQbyCh6FKt1YRh_P1jsnGMqsOkcnPuFOVjh7QWG4RgQck0qvRrucVZg3dyPAIjhtm0rJ7E-3nvbTG5rpEc/s1600/Screen+Shot+2019-10-27+at+6.15.44+PM.png)

  
Here, we have created 3 files of the same size having same content. Let us now transfer those files to Mac OS.  
  
At the receiving end, open a port using the following command:  


# For Mac systems  
nc -l [port_no] > [output_file_name]   
  
# For Linux systems  
nc -l -p [port_no] > [output_file_name] 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAUbdyLoli_vPvJEnJM_FdedVmfCs4Sg0TEYU0BozxFXw01jCcXR1OcEfa7tAFRcUTabxk2_bia86Bq3WvrtUBXEjcoFvO8pv0AfXtX5yLu00FfGT_O8n5KHhxWXqYmuz9vaZJ-KuMJdP4/s400/Screen+Shot+2019-10-27+at+6.25.53+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAUbdyLoli_vPvJEnJM_FdedVmfCs4Sg0TEYU0BozxFXw01jCcXR1OcEfa7tAFRcUTabxk2_bia86Bq3WvrtUBXEjcoFvO8pv0AfXtX5yLu00FfGT_O8n5KHhxWXqYmuz9vaZJ-KuMJdP4/s1600/Screen+Shot+2019-10-27+at+6.25.53+PM.png)

  
Now, run the following command from the sender side to send the file.  


nc [destination_ip] [destination_port] < [file_to_be_transferred] 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgKDM-1Winqb2HvcCosrvLSSMOY9kkdHzroXoH4RcAHaggunjE63vPzWxXaB6SZylGs-eWTuYKne69lTWrzQg03uVCpXzoC3hw8Yf-riF69MiGT3hjvIHYeMRilAo5XNRdCVUvcphFfr8p/s640/Screen+Shot+2019-10-27+at+6.28.03+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgKDM-1Winqb2HvcCosrvLSSMOY9kkdHzroXoH4RcAHaggunjE63vPzWxXaB6SZylGs-eWTuYKne69lTWrzQg03uVCpXzoC3hw8Yf-riF69MiGT3hjvIHYeMRilAo5XNRdCVUvcphFfr8p/s1600/Screen+Shot+2019-10-27+at+6.28.03+PM.png)

  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD923sWDkpMPcfGX_ATfYfrloU-Nf2rYSCdPXCeI31vtK-eNF1t_ohv07Gcu538GOZc7vjz2D0Ent6xPxET2KmqzNK41027d5eiiYXSwWA2vYu47b3mDUa4WoOvL-CKjkdxzMnRCCgVCfC/s640/Screen+Shot+2019-10-27+at+6.28.52+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD923sWDkpMPcfGX_ATfYfrloU-Nf2rYSCdPXCeI31vtK-eNF1t_ohv07Gcu538GOZc7vjz2D0Ent6xPxET2KmqzNK41027d5eiiYXSwWA2vYu47b3mDUa4WoOvL-CKjkdxzMnRCCgVCfC/s1600/Screen+Shot+2019-10-27+at+6.28.52+PM.png)

In the above pic, the sender machine is on the left hand side while receiver is on right. You can clearly see that the receiver has received the file of size 1 GB.  
  
Netcat is a great alternative to ssh based tools in transfering files across systems and it works for different architectures.

