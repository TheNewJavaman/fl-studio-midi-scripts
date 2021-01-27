# name=M-Audio Keystation 49 MK3 Buttons

import channels
import transport
import midi

UP = 23
DOWN = 24
LEFT = 21
RIGHT = 22
ENTER = 20
STOP = 118
PLAY = 119
RECORD = 114


def OnMidiMsg(event):
    event.handled = True
    print(event.data1, event.data2)
    if event.data2 == 127:
        if event.data1 == UP:
            channel = channels.channelNumber()
            channel -= 1
            if channel == -1:
                channel = channels.channelCount() - 1
            channels.selectOneChannel(channel)
        elif event.data1 == DOWN:
            channel = channels.channelNumber()
            channel += 1
            if channel == channels.channelCount():
                channel = 0
            channels.selectOneChannel(channel)
        elif event.data1 == LEFT:
            transport.globalTransport(midi.FPT_Metronome, 1)
        elif event.data1 == RIGHT:
            transport.globalTransport(midi.FPT_CountDown, 1)
        elif event.data1 == ENTER:
            channel = channels.channelNumber()
            channels.soloChannel(channel)
        elif event.data1 == STOP:
            transport.stop()
        elif event.data1 == PLAY:
            transport.start()
        elif event.data1 == RECORD:
            transport.record()
        else:
            event.handled = False
    else:
        event.handled = False


'''
SETUP = 15
DIRECTIONAL = 13
TRANSPORT = 14
ACTION = 47

UP = 68
DOWN = 64
LEFT = 65
RIGHT = 67
ENTER = 66
STOP = 67
PLAY = 68
RECORD = 69

next_action = 0


def OnMidiMsg(event):
    global next_action
    event.handled = True
    print(event.data1, event.data2)
    if event.data1 == SETUP:
        next_action = event.data2
    elif event.data1 == ACTION:
        if next_action == DIRECTIONAL:
            if event.data2 == UP:
                channel = channels.channelNumber()
                channel -= 1
                if channel == -1:
                    channel = channels.channelCount() - 1
                channels.selectOneChannel(channel)
            elif event.data2 == DOWN:
                channel = channels.channelNumber()
                channel += 1
                if channel == channels.channelCount():
                    channel = 0
                channels.selectOneChannel(channel)
            elif event.data2 == LEFT:
                transport.globalTransport(midi.FPT_Metronome, 1)
            elif event.data2 == RIGHT:
                transport.globalTransport(midi.FPT_CountDown, 1)
            elif event.data2 == ENTER:
                channel = channels.channelNumber()
                channels.soloChannel(channel)
            else:
                event.handled = False
        elif next_action == TRANSPORT:
            if event.data2 == STOP:
                transport.stop()
            elif event.data2 == PLAY:
                transport.start()
            elif event.data2 == RECORD:
                transport.record()
            else:
                event.handled = False
        else:
            event.handled = False
    else:
        event.handled = False
'''
