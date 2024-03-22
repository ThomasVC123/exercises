class Distance:
    def __init__(self, *, size_in_meters):
        self.size_in_meters = size_in_meters

    @staticmethod
    def meters(amount):
        return Distance(size_in_meters=amount)

    @staticmethod
    def millimeters(amount):
        return Distance(size_in_meters=amount / 1000)

    @staticmethod
    def miles(amount):
        return Distance(size_in_meters=amount / 1609.34)

    # ...

class Duration:
    def __init__(self, *, duration_in_seconds):
        self.duration_in_seconds = int(duration_in_seconds)
    
    @staticmethod
    def from_seconds(amount):
        return Duration(duration_in_seconds=amount)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(duration_in_seconds=amount*60)
    
    @staticmethod
    def from_hours(amount):
        return Duration(duration_in_seconds=amount*3600)
    
    @property
    def seconds(self):
        return self.duration_in_seconds
    
    @property
    def minutes(self):
        return int(self.duration_in_seconds/60)
    
    @property
    def hours(self):
        return int(self.duration_in_seconds/3600)
    

    
