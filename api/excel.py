import openpyxl

workbook = openpyxl.load_workbook("常规二类台账_补数台账20220705.xlsx")

sh = workbook["常规二类授信"]
res = list(sh.columns)

with open('sql001_test', mode='w', encoding='utf-8') as f:
    for i in res[1][1:]:
        sql = "update hlpj_project set regular_class = 1 where project_id = {};".format(i.value)
        f.write(sql)
        f.write("\n")
