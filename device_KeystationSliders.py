# name=M-Audio Keystation 49 MK3 Sliders

import channels

PITCH = 0
MAX_PITCH = 127
MODULATION = 1
VOLUME = 7


def OnMidiMsg(event):
    event.handled = True
    print(event.data1, event.data2)
    if event.data1 == PITCH:
        channel = channels.channelNumber()
        pitch = event.data2 - 64
        if pitch < 0:
            pitch /= 64
        elif pitch > 0:
            pitch /= 63
        print(pitch)
        channels.setChannelPitch(channel, pitch)
    elif event.data1 == MAX_PITCH:
        channel = channels.channelNumber()
        pitch = 1
        channels.setChannelPitch(channel, pitch)
    elif event.data1 == MODULATION:
        pass
    elif event.data1 == VOLUME:
        channel = channels.channelNumber()
        volume = event.data2 / 127
        channels.setChannelVolume(channel, volume)
    else:
        event.handled = False
