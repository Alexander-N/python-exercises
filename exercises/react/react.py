class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        self._observers = []

    def add_observer(self, obs):
        self._observers.append(obs)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for obs in self._observers:
            obs.update()

class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        for inp in inputs:
            inp.add_observer(self)

        self.inputs = inputs
        self.compute_function = compute_function
        self._observers = []
        self._callbacks = []
        self._value = None

        self.update()

    def add_observer(self, obs):
        self._observers.append(obs)

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        try:
            self._callbacks.remove(callback)
        except ValueError:
            pass

    def expect_callback_values(self, callback):
        pass

    def update(self):
        old_value = self._value
        inputs = self.inputs
        compute_function = self.compute_function

        self._value = compute_function([input.value for input in inputs])
        if self._value == old_value:
            return

        for obs in self._observers:
            obs.update()

        for cb in self._callbacks:
            cb(self._value)

    @property
    def value(self):
        return self._value
