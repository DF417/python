import pytest
from television import *


def test_init():
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__volume == 0
    assert tv._Television__channel == 0

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True
    tv.power()
    assert tv._Television__status == False
    
def test_mute():
    #off
    tv = Television()
    tv.mute()
    assert tv._Television__muted == False
    tv.mute()
    assert tv._Television__muted == False
    #on
    tv.power()
    tv.mute()
    assert tv._Television__muted == True
    tv.mute()
    assert tv._Television__muted == False

def test_channel_up():
    #off
    tv = Television()
    tv._Television__channel = 2
    tv.channel_up()
    assert tv._Television__channel == 2
    #on
    tv.power()
    tv._Television__channel = 2
    tv.channel_up()
    assert tv._Television__channel == 3
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down():
    #off
    tv = Television()
    tv._Television__channel = 2
    tv.channel_down()
    assert tv._Television__channel == 2
    #on
    tv.power()
    tv._Television__channel = 2
    tv.channel_down()
    assert tv._Television__channel == 1
    tv._Television__channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

def test_volume_up():
    #off
    tv = Television()
    tv._Television__volume = 1
    tv.volume_up()
    assert tv._Television__volume == 1
    #on
    tv.power()
    tv._Television__volume = 1
    tv.volume_up()
    assert tv._Television__volume == 2
    tv._Television__volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down():
    #off
    tv = Television()
    tv._Television__volume = 1
    tv.volume_down()
    assert tv._Television__volume == 1
    #on
    tv.power()
    tv._Television__volume = 1
    tv.volume_down()
    assert tv._Television__volume == 0
    tv._Television__volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME

def test_str():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.volume_up()
    tv.mute()
    assert tv.__str__() == 'Power = True, Channel = 1, Volume = 0'
    tv.mute()
    assert tv.__str__() == 'Power = True, Channel = 1, Volume = 1'
