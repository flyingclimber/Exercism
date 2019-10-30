EARTH_ORBITAL = 365.25
MERCURY_ORBITAL = 0.2408467
VENUS_ORBITAL = 0.61519726
MARS_ORBITAL = 1.8808158
JUPITER_ORBITAL = 11.862615
SATURN_ORBITAL = 29.447498
URANUS_ORBITAL = 84.016846
NEPTUNE_ORBITAL = 164.79132
DAILY_SECONDS = 24 * 60 * 60


def format_seconds(seconds):
    return round(seconds, 2)


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return format_seconds(self.seconds / (EARTH_ORBITAL * DAILY_SECONDS))

    def on_mercury(self):
        return format_seconds(self.seconds / (MERCURY_ORBITAL * EARTH_ORBITAL * DAILY_SECONDS))

    def on_venus(self):
        return format_seconds(self.seconds / (VENUS_ORBITAL * EARTH_ORBITAL * DAILY_SECONDS))

    def on_mars(self):
        return format_seconds(self.seconds / (MARS_ORBITAL * EARTH_ORBITAL * DAILY_SECONDS))

    def on_jupiter(self):
        return format_seconds(self.seconds / (JUPITER_ORBITAL * EARTH_ORBITAL* DAILY_SECONDS))

    def on_saturn(self):
        return format_seconds(self.seconds / (SATURN_ORBITAL * EARTH_ORBITAL * DAILY_SECONDS))

    def on_uranus(self):
        return format_seconds(self.seconds / (URANUS_ORBITAL * EARTH_ORBITAL * DAILY_SECONDS))

    def on_neptune(self):
        return format_seconds(self.seconds / (NEPTUNE_ORBITAL * EARTH_ORBITAL * DAILY_SECONDS))
