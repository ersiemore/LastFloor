
from imagebutton import ImageButton
import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.set_reserved(4)
clock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 720
FPS = 60

call_step = 0

second_call_start = 0
second_call_step = 0

mistakes = 0
floor = 0
scene = "menu"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Last Floor")


phone_visible = False
call_start = pygame.time.get_ticks()



bg = {
    "main": pygame.image.load("backgrounds/startmenu.png").convert(),
    "firstscene": pygame.image.load("backgrounds/firstscene.png").convert(),
    "coridor": pygame.image.load("backgrounds/coridor.png").convert(),
    "elevator": pygame.image.load("backgrounds/elev.png").convert(),
    "entrance": pygame.image.load("backgrounds/entrance.png").convert(),
    "zero_floor": pygame.image.load("backgrounds/elevator.png").convert(),
    "openelv": pygame.image.load("backgrounds/openelv.png").convert(),
    "firstdeath": pygame.image.load("backgrounds/firstdeathbgg.png").convert(),
    "jumpscare": pygame.image.load("backgrounds/jumpscare.png").convert(),
    "close_mouth": pygame.image.load("backgrounds/man1.png").convert(),
    "open_mouth": pygame.image.load("backgrounds/man2.png").convert(),
    "scoop": pygame.image.load("backgrounds/scoop.png").convert(),
    "scoopp": pygame.image.load("backgrounds/scoopp.png").convert(),
    "close_mouth_anonim": pygame.image.load("backgrounds/closemouth.png").convert(),
    "open_mouth_anonim": pygame.image.load("backgrounds/openmouth.png").convert(),
    "2flooropen": pygame.image.load("backgrounds/2flooropen.png").convert(),
    "2floorclose": pygame.image.load("backgrounds/2floorclose.png").convert(),
}

font = pygame.font.Font("fonts/monogram.ttf", 70)
second_font = pygame.font.Font("fonts/NotoSans-Regular.ttf", 70)

fonts = {
    "LastFloor": font.render("LastFloor", True, (255, 255, 255)),
    "ersiemore": font.render("By: Ersiemore", True, (255, 255, 255)),
    "first": second_font.render("В следующий раз возьми трубку.", True, (255, 255, 255)),
    "second": second_font.render("Нажмите R чтоб выйти в меню.", True, (255, 255, 255))
}

buttons = {
    "start": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="НАЧАТЬ ИГРУ",
        sound="audio/click.mp3",
        size=(300, 80)
    ),

    "info": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ОБ ИГРЕ",
        sound="audio/click.mp3",
        size=(300, 80)
    ),

    "exit": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ВЫХОД",
        sound="audio/click.mp3",
        size=(300, 80)
    ),

    "phone": ImageButton(
        "icons/normalphone.png",
        "icons/hoverphone.png",
        "",
        sound="audio/click.mp3",
        size=(300, 450)
    ),

    "sleep": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ОСТАТСЯ",
        sound="audio/click.mp3",
        size=(300, 80)

    ),

    "leave": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ВЫЙТИ",
        sound="audio/click.mp3",
        size=(300, 80)
    ),

    "enter_elevator": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ВОЙТИ В ЛИФТ",
        sound="audio/дзынь.mp3",
        size=(300, 80)
    ),

    "firstfloor": ImageButton(
        "buttons/btn.png",
        "buttons/btn.png",
        sound="audio/дзынь.mp3",
        size=(300, 300)
    ),

    "secondfloor": ImageButton(
        "buttons/btn.png",
        "",
        sound="audio/дзынь.mp3",
        size=(50, 50)
    ),

    "choose1": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ВПУСТИТЬ",
        sound="audio/click.mp3",
        size=(300, 80)
    ),

    "choose2": ImageButton(
        "buttons/normalbtn.png",
        "buttons/hoverbtn.png",
        text="ЗАКРЫТЬ ДВЕРИ",
        sound="audio/дзынь.mp3",
        size=(300, 80)
    )
}


normal_phone = pygame.image.load(
    "icons/normalphone.png"
).convert_alpha()

normal_phone = pygame.transform.scale(
    normal_phone,
    (300, 450)
)

hover_phone = pygame.image.load(
    "icons/hoverphone.png"
).convert_alpha()

hover_phone = pygame.transform.scale(
    hover_phone,
    (300, 450)
)

