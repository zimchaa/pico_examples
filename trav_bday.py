# This example shows you a simple, non-interrupt way of reading Pico Display's buttons with a loop that checks to see if buttons are pressed.
# updated to make a birthday card style thing for Trav's 40th birthday
# author: Pimoroni + Jaison - code taken from a number of different examples

import time
import random
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_P4
from pimoroni import RGBLED

# We're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_P4, rotate=0)
led = RGBLED(6, 7, 8)

display.set_backlight(0.5)
display.set_font("serif_italic")
display.set_thickness(1)

led.set_rgb(0, 0, 0)

msg_t_x = 0
msg_disp_num = 0
disp_x = 10
disp_w = 295
disp_sz = 2

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)
BLUE = display.create_pen(0, 0, 255)

WIDTH, HEIGHT = display.get_bounds()

messages = {"Testing": "This is a long message! This message can be this long and still display fine on the screen! This is an even longer bit of lorem ipsum dolor sit amet that really takes the cake in terms of length. I might leave this in as an easter egg!",
            "J.C>S.A": "Hey Trav, I hope this card makes you smile a little - there are over 114 (i.e. 115) different combinations for the front screen! See if you can find them all - I can update this to add more messages as they come in and just send you a link to a new set of code every year for your birthday (find and replace 40 with 41, etc.) - Love from your slightly older brother (40/41 = 97% - I'm only 3% older than you! HAHA!) Carrie, Sam and Alex!",
            "Mum": "To such a great Son and a wonderful Dad, Brother, Uncle, Husband and Friend - may your next forty years and more be full of joy and happiness, with great abundance of health and wealth. May each one if your relationships bring you tenfold in blessings for you and your wonderful family in the coming years. I am so grateful to you for your support encouragement and love and delight in my gift of grandchildren. Thank you for being you. Happy birthday Travito - Lots of love M",
            "Wendy & Cassidy": "CUZ! Happiest of naughty 40's to you! Thank you for finding our wife and sharing her with me. Thank you for all the times you've helped me move. Thank you for the cousins you gave my baby. Here's to another 40 years of shenanigans! <3 Wendy *cake emoji* *booze cheers emoji*",
            "Dan Welch": "Happy Birthday from Dan and Family!",
            "Helz Lee": "Happy Birthday Trav hope you have a great day! From over the water... Helen, Steve & Kids XXX",
            "Sarah Cronje": "Dear Trav, Happy 40th Birthday!  Wow... I thought I'd take you down memory lane a bit in this message: So we met through Mogs and Chris, here are a few memories - Being on the Whitestone field and you calling me 'Aunty Sarah'. Going to your farm for Christmas in Esigodini.  Crashing the motorbike in the fence. Volley ball in the river. All whilst listening to Alanis Morissette on walkmans. In teenage years we spent a lot of time hanging out with the Bournes - scary movies and caramel popcorn. Spending time at granny Jane's house on the Burnside Road. Good memories of times when we had less responsibility. I hope you have a wonderful day surrounded by friends and family Trav! Happy 40th!!",
            "Kate Wood": "Happy 40th birthday! I can't believe how old you are! I remember your 21st like it was yesterday! We hope you have an awesome day and year. Love from your cuz and her huge family. *heart emoji*",
            "Neville and Cheryl": "Hi Travis. Wishing you an amazing 40th birthday. We'll have a Mozambican R&R or 2 *red wine emoji* for you on your big day, as we remember our time with you there. Lotsa love from the Millers in SA *SA flag emoji*",
            "Darren Mcnicol": "Happy birthday, and only drink until you fall over!",
            "Janine Shannon": "Happy 40th Birthday Trav! Hope you have an amazing day and here is to the next 40 *beer emoji* *party hat emoji* from the WW's / Jannine and family xx",
            "Chris, Margs, Luke & Abby": "The 1st 40 years of childhood are the hardest. Now it's time to enjoy quality friends and toys.",
            "Trevor Barrett-cross": "Happy Birthday! - Trev",
            "": "",}

notes = ["This card / thing is also a digital I.O.U. #picocoin, only 1 in the world - for £270 - meant to be for motorcycling and other related activities and redeemable at your nearest Mother, we ",
         "Instructions: This thing has 2 modes - from the homescreen Press A to go to view the messsages, X for my message. Press Y to view the instructions and B does nothing. When viewing the messages X goes back to the homescreen, B and Y = back and next! You got this.",
         "This button does nothing... or does it!? Who knows!"]

msg_disp_num = 0
travis = ["Travito!", "No. 2 Son", "Trav", "Ravvy T", "Travis!", "Travis?", "TRAVIS!", "Trav!?", "DAD!", "T Vizz", "Cuz!", "724v15", "lodose", "#bandwagon", "Unky Tee", "T-dawg", "T>S", "!SIVART", "Bru", "Eksay", "T-9000", "T.R.V.S.", "Fab@40!"]
trav = "Travis!"
t_fonts = ["sans", "gothic", "cursive", "serif_italic", "serif"]
t_font = "serif"

print(len(messages))

class Ball:
    def __init__(self, x, y, r, dx, dy, pen):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.pen = pen
        
