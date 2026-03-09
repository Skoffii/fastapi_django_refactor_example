from fastapi import ApiRouter, HTTPExeptions, status
from test_db import categories_db, posts_db
from schemas.category import CategoryResponse

router = ApiRouter()


@router.get(
    "/category/{category_slug}/",
    satus_code=status.HTTP_200_OK,
    response_model=CategoryResponse,
)
async def category_posts(category_slug: str):
    for category in categories_db:
        if category["slug"] == category_slug:
            cat_posts = []
            for post in posts_db:
                if post["category"] == category_slug:
                    cat_posts.append(post)
                    return cat_posts
    raise HTTPExeptions(status_code=status.HTTP_404_NOT_FOUND)
