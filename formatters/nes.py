import json
import sys
#  TODO Abstract this into a base formatter class
if len(sys.argv) < 3:
    print "Formatter requires 2 arguments, input file and output file name"

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file_data = open(input_file_name).read()
controller_mapping = json.loads(input_file_data)

#  Converts our mapping into a emulator specific value
def convert_event(event, default, joystick=False):
    if event["type"] == 3 and not joystick:
            return event["key"]
    elif event["type"] == 11 and joystick:
        return event["button"]
    elif event["type"] == 7 and joystick:
        return event["axis"]
    return default
try:
    output_file_data = """

    # Auto-generated
    # SDL keysyms defined in /usr/include/SDL/SDL_keysym.h
    # getSDLKey can be found             in the source directory and can assist in remapping hotkeys
    #
    SDL.Arkanoid.0.DeviceNum = 0
    SDL.AutoScale = 1
    SDL.BitsPerPixel = 32
    SDL.ClipSides = 0
    SDL.DisableSpriteLimit = 1
    SDL.DoubleBuffering = 0
    SDL.FourScore = 0
    SDL.Frameskip = 0
    SDL.Fullscreen = 0
    SDL.GameGenie = 0
    SDL.Hotkeys.BindState = 283
    SDL.Hotkeys.CheatMenu = 282
    SDL.Hotkeys.DecreaseSpeed = 45
    SDL.Hotkeys.FDSEject = 289
    SDL.Hotkeys.FDSSelect = 287
    SDL.Hotkeys.FrameAdvance = 92
    SDL.Hotkeys.FrameAdvanceLagSkip = 127
    SDL.Hotkeys.IncreaseSpeed = 61
    SDL.Hotkeys.LagCounterDisplay = 47
    SDL.Hotkeys.LoadLua = 284
    SDL.Hotkeys.LoadState = 288
    SDL.Hotkeys.MovieToggleFrameDisplay = 46
    SDL.Hotkeys.MuteCapture = 39
    SDL.Hotkeys.Pause = 19
    SDL.Hotkeys.Quit = 27
    SDL.Hotkeys.Reset = 292
    SDL.Hotkeys.SaveState = 286
    SDL.Hotkeys.Screenshot = 293
    SDL.Hotkeys.SelectState0 = 48
    SDL.Hotkeys.SelectState1 = 49
    SDL.Hotkeys.SelectState2 = 50
    SDL.Hotkeys.SelectState3 = 51
    SDL.Hotkeys.SelectState4 = 52
    SDL.Hotkeys.SelectState5 = 53
    SDL.Hotkeys.SelectState6 = 54
    SDL.Hotkeys.SelectState7 = 55
    SDL.Hotkeys.SelectState8 = 56
    SDL.Hotkeys.SelectState9 = 57
    SDL.Hotkeys.SelectStateNext = 280
    SDL.Hotkeys.SelectStatePrev = 281
    SDL.Hotkeys.SubtitleDisplay = 291
    SDL.Hotkeys.ToggleBG = 285
    SDL.Hotkeys.ToggleInputDisplay = 44
    SDL.Hotkeys.ToggleMovieRW = 113
    SDL.Hotkeys.Turbo = 9
    SDL.Hotkeys.VSInsertCoin = 287
    SDL.Hotkeys.VSToggleDip = 289
    SDL.Hue = 72
    SDL.Input.EnableOppositeDirectionals = 1
    SDL.Input.FTrainer.0 = 111
    SDL.Input.FTrainer.1 = 112
    SDL.Input.FTrainer.2 = 91
    SDL.Input.FTrainer.3 = 93
    SDL.Input.FTrainer.4 = 107
    SDL.Input.FTrainer.5 = 108
    SDL.Input.FTrainer.6 = 59
    SDL.Input.FTrainer.7 = 39
    SDL.Input.FTrainer.8 = 109
    SDL.Input.FTrainer.9 = 44
    SDL.Input.FTrainer.A = 46
    SDL.Input.FTrainer.B = 47
    SDL.Input.FTrainer.DeviceNum = 0
    SDL.Input.FamicomPad2.EnableMic = 0
    SDL.Input.FamilyKeyBoard.0 = 48
    SDL.Input.FamilyKeyBoard.1 = 49
    SDL.Input.FamilyKeyBoard.2 = 50
    SDL.Input.FamilyKeyBoard.3 = 51
    SDL.Input.FamilyKeyBoard.4 = 52
    SDL.Input.FamilyKeyBoard.5 = 53
    SDL.Input.FamilyKeyBoard.6 = 54
    SDL.Input.FamilyKeyBoard.7 = 55
    SDL.Input.FamilyKeyBoard.8 = 56
    SDL.Input.FamilyKeyBoard.9 = 57
    SDL.Input.FamilyKeyBoard.A = 97
    SDL.Input.FamilyKeyBoard.APOSTROPHE = 39
    SDL.Input.FamilyKeyBoard.B = 98
    SDL.Input.FamilyKeyBoard.BACKSLASH = 92
    SDL.Input.FamilyKeyBoard.BACKSPACE = 8
    SDL.Input.FamilyKeyBoard.BRACKET_LEFT = 91
    SDL.Input.FamilyKeyBoard.BRACKET_RIGHT = 93
    SDL.Input.FamilyKeyBoard.C = 99
    SDL.Input.FamilyKeyBoard.COMMA = 44
    SDL.Input.FamilyKeyBoard.CURSORDOWN = 274
    SDL.Input.FamilyKeyBoard.CURSORLEFT = 276
    SDL.Input.FamilyKeyBoard.CURSORRIGHT = 275
    SDL.Input.FamilyKeyBoard.CURSORUP = 273
    SDL.Input.FamilyKeyBoard.D = 100
    SDL.Input.FamilyKeyBoard.DELETE = 127
    SDL.Input.FamilyKeyBoard.DeviceNum = 0
    SDL.Input.FamilyKeyBoard.E = 101
    SDL.Input.FamilyKeyBoard.END = 279
    SDL.Input.FamilyKeyBoard.ENTER = 13
    SDL.Input.FamilyKeyBoard.EQUAL = 61
    SDL.Input.FamilyKeyBoard.ESCAPE = 27
    SDL.Input.FamilyKeyBoard.F = 102
    SDL.Input.FamilyKeyBoard.F1 = 282
    SDL.Input.FamilyKeyBoard.F2 = 283
    SDL.Input.FamilyKeyBoard.F3 = 284
    SDL.Input.FamilyKeyBoard.F4 = 285
    SDL.Input.FamilyKeyBoard.F5 = 286
    SDL.Input.FamilyKeyBoard.F6 = 287
    SDL.Input.FamilyKeyBoard.F7 = 288
    SDL.Input.FamilyKeyBoard.F8 = 289
    SDL.Input.FamilyKeyBoard.G = 103
    SDL.Input.FamilyKeyBoard.GRAVE = 96
    SDL.Input.FamilyKeyBoard.H = 104
    SDL.Input.FamilyKeyBoard.I = 105
    SDL.Input.FamilyKeyBoard.INSERT = 277
    SDL.Input.FamilyKeyBoard.J = 106
    SDL.Input.FamilyKeyBoard.K = 107
    SDL.Input.FamilyKeyBoard.L = 108
    SDL.Input.FamilyKeyBoard.LEFTALT = 308
    SDL.Input.FamilyKeyBoard.LEFTCONTROL = 306
    SDL.Input.FamilyKeyBoard.LEFTSHIFT = 304
    SDL.Input.FamilyKeyBoard.M = 109
    SDL.Input.FamilyKeyBoard.MINUS = 45
    SDL.Input.FamilyKeyBoard.N = 110
    SDL.Input.FamilyKeyBoard.O = 111
    SDL.Input.FamilyKeyBoard.P = 112
    SDL.Input.FamilyKeyBoard.PAGEDOWN = 281
    SDL.Input.FamilyKeyBoard.PERIOD = 46
    SDL.Input.FamilyKeyBoard.Q = 113
    SDL.Input.FamilyKeyBoard.R = 114
    SDL.Input.FamilyKeyBoard.RIGHTALT = 307
    SDL.Input.FamilyKeyBoard.RIGHTSHIFT = 303
    SDL.Input.FamilyKeyBoard.S = 115
    SDL.Input.FamilyKeyBoard.SEMICOLON = 59
    SDL.Input.FamilyKeyBoard.SLASH = 47
    SDL.Input.FamilyKeyBoard.SPACE = 32
    SDL.Input.FamilyKeyBoard.T = 116
    SDL.Input.FamilyKeyBoard.U = 117
    SDL.Input.FamilyKeyBoard.V = 118
    SDL.Input.FamilyKeyBoard.W = 119
    SDL.Input.FamilyKeyBoard.X = 120
    SDL.Input.FamilyKeyBoard.Y = 121
    SDL.Input.FamilyKeyBoard.Z = 122
    SDL.Input.GamePad.0A = %d
    SDL.Input.GamePad.0B = %d
    SDL.Input.GamePad.0DeviceNum = 0
    SDL.Input.GamePad.0Down = %d
    SDL.Input.GamePad.0Left = %d
    SDL.Input.GamePad.0Right = %d
    SDL.Input.GamePad.0Select = %d
    SDL.Input.GamePad.0Start = %d
    SDL.Input.GamePad.0TurboA = 0
    SDL.Input.GamePad.0TurboB = 0
    SDL.Input.GamePad.0Up = %d
    SDL.Input.GamePad.1A = 0
    SDL.Input.GamePad.1B = 0
    SDL.Input.GamePad.1DeviceNum = 0
    SDL.Input.GamePad.1Down = 0
    SDL.Input.GamePad.1Left = 0
    SDL.Input.GamePad.1Right = 0
    SDL.Input.GamePad.1Select = 0
    SDL.Input.GamePad.1Start = 0
    SDL.Input.GamePad.1TurboA = 0
    SDL.Input.GamePad.1TurboB = 0
    SDL.Input.GamePad.1Up = 0
    SDL.Input.GamePad.2A = 0
    SDL.Input.GamePad.2B = 0
    SDL.Input.GamePad.2DeviceNum = 0
    SDL.Input.GamePad.2Down = 0
    SDL.Input.GamePad.2Left = 0
    SDL.Input.GamePad.2Right = 0
    SDL.Input.GamePad.2Select = 0
    SDL.Input.GamePad.2Start = 0
    SDL.Input.GamePad.2TurboA = 0
    SDL.Input.GamePad.2TurboB = 0
    SDL.Input.GamePad.2Up = 0
    SDL.Input.GamePad.3A = 0
    SDL.Input.GamePad.3B = 0
    SDL.Input.GamePad.3DeviceNum = 0
    SDL.Input.GamePad.3Down = 0
    SDL.Input.GamePad.3Left = 0
    SDL.Input.GamePad.3Right = 0
    SDL.Input.GamePad.3Select = 0
    SDL.Input.GamePad.3Start = 0
    SDL.Input.GamePad.3TurboA = 0
    SDL.Input.GamePad.3TurboB = 0
    SDL.Input.GamePad.3Up = 0
    SDL.Input.HyperShot.0 = 113
    SDL.Input.HyperShot.1 = 119
    SDL.Input.HyperShot.2 = 101
    SDL.Input.HyperShot.3 = 114
    SDL.Input.HyperShot.DeviceNum = 0
    SDL.Input.Mahjong.00 = 113
    SDL.Input.Mahjong.01 = 119
    SDL.Input.Mahjong.02 = 101
    SDL.Input.Mahjong.03 = 114
    SDL.Input.Mahjong.04 = 116
    SDL.Input.Mahjong.05 = 97
    SDL.Input.Mahjong.06 = 115
    SDL.Input.Mahjong.07 = 100
    SDL.Input.Mahjong.08 = 102
    SDL.Input.Mahjong.09 = 103
    SDL.Input.Mahjong.10 = 104
    SDL.Input.Mahjong.11 = 106
    SDL.Input.Mahjong.12 = 107
    SDL.Input.Mahjong.13 = 108
    SDL.Input.Mahjong.14 = 122
    SDL.Input.Mahjong.15 = 120
    SDL.Input.Mahjong.16 = 99
    SDL.Input.Mahjong.17 = 118
    SDL.Input.Mahjong.18 = 98
    SDL.Input.Mahjong.19 = 110
    SDL.Input.Mahjong.20 = 109
    SDL.Input.Mahjong.DeviceNum = 0
    SDL.Input.PowerPad.0 = 111
    SDL.Input.PowerPad.1 = 112
    SDL.Input.PowerPad.2 = 91
    SDL.Input.PowerPad.3 = 93
    SDL.Input.PowerPad.4 = 107
    SDL.Input.PowerPad.5 = 108
    SDL.Input.PowerPad.6 = 59
    SDL.Input.PowerPad.7 = 39
    SDL.Input.PowerPad.8 = 109
    SDL.Input.PowerPad.9 = 44
    SDL.Input.PowerPad.A = 46
    SDL.Input.PowerPad.B = 47
    SDL.Input.PowerPad.DeviceNum = 0
    SDL.Input.QuizKing.0 = 113
    SDL.Input.QuizKing.1 = 119
    SDL.Input.QuizKing.2 = 101
    SDL.Input.QuizKing.3 = 114
    SDL.Input.QuizKing.4 = 116
    SDL.Input.QuizKing.5 = 121
    SDL.Input.QuizKing.DeviceNum = 0
    SDL.Input.TopRider.0 = 113
    SDL.Input.TopRider.1 = 119
    SDL.Input.TopRider.2 = 101
    SDL.Input.TopRider.3 = 114
    SDL.Input.TopRider.4 = 116
    SDL.Input.TopRider.5 = 121
    SDL.Input.TopRider.6 = 117
    SDL.Input.TopRider.7 = 105
    SDL.Input.TopRider.DeviceNum = 0
    SDL.InputDisplay = 0
    SDL.KeepRatio = 1
    SDL.MovieMsg = 1
    SDL.NTSCpalette = 0
    SDL.NetworkIsServer = 0
    SDL.NetworkPlayers = 1
    SDL.NetworkPort = 4046
    SDL.NewPPU = 0
    SDL.NoConfig = 0
    SDL.NoFrame = 0
    SDL.NoFullscreenCursor = 1
    SDL.OekaKids.0.DeviceNum = 0
    SDL.OpenGL = 0
    SDL.OpenGLip = 0
    SDL.PAL = 0
    SDL.PauseFrame = 0
    SDL.RecordHUD = 1
    SDL.ScanLineEnd = 239
    SDL.ScanLineStart = 0
    SDL.Shadow.0.DeviceNum = 0
    SDL.ShowFPS = 0
    SDL.Sound = 1
    SDL.Sound.BufSize = 128
    SDL.Sound.LowPass = 0
    SDL.Sound.NoiseVolume = 256
    SDL.Sound.PCMVolume = 256
    SDL.Sound.Quality = 0
    SDL.Sound.Rate = 44100
    SDL.Sound.Square1Volume = 256
    SDL.Sound.Square2Volume = 256
    SDL.Sound.TriangleVolume = 256
    SDL.Sound.Volume = 150
    SDL.SpecialFX = 0
    SDL.SpecialFilter = 0
    SDL.SubtitleDisplay = 1
    SDL.Tint = 56
    SDL.Vsync = 1
    SDL.XResolution = 1366
    SDL.XStretch = 0
    SDL.YResolution = 768
    SDL.YStretch = 0
    SDL.Zapper.0.DeviceNum = 0
    SDL.XScale = 1.000000
    SDL.YScale = 1.000000
    SDL.Arkanoid.0.DeviceType = Mouse
    SDL.FCMConvert =
    SDL.Input.0 = GamePad.0
    SDL.Input.1 = GamePad.1
    SDL.Input.2 = Gamepad.2
    SDL.Input.3 = Gamepad.3
    SDL.Input.FTrainer.DeviceType = Keyboard
    SDL.Input.FamilyKeyBoard.DeviceType = Keyboard
    SDL.Input.GamePad.0DeviceType = Keyboard
    SDL.Input.GamePad.1DeviceType = None
    SDL.Input.GamePad.2DeviceType = None
    SDL.Input.GamePad.3DeviceType = None
    SDL.Input.HyperShot.DeviceType = Keyboard
    SDL.Input.Mahjong.DeviceType = Keyboard
    SDL.Input.PowerPad.DeviceType = Keyboard
    SDL.Input.QuizKing.DeviceType = Keyboard
    SDL.Input.TopRider.DeviceType = Keyboard
    SDL.Movie =
    SDL.NetworkGameKey =
    SDL.NetworkIP =
    SDL.NetworkPassword =
    SDL.NetworkUsername =
    SDL.OekaKids.0.DeviceType = Mouse
    SDL.Palette =
    SDL.RipSubs =
    SDL.Shadow.0.DeviceType = Mouse
    SDL.Sound.RecordFile =
    SDL.Zapper.0.DeviceType = Mouse


    """ % (convert_event(controller_mapping['A'], 100), 
 convert_event(controller_mapping['B'], 99),
 convert_event(controller_mapping['DOWN'], 274),
 convert_event(controller_mapping['LEFT'], 276),
 convert_event(controller_mapping['RIGHT'], 275),   
 convert_event(controller_mapping['SELECT'], 9),
 convert_event(controller_mapping['START'], 13), 
 convert_event(controller_mapping['UP'], 273))

except KeyError, e:
    print "Your input controller configuration didn't support a required button. Error: %s button required." % str(e)
    sys.exit()

with open(output_file_name, "w") as output_file:
    output_file.write(output_file_data)

print output_file_name + " created."