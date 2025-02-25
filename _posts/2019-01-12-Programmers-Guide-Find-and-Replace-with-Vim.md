---
layout: post
title: "Programmer's Guide: Find and Replace with Vim"
date: 2019-01-12
---

Many of us don't like Vim because of it's unconventional and unique command set. But if you get to know certain functionalities common to other popular editors, you would not be required to lift your hands from keyboard while typing. One such functionality that we often use in editors is "Find and Replace". The same feature, with many more customizations, is also provided by Vim. This post will focus on various Find and Replace features of Vim.  
  
Let's start with a file which contains a lot of "lorem ipsum".  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggT2aj5hjjWvzMqnXumXQ77gSywHZ3qPpV2ui900Nl0mtjaWEXxLTlWUzXWMGGsCtW2EqomKZ8PzdbdWO6RiBGsv1AVMWgrznnsXo2AqQnJBCpU-Td_z01tMa8AKvW_nPz5anisrIpm3TZ/s640/Screen+Shot+2019-09-19+at+1.32.29+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggT2aj5hjjWvzMqnXumXQ77gSywHZ3qPpV2ui900Nl0mtjaWEXxLTlWUzXWMGGsCtW2EqomKZ8PzdbdWO6RiBGsv1AVMWgrznnsXo2AqQnJBCpU-Td_z01tMa8AKvW_nPz5anisrIpm3TZ/s1600/Screen+Shot+2019-09-19+at+1.32.29+PM.png)

  
Now let us replace "lorem ipsum" with "hello world".  
  
First, we will focus on replacing "lorem" with "hello" in the first line. We need to execute following command in vim.  


:s/lorem/hello/g 

  
The **:s** signifies "substitute" command provided by vim.  
The **g** flag at the end means "global". This means that all the occurrences in the selected context will be changed. In this case, all the occurrences in the first line will be changed.  
  
In the below image, you can see "lorem" has been replace by "hello" in the first line.  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdmXNihAUrI1LuQEMg3k2rGkI3cWKxUOPMVNW4D5sShwn3bAmSC3ZCsp_09iXDhpX8q0FgZrHanrdHKOIFrIyehgdoOMxNLxosVXJTYtrzeh-qyKgamT_5pf47l3KOuqoMvOB7Loslt5Qc/s640/Screen+Shot+2019-09-19+at+1.38.47+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdmXNihAUrI1LuQEMg3k2rGkI3cWKxUOPMVNW4D5sShwn3bAmSC3ZCsp_09iXDhpX8q0FgZrHanrdHKOIFrIyehgdoOMxNLxosVXJTYtrzeh-qyKgamT_5pf47l3KOuqoMvOB7Loslt5Qc/s1600/Screen+Shot+2019-09-19+at+1.38.47+PM.png)

  
  
Let us now replace all the "lorem" with "hello". To replace all, we use **:%s** instead of **:s**.  
Command:  


:%s/lorem/hello/g 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1o6JiCKLJxGBJs6FjFuFIBJCiVpX7c6A4OZBkvlR3i5APzP8dx7mPm1S8PMrJ3P9SUx-73COnlJ6EQ_dKFOZiiG0eB1rrVrWiAMbusfgW2URfsxYJFzs5KMxpoIskx0PAwMukGnZxyo9Z/s640/Screen+Shot+2019-09-20+at+1.22.28+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1o6JiCKLJxGBJs6FjFuFIBJCiVpX7c6A4OZBkvlR3i5APzP8dx7mPm1S8PMrJ3P9SUx-73COnlJ6EQ_dKFOZiiG0eB1rrVrWiAMbusfgW2URfsxYJFzs5KMxpoIskx0PAwMukGnZxyo9Z/s1600/Screen+Shot+2019-09-20+at+1.22.28+PM.png)

  
If you observe closel, the "Lorem" in the second line has not been replaced. This is because, by default, the substitute function is case-sensitive. We need to use **i** flag to make it case-insensitive.  
Command:  


:%s/lorem/hello/gi 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOfZ7KNSPYrfqYHntDRFONx0mMb2RBpf3j4b8u6nLCUioEK5SOunYqDPkMMw7aO98sbjswiRj7_uaDUuf5dmkiLcZJ048Ts66cy6hw2FVf_wr2LyS4Z-VL7Mhkftm-69_PpLSlTNbRKtUf/s640/Screen+Shot+2019-09-20+at+1.36.51+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOfZ7KNSPYrfqYHntDRFONx0mMb2RBpf3j4b8u6nLCUioEK5SOunYqDPkMMw7aO98sbjswiRj7_uaDUuf5dmkiLcZJ048Ts66cy6hw2FVf_wr2LyS4Z-VL7Mhkftm-69_PpLSlTNbRKtUf/s1600/Screen+Shot+2019-09-20+at+1.36.51+PM.png)

  
But Find and Replace (F&R) tools also ask for confirmation before actually making changes. Can we do that in vim? Yes of course! Vim can do everything that a normal F&R tool can do. Just use **c** flag at the end. Let us replace all the "ipsum" with "world".  
Command:  


