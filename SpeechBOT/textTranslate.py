def trans(text, dst):
    import six
    import os
    from google.cloud import translate_v2 as translate
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json" #Ohad' account
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    result = translate_client.translate(text, target_language=dst)

    return format(result["translatedText"])