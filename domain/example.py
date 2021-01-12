class Example:
    def __init__(self, **kwargs):
        self.example_id = kwargs.get('example_id')
        self.name = kwargs.get('name')
        self.is_active = True

    def __str__(self):
        return '<Object %s>' % (self.name)