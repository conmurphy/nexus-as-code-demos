import yaml
from jinja2 import Environment, FileSystemLoader

# with open('config.yaml') as config_file:
#     config = yaml.safe_load(config_file)

site_name = "warehouse-distribution-centre" #config['site_name']
site_count = 10 #config['site_count']

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('site-template.j2')

# Generate YAML files for each site
for site_number in range(1, site_count + 1):
    # Format site_number with leading zeros
    formatted_site_number = f"{site_number:02}"
    filename = f"../data/{site_name}-{formatted_site_number}.nac.yaml"
    with open(filename, 'w') as output_file:
        output_file.write(template.render(site_name=site_name, site_number=formatted_site_number))
    print(f"Generated {filename}")