white_phone = pygame.image.load(
    "icons/whitephone.png"
).convert_alpha()

white_phone = pygame.transform.scale(
    white_phone,
    (300, 450)
)


background_audio = {
    "menu": pygame.mixer.Sound("audio/mainmenusound.mp3"),
    "phone": pygame.mixer.Sound("audio/ringtone.mp3"),
    "breath": pygame.mixer.Sound("audio/breath.mp3"),
    "rain": pygame.mixer.Sound("audio/rain.mp3"),
    "dzin": pygame.mixer.Sound("audio/дзынь.mp3"),
    "sololift": pygame.mixer.Sound("audio/sololift.mp3"),
    "Lost": pygame.mixer.Sound("audio/Lost.mp3"),
    "Jumpscare": pygame.mixer.Sound("audio/Jumpscare.mp3"),
    "break_door": pygame.mixer.Sound("audio/выломал.mp3"),
    "touch_glass": pygame.mixer.Sound("audio/glass.mp3"),
    "explosion": pygame.mixer.Sound("audio/ball.mp3"),
    "att": pygame.mixer.Sound("audio/att.mp3"),
}


anonim_voice = {
    "audio1": pygame.mixer.Sound("audio/first.mp3"),
    "audio2": pygame.mixer.Sound("audio/second.mp3"),
    "audio3": pygame.mixer.Sound("audio/three.mp3"),
    "audio4": pygame.mixer.Sound("audio/four.mp3"),
    "audio5": pygame.mixer.Sound("audio/five.mp3"),
    "audio6": pygame.mixer.Sound("audio/anonimdown.mp3"),
    "audio7": pygame.mixer.Sound("audio/зря.mp3"),
    "audio8": pygame.mixer.Sound("audio/игру.mp3"),
    "audio9": pygame.mixer.Sound("audio/long1.mp3"),
    "audio10": pygame.mixer.Sound("audio/long2.mp3"),
    "audio11": pygame.mixer.Sound("audio/long3.mp3"),
    "audio12": pygame.mixer.Sound("audio/anonimaudio13.mp3"),
}

man_voice = {
    "audio1": pygame.mixer.Sound("audio/audioman.mp3"),
    "audio2": pygame.mixer.Sound("audio/audioman2.mp3"),
    "audio3": pygame.mixer.Sound("audio/audioman3.mp3"),
    "audio4": pygame.mixer.Sound("audio/audioman4.mp3"),
}

female_kid_voice = {
    "audio1": pygame.mixer.Sound("audio/firstkid.mp3"),
    "audio2": pygame.mixer.Sound("audio/secondkid.mp3"),
    "audio3": pygame.mixer.Sound("audio/threekid.mp3"),
    "audio4": pygame.mixer.Sound("audio/crying.mp3")
}

hero_voice = {

}


background_audio["menu"].set_volume(0.1)
background_audio["phone"].set_volume(0.5)
background_audio["breath"].set_volume(0.15)
background_audio["rain"].set_volume(0.15)
background_audio["sololift"].set_volume(0.15)


voice_channel = pygame.mixer.Channel(1)
man_channel = pygame.mixer.Channel(2)
kid_channel = pygame.mixer.Channel(3)

mouth_open = False
mouth_timer = 0


background_audio["menu"].play(-1)

idle_frames = [
    pygame.image.load("first_floor_person/frame_000.png").convert_alpha(),
    pygame.image.load("first_floor_person/frame_001.png").convert_alpha(),
    pygame.image.load("first_floor_person/frame_002.png").convert_alpha(),
    pygame.image.load("first_floor_person/frame_003.png").convert_alpha()
]

idle_frames = [
    pygame.transform.scale(
        frame,
        (frame.get_width() * 5, frame.get_height() * 5)
    )
    for frame in idle_frames
]

idle_frames_kid = [
    pygame.image.load("second_floor_person_idle/frame_000.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_001.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_002.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_003.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_004.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_005.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_006.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_007.png").convert_alpha(),
    pygame.image.load("second_floor_person_idle/frame_008.png").convert_alpha(),
]

crying_frames_kid = [
    pygame.image.load("second_floor_person_crying/frame_000.png").convert_alpha(),
    pygame.image.load("second_floor_person_crying/frame_001.png").convert_alpha(),
    pygame.image.load("second_floor_person_crying/frame_002.png").convert_alpha(),
]

