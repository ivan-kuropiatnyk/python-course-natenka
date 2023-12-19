from jinja2 import Environment, FileSystemLoader
import yaml
env = Environment(loader=FileSystemLoader('templates'))#templates-папка где находятся шаблоны
template = env.get_template('page511-V-20-router_template.txt')
with open('data_files/page512-V-20-routers_info.yml') as f:
    routers = yaml.safe_load(f)
for router in routers:
    r1_conf = "results/page512-V-20_RESULTS_"+router['name']+'_r1.txt'
    with open(r1_conf, 'w') as f:
        f.write(template.render(router))