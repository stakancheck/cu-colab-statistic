import asyncio
from pprint import pprint

from api_requests import fetch_all_reviews
from data_processing import filter_reviews
from post_review import post_new_review
from save_data import save_reviews


async def process():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1/comments',
        'https://jsonplaceholder.typicode.com/posts/2/comments',
        'https://jsonplaceholder.typicode.com/posts/3/comments'
    ]

    # Fetch all reviews
    reviews = await fetch_all_reviews(urls)

    # Filter reviews
    filtered_reviews = filter_reviews(reviews, min_length=100)

    # Save reviews to file and print
    if filtered_reviews: pprint(filtered_reviews)
    await save_reviews(filtered_reviews)

    # Post a new review
    new_review = {
        'postId': 1,
        'name': 'test_user',
        'email': 'test_user@example.com',
        'body': 'Отличный товар!'
    }
    await post_new_review('https://jsonplaceholder.typicode.com/posts/1/comments', new_review)


def main():
    asyncio.run(process())


if __name__ == "__main__":
    main()
