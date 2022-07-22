
def progress_bar(pourcentage):
    points = "".join(["." for _ in range(round(100-pourcentage))])
    hashtag = "".join(["#" for _ in range(round(pourcentage))])

    return f"[{hashtag}{points}]"