"""
Background
==========

Check on specific background image using article names and tags

Author: Viviane Pons

"""
import os
from pelican import signals

EXTENSION = ".jpg"

def set_background_tag(articles_generator, folder_path):
    for tag in articles_generator.tags:
        filename = folder_path + tag.slug + EXTENSION
        if os.path.isfile(filename):
            tag.background_image = tag.slug + EXTENSION
            for article in articles_generator.tags[tag]:
                article.background_image = tag.background_image

def set_background_article(articles_generator, folder_path):
    for article in articles_generator.articles:
        # checking background from article name
        filename = folder_path + article.slug + EXTENSION
        if os.path.isfile(filename):
            article.background_image = article.slug + EXTENSION



def set_background(generators):
    local_path = os.getcwd()
    articles_generator = generators[0]
    background_path = local_path + articles_generator.settings["BACKGROUND_PATH"]
    set_background_tag(articles_generator, background_path)
    set_background_article(articles_generator, background_path)

def register():
    signals.all_generators_finalized.connect(set_background)
