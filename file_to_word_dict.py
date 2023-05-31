import json
import jieba
from read_file import get_files_dir, replace_tags

DATA_PATH = "data"
JSON_WORD_RESULT_PATH = 'result/word_dict.json'

# 词语字典
word_dict = {

}


def add_count(content):
    """
    词频统计
    :param content:
    :return:
    """
    content = replace_tags(content)
    cut_results = jieba.cut(content, cut_all=True)
    for res in cut_results:
        if res in word_dict.keys():
            word_dict[res] = word_dict[res] + 1
        else:
            word_dict[res] = 1


def dump():
    with open(JSON_WORD_RESULT_PATH, 'w') as f:
        json.dump(word_dict, f)


def deal_file(dir):
    with open(dir, "r", encoding="utf-8") as f:
        # 读取单个文件
        content = f.read()
        add_count(content)

def main():
    dirs = get_files_dir(DATA_PATH)
    for idx, dir in enumerate(dirs):
        print("正在处理：" + str(idx) + " / " + str(len(dirs)))
        deal_file(dir)
    dump()


if __name__ == '__main__':
    main()

