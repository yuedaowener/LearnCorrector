import os

import jieba


class RuleCorrector():
    def __init__(self, config):
        self.confusion_path = config.confusion_path
        self.word_dict_path = config.word_dict_path
        self.same_pinyin_path = config.same_pinyin_path
        self.same_stroke_path = config.same_stroke_path
        self.char_set_path = config.char_set_path
        self.lm_model_path = config.lm_model_path  # TODO：所以这个是训练好了的，这里不需要训练？？
        self.pinyin2word_path = config.pinyin2word_path

    def _detect_by_confusion(self, text):
        pass

    def _detect_error(self, text):
        maybe_errors = []

        return maybe_errors

    def _generate_candidates(self, item):
        candidates = []
        return candidates

    def _grade_candidates(self, candidates):
        candi_grades_pair = []
        return candi_grades_pair

    def _detect_by_token(self, text):
        tokens = None
        pass

    def correct(self, text):
        # 检查可能出错的
        error_item = self._detect_error(text)
        # 找出候选
        candidates = self._generate_candidates(error_item)
        # 候选词得分
        candi_grades_pair = self._grade_candidates(candidates)
        # 找出得分最高的候选来修改
        corrected_item = candi_grades_pair[0][0]
        # 合成新句子
        new_text = f" {corrected_item} ".join(text.split(error_item))

        return new_text


class Config:
    data_dir = r"D:\Efficiency\21_Career\Projects\YoungCorrector\data"
    confusion_path = os.path.join(data_dir, "custom_confusion.txt")
    word_dict_path = os.path.join(data_dir, "../../data/dict.txt")
    same_pinyin_path = os.path.join(data_dir, "../../data/same_pinyin.txt")
    same_stroke_path = os.path.join(data_dir, "../../data/same_stroke.txt")
    lm_model_path = os.path.join(data_dir, "../../data/people_chars_lm.klm")
    char_set_path = os.path.join(data_dir, "../../data/common_char_set.txt")
    pinyin2word_path = os.path.join(data_dir, "../../data/pinyin2word.model")


def main():
    texts = [
        '这件事情针让人想象难以',
        '这周末我要去配副眼睛',
        '感帽了',
        '你儿字今年几岁了',
        '少先队员因该为老人让坐',
    ]

    corrector = RuleCorrector(Config)
    for text in texts:
        new_text = corrector.correct(text)
        print(new_text)

    pass


if __name__ == '__main__':
    pass
