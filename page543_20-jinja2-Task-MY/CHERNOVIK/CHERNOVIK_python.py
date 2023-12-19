data_file = "data_files/for.yml"
with open(data_file) as f:
    data = yaml.safe_load(f)
    print(data)