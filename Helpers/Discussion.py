from Helpers.HelperEnums import DiscussionCategory


class Discussion(object):
    def __init__(self, title, category, tag, content):
        self.title = title
        if type(category) is not DiscussionCategory:
            raise TypeError("Category should be DiscussionCategory Enum Type")
        self.category = category
        self.tag = tag
        self.content = content
