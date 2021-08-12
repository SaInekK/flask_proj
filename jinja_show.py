# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:13:44 2021

@author: User
"""
from jinja2 import Template, escape

name = 'alex'
age = 21

tm = Template("Hello, {{ n.capitalize() }} {{ a }} years old")
msg = tm.render(n=name, a = age)

print(msg)


# Экраниерование скобок
data = '''{% raw %} {{ This  is usual text with curved brackets}}
{% endraw %}'''

tm = Template(data)
msg = tm.render(n=name, a = age)

print(msg)


# Экранирование тэгов
link = '''Links in HTML document:
<a href ="#">Ссылка</a>'''

tm = Template("{{link | e}}")
msg = tm.render(link=link)

print(msg)

# То же самое
msg = escape(link)

print(msg)



cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 2, 'city': 'SPb'},
          {'id': 5, 'city': 'Minsk'}]
# "-" для переноса строки
link = '''<select name="cities">
{% for c in cities -%} 
{% if c.id >1 -%}
    <option value="{{ c['id'] }}"> {{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%} 
{% endfor -%} 
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)



cars = [
        {'model': 'Audi', 'price': 23000},
        {'model': 'Skoda', 'price': 17000},
        {'model': 'Volvo', 'price': 43200}
]


tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price')}}" # фильтр шаблона
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Максимальная цена автомобиля {{ (cs | max(attribute='price')).model}}" # фильтр шаблона
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Автомобиль {{ cs | random }}" # фильтр шаблона
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Автомобиль {{ cs | replace('o', 'O') }}" # фильтр шаблона
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

digs = [1,2,3,4,5]
tpl = "Суммарная значений списка {{ cs | sum}}" # фильтр шаблона
tm = Template(tpl)
msg = tm.render(cs=digs)
print(msg)



persons = [
        {'name': 'Alexei', 'old': 18, 'weight': 78.3},
        {'name': 'Nikolai', 'old': 27, 'weight': 82.4},
        {'name': 'Ivan', 'old': 33, 'weight': 93.}
]
# Блок фильтр
tpl = '''
{% for u in users -%} 
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%} 
'''
tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)



html = '''
{% macro input(name, value='', type='text', size = 20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}" 
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm = Template(html)
msg = tm.render()
print(msg)



html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}
{%- endfor %} 
</ul>
{%- endmacro %}


{{ list_users(users) }}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)



html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %} 
</ul>
{%- endmacro %}


{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)



from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
        {'name': 'Alexei', 'old': 18, 'weight': 78.3},
        {'name': 'Nikolai Петруш', 'old': 27, 'weight': 82.4},
        {'name': 'Ivan', 'old': 33, 'weight': 93.}
]


def loadTpl(path):
    if path == "index":
        return "Name {{u.name}}, age {{u.old}}"
    else:
        return "Data: {{u}}"


file_loader = FileSystemLoader('templates') # file in templates folder
env = Environment(loader=file_loader)

tm = env.get_template('main.htm') # Template class object
msg = tm.render(users=persons)

print(msg)


file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index') # Template class object
msg = tm.render(u=persons[0])

print(msg)



print()



file_loader = FileSystemLoader('templates') # file in templates folder
env = Environment(loader=file_loader)

tm = env.get_template('page.htm') # Template class object
msg = tm.render(domain='http://proproprogs.ru', title='About Jinja')

print(msg)

print()

subs = ['math', 'physics', 'english', 'CS']

file_loader = FileSystemLoader('templates') # file in templates folder
env = Environment(loader=file_loader)

tm = env.get_template('about.htm') # Template class object
output = tm.render(list_table=subs)

print(output)
