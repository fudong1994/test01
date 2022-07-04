from datetime import datetime

with open(file='sql_test.text', mode='w', encoding='utf-8') as f:
    now = datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    # print(time)
    staff_information_id = 1173
    count = 0
    for i in range(10):
        staff_information_id += 1
        name = "伍福东" + str(i + 1)
        sql = "INSERT INTO `fe_bus`.`hlcm_bp_main_staff_info`(`staff_information_id`, `bp_id`, `staff_name`, `staff_job`, `object_version_number`, `created_by`, `creation_date`, `last_updated_by`, `last_update_date`, ) VALUES (" + str(
            staff_information_id) + ", 9039051, '" + name + "', '董事长', 1, 2105, '" + time + "', 2105, '" + time + "')"
        f.write(sql)
        f.write("\n")
        count += 1
    print("总共创建了{}数据".format(count))