:%s/ipsum/world/gc 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJurX62iWKzbWzUVHvatGqK81FFrzSQQjXdSf1ya1j2ongE5zCrmIbYQUWcdUCKro0VKzDdgkQknAoBzBnC7VCdliAwxBzku1S3xFIH5EkM0uNKdE3WpSTitB1k6bmP4jtZlzf7SLLZd87/s640/Screen+Shot+2019-09-20+at+1.42.27+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJurX62iWKzbWzUVHvatGqK81FFrzSQQjXdSf1ya1j2ongE5zCrmIbYQUWcdUCKro0VKzDdgkQknAoBzBnC7VCdliAwxBzku1S3xFIH5EkM0uNKdE3WpSTitB1k6bmP4jtZlzf7SLLZd87/s1600/Screen+Shot+2019-09-20+at+1.42.27+PM.png)

Here,  
y: yes, replace this match  
n: no, skip this match  
a: all, replace all  
q: quit  
l: last match i.e.replace this match and exit  
The last two are just to scroll up or down.  
  
So, after pressing **a** , we have accomplished our objective of replacing "lorem ipsum" with "hello world".  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLO0r2lF_qxYRba55F9a3YqUOc1OARnXnti21BtM5shVRDuWHnrvBYtOgyt-pnfbY68AcA7-sztiXXgHSgDPGNqraI_p7YggHB83iFyvKjzSGZEdUyo1Fu0FMRE7b3LDtvxbHEFYb-bmYh/s640/Screen+Shot+2019-09-20+at+1.48.25+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLO0r2lF_qxYRba55F9a3YqUOc1OARnXnti21BtM5shVRDuWHnrvBYtOgyt-pnfbY68AcA7-sztiXXgHSgDPGNqraI_p7YggHB83iFyvKjzSGZEdUyo1Fu0FMRE7b3LDtvxbHEFYb-bmYh/s1600/Screen+Shot+2019-09-20+at+1.48.25+PM.png)

  
Finally, when we want to replace exactly matching words and not all the matches, for example, in the above file if we want to replace "is" with "was" but do not want to replace the substring "**is** " in "Th**is** ", we can use the following command:  


:%s/\&#60is\&#62/was/gc 

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgglfqKdq6gRwGIF7p7p7pLataYlKkn_3HnT9W_7yDXl2GFVQGDfkVFLV_QEjOqJk72fPFvzOTkyTP1ODnMXvuBpq_Kk326SKUxJ5Uwkm7CbCwUCI50VtR4Z5lREiJGXBwGF5izEd05BaLA/s640/Screen+Shot+2019-09-20+at+2.04.01+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgglfqKdq6gRwGIF7p7p7pLataYlKkn_3HnT9W_7yDXl2GFVQGDfkVFLV_QEjOqJk72fPFvzOTkyTP1ODnMXvuBpq_Kk326SKUxJ5Uwkm7CbCwUCI50VtR4Z5lREiJGXBwGF5izEd05BaLA/s1600/Screen+Shot+2019-09-20+at+2.04.01+PM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Q3EX3BUtQ4pZmi7wuVBJBHDauAqPQPPNMt2Za6Yz4xM686TgtpQz38uizMbgCULcMFZ6zKP9Xwy6rn45gX-W62SjzQko8nv2UakWcaPwDYXq3WKxmFjK_lo6gaeyzqHOaOXswEmV67uN/s640/Screen+Shot+2019-09-20+at+2.04.21+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Q3EX3BUtQ4pZmi7wuVBJBHDauAqPQPPNMt2Za6Yz4xM686TgtpQz38uizMbgCULcMFZ6zKP9Xwy6rn45gX-W62SjzQko8nv2UakWcaPwDYXq3WKxmFjK_lo6gaeyzqHOaOXswEmV67uN/s1600/Screen+Shot+2019-09-20+at+2.04.21+PM.png)

  
There are many more uses of Vim ":substitute" command. I hope this post will encourage you to explore more about them. I would recommend using command line and Vim to work with files on remote servers.

