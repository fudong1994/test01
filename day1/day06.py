import pymysql


def get_project(chance_id):
    # 1. 建立连接
    conn = pymysql.connect(host='10.224.67.135',
                           port=3306,
                           user='sit1_data',
                           passwd='sit10316',  # password也可以
                           db='fe_bus',
                           charset='utf8')  # 如果查询有中文需要指定数据库编码

    # 2. 从连接建立游标（有了游标才能操作数据库）
    cur = conn.cursor()

    # 3. 查询数据库（读）
    cur.execute('select project_id,project_number from hlpj_project hp where hp.chance_id = {}'.format(chance_id))

    # 4. 获取查询结果
    result = cur.fetchall()
    project_id = result[0][0]
    project_number = result[0][-1]

    cur.execute('select project_info_id from hlpj_project_gather_info where project_id = {}'.format(project_id))
    result2 = cur.fetchall()
    project_info_id = result2[0][0]

    cur.execute('SELECT prj_bp_id FROM hlpj_project_bp WHERE project_id = {}'.format(project_id))
    result3 = cur.fetchall()
    prj_bp_id = result3[0][0]

    cur.close()
    conn.close()
    return project_id, project_number, project_info_id, prj_bp_id


if __name__ == '__main__':
    prpject = get_project(6996)
    print(prpject)