idle_frames_kid = [
    pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    for frame in idle_frames_kid
]

crying_frames_kid = [
    pygame.transform.scale(frame, (frame.get_width() * 4, frame.get_height() * 4))
    for frame in crying_frames_kid
]



idle_index = 0
idle_delay = 180
idle_last_update = pygame.time.get_ticks()


kid_idle_index = 0
kid_idle_delay = 300
kid_last_update = pygame.time.get_ticks()

kid_crying_index = 0
kid_crying_delay = 300
kid_crying_last_update = pygame.time.get_ticks()
att_after_phrase = False


jumpscare_start = 0
glass_hitbox = pygame.Rect(170, 150, 50, 50)
first_man_hitbox = pygame.Rect(590, 330, 100, 200)
kid_hitbox = pygame.Rect(610, 400, 50, 100)
ball_hitbox = pygame.Rect(690, 300, 50, 50)
window_clicked = False
man_clicks = 0
kid_clicks = 0



def transition():
    fade = pygame.Surface((WIDTH, HEIGHT))

    for alpha in range(0, 256, 5):
        fade.fill((0, 0, 0))
        fade.set_alpha(alpha)

        screen.blit(fade, (0, 0))

        pygame.display.flip()
        pygame.time.delay(20)


def menu():
    screen.blit(bg["main"], (0, 0))

    buttons["start"].blit(screen, (500, 140))
    buttons["info"].blit(screen, (500, 200))
    buttons["exit"].blit(screen, (500, 260))
    screen.blit(fonts["LastFloor"], (60, 50))
    screen.blit(fonts["ersiemore"], (60, 150))


def first_scene():
    global scene

    if pygame.time.get_ticks() - call_start >= 60000:
        background_audio["phone"].stop()
        transition()
        background_audio["break_door"].play()
        scene = "first_death"
        return

    screen.blit(bg["firstscene"], (0, 0))
    buttons["phone"].blit(screen, (500, 340))


def first_death():
    global call_step
    global scene
    global jumpscare_start
    draw_first_death()

    if call_step == 0:
        voice_channel.play(
            background_audio["Lost"]
        )
        call_step = 1

    elif call_step == 1 and not voice_channel.get_busy():
        scene = "jumpscare"
        jumpscare_start = pygame.time.get_ticks()
        background_audio["Jumpscare"].play()


def draw_first_death():
    screen.blit(bg["firstdeath"], (0, 0))

def draw_jumpscare():
        global scene
        screen.blit(bg["jumpscare"], (0, 0))
        if pygame.time.get_ticks() - jumpscare_start  >= 5000:
            scene = "first_return"

def draw_first_return():
    screen.fill((0, 0, 0))
    screen.blit(fonts["first"], (100, 200))
    screen.blit(fonts["second"], (200, 300))




def call():
    global call_step
    global scene

    screen.blit(bg["firstscene"], (0, 0))
    buttons["phone"].blit(screen, (500, 340))

    if call_step == 0:
        voice_channel.play(
            anonim_voice["audio1"]
        )
        call_step = 1

    elif call_step == 1:
        if not voice_channel.get_busy():
            voice_channel.play(
                anonim_voice["audio2"]
            )
            call_step = 2

    elif call_step == 2:
        if not voice_channel.get_busy():
            voice_channel.play(
                anonim_voice["audio3"]
            )
            call_step = 3

    elif call_step == 3:
        if not voice_channel.get_busy():
            voice_channel.play(
                anonim_voice["audio4"]
            )
            call_step = 4

    elif call_step == 4:
        if not voice_channel.get_busy():
            voice_channel.play(
                anonim_voice["audio5"]
            )
            call_step = 5

    elif call_step == 5:
        if not voice_channel.get_busy():
            voice_channel.play(
                anonim_voice["audio6"]
            )
            call_step = 6

    elif call_step == 6:
        if not voice_channel.get_busy():
            background_audio["breath"].stop()
            transition()
            background_audio["rain"].play(-1)
            scene = "after_call"


def after_call():
    screen.blit(bg["firstscene"], (0, 0))
    buttons["sleep"].blit(screen, (850, 550))
    buttons["leave"].blit(screen, (850, 630))

