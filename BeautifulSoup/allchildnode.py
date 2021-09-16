from bs4 import BeautifulSoup

html='''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup</title>
    <tag1><a><b></b></a></tag1>
</head>
<body>
<div>
    <ul>
        <li class='item1' value="hello world">
           <a href='http://geekori.com'>geekori.com
           </a>
        </li>
        <li class='item2'><a href='http://www.jd.com'>京东</a></li>
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.head.contents)