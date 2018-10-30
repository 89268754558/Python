# Python
![alt text](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)



Данный репозиторий содержит все задания, информацию, краткие сводки по лекциям и дополнительные материалы по курсу Власова Е. **Python**

# Общая информация
  
  
  Данный раздел будет содержать общую информацию по нашему курсу. Здесь вы можете найти полезные материалы для решения различных задач, а также список допольнительных ресурсов, книг,  учебный план, код с занятий и домашки. Также здесь будет описано правило **дедлайнов** и форма предложений по нашему курсу. Надеюсь, вам понравится.
## О языке Python 
  
  
Начнем с основ. **Python** - высокоуровневый интерпретируемый язык программирования, ориентированный на производительность, упрощенную семантику (удобочитаемость кода) и простоту освоения. Разработчиков, пишущих на языке *Python* часто кличут "питонистами". А главой всемирной тусовки питонистов является  [вот этот дядька](https://gvanrossum.github.io/):)
  
  
Вместе с Тимом Питерсом был придуман, так называемый, Zen of Python (Дзен Питона), который является краткой сводкой правил написания программ на языке Python (о том, как его вызвать в программе я расскажу позже). Ознакомиться с этими правилами можно [здесь](https://www.python.org/dev/peps/pep-0020/).
 
Для некоторых из вас *Python* будет первым языком программирования. Я считаю, это лучшее, что могло с вами произойти. Почему так считаю? Все просто.
 * Во-первых, это очень простой язык, не требующий предварительных навыков.
 * Во-вторых, он очень мощный и гибкий. Несмотря на свою кажущуюся простоту, Python является одним из мощных инструментов в арсенале любого разработчика. Посмотрите [сюда](https://www.instagram.com/) и попробуйте угадать, на чем его сделали?
 * В-третьих, коммьюнити. По-хорошему, это должно быть первым пунктом. У питонщиков одно из самых больших и самых ламповых коммьюнити из ныне существующих. Вы всегда можете найти кучу форумов, сайтов и туториалов, постоянные обновления библиотек и топовые митапы. Все это свидетельствует о том, что язык развивается. А движет его - [коммьюнити](https://www.python.org/community/)
 * В-четвертых, этот язык настолько крут, что он входит в топ-10 самых востребованных языков мира. Освоив основы на нашем курсе, каждый из вас найдет для себя определенную нишу применения языка (это может быть WEB, Desktop App, Data Analysis, Machine Learning, Chat-Bots, Android App, CyberSecurity and etc.)
 Поглядите на этот [ресурс](https://usersnap.com/blog/programming-languages-2018/). Воодушевляет, верно?
 
 
## О том, как начать кодить
  
 Достаточно болтовни, давайте кодить. Прежде, чем вы напишите свой *Hello World!*, необхдимы 2 вещи.
  * 1 - Желание (если ты дочитал то этого момента, то можешь ставить галочку)
  * 2 - Сам Python
 Для наиболее комфортного прохождения курса, работы с различными библиотеками и фреймворками, рекомендую установить готовую сборку Python, которая называется Anaconda. Скачать вы ее можете [тут](https://usersnap.com/blog/programming-languages-2018/). На момент написания - самая свежая версия была 3.7.
 Не забудьте прожать везде *Add To Path* и ассоциируйте именно эту версию питона как основную.
 В конце установки вам будет предложено скачать удобнейший редактор кода VSCode, который я также очень рекомедую. Отдельно его скачать можно [тут](https://code.visualstudio.com/).
 Для проверки того, что вы правильно все сделали, откройте командную строку комбинацией Win+R, пропишите cmd (от сокращения Command), и в открывшейся консоли наберите *python*.
 Результат должен быть примерно таким:
 ```
workingcloud@evgen-pc:~$ python
Python 3.6.6 |Anaconda custom (64-bit)| (default, Oct  9 2018, 12:34:16) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
``` 
Я использую Linux, поэтому у вас будет надпись on windows или что-то в этом роде).
Если все окей, пишем сразу долгожданный *Hello World!*:
```
Python 3.6.6 |Anaconda custom (64-bit)| (default, Oct  9 2018, 12:34:16) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello World!')
Hello World!
>>> 
```
И все готово.

## Ошибаться - круто, некруто не ошибаться
  В процессе написния кода часто возникают ошибки (либо по невнимательности, либо по невнимательности, а чаще всего по невнимательности). И это абсолютно нормально). Не бойтесь увидеть очередное сообщение об ошибке или о том, что вы функцией *print()* сломали временной континуум. Ошибиться - это получить больший опыт, нежели чем глупо следовать инструкции. Матерые кодеры ошибались огромное число раз за свою жизнь. **Не стесняйтесь задавать глупые вопросы!** Только полное понимание проблемы и ее решение позволит избегать вам этой ошибки в будущем, а также привьет понимание различных частей кода. Поэтому смело атакуйте мою электронную почту, гугл и форумы, описанные в разделе **Ресурсы, где ты обязан быть каждый день**, если внезапно столкнулись с проблемой в коде.
  
  
## О курсе
В рамках данного курса мы охватим тот необходимый вам материал, чтобы по итогу вы могли считаться матерыми новичками, умели общаться с другими кодерами о коде без кода и понимали базовые принципы программирования. Также я буду стараться приводить наглядные примеры именно функциональной части *Python*, попишем небольшие PWA, интерфейсы, сделаем простой сайт и контент-бота.

В куре будет система дедлайнов реализованная следующим образом:
Если ваше занятие проходит в день А (скажем, в субботу). То вам неоходимо прислать мне ДЗ следующей недели до дня А-1 не позднее 20:00 (то есть, в пятицу до 20:00). Это сделано для того, чтобы преподаватель успел все проверить и понять, нужно ли уделить данному материалу еще внимание, или можно смело идти вперед и рассказывать что-нибудь новое и классное.

Я всячески поощраю, если вы будете атаковать мою почту на протяжении всей недели вопросами в стиле :
"Ничего не работает. Помогите. Прилагаю код", "Нашел новую классную фичу, можешь рассказать о ней на следующем занятии?", "Что это? Почему оно выдает ошибки?","Хочу доп.задачку по такой-то теме" и т.д. и т.п.

**ACHTUNG!** После каждого нашего занятия вы можете вместо домашки взять доклад про какую-нибудь фичу, фреймворк, библиотеку или алгоритм и выступить на следующем занятии, предварительно разобравшись в теме вместе со мной и приготовив выступление на 5-7 минут. Таким образом, вы научитесь говорить (не заучивать, как в школе, а именно говорить и излагать мысли). Поэтому не стесняйтесь подходить ко мне после занятий и трясти (1-2 выступления всегда можно заслушать).
  
## Программа курса (на данный момент редактируется)
* 27.10.18 ---- Строки и Листы. Базовые операции. Изменяемость листов.
* 03.11.18 ---- Jupyter Notebook, зачем и как работать? Словари и кортежи. Базовые операции. Изменяемость и неизменяемость. Бонус - List Comprehension
* 10.11.18 ---- Функции. Работа с функциями. Работа с файлами. Практическое занятие по обработке данных (почти BigData, только чуть поменьше).

  
## Необходимый софт
Для наиболее комфортного написания кода я рекомендую использовать сборку Anaconda и VSCode.
Если же хотите писать код в обычном блокноте и не хотите заморачиваться с установкой дополнительного софта - просто скачайте Python, а дополнительные библиотеки устанавливаются вручную следующим образом:
Открываем cmd и пишем:
```
pip install %Library_Name%
```
**pip** - очень удобный менеджер пакетов языка Python, команда **install** позволяет вам установить в корень системы библиотеку с названием %Library_Name%. Пример, установлю библиотеку [tweepy](http://www.tweepy.org/) для работы с твиттером:
```
workingcloud@evgen-pc:~$ pip install tweepy
Collecting tweepy
  Downloading https://files.pythonhosted.org/packages/05/f1/2e8c7b202dd04117a378ac0c55cc7dafa80280ebd7f692f1fa8f27fd6288/tweepy-3.6.0-py2.py3-none-any.whl
Requirement already satisfied: six>=1.10.0 in ./anaconda3/lib/python3.6/site-packages (from tweepy) (1.11.0)
Requirement already satisfied: requests>=2.11.1 in ./anaconda3/lib/python3.6/site-packages (from tweepy) (2.19.1)
Requirement already satisfied: PySocks>=1.5.7 in ./anaconda3/lib/python3.6/site-packages (from tweepy) (1.6.8)
Collecting requests-oauthlib>=0.7.0 (from tweepy)
  Downloading https://files.pythonhosted.org/packages/94/e7/c250d122992e1561690d9c0f7856dadb79d61fd4bdd0e598087dce607f6c/requests_oauthlib-1.0.0-py2.py3-none-any.whl
Requirement already satisfied: urllib3<1.24,>=1.21.1 in ./anaconda3/lib/python3.6/site-packages (from requests>=2.11.1->tweepy) (1.23)
Requirement already satisfied: idna<2.8,>=2.5 in ./anaconda3/lib/python3.6/site-packages (from requests>=2.11.1->tweepy) (2.7)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in ./anaconda3/lib/python3.6/site-packages (from requests>=2.11.1->tweepy) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.6/site-packages (from requests>=2.11.1->tweepy) (2018.10.15)
Collecting oauthlib>=0.6.2 (from requests-oauthlib>=0.7.0->tweepy)
  Downloading https://files.pythonhosted.org/packages/e6/d1/ddd9cfea3e736399b97ded5c2dd62d1322adef4a72d816f1ed1049d6a179/oauthlib-2.1.0-py2.py3-none-any.whl (121kB)
    100% |████████████████████████████████| 122kB 1.4MB/s 
Installing collected packages: oauthlib, requests-oauthlib, tweepy
Successfully installed oauthlib-2.1.0 requests-oauthlib-1.0.0 tweepy-3.6.0
```
Написал я только первую строчку, дальше **pip** сделал все сам.

## Ресурсы, где ты обязан быть каждый день
  * [Хабр](https://habr.com/)  - русскоязычная тусовка программистов. Всегда можно найти что-то полезное, интересную жизу, чтиво на вечер, а также ответы на вопросы "как написать будильник на стиральной машинке на python".
  * [Stackoverflow](https://stackoverflow.com/) - то же, что предыдущий, только больше, круче, подробнее и на английском. Здесь можно найти ответ ну практически на все.
  * [Medium](https://medium.com/) - довольно популярный среди кодеров ресурс, подписывайтесь на новости о python, а также покопайтесь в таких сферах как машинное обучение, анализ данных, веб-программирование и т.д. и т.п. Словом - учитесь читать.
  * [Codelabs](https://codelabs.developers.google.com/) - очень полезный ресурс от Гуглов. Содержит массу тутуриалов о том, как делать крутые штуки (если вам в особенности приглянутся какие-то фичи - давайте разберем что-нибудь на занятии).
  
  
## Рекомендуемый и дополнительный материал 
* Моя первая книжка по Python в открытом доступе. [Python for Everybody](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf)
* [Сборник упраженений на английском](https://www.practicepython.org/)
* [Математика в Python](https://www.w3resource.com/python-exercises/math/)


## Фидбек
Отзывы, предложения, пожелания можете отправлять мне прямо :
* [В телеграмм](https://t.me/Vlasov_Evgeny)
* На почту *evgeny_vlasov@yahoo.com*
* [В эту гугл форму](https://goo.gl/forms/s5Ig99A6QikMuiXs1) 
