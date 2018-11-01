from selenium.webdriver.support.select import Select


class DropDownList(object):
    def __init__(self, by_type, dd_locator, dictionary_items, browser):
        self.by_type = by_type
        self.dd_locator = dd_locator
        self.dictionary_items = dictionary_items
        self.browser = browser

    def select_by_enum(self, dd_enum_type, dd_enum_item_to_select):
        if not isinstance(dd_enum_item_to_select, dd_enum_type):
            raise TypeError(f"Item to select should be from type Enum: {dd_enum_type}")

        text_to_select = self.dictionary_items[dd_enum_item_to_select]
        web_element = self.browser.wait_for_element(self.by_type, self.dd_locator,"DropDown List Box Element")
        select_element = Select(web_element)
        select_element.select_by_visible_text(text_to_select)
