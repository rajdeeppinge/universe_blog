---
layout: post
title: "Programmer's Guide: The "set" command in bash"
date: 2018-12-16
published: false
---

The "set" command in shell allows you to set various shell options and positional parameters. The purpose of this post is to highlight how much this command has been helpful to me in my bash programming. I would not go into much depth about all the possible flag, because you can find many posts and documentation on the internet, like [this post](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html#The-Set-Builtin) by GNU, which cover all the possible options that the "set" command provides. I will mainly focus on two options,  
  


###  The "**set -x** " option: 

This option allows us to print commands and their arguments, after they are expanded (interpolated) but before they are executed.  
  
Let us execute a simple hello world programme in bash.  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi91y_g7mZoOj0SjHz3YZtWTYcCvbPleOt8tMqrhmqA9l-wKIfXK03KAwxbOamUWzbxOuMY0Axj7wiqPAdAi4XS7dqg3dwBG86xMPeoi7yyr5nCuIl1l7w6cw2_VMhHdOF6QZLqtiYmaNAm/s320/Screen+Shot+2019-09-17+at+12.33.58+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi91y_g7mZoOj0SjHz3YZtWTYcCvbPleOt8tMqrhmqA9l-wKIfXK03KAwxbOamUWzbxOuMY0Axj7wiqPAdAi4XS7dqg3dwBG86xMPeoi7yyr5nCuIl1l7w6cw2_VMhHdOF6QZLqtiYmaNAm/s1600/Screen+Shot+2019-09-17+at+12.33.58+AM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7OMtCBjBgr54Ze7-x1uVIKvS3WkXqzCv-n6Vr2Spd1dzWxvKDBq_o_8FfQ4qi7-FJ8e63CPnE_dNb9Lkd9EKvxpvDRs2wvW3w0QZtW9-x9IxBTW3Migfg5N1VUG5bU_jjPu2JNwoAP8sk/s320/Screen+Shot+2019-09-17+at+12.36.52+AM.png) ](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7OMtCBjBgr54Ze7-x1uVIKvS3WkXqzCv-n6Vr2Spd1dzWxvKDBq_o_8FfQ4qi7-FJ8e63CPnE_dNb9Lkd9EKvxpvDRs2wvW3w0QZtW9-x9IxBTW3Migfg5N1VUG5bU_jjPu2JNwoAP8sk/s1600/Screen+Shot+2019-09-17+at+12.36.52+AM.png)

  


When the programme is executed, we see the entire printf statement being printed before the actual "Hello World!" message is printed. This way, we can check the command that is being executed along with its output. 

  


  


Setting the flag also expands any variables or arguments (interpolation) and prints them before execution. Furthermore, we can unset the option using "**+** " sign. 

In the below example, **$1** implies that the programme should print 1st argument provided to it. Also, -x option is unset by setting +x.

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1SrmOJmIA9O0-BAFtKKjelbNKmL111kfNbNxPFwyG7UTv2u7g10zYI8bpojm8d6qqEuSSE8KgmVMFS0D27UvFXlFGtQvXDxQclrCp1dL-0Vc9qmVHdeUS1IaiUxCtdNeyaPrZnrAJXMlc/s400/Screen+Shot+2019-09-17+at+12.47.53+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1SrmOJmIA9O0-BAFtKKjelbNKmL111kfNbNxPFwyG7UTv2u7g10zYI8bpojm8d6qqEuSSE8KgmVMFS0D27UvFXlFGtQvXDxQclrCp1dL-0Vc9qmVHdeUS1IaiUxCtdNeyaPrZnrAJXMlc/s1600/Screen+Shot+2019-09-17+at+12.47.53+AM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3AW6H9HwLVT9NqHEXiUcq5cqu_48hCiFKPn-ByLyovwhiWlMY0inlypaxPi1Ny54Ah7_jRJGQBZ_x-VfQyqnWJQhZ-iv7P8LIlBNjT2qUqg3CKhXJUvlS2IMfa-9S2ZTZWrE3pY1Iz78Q/s400/Screen+Shot+2019-09-17+at+12.48.29+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3AW6H9HwLVT9NqHEXiUcq5cqu_48hCiFKPn-ByLyovwhiWlMY0inlypaxPi1Ny54Ah7_jRJGQBZ_x-VfQyqnWJQhZ-iv7P8LIlBNjT2qUqg3CKhXJUvlS2IMfa-9S2ZTZWrE3pY1Iz78Q/s1600/Screen+Shot+2019-09-17+at+12.48.29+AM.png)

If we run the code with 1st argument "**Bash** ", observe that it prints Bash in the print statement before actually printing it. Also observe that the printf command is not shown after unsetting the -x option.  
  


