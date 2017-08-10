# -*- coding: utf-8 -*-

"""
    作者:     高岱恒
    版本:     1.1
    日期:     2017/02/19
    项目名称：科技工作者心理健康数据分析 (Mental Health in Tech Survey)
    对男女平均年龄分别进行统计分析
"""

#目标：每个国家的有心理问题的人的平均年龄。
import csv

# 数据集路径
data_path = './survey.csv'

#现在的数据是按行操作的：后面用pandas可以直接按列操作数据，很快。
def main():
    """
        主函数
    """
    #male_set 和 female_set的数据类型是set
    male_set = {'male', 'm'}  # “男性”可能的取值
    female_set = {'female', 'f'}  # “女性”可能的取值

    # 构造统计结果的数据结构 result_dict
    # 其中每个元素是键值对，“键”是国家名称，“值”是列表结构，
    # 列表的第一个数为该国家女性统计数据，第二个数为该国家男性统计数据
    # 如 {'United States': [20, 50], 'Canada': [30, 40]}
    # 思考：这里的“值”为什么用列表(list)而不用元组(tuple)
    result_dict = {}

    with open(data_path, 'r', newline='') as csvfile:
        #参数newline是用来控制文本模式之下，一行的结束字符。可以是None，’’，\n，\r，\r\n等。
        # 加载数据
        rows = csv.reader(csvfile)
        for i, row in enumerate(rows):
            if i == 0:
                # 跳过第一行表头数据
                continue

            if i % 50 == 0:
                print('正在处理第{}行数据...'.format(i))
            # 年龄、性别、国家数据
            age_val = row[1]
            gender_val = row[2]
            country_val = row[3]

            # 去掉可能存在的空格
            gender_val = gender_val.replace(' ', '')
            # 转换为小写
            gender_val = gender_val.lower()

            # 判断“国家”是否已经存在
            if country_val not in result_dict:
                # 如果不存在，初始化数据
                result_dict[country_val] = [0, 0, 0, 0]

            # 判断性别
            if gender_val in female_set:
                # 女性
                result_dict[country_val][0] += 1
                if int(age_val) > 1 and int(age_val) < 80:
                    # 合理年龄
                    result_dict[country_val][2] += int(age_val)
                else:
                    # 噪声数据，不做处理
                    pass
            elif gender_val in male_set:
                # 男性
                result_dict[country_val][1] += 1
                if int(age_val) > 1 and int(age_val) < 80:
                    # 合理年龄
                    result_dict[country_val][3] += int(age_val)
                else:
                    # 噪声数据，不做处理
                    pass
            else:
                # 噪声数据，不做处理
                pass


    # 分男女的统计年龄
    with open('age_country.csv', 'w', newline='', encoding='utf-16') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        # 写入表头
        csvwriter.writerow(['国家', '男性平均年龄', '女性平均年龄'])

        # 写入统计结果
        for k, v in list(result_dict.items()):
            try:
                csvwriter.writerow([k, v[2]/v[0], v[3]/v[1]])
            except ZeroDivisionError:
                if v[0] == 0 and v[1] != 0:
                    csvwriter.writerow([k, 0, v[3]/v[1]])
                elif v[0] != 0 and v[1] == 0:
                    csvwriter.writerow([k, v[2]/v[0], 0])
                else:
                    csvwriter.writerow([k, 0, 0])



if __name__ == '__main__':
    main()
