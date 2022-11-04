import warnings

import openrouteservice
from openrouteservice.exceptions import ApiError


class GeoDistance:
    api_keys: list[str]
    client: openrouteservice.Client

    def __init__(self, api_keys: list[str]):
        self.api_keys = api_keys
        self.client = self.initialize_client(self.api_keys[0])

    @staticmethod
    def initialize_client(api_key: str) -> openrouteservice.Client:
        client = openrouteservice.Client(api_key)
        return client

    def get_geodistance(
        self,
        origin_latitude: float,
        origin_longitude: float,
        destination_latitude: float,
        destination_longitude: float,
    ) -> float:
        coords: tuple[tuple[int]] = (
            (origin_longitude, origin_latitude),
            (destination_longitude, destination_latitude),
        )
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            warnings.simplefilter("ignore", ResourceWarning)
            try:
                response: dict[str, dict] = self.client.directions(coords)
            except (UserWarning, ApiError) as exception:
                if len(self.api_keys) == 1:
                    raise IndexError("No more API keys available.") from exception
                self.api_keys.pop(0)
                self.client = self.initialize_client(self.api_keys[0])
                return self.get_geodistance(
                    origin_latitude,
                    origin_longitude,
                    destination_latitude,
                    destination_longitude,
                )
        kilometers_distance: float = -1
        minutes_distance: float = -1
        try:
            kilometers_distance = response["routes"][0]["summary"]["distance"] / 1000
            minutes_distance = response["routes"][0]["summary"]["duration"] / 60
        except KeyError:
            pass
        warnings.simplefilter("default", ResourceWarning)
        return (kilometers_distance, minutes_distance)
