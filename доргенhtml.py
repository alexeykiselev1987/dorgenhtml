from time import sleep
import webbrowser
import os
import time
import pyautogui, sys
import shutil
domen=open("C:\\doorways\\домены.txt", "r", encoding="utf-8")#подгрузка доменов
login=open("C:\\doorways\\логины.txt", "r", encoding="utf-8")#подгрузка логинов
password=open("C:\\doorways\\пароли.txt", "r", encoding="utf-8")#подгрузка паролей
folder=open("C:\\doorways\\домены для папок.txt", "r", encoding="utf-8")#начало копирования содержимого папки шаблона в директорию дорвея
gorod=open("C:\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
c=open("C:\\doorways\\домены.txt", "r", encoding="utf-8")#подгрузка доменов для папок
e=open("C:\\doorways\\логины.txt", "r", encoding="utf-8")#подгрузка логинов
f=open("C:\\doorways\\пароли.txt", "r", encoding="utf-8")#подгрузка паролей
g=open("C:\\doorways\\домены для папок.txt", "r", encoding="utf-8")
domens=open("C:\\doorways\\домены для папок.txt", "r", encoding="utf-8")
domenstmp=open("C:\\doorways\\домены для папок.txt", "r", encoding="utf-8")
stmpfile1=open("C:\doorways\\stmp1.txt", "r", encoding="utf-8")
stmpfile1a=stmpfile1.read()
stmpfile2=open("C:\doorways\\stmp2.txt", "r", encoding="utf-8")
stmpfile1b=stmpfile2.read()

print("Начало цикла...")
x=0
y=7#количество сайтов ставится вручную
while x<y:
    frl=folder.readline()
    folder1="C:\\doorways\\cleaning\\"+frl
    folder1=str(folder1[0:-1])
    print(folder1)
    shutil.copytree("C:\\doorways\\cleaning\\template", folder1)#конец копирования содержимого папки шаблона в директорию дорвея
    time.sleep(10)
    #ПОДГРУЗКА ГОРОДОВ
    print("Подгрузка городов...")
    town=str(gorod.readline()[0:-1])
    #СОЗДАНИЕ INDEX ФАЙЛА
    print("Создание index.html...")
    pyautogui.click(x=124, y=1062, clicks=1, interval=1, button='left')#начало создания
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("cmd",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(" cd \doorways\cleaning\\"+"\\"+frl,interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("copy con index.txt",interval=0.1 )#index.txt
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey("F6")
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("exit",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")#конец создания
    #ПОДГРУЗКА INDEX ФАЙЛА, СОДЕРЖИМОГО HTML СТРАНИЦЫ И КЛЮЧЕВИКОВ
    print("Подгрузка index.html и ключевиков...")
    index=str("C:\doorways\\cleaning"+"\\"+str(domens.readline()[0:-1])+"\\"+"index.txt")
    print(index)
    indexfile=open(index, "a+", encoding="utf-8")
    #!!!подгрузка содержимого страницы html и ключевиков
    aa=open("C:\doorways\\1.txt", "r", encoding="utf-8")
    aa1=aa.read()
    indexfile.write(aa1)
    indexfile.write("\n")
    indexfile.write("<title>Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", готовый сайт в "+town+"</title>")
    indexfile.write("\n")
    bb=open("C:\doorways\\2.txt", "r", encoding="utf-8")
    bb1=bb.read()
    indexfile.write(bb1)
    indexfile.write("\n")
    indexfile.write("<meta name=\"description\" content=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", создание сайтов в "+town+", готовый сайт в "+town+"\"/>")
    indexfile.write("\n")
    cc=open("C:\doorways\\3.txt", "r", encoding="utf-8")
    cc1=cc.read()
    indexfile.write(cc1)
    indexfile.write("\n")
    indexfile.write("<meta property=\"og:title\" content=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", готовый сайт в "+town+"\"/>")
    indexfile.write("\n")
    indexfile.write("<meta property=\"og:description\" content=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", создание сайто в "+town+"в, готовый сайт в "+town+"\" />")
    indexfile.write("\n")
    dd=open("C:\doorways\\4.txt", "r", encoding="utf-8")
    dd1=dd.read()
    indexfile.write(dd1)
    indexfile.write("\n")
    indexfile.write("<meta name=\"twitter:description\" content=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", создание сайтов в "+town+", готовый сайт в "+town+"\" />")
    indexfile.write("\n")
    indexfile.write("<meta name=\"twitter:title\" content=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", готовый сайт в "+town+"\" />")
    indexfile.write("\n")
    ee=open("C:\doorways\\5.txt", "r", encoding="utf-8")
    ee1=ee.read()
    indexfile.write(ee1)
    indexfile.write("\n")
    indexfile.write("<link rel=\"alternate\" type=\"application/rss+xml\" title=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", создание сайтов в "+town+", готовый сайт в "+town+" &raquo; Лента\" href=\"/feed/\" />")
    indexfile.write("\n")
    indexfile.write("<link rel=\"alternate\" type=\"application/rss+xml\" title=\"Купить готовый сайт в "+town+", купить готовый лендинг в "+town+", создание сайтов в "+town+", готовый сайт в "+town+" &raquo; Лента комментариев\" href=\"/comments/feed/\" />")
    indexfile.write("\n")
    ff=open("C:\doorways\\6.txt", "r", encoding="utf-8")
    ff1=ff.read()
    indexfile.write(ff1)
    indexfile.write("\n")
    gg=open("C:\doorways\\7.txt", "r", encoding="utf-8")
    gg1=gg.read()
    indexfile.write(gg1)
    indexfile.write("\n")
    indexfile.write("			<h1 class=\"elementor-heading-title elementor-size-default\">Нужен готовый сайт за 3000 в "+town+"?</h1>		</div>")
    indexfile.write("\n")
    hh=open("C:\doorways\\8.txt", "r", encoding="utf-8")
    hh1=hh.read()
    indexfile.write(hh1)
    indexfile.write("\n")
    indexfile.write("			<h2 class=\"elementor-heading-title elementor-size-default\">Отправьте заявку на создание сайта в "+town+"!</h2>		</div>")
    indexfile.write("\n")
    ii=open("C:\doorways\\9.txt", "r", encoding="utf-8")
    ii1=ii.read()
    indexfile.write(ii1)
    indexfile.write("\n")
    indexfile.write("\n")
    indexfile.write("						<span class=\"elementor-button-text\">Заказать готовый сайт <br/>в "+town+"!</span>")
    indexfile.write("\n")
    jj=open("C:\doorways\\10.txt", "r", encoding="utf-8")
    jj1=jj.read()
    indexfile.write(jj1)
    indexfile.write("\n")
    indexfile.write("			<h2 class=\"elementor-heading-title elementor-size-default\">Почему в "+town+" лучше купить готовый сайт у нас?</h2>		</div>")
    indexfile.write("\n")
    kk=open("C:\doorways\\11.txt", "r", encoding="utf-8")
    kk1=kk.read()
    indexfile.write(kk1)
    indexfile.write("\n")
    indexfile.write("										<span class=\"elementor-icon-list-text\">Даем гарантию качества на созданный сайт в "+town+"</span>")
    indexfile.write("\n")
    ll=open("C:\doorways\\12.txt", "r", encoding="utf-8")
    ll1=ll.read()
    indexfile.write(ll1)
    indexfile.write("\n")
    indexfile.write("										<span class=\"elementor-icon-list-text\">Более 5 лет на рынке создания сайтов в "+town+"</span>")
    indexfile.write("\n")
    mm=open("C:\doorways\\13.txt", "r", encoding="utf-8")
    mm1=mm.read()
    indexfile.write(mm1)
    indexfile.write("\n")
    indexfile.write("										<span class=\"elementor-icon-list-text\">Идеальное решение для малого бизнеса в "+town+"</span>")
    indexfile.write("\n")
    nn=open("C:\doorways\\14.txt", "r", encoding="utf-8")
    nn1=nn.read()
    indexfile.write(nn1)
    indexfile.write("\n")
    indexfile.write("										<span class=\"elementor-icon-list-text\">Жмете кнопку \"Заказать готовый сайт в "+town+"\"</span>")
    indexfile.write("\n")
    oo=open("C:\doorways\\15.txt", "r", encoding="utf-8")
    oo1=oo.read()
    indexfile.write(oo1)
    indexfile.write("\n")
    indexfile.write("			<h2 class=\"elementor-heading-title elementor-size-default\">Отзывы клиентов в "+town+"</h2>		</div>")
    indexfile.write("\n")
    pp=open("C:\doorways\\16.txt", "r", encoding="utf-8")
    pp1=pp.read()
    indexfile.write(pp1)
    indexfile.write("\n")
    indexfile.write("			<div class=\"lae-testimonials lae-grid-container  lae-grid-desktop-3 lae-grid-tablet-2 lae-grid-mobile-1\"><div class=\"lae-grid-item lae-testimonial  lae-animate-on-scroll lae-visible-on-scroll\"  data-animation=\"fadeInLeft\"><div class=\"lae-testimonial-text\"><p>Живу в "+town+", где уже есть у меня клиентская база. Заказал лендинг по ремонту телефонов. Продажи повысились. Рекомендую всем!</p></div><div class=\"lae-testimonial-user\"><div class=\"lae-image-wrapper\"></div><div class=\"lae-text\"><h4 class=\"lae-author-name\">Андрей Фатеев</h4><div class=\"lae-author-credentials\"></div></div><!-- .lae-text --></div><!-- .lae-testimonial-user --></div><!-- .lae-testimonial --><div class=\"lae-grid-item lae-testimonial  lae-animate-on-scroll lae-visible-on-scroll\"  data-animation=\"fadeIn\"><div class=\"lae-testimonial-text\"><p>Самый оптимальный вариант для небольшой ремонтной мастерской в "+town+". Заказывал лендинг по ремонту телевизоров. Остался доволен.</p></div><div class=\"lae-testimonial-user\"><div class=\"lae-image-wrapper\"></div><div class=\"lae-text\"><h4 class=\"lae-author-name\">Игорь Удальцов</h4><div class=\"lae-author-credentials\"></div></div><!-- .lae-text --></div><!-- .lae-testimonial-user --></div><!-- .lae-testimonial --><div class=\"lae-grid-item lae-testimonial  lae-animate-on-scroll lae-visible-on-scroll\"  data-animation=\"fadeInRight\"><div class=\"lae-testimonial-text\"><p>Заказывала лендинг по клинингу в "+town+". Быстро, качественно и недорого. Я довольна! Идеально, если у вас стартап или маленький бизнес в "+town+".</p></div><div class=\"lae-testimonial-user\"><div class=\"lae-image-wrapper\"></div><div class=\"lae-text\"><h4 class=\"lae-author-name\">Ирина Мозолина</h4><div class=\"lae-author-credentials\"></div></div><!-- .lae-text --></div><!-- .lae-testimonial-user --></div><!-- .lae-testimonial --></div><!-- .lae-testimonials --><div class=\"lae-clear\"></div>		</div>")
    indexfile.write("\n")
    qq=open("C:\doorways\\17.txt", "r", encoding="utf-8")
    qq1=qq.read()
    indexfile.write(qq1)
    indexfile.write("\n")
    indexfile.write("						Готовые лендинги в "+town+". Все права защищены					</div>")
    indexfile.write("\n")
    rr=open("C:\doorways\\18.txt", "r", encoding="utf-8")
    rr1=rr.read()
    indexfile.write(rr1)
    indexfile.close()
    #запуск блокнота
    print("Запуск блокнота...")
    pyautogui.click(x=124, y=1062, clicks=1, interval=1, button='left')#начало создания
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("cmd",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(" cd \doorways\cleaning\\"+"\\"+frl,interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("start index.txt",interval=0.1 )#index.txt
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=800, y=749, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("exit",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")#конец открытия
    time.sleep(30)
    pyautogui.click(x=320, y=186, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=361, y=297, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=960, y=597, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=920, y=630, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=927, y=576, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("index.html", interval=0.1)
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=799, y=644, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=803, y=746, clicks=1, interval=1, button='right')
    pyautogui.PAUSE = 5.0
    pyautogui.click(x=806, y=700, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5 
    #создание файла sitemap
    print("Создание sitemap.xml...")
    pyautogui.click(x=124, y=1062, clicks=1, interval=1, button='left')#начало создания
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("cmd",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(" cd \doorways\cleaning\\"+"\\"+frl,interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("copy con sitemap.txt",interval=0.1 )#index.txt
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey("F6")
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("exit",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")#конец создания
    #запись sitemap
    sitemap=str("C:\doorways\\cleaning"+"\\"+str(domenstmp.readline()[0:-1])+"\\"+"sitemap.txt")
    print("запись файла sitemap")
    sitemapfile=open(sitemap, "a+", encoding="utf-8")
    sitemapfile.write(stmpfile1a)
    sitemapfile.write("\n")
    sitemapfile.write("  <loc>http://"+str(domen.readline()[0:-1])+"/</loc>")
    sitemapfile.write("\n")
    sitemapfile.write(stmpfile1b)
    sitemapfile.write("\n")
    sitemapfile.close()
    #конец записи sitemap
    #запуск sitemap
    print("Запуск sitemap...")
    pyautogui.click(x=124, y=1062, clicks=1, interval=1, button='left')#начало создания
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("cmd",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(" cd \doorways\cleaning\\"+"\\"+frl,interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("start sitemap.txt",interval=0.1 )#index.txt
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=800, y=749, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("exit",interval=0.1 )
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")#конец открытия
    time.sleep(30)
    pyautogui.click(x=320, y=186, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=361, y=297, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=960, y=597, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=920, y=630, clicks=1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=927, y=576, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("sitemap.xml", interval=0.1)
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=799, y=644, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=803, y=746, clicks=1, interval=1, button='right')
    pyautogui.PAUSE = 5.0
    pyautogui.click(x=806, y=700, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    #ЗАЛИВКА САЙТА НА ХОСТИНГ ЧЕРЕЗ FILEZILLA
    print("Заливка на хостинг...")
    pyautogui.click(x=659, y=749, clicks=2, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=659, y=749, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=14, y=52, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=353, y=472, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    c1=c.readline()
    e1=e.readline()
    f1=str(f.readline()[0:-1])
    g1=str(g.readline()[0:-1])
    g2=("C:\doorways\\cleaning\\")
    pyautogui.typewrite(c1, interval=0.1)
    pyautogui.click(x=826, y=230, clicks=1, interval=1, button='left')#координаты хостинга
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(c1, interval=0.1)#ввод хостинга
    pyautogui.PAUSE =2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=830, y=324, clicks=1, interval=1, button='left')#координаты логина
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(e1, interval=0.1)#ввод логина
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=495, y=412, clicks=1, interval=1, button='left')#галочка
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=723, y=444, clicks=1, interval=1, button='left')#галочка
    pyautogui.PAUSE = 2.5 
    pyautogui.click(x=17, y=52, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=813, y=353, clicks=1, interval=1, button='left')#координаты пароля
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite(f1, interval=0.1)#ввод пароля
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=923, y=577, clicks=1, interval=1, button='left')
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=997, y=218, clicks=1, interval=1, button='left')#координаты директории установки
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite("/"+c1+"//public_html", interval=0.1)
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.click(x=160, y=218, clicks=1, interval=1, button='left')#координаты загрузочной директории
    pyautogui.PAUSE =2.5
    pyautogui.typewrite(g2+g1, interval=0.1)
    pyautogui.PAUSE = 2.5
    pyautogui.press("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.mouseDown(button = 'left', x=516, y=398)
    pyautogui.PAUSE = 2.5
    pyautogui.moveTo(x=171, y=647)
    pyautogui.PAUSE = 2.5
    pyautogui.mouseUp(button = 'left', x=171, y=647)
    pyautogui.PAUSE =2.5
    pyautogui.click(x=226, y=434, clicks =1, interval=1, button='right')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=240, y=440, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.PAUSE =100.0
    time.sleep(100)
    pyautogui.click(x=709, y=744, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=228, y=52, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.typewrite("google search console", interval=0.1)
    pyautogui.PAUSE =2.5
    pyautogui.press("enter")
    pyautogui.PAUSE =2.5
    pyautogui.click(x=371, y=278, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=267, y=590, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=261, y=164, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=113, y=685, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=783, y=511, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.typewrite("http://"+c1, interval=0.1)
    pyautogui.PAUSE =2.5
    pyautogui.click(x=830, y=611, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    print(g1+" загружен успешно!")
    pyautogui.click(x=1344, y=7, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=1344, y=7, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    pyautogui.click(x=1344, y=7, clicks =1, interval=1, button='left')
    pyautogui.PAUSE =2.5
    y=y-1
    
    
