import math

class Location:
    """
    Represents a geographic location
    """

    def __init__(self, latitude, longitude):
        """
        Constructor
        Input: latitude, longitude: (float) The coordinates
            for this location.
        """
        self.latitude = latitude
        self.longitude = longitude

    def to_string(self):
        """
        Produces a string representation of the location.
        Input: None
        Returns: String representation of the location
        """
        if self.latitude < 0.0:
            lat = "S"
        else:
            lat = "N"

        if self.longitude < 0.0:
            lon = "W"
        else:
            lon = "E"

        return "({} {}, {} {})".format(abs(self.latitude),
                                       lat,
                                       abs(self.longitude),
                                       lon)

    def distance_to(self, other):
        """
        Computes the distance (m) to another location using the
        Haversine Formula
        Input: other: (Location object) Another location
        Returns: (float) the distance (m) to the other location
        """
        diffLatitude = math.radians(other.latitude - self.latitude)
        diffLongitude = math.radians(other.longitude - self.longitude)

        a = (math.sin(diffLatitude / 2))**2 \
            + math.cos(math.radians(self.latitude)) \
            * math.cos(math.radians(other.latitude)) \
            * (math.sin(diffLongitude / 2))**2
        d = 2 * math.asin(math.sqrt(a))

        return 6371000.0 * d
