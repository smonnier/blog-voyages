"""
Voyages tags
=============

Attach a special parameter and dates of tags from teh category "voyages"

Author: Viviane Pons

"""
from pelican import signals
import datetime


KEY = "voyages"

def is_tag_voyage(tags, tag, exclude):
    if not tag.slug in exclude:
        for article in tags[tag]:
            if article.category.slug == KEY:
                return True
    return False

def set_tag_dates(tags, tag):
    year_start = datetime.MAXYEAR
    year_end = datetime.MINYEAR
    for article in tags[tag]:
        y = article.date.year
        if y < year_start:
            year_start = y
        if y > year_end:
            year_end = y
    tag.year_start = year_start
    tag.tear_end = year_end
    tag.year_str = str(year_start)
    if year_end != year_start:
        tag.year_str += " - " + str(year_end)

def set_voyages_tags(generators):
    articles_generator = generators[0]
    exclude = articles_generator.settings["EXCLUDE_FROM_CATEGORY"][KEY]
    for tag in articles_generator.tags:
        if is_tag_voyage(articles_generator.tags, tag, exclude):
            tag.is_voyage = True
            set_tag_dates(articles_generator.tags, tag)


def register():
    signals.all_generators_finalized.connect(set_voyages_tags)
