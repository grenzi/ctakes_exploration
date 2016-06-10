from zato.server.service import Service

class MyService(Service):
    class SimpleIO:
        output_required = ('name', 'last_name')

    def handle(self):
        self.response.payload.name = 'Mark'
        self.response.payload.last_name = 'Twain'