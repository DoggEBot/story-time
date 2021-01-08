class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
scene.set_background_image(img("""
    5555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        5555555555555555888888888888888888888888888888888888888888888888888888888888888888888888888888888777778888888888888888888888888888888888888888888888888888888888
        5555555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888777777888888888888888888888888888888888888888888888888888888888
        5555555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888887777777788888888888888888888888888888888888888888888888888888888
        5555555588888888888888888888888888888888888888888888888888888888888888888888888888888888888888877777777778888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888777777777778888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888887777777777777888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888887777777777777788888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888777777888888888888888888888888888888888888888877777777777777778888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888777777788888888888888888888888888888888888888777777777777777777888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888887777777788888888888888888888888888888888888887777777777777777777788888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888877777777778888888888888888888888888888888888877777777777777777777778888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888877777777777888888888888888888888888888888888777777777777777777777778888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888777777777777888888888888888888888888888888887777777777777777777777777888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888777777777777788888888888888888888888888888877777777777777777777777777788888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888887777777777777788888888888888888888888888888777777777777777777777777777778888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888877777777777777778888888888888888888888888888777777777777777777777777777777888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888877777777777777778888888888888888888888888887777777777777777777777777777777788888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888777777777777777777888888888888888888888888877777777777777777777777777777777778888888888888888888888888888888888888888888
        8888888888888888888888888888888888888887777777777777777777788888888888888888888888777777777777777777777777777777777778888888888888888888888888888888888888888888
        8888888888888888888888888888888888888887777777777777777777788888888888888888888887777777777777777777777777777777777777888888888888888888888888888888888888888888
        8888888888888888888888888888888888888877777777777777777777788888888888888888888877777777777777777777777777777777777777788888888888888888888888888888888888888888
        8888888888888888888888888888888888888777777777777777777777777888888888888888888877777777777777777777777777777777777777788888888888888888888888888888888888888888
        8888888888888888888888888888888888888777777777777777777777777888888888888888888877777777777777777777777777777777777777788888888888888888888888888888888888888888
        8888888888888888888888888888888888888777777777777777777777777888888888888888888877777777777777777777777777777777777777788888888888888888888888888888888888888888
        8888888888888888888888888888888888888777777777777777777777777888888888888888888877777777777777777777777777777777777777788888888888888888888888888888888888888888
        8888888888888888888888888888888888888777777777777777777777777888888888888888888887777777777777777777777777777777777777888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee88888888888888888888888888888887777777777777777777788888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888eeeee888888888888888888888888888888888888888888888888888888888888
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
Player_1 = sprites.create(img("""
        . . . . . . f f f f f f . . . . 
            . . . . f f e e e e f 2 f . . . 
            . . . f f e e e e f 2 2 2 f . . 
            . . . f e e e f f e e e e f . . 
            . . . f f f f e e 2 2 2 2 e f . 
            . . . f e 2 2 2 f f f f e 2 f . 
            . . f f f f f f f e e e f f f . 
            . . f f e 4 4 e b f 4 4 e e f . 
            . . f e e 4 d 4 1 f d d e f . . 
            . . . f e e e 4 d d d d f . . . 
            . . . . f f e e 4 4 4 e f . . . 
            . . . . . 4 d d e 2 2 2 f . . . 
            . . . . . e d d e 2 2 2 f . . . 
            . . . . . f e e f 4 5 5 f . . . 
            . . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . . .
    """),
    SpriteKind.player)
NPC_1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . f 4 4 f f f f . . . . . . 
            . . f 4 5 5 4 5 f b f f . . . . 
            . . f 5 5 5 5 4 e 3 3 b f . . . 
            . . f e 4 4 4 e 3 3 3 3 b f . . 
            . f 3 3 3 3 3 3 3 3 3 3 3 f . . 
            . f 3 3 e e 3 b e 3 3 3 3 f . . 
            . f 3 3 e e e f f 3 3 3 3 f . . 
            . . f e e e f b f b b b b f f . 
            . . . e 4 4 f 1 e b b b b b f . 
            . . . f 4 4 4 4 f b b b b b f . 
            . . . f d d d e 4 4 b b b f . . 
            . . . f d d d e 4 4 f f f . . . 
            . . f d d d b b e e b b f . . . 
            . . f b d 1 d 1 d d b f . . . . 
            . . . f f f b b f f f . . . . .
    """),
    SpriteKind.player)
NPC_1.set_position(100, 93)
Player_1.set_position(10, 93)
pause(2000)
NPC_1.say("Hello adventurer")
pause(2000)
NPC_1.say("Come this way")
pause(1000)
NPC_1.set_image(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . f f f f 4 4 f . . . 
        . . . . f f b f 5 4 5 5 4 f . . 
        . . . f b 3 3 e 4 5 5 5 5 f . . 
        . . f b 3 3 3 3 e 4 4 4 e f . . 
        . . f 3 3 3 3 3 3 3 3 3 3 3 f . 
        . . f 3 3 3 3 e b 3 e e 3 3 f . 
        . . f 3 3 3 3 f f e e e 3 3 f . 
        . f f b b b b f b f e e e f . . 
        . f b b b b b e 1 f 4 4 e . . . 
        . f b b b b b f 4 4 4 4 f . . . 
        . . f b b b 4 4 e d d d f . . . 
        . . . f f f 4 4 e d d d f . . . 
        . . . f b b e e b b d d d f . . 
        . . . . f b d d 1 d 1 d b f . . 
        . . . . . f f f b b f f f . . .
"""))
for index in range(70):
    NPC_1.x += 1
    pause(25)
animation.run_image_animation(Player_1,
    [img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 2 2 2 f . . . 
                . . . . . e d d e 2 2 2 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e e e d d d f . . . 
                . . . . . f 4 d d e 4 e f . . . 
                . . . . . f e d d e 2 2 f . . . 
                . . . . f f f e e f 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """),
        img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 2 2 2 f . . . 
                . . . . . e d d e 2 2 2 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . 4 d d e 4 4 4 e f . . . 
                . . . . e d d e 2 2 2 2 f . . . 
                . . . . f e e f 4 4 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """)],
    200,
    True)