class EventChannel(object):
    def __init__(self):
        self.subscribers = {}

    def unsubscribe(self, event, callback):
        if event is not None or event != ""\
                and event in self.subscribers.keys():
            self.subscribers[event] = list(
                filter(
                    lambda x: x is not callback,
                    self.subscribers[event]
                )
            )

    def subscribe(self, event, callback):
        if not callable(callback):
            raise ValueError("callback must be callable")

        if event is None or event == "":
            raise ValueError("Event cant be empty")

        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            self.subscribers[event].append(callback)

    def publish(self, event, args):
        if event in self.subscribers.keys():
            for callback in self.subscribers[event]:
                callback(args)


event_channel = EventChannel()

callback = lambda x: print(x)

event_channel.subscribe("myevent", callback)

event_channel.publish("myevent", "Hello, world!")

def prova(valore):
	print("Ecco il valore di valore  :{}".format(valore))
 
event_channel.subscribe("team_left", prova)
event_channel.publish("aristide", 121)
# FUNZIONA


team_left = "Grosseto A.S."
team_right = "Roccacannuccia"
periodo = 3
team_scoreL = 139
team_scoreR = 119
tempo = datetime.now().strftime('%H:%M:%S')
falliL = 3
falliR = 5