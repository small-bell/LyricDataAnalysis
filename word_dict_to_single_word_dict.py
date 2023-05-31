import json

from utils.JSONSetEncoder import JSONSetEncoder

DATA_PATH = "data"
JSON_WORD_RESULT_PATH = 'result/word_dict.json'
JSON_SINGLE_WORD_RESULT_PATH = 'result/single_word_dict.json'

# 单字字典
single_word_dict = {

}


def read_json():
    with open(JSON_WORD_RESULT_PATH, "r") as f:
        return json.load(f)


def dump():
    with open(JSON_SINGLE_WORD_RESULT_PATH, 'w') as f:
        json.dump(single_word_dict, f, cls=JSONSetEncoder)

def main():
    word_dict = read_json()
    for key in word_dict.keys():
        # key 是单词 value 是单词数量
        value = word_dict[key]
        # 遍历单个字
        for word in key:
            if word in single_word_dict.keys():
                word_res = single_word_dict[word]
                # 添加num
                single_word_dict[word]["num"] = single_word_dict[word]["num"] + value
                # 添加set
                word_set = single_word_dict[word]["set"]
                word_set.add(key)
                single_word_dict[word]["set"] = word_set
            else:
                word_set = set()
                word_set.add(key)
                single_word_dict[word] = {
                    "num": value,
                    "set": word_set
                }
    dump()


if __name__ == '__main__':
    main()
