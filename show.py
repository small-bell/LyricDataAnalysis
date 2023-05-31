import json

JSON_WORD_RESULT_PATH = 'result/word_dict.json'
JSON_SINGLE_WORD_RESULT_PATH = 'result/single_word_dict.json'


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


if __name__ == '__main__':
    all_data = read_json(JSON_WORD_RESULT_PATH)
    single = read_json(JSON_SINGLE_WORD_RESULT_PATH)
    while True:
        print("==============================")
        input_str = input("请输入字符或字符串:\n")
        if len(input_str) == 1:
            if input_str in single:
                res = single[input_str]
                print(input_str + " 总计 : " + str(res["num"]))
                for element in res["set"]:
                    print(element + " : " + str(all_data[element]))
            else:
                print(input_str + " : 0")
        else:
            if input_str in all_data:
                print(input_str + " : " + str(all_data[input_str]))
            else:
                print(input_str + " : 0")
