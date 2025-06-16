from flask import request, render_template

def handle_word_list_route():
    result = None
    words_input = ""

    if request.method == "POST":
        words_input = request.form.get("words", "")
        words_list = [w.strip() for w in words_input.split(",") if w.strip()]
        result = list_words(words_list)

    return render_template("third_challenge.html", result=result, words=words_input)

def list_words(word_list):
    lists = {}
    for word in word_list:
        if word in lists:
            lists[word] += 1
        else:
            lists[word] = 1
    return lists
