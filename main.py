# -*- coding: utf-8 -*-

"""
    ����:     ��᷺�
    �汾:     1.1
    ����:     2017/02/19
    ��Ŀ���ƣ��Ƽ����������������ݷ��� (Mental Health in Tech Survey)
    ����Ůƽ������ֱ����ͳ�Ʒ���
"""

#Ŀ�꣺ÿ�����ҵ�������������˵�ƽ�����䡣
import csv

# ���ݼ�·��
data_path = './survey.csv'

#���ڵ������ǰ��в����ģ�������pandas����ֱ�Ӱ��в������ݣ��ܿ졣
def main():
    """
        ������
    """
    #male_set �� female_set������������set
    male_set = {'male', 'm'}  # �����ԡ����ܵ�ȡֵ
    female_set = {'female', 'f'}  # ��Ů�ԡ����ܵ�ȡֵ

    # ����ͳ�ƽ�������ݽṹ result_dict
    # ����ÿ��Ԫ���Ǽ�ֵ�ԣ��������ǹ������ƣ���ֵ�����б�ṹ��
    # �б�ĵ�һ����Ϊ�ù���Ů��ͳ�����ݣ��ڶ�����Ϊ�ù�������ͳ������
    # �� {'United States': [20, 50], 'Canada': [30, 40]}
    # ˼��������ġ�ֵ��Ϊʲô���б�(list)������Ԫ��(tuple)
    result_dict = {}

    with open(data_path, 'r', newline='') as csvfile:
        #����newline�����������ı�ģʽ֮�£�һ�еĽ����ַ���������None��������\n��\r��\r\n�ȡ�
        # ��������
        rows = csv.reader(csvfile)
        for i, row in enumerate(rows):
            if i == 0:
                # ������һ�б�ͷ����
                continue

            if i % 50 == 0:
                print('���ڴ����{}������...'.format(i))
            # ���䡢�Ա𡢹�������
            age_val = row[1]
            gender_val = row[2]
            country_val = row[3]

            # ȥ�����ܴ��ڵĿո�
            gender_val = gender_val.replace(' ', '')
            # ת��ΪСд
            gender_val = gender_val.lower()

            # �жϡ����ҡ��Ƿ��Ѿ�����
            if country_val not in result_dict:
                # ��������ڣ���ʼ������
                result_dict[country_val] = [0, 0, 0, 0]

            # �ж��Ա�
            if gender_val in female_set:
                # Ů��
                result_dict[country_val][0] += 1
                if int(age_val) > 1 and int(age_val) < 80:
                    # ��������
                    result_dict[country_val][2] += int(age_val)
                else:
                    # �������ݣ���������
                    pass
            elif gender_val in male_set:
                # ����
                result_dict[country_val][1] += 1
                if int(age_val) > 1 and int(age_val) < 80:
                    # ��������
                    result_dict[country_val][3] += int(age_val)
                else:
                    # �������ݣ���������
                    pass
            else:
                # �������ݣ���������
                pass


    # ����Ů��ͳ������
    with open('age_country.csv', 'w', newline='', encoding='utf-16') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        # д���ͷ
        csvwriter.writerow(['����', '����ƽ������', 'Ů��ƽ������'])

        # д��ͳ�ƽ��
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