def spawn_elevator():
    global second_call_step
    global scene
    global phone_visible
    screen.blit(bg["elevator"], (0, 0))

    if second_call_step == 0:
        voice_channel.play(
            anonim_voice["audio7"]
        )
        second_call_step = 1

    elif second_call_step == 1:
        if not voice_channel.get_busy():
            voice_channel.play(
                anonim_voice["audio8"]
            )
            second_call_step = 2
    if not pygame.mixer.get_busy():
        phone_visible = True

    if phone_visible:
        buttons["enter_elevator"].blit(screen, (800, 600))







def hallway():
    screen.blit(bg["coridor"], (0, 0))
    buttons["leave"].blit(screen, (500, 300))



def zero_floor():
    screen.blit(bg["zero_floor"], (0, 0))
    buttons["phone"].blit(screen, (500, 340))

def second_call():
    global second_call_step
    global phone_visible

    screen.blit(bg["zero_floor"], (0, 0))

    if phone_visible:
        buttons["phone"].image = white_phone
        buttons["phone"].hover_image = white_phone
        buttons["phone"].blit(screen, (500, 340))

    if second_call_step == 0:
        voice_channel.play(anonim_voice["audio9"])
        second_call_step = 1

    elif second_call_step == 1:
        if not voice_channel.get_busy():
            voice_channel.play(anonim_voice["audio10"])
            second_call_step = 2

    elif second_call_step == 2:
        if not voice_channel.get_busy():
            voice_channel.play(anonim_voice["audio11"])
            second_call_step = 3

    elif second_call_step == 3:
        if not voice_channel.get_busy():
            phone_visible = False
            second_call_step = 4
            background_audio["sololift"].play(-1)

    elif second_call_step == 4:
        buttons["firstfloor"].blit(screen, (150, 390))


def first_floor():
    global idle_index, idle_last_update

    screen.blit(bg["openelv"], (0, 0))

    now = pygame.time.get_ticks()

    if now - idle_last_update >= idle_delay:
        idle_index = (idle_index + 1) % len(idle_frames)
        idle_last_update = now

    character_image = idle_frames[idle_index]
    character_rect = character_image.get_rect(
        midbottom=(640, 660)
    )

    screen.blit(character_image, character_rect)

    if man_clicks >= 3:
        buttons["choose1"].blit(screen, (850, 550))
        buttons["choose2"].blit(screen, (850, 630))

def man_closeup():
    global scene
    global mouth_open
    global mouth_timer
    now = pygame.time.get_ticks()

    if man_channel.get_busy():
        if now - mouth_timer >= 120:
            mouth_open = not mouth_open
            mouth_timer = now
    else:
        background_audio["dzin"].play()
        transition()
        background_audio["sololift"].play(-1)
        scene = "2_floor_transition"
        mouth_open = False

    if mouth_open:
        screen.blit(bg["open_mouth"], (0, 0))
    else:
        screen.blit(bg["close_mouth"], (0, 0))

def second_floor_transition():
    screen.blit(bg["zero_floor"], (0, 0))
    buttons["firstfloor"].blit(screen, (100, 200))

def second_floor():
    global scene, kid_idle_index, kid_last_update

    screen.blit(bg["2flooropen"], (0, 0))

    now = pygame.time.get_ticks()

    if now - kid_last_update >= kid_idle_delay:
        kid_idle_index = (kid_idle_index + 1) % len(idle_frames_kid)
        kid_last_update = now

    character_image = idle_frames_kid[kid_idle_index]
    character_rect = character_image.get_rect(
        midbottom=(650, 640)
    )

    screen.blit(character_image, character_rect)

