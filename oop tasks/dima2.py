class Button:
    number_of_clicks = 0

    def click(self):
        self.number_of_clicks += 1

    def click_count(self):
        return self.number_of_clicks

    def reset(self):
        self.number_of_clicks = 0


button = Button()
button.click()
button.click()
print(button.click_count())
button.click()
print(button.click_count())
button.reset()
print(button.click_count())