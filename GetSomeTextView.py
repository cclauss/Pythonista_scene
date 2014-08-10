import ui

class GetSomeTextView(ui.View):
    def __init__(self):
        self.name = 'Enter some text:'
        tf1 = self.make_text_field('top_field', 'Change me')
        tf1.y += 20  # move it down
        tf2 = self.make_text_field('bottom_field', 'Me too')
        tf2.y += 60
        tf1.action = tf2.action = self.textfield_action
        self.present('sheet')
        print('-' * 20)
        self.wait_modal()

    def make_text_field(self, name, default_text = ''):
        text_field = ui.TextField(name=name)
        text_field.text = default_text
        text_field.x = 175
        text_field.height = 20
        text_field.width = 200
        self.add_subview(text_field)
        return text_field
    
    def textfield_action(self, sender):
        fmt = 'Field {:<12} has a action value of "{}".'
        print(fmt.format(sender.name, sender.text))

    def will_close(self):
        fmt = 'Field {:<12} has a final value of "{}".'
        for subview in self.subviews:
            if isinstance(subview, ui.TextField):
                print(fmt.format(subview.name, subview.text))

GetSomeTextView()