def crying_kid():
    global kid_crying_index, kid_crying_last_update, att_after_phrase

    if att_after_phrase and not kid_channel.get_busy():
        background_audio["att"].play()
        att_after_phrase = False

    screen.blit(bg["2flooropen"], (0, 0))

    now = pygame.time.get_ticks()

    if now - kid_crying_last_update >= kid_crying_delay:
        kid_crying_index = (kid_crying_index + 1) % len(crying_frames_kid)
        kid_crying_last_update = now

    character_image = crying_frames_kid[kid_crying_index]
    character_rect = character_image.get_rect(
        midbottom=(640, 620)
    )

    screen.blit(character_image, character_rect)


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if scene == "menu":

            if buttons["start"].click(event):
                call_step = 0
                call_start = pygame.time.get_ticks()
                transition()

                background_audio["menu"].stop()
                background_audio["phone"].play(-1)
                scene = "first_scene"

            elif buttons["exit"].click(event):
                running = False

        elif scene == "first_scene":

            if buttons["phone"].click(event):
                background_audio["phone"].stop()

                buttons["phone"].image = white_phone
                buttons["phone"].hover_image = white_phone

                background_audio["breath"].play(-1)

                call_step = 0
                scene = "call"
        elif scene == "after_call":
            if buttons["leave"].click(event):
                background_audio["rain"].stop()
                scene = "hallway"
            elif buttons["sleep"].click(event):
                background_audio["rain"].stop()
                second_call_step = 0
                scene = "elevator"
        elif scene == "elevator":
            if buttons["enter_elevator"].click(event):
                floor = 0
                transition()
                background_audio["phone"].play(-1)
                buttons["phone"].image = normal_phone
                buttons["phone"].hover_image = hover_phone
                scene = "zero_floor"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if glass_hitbox.collidepoint(event.pos) and not window_clicked:
                    background_audio["touch_glass"].play()
                    window_clicked = True


        elif floor == 0 and scene == "zero_floor":
            if buttons["phone"].click(event):
                background_audio["phone"].stop()
                second_call_step = 0
                phone_visible = True
                scene = "second_call"
        elif scene == "second_call":
           if second_call_step == 4:
               if buttons["firstfloor"].click(event):
                   floor = 1
                   scene = "1_floor"
        elif scene == "1_floor":
            if event.type == pygame.MOUSEBUTTONDOWN and not man_channel.get_busy():
                if first_man_hitbox.collidepoint(event.pos):
                    man_clicks += 1

                    if man_clicks == 1:
                        man_channel.play(man_voice["audio1"])
                    elif man_clicks == 2:
                        man_channel.play(man_voice["audio2"])
                    elif man_clicks == 3:
                        man_channel.play(man_voice["audio3"])

            if man_clicks >= 3:
                if buttons["choose1"].click(event):
                    mistakes += 1
                    man_channel.play(man_voice["audio4"])
                    mouth_open = False
                    mouth_timer = pygame.time.get_ticks()
                    scene = "man_closeup"

                elif buttons["choose2"].click(event):
                    transition()
                    background_audio["sololift"].play(-1)
                    scene = "2_floor_transition"

        elif scene == "first_return":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                background_audio["menu"].play(-1)
                scene = "menu"

        elif scene == "2_floor_transition":
            if buttons["firstfloor"].click(event):
                background_audio["sololift"].stop()
                floor = 2
                background_audio["sololift"].play(-1)
                scene = "2_floor"

        elif scene == "2_floor":
            if event.type == pygame.MOUSEBUTTONDOWN and not kid_channel.get_busy():
                if kid_hitbox.collidepoint(event.pos):
                    kid_clicks += 1

                    if kid_clicks == 1:
                        kid_channel.play(female_kid_voice["audio1"])
                    elif kid_clicks == 2:
                        kid_channel.play(female_kid_voice["audio2"])
                    elif kid_clicks == 3:
                        kid_channel.play(female_kid_voice["audio3"])

                elif kid_clicks >= 3 and ball_hitbox.collidepoint(event.pos):
                    att_after_phrase = True
                    background_audio["explosion"].play()
                    kid_channel.play(female_kid_voice["audio4"])
                    kid_crying_index = 0
                    kid_crying_last_update = pygame.time.get_ticks()
                    scene = "crying_kid"



    if scene == "menu":
        menu()

    elif scene == "first_scene":
        first_scene()

    elif scene == "call":
        call()

    elif scene == "after_call":
        after_call()

    elif scene == "hallway":
        hallway()

    elif scene == "jumpscare":
        draw_jumpscare()

    elif scene == "elevator":
        spawn_elevator()

    elif floor == 0 and scene == "zero_floor":
        zero_floor()

    elif floor == 1 and scene == "1_floor":
        first_floor()

    elif scene == "second_call":
        second_call()

    elif scene == "first_death":

        first_death()

    elif scene == "first_return":
        draw_first_return()

    elif scene == "man_closeup":
        man_closeup()

    elif scene == "2_floor_transition":
        second_floor_transition()

    elif floor == 2 and scene == "2_floor":
        second_floor()

    elif scene == "crying_kid":
        crying_kid()

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()