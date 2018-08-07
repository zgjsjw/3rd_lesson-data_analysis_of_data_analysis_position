import os
import pandas as pd

data_in_path = './data'
data_out_path = './result'

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

def data_area(data_in):
    data_count_city = data_in

def main():
    if not os.path.exists(os.path.join(data_out_path, 'result.csv')):
        clean_data(data_in_path, data_out_path)
        
    data_area()

if __name__ == '__main__':
    main()
