import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('images/house.png')
monika_image = pyglet.image.load('images/monika.png')
monika = pyglet.sprite.Sprite(monika_image)

image.width = 1000
image.height = 550
# monika.height = 500
# monika.width = 300
monika.x = 700
monika.y = -200
monika.scale = 0.5


try:
    background_msc = pyglet.media.load('background_music/bg1.mp3')
    player = pyglet.media.Player()
    player.queue(background_msc)
    player.play()
except pyglet.media.MediaDecodeException as e:
    print(f"Error loading audio: {e}")


player = pyglet.media.Player()

player.queue(background_msc)
player.play()

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
  
    monika.draw()
    
@window.event
def on_close():
    player.delete()  # Stops and cleans up the player
    pyglet.app.exit()  # Exit the pyglet application


pyglet.app.run()