# initialise shapes
balls = []
for i in range(0, 10):
    r = random.randint(0, 10) + 3
    balls.append(
        Ball(
            random.randint(r, r + (WIDTH - 2 * r)),
            random.randint(r, r + (HEIGHT - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            BLUE
        )
    )
    
for i in range(0, 10):
    r = random.randint(0, 10) + 3
    balls.append(
        Ball(
            random.randint(r, r + (WIDTH - 2 * r)),
            random.randint(r, r + (HEIGHT - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            RED
        )
    )
    
for i in range(0, 10):
    r = random.randint(0, 10) + 3
    balls.append(
        Ball(
            random.randint(r, r + (WIDTH - 2 * r)),
            random.randint(r, r + (HEIGHT - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            GREEN
        )
    )

for i in range(0, 10):
    r = random.randint(0, 10) + 3
    balls.append(
        Ball(
            random.randint(r, r + (WIDTH - 2 * r)),
            random.randint(r, r + (HEIGHT - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            YELLOW
        )
    )

def bouncy_balls():
    for ball in balls:
        display.set_pen(BLACK)
        display.circle(int(ball.x), int(ball.y), int(ball.r))
        ball.x += ball.dx
        ball.y += ball.dy

        xmax = WIDTH - ball.r
        xmin = ball.r
        ymax = HEIGHT - ball.r
        ymin = ball.r

        if ball.x < xmin or ball.x > xmax:
            ball.dx *= -1

        if ball.y < ymin or ball.y > ymax:
            ball.dy *= -1

        display.set_pen(ball.pen)
        display.circle(int(ball.x), int(ball.y), int(ball.r))
        

# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    led.set_rgb(0, 0, 0)


# set up
clear()

def display_message(from_name, message, num, total, disp_y):
    display.set_pen(BLACK)
    display.clear()
    led.set_rgb(50, 0, 0)
    
    display.set_pen(WHITE)
    display.set_font("bitmap8")
    display.text("From - {}".format(from_name), disp_x, disp_y, disp_w, disp_sz)
    display.set_pen(GREEN)
    display.text("{} - [{} of {}]".format(message, num, total), disp_x, disp_y + 24, disp_w, disp_sz)
    
    
def display_note(note, colour):
    clear()
    
    led.set_rgb(0, 0, 30)
    
    display.set_pen(colour)
    display.set_font("bitmap8")
    display.text("{}".format(note), 10, 10, 295, 2)
    
def messages_mode():
    
    disp_messages = True
    msg_disp_num = 0
    msg_disp_y = 10
    print(msg_disp_num)
        
    while disp_messages:
        if button_a.read():
            # go to the messages
            msg_disp_num = 0
            msg_disp_y = 10
            clear()
        elif button_b.read():
            # go back a message
            msg_disp_num -= 1
            msg_disp_y = 10
            if (msg_disp_num < 0):
                msg_disp_num = (len(messages) - 1)
            clear()
        elif button_x.read():
            # view the home screen
            disp_messages = False
        elif button_y.read():
            # go to the next message
            msg_disp_num += 1
            msg_disp_y = 10
            if (msg_disp_num > (len(messages) - 1)):
                msg_disp_num = 0
            clear()
        else:
            # keep displaying the current message
            
            display_message(list(messages.keys())[msg_disp_num], list(messages.values())[msg_disp_num], msg_disp_num+1, len(messages), msg_disp_y)
            if msg_disp_y < -210:
                msg_disp_y = 10
                
            msg_disp_y -= 2
            
        display.update()
        time.sleep(0.1)

while True:
    if button_x.read():                                   # if a button press is detected then...
        clear()                                           # clear to black
        # display.set_pen(WHITE)                            # change the pen colour
        # display.text("Button A pressed", 10, 10, 240, 4)  # display some text on the screen
        display_note(notes[0], WHITE)
        display.update()                                  # update the display
        time.sleep(10)                                     # pause for a sec
        clear()                                           # clear to black again
    elif button_b.read():
        clear()
        display_note(notes[1], WHITE)
        display.update()
        time.sleep(10)
        clear()
    elif button_a.read():
        clear()
        messages_mode()
        clear()
    elif button_y.read():
        clear()
        display_note(notes[2], BLUE)
        trav = random.choice(travis)
        t_font = random.choice(t_fonts)
        msg_t_x = 10
        display.update()
        time.sleep(1)
        clear()
    else:
        bouncy_balls()
        display.set_pen(BLACK)
        display.text(trav, msg_t_x, 200, 100, 3)
        # clear()
        msg_t_x -= 3
        if (msg_t_x < -400):
            msg_t_x = 340
        display.set_font("serif_italic")
        display.set_pen(CYAN)
        display.set_thickness(2)
        display.text("Happy", 50, 35, 100, 2)
        display.set_pen(MAGENTA)
        display.text("Birthday", 20, 100, 100, 2)
        display.set_pen(YELLOW)
        display.set_font(t_font)
        display.set_thickness(3)
        display.text(trav, msg_t_x, 200, 100, 3)
        display.update()
    # time.sleep(0.001)  # this number is how frequently the Pico checks for button presses
