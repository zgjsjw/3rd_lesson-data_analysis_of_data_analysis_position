import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_in_path = './data'
data_out_path = './result'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def clean_data(path_in, path_out):
    if not os.path.exists(path_out):
        os.mkdir(path_out)
    data_in = pd.read_csv(os.path.join(path_in, 'data.csv'))
    print("原始数据总共有{}行".format(len(data_in)))
    # 去掉一些不需要的字段：发布时间、职位描述、工作地址、爬取时间
    data_mid = data_in.drop(['发布时间', '职位描述', '工作地址', '爬取时间'], axis=1)
    #去掉空值
    data_no_na = data_mid.dropna()
    print("去掉空值后，还剩{}行".format(len(data_no_na)))
    #去掉重复值
    data_out = data_no_na.drop_duplicates()
    data_out.to_csv(os.path.join(path_out, 'result.csv'), index=False, encoding='utf_8_sig')
    print("去重后，有效数据{}行".format(len(data_out)))
    return data_out

def data_area(data_in):
    data_count_city = data_in['工作地点'].value_counts()
    #print(data_count_city)
    #绘制地域分布条形图
    #plt.figure(figsize=(32, 20))
    data_count_city.plot.bar()
    plt.xticks(rotation=60)
    plt.title("数据分析职位需求量地域分布")
    plt.tight_layout()
    plt.savefig(os.path.join(data_out_path, 'data_area.png'))
    plt.show()

def data_salary(data_in):
    salary = data_in['薪资区间'].str.split('-').map(lambda t: (int(t[0][:-1]) + int(t[1][:-1]))/2)
    print(salary)

    #plt.figure(figsize=(32, 20))
    plt.title("职位薪酬分布情况")
    plt.hist(salary, bins=30, color='g')
    plt.xticks(range(5, 65, 5))
    plt.xlabel('K/月')
    plt.tight_layout()
    plt.savefig(os.path.join(data_out_path, 'data_salary.png'))
    plt.show()

def salary_area(data_in):
    data_in['average_salary'] = data_in['薪资区间'].str.split('-').map(lambda t: (int(t[0][:-1]) + int(t[1][:-1]))/2)
    #print(data_in['average_salary'])
    data = data_in.groupby("工作地点")['average_salary']
    city = data_in['工作地点'].value_counts().index[0:6]
    salary = []
    for key in city:
        salary.append(data.get_group(key).values)
    #print(salary)
    plt.figure()
    ax = plt.subplot(1,1,1)
    plt.title("薪酬--地域分布情况")
    plt.boxplot(salary)
    ax.set_xticklabels(city)
    plt.xlabel("城市")
    plt.ylabel('K/月')
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

def experience(data_in):
    raw_data = data_in['工作经验'].value_counts()
    explode = 0.01 / raw_data.values * data_in['工作经验'].count() + [0,0,0,0,-0.4,-0.4]
    print(explode)
    #print(raw_data)
    plt.title("工作经验占比情况")
    plt.pie(raw_data, labels=raw_data.index, autopct='%1.2f%%', shadow=True, radius=0.6, explode=explode,
            startangle=0, pctdistance=0.7)
    #plt.tight_layout()
    plt.show()

def main():
    if not os.path.exists(os.path.join(data_out_path, 'result.csv')):
        data = clean_data(data_in_path, data_out_path)
    else:
        print("读取已清理好数据")
        data = pd.read_csv(os.path.join(data_out_path, 'result.csv'))

    #data_area(data)
    #data_salary(data)
    #salary_area(data)
    experience(data)

if __name__ == '__main__':
    main()
