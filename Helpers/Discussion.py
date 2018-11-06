from Helpers.HelperEnums import DiscussionCategory
from Helpers.TypeValidator import TypeValidator


class Discussion(object):
    def __init__(self, title, category, tag, content):
        TypeValidator.validate_type(category, DiscussionCategory)
        self.title = title
        self.category = category
        self.tag = tag
        self.content = content
