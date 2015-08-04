# See: https://omz-forums.appspot.com/pythonista/post/6142748495183872

import console, datetime, scene

fmt = '{} is {} days away.'

class days_until_event(scene.Scene):
    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date
        scene.run(self)
    def setup(self):
        self.center = self.bounds.center()
        self.font_size = 64 if self.size.w > 700 else 32
    def draw(self):
        scene.background(0, 0, 0)
        msg = fmt.format(self.event_name, (self.event_date - datetime.date.today()).days)
        scene.text(msg, 'Futura', self.font_size, *self.center)

prompt = '''Please enter the event name.
i.e. First day of school'''
event_name = console.input_alert('Event', prompt, '', 'Enter')
prompt = '''Please enter the date you would like to countdown to.
i.e. 2009 (year),6 (month),29 (day)'''
event_date = console.input_alert('Date', prompt, '', 'Enter')
try:
    year, month, day = [int(s.strip()) for s in event_date.split(',')]
    event_date = datetime.date(year, month, day)
except ValueError:
    exit('Incorrect date format (must be "year, month, day")')

days_until_event(event_name, event_date)
