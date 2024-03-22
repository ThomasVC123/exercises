class Person:
    def __init__(self, age):
        self.age = age       # Calls age's setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self, hours):
        if hours < 24 and hours >= 0:
            self.__hours = hours
        else:
            raise ValueError
    
    @minutes.setter
    def minutes(self, minutes):
        if minutes < 60 and minutes >= 0:
            self.__minutes = minutes
        else:
            raise ValueError
    
    @seconds.setter
    def seconds(self, seconds):
        if seconds < 60 and seconds >= 0:
            self.__seconds = seconds
        else:
            raise ValueError
    