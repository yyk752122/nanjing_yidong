import yaml


def analyze_file(lyze_file,keys):
    with open("./data/"+lyze_file,"r",encoding="utf_8") as f:
        data=yaml.load(f)
        data_list=data[keys]
        list_data=[]
        for i in data_list.values():
            list_data.append(i)
        return list_data
