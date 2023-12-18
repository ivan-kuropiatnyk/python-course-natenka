from jinja2 import Environment, FileSystemLoader
import yaml
'''
Скрипт импортирует из модуля jinja2:
• FileSystemLoader - загрузчик, который позволяет работать с файловой системой. Тут ука-
зывается путь к каталогу, где находятся шаблоны в данном случае шаблон находится в
текущем каталоге
• Environment - класс для описания параметров окружения. В данном случае указан только
загрузчик, но в нём можно указывать методы обработки шаблона
'''
env = Environment(loader=FileSystemLoader("."))
templ = env.get_template("templates/page509-V-20-cfg_template.txt")
liverpool = {"id": "11", "name": "Liverpool", "int": "Gi1/0/17", "ip": "10.1.1.10"}
#последняя строка рендерит шаблон, используя словарь liverpool, подставляет значения в переменные шаблона.
print(templ.render(liverpool))