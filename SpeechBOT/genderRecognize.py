from inaSpeechSegmenter import Segmenter


def recognize(audioFile):
    gender = []
    seg = Segmenter()
    segmentation = seg(audioFile)
    return (max(set(gender), key=gender.count))
