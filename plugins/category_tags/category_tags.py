"""
Category tags
=============

Attach to each category a list of tags depending on articles

Author: Viviane Pons

"""
from pelican import signals

def set_category_tags(articles_generator):
    exclude = articles_generator.settings["EXCLUDE_FROM_CATEGORY"]
    category_tags = {}
    category_tag_slugs = {}
    for category, articles in articles_generator.categories:
        list_tags = []
        list_slugs = set()
        for article in articles:
            if hasattr(article, "tags"):
                for tag in article.tags:
                    if not tag.slug in exclude[category.slug] and not tag.slug in list_slugs:
                        list_tags.append(tag)
                        list_slugs.add(tag.slug)
            else:
                print article.slug
        category.tags = list_tags

def register():
    signals.article_generator_finalized.connect(set_category_tags)

