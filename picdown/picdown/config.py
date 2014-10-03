#/bin/env python
__author__ = 'zhuangyongyao'

# maya
MY_PIC_SITE = 'maya'



src_dict = {
    'maya': {
        'domain': 'klmaya.info',
        'login_url': 'http://a.klmaya.info/logging.php?action=login',
        'login_form' : {
            'formhash' : '4ea20abd',
            'referer' : 'http://a.klmaya.info/index.php',
            'loginfield' : 'username',
            'username':'togetav',
            'password':'togetav',
            #'questionid':'0',
            #'answer':'',
            'cookietime':'2592000',
            #'loginmode':'',
            #'styleid':'',
         },
        #'username' : 'togetav',
        #'password' : 'togetav',
        'urls' : [
            'forumdisplay.php?fid=5', #tupatianxia
            #'forumdisplay.php?fid=86', #zouguangtoupai
            #'forumdisplay.php?fid=53', #yazhoutietu
            #'forumdisplay.php?fid=59', #wangyouzipai
            #'forumdisplay.php?fid=60', #oumeitietu
         ],
        'picpage_xpath' : '//td[@class="f_title"]/a[1]/@href',
        'pic_xpath': '//div[@class="t_msgfont"][1]/img/@src',
        'text_xpath': '//tr[@class="head"]/td/text()',
        #'time_xpath': '//table[@class="t_msg"]/text()',
        #'next_xpath': '//a[@class="nxt"]/@href',
        #'maingate_xpath': '//div[@class="info"]/a/@href',
    },
}
