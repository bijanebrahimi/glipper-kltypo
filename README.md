Keyboard Layout Typo (KLTypo)
====
KLTypo is a [glipper](https://launchpad.net/glipper) plugin to correct the Typos which happens when the wrong keyboard layout is selected.

Senario [ENG]
---------------
Consider writing **"Hello World"** but you forgot to set the keyboard layout to English, let's say it's Persian Layout Now, the outcome is **"اثممخ صخقمی"**! to correct this without writing the text again, just select the text (after enabling KLTypo plugin in glipper of course) and Select "**Persian > English**"  from KLTypo menu! the correct text will be replaced into clipboard and Will be ready to paste.

Senario [فارسی]
---------------
تصور کنید که جمله **«سلام جهان»** را می‌خواهید تایپ کنید ولی متوجه نیستید که لی‌اوت کیبورد شما فارسی نیست، بیایید تصور کنیم که لی‌اوت انگلیسی را انتخاب کرده‌اید، خروجی شما متن **"sghl [ihk"** خواهد بود! برای تصحیح این خطای تایپی بدون نگارش دوباره جمله کافی است متن اشتباه را انتخاب کرده (البته قبلا پلاگین kltypo را باید در glipper فعال کرده باشید) و گزینه **«English > Persian»** را از منوی KLTypo انتخاب کنید! متن تصحیح شده به فارسی در کلیپ‌برد شما قرار خواهد گرفت و آماده چسبانده (paste) شدن می‌باشد.

Installation
---------------
To use the plugin just copy the "kltypo.py" to plugins directory at */usr/share/glipper/*!

        # cp kltypo.py /usr/share/glipper/plugins/

Note: you need to have root permissions!


Keyboard Layouts
---------------
Currently only the **Persian** and **English (US)** layouts are supported. if you're interested in adding new layouts please let us know. :)

Version
---------------
the currect version is 0.1


License
---------------
KLTypo is published under GPL version 3.0 or later license but the libraries
used in project may be different, for that you can check the header of each
library. but basically, crow is a Free and OpenSource software. you can fork
the project and improve the code as longs as you keep the code Free :)
