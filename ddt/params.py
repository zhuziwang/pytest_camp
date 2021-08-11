def yaml_params():
    import yaml
    datas = None
    with open('lib/cases/cases.yaml',encoding='utf8') as f:
        datas = yaml.safe_load(f)
    return datas


def excel_params():
    from models.model_excel import sheet_to_list
    table_sheet = sheet_to_list("lib/cases/A2103.xlsx", 'Sheet1')
    #print(table)
    return table_sheet