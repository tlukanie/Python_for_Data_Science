from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    @property
    def eyes(self):
        """Getter for eyes."""
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        """Setter for eyes."""
        self._eyes = color

    @property
    def hairs(self):
        """Getter for hairs."""
        return self._hairs

    @hairs.setter
    def hairs(self, hue):
        """Setter for hairs."""
        self._hairs = hue

    # wrappers for tests
    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, hue):
        self.hairs = hue

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
