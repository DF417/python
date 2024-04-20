class Television:
    
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        '''Initializes a Television object'''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    
    def power(self) -> None:
        '''This function turns the tv on and off'''
        self.__muted = False
        self.__status = not self.__status
        
    def mute(self) -> None:
        '''This function changes the mute state on and off when tv is on'''
        if self.__status == True:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        '''This function increases the tv channel number when the tv is on'''
        if self.__status == True:
            if self.__channel >= Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''This function decreases the tv channel number when the tv is on'''
        if self.__status == True:
            if self.__channel <= Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
                
    def volume_up(self) -> None:
        '''This function increases tv volume when the tv is on'''

        self.__muted = False
        if self.__status == True:
            if self.__volume >= Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        '''This function decreases tv volume when the tv is on'''
        
        self.__muted = False
        if self.__status == True:
            if self.__volume <= Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        This function returns the current state of the tv.

        Returns:
            str: Power = [status], Channel = [channel], Volume = [volume]
        '''
        power = self.__status
        chan = self.__channel
        
        if self.__muted == True:
            vol = 0
        else:
            vol = self.__volume

        return f'Power = {power}, Channel = {chan}, Volume = {vol}'