###  **The "set -e" option:******

This causes the programme to exit immediately if the command being executed returns a non-zero status. This is useful if you want to prevent further, possibly critical, code execution in case a certain command fails.  
  
****Continuing with our programme, I have modified the code to cat (print contents) of a file that doesn't exist. I have also "set -e".  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5_HgdJGOPvnGrzcXnduacuzzSG3usVXyfA6hA00JP-Ukhb6ektoPe4-vpc86A_ytOdlu6o92NccjohwBslSy1DWGps40xeegn8yB94-Tonjc8vT_7CLo9XS3Nx6ciFdeFgjsrfLmLrQyy/s640/Screen+Shot+2019-09-17+at+1.06.45+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5_HgdJGOPvnGrzcXnduacuzzSG3usVXyfA6hA00JP-Ukhb6ektoPe4-vpc86A_ytOdlu6o92NccjohwBslSy1DWGps40xeegn8yB94-Tonjc8vT_7CLo9XS3Nx6ciFdeFgjsrfLmLrQyy/s1600/Screen+Shot+2019-09-17+at+1.06.45+AM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrM-ctLQ1MYHS2IzcZtEgZ9U3nWxFyGdUF2liZCKnNIUF80uh5yij-HNkH-PPYkrpFea3HmZ0VhYjFXB7-KlVeXYWOKPqv8Ob_baX4lJehFB-dpyNQOe2_zG2m7gdkrO0m6Qg69hAKZjMN/s640/Screen+Shot+2019-09-17+at+1.07.40+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrM-ctLQ1MYHS2IzcZtEgZ9U3nWxFyGdUF2liZCKnNIUF80uh5yij-HNkH-PPYkrpFea3HmZ0VhYjFXB7-KlVeXYWOKPqv8Ob_baX4lJehFB-dpyNQOe2_zG2m7gdkrO0m6Qg69hAKZjMN/s1600/Screen+Shot+2019-09-17+at+1.07.40+AM.png)

  
The programme execution stops immediately and does not execute the critical section that comes after.  
  
  
This flag is also useful in debugging a code. If you want to allow execution of certain commands which may cause errors but not allow certain commands whose output is not known, you can prevent termination of code by creating a complex command which returns status-code 0.  
  
In the below code, we can continue execution in case a certain non-critical file doesn't exist, but we must not execute any further if a critical input file is not present.  
  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgc0tkRtNVWWxED4jw_wsirXQ_UUUsr9oWlvSVWrWlPiW1wsB4RayEB0Wx_c7gutT3hkFX1FTcCB7CtNYse0AUftI8n-uI-hCQQcroobAI1I5wvVGVqpu0CYk1cq_57iwaSRsxaAcbNUSbC/s640/Screen+Shot+2019-09-17+at+1.18.03+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgc0tkRtNVWWxED4jw_wsirXQ_UUUsr9oWlvSVWrWlPiW1wsB4RayEB0Wx_c7gutT3hkFX1FTcCB7CtNYse0AUftI8n-uI-hCQQcroobAI1I5wvVGVqpu0CYk1cq_57iwaSRsxaAcbNUSbC/s1600/Screen+Shot+2019-09-17+at+1.18.03+AM.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_HLxCyP6nS-aAyCal8d9Akk1RbxJo1Kwsp4GRUzPA9a-vOnpljp3nRcVtMDltEdc_if-2wkIfcNx1fdrUz4V0pkC_VuHyaWTLRmgp1ycxkiWEkR081GtKhfOnmZ8WvT1iB3fpHIUerxgU/s640/Screen+Shot+2019-09-17+at+1.18.55+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_HLxCyP6nS-aAyCal8d9Akk1RbxJo1Kwsp4GRUzPA9a-vOnpljp3nRcVtMDltEdc_if-2wkIfcNx1fdrUz4V0pkC_VuHyaWTLRmgp1ycxkiWEkR081GtKhfOnmZ8WvT1iB3fpHIUerxgU/s1600/Screen+Shot+2019-09-17+at+1.18.55+AM.png)

  
As can be observed in the above execution, if a temporary file is missing and if we can safely ignore it, we can use "**true** " value and OR it with the command output to make a complex command whose exit status code is 0. You can read more about "**true** " value and exit status codes in bash [here](https://shodhfortruth.blogspot.com/2018/12/true-or-false-with-unix.html).  
Status code 0 means that the overall command doesn't have any errors and the programme doesn't terminate. But it still terminates if a critical file is not present. So, execution of critical block is prevented which might have caused major issues.  
  
Both these options have helped me tremendously while writing bash scripts. I hope you will find these options useful. Do explore other set options and let me know their uses in comments below.

