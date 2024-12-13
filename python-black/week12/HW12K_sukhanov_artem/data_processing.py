
def filter_reviews(reviews, min_length=50):
    return [review for review in reviews if len(review['body']) >= min_length]
