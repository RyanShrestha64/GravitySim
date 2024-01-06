import pygame, sys
from src.force import force
from src.object import Obj
pygame.font.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 300
linear_factor = 500000
FONT = pygame.font.SysFont("monospace", 20)

clock = pygame.time.Clock()

scale = 2806000000 / 5
WIDTH_TOT, HEIGHT_TOT = scale * WIDTH, scale * HEIGHT
# scale = 696000000
sun1 = Obj(WIDTH_TOT / 2, HEIGHT_TOT/ 2, 30, int(1.9891 * (10 ** 30)), 20000, 000, (255, 255, 255), 0, 0, 0, "Sun1")
sun2 = Obj(WIDTH_TOT / 4, HEIGHT_TOT / 4, 20, int(1.9891 * (10 ** 30)), 200000, 3000, (255, 255, 255), 0, 0, 0, "Sun2")
omar = Obj(WIDTH_TOT/3, HEIGHT_TOT/2, 2, 10**31, 0, 0, (54,34,53), 0, 0, 0, "Greg", False)
sun3 = Obj(WIDTH_TOT / 6, HEIGHT_TOT/ 6, 20, int(1.9891 * (10 ** 30)), -20000, -1000, (255, 255, 255), 0, 0, 0, "Sun3")
sun4 = Obj(WIDTH_TOT / 7, HEIGHT_TOT/ 7, 20, int(1.9891 * (10 ** 30)), 0, 0, (255, 255, 255), 0, 0, 0, "Sun4")
earth = Obj(round(sun1.x + 152000000000), round(sun1.y + 0), 5, int(5.97219 * (10 ** 24)), 0 + sun1.v_x, 29290 + sun1.v_y, (128, 154, 240), 0, 0, 0, "Earth")
mars = Obj(round(sun1.x + 228000000000), round(sun1.y + 0), 12, int(6.41693 * (10 ** 23)), 0 + sun1.v_x, 24080 + sun1.v_y, (236, 47, 85), 0, 0, 0, "Mars")
venus = Obj(round(sun1.x + 108000000000), round(sun1.y + 0), 10, int(4.86732 * (10 ** 24)), 0 + sun1.v_x, 35020 + sun1.v_y, (255, 255, 255), 0, 0, 0, "Venus")
mercury = Obj(round(sun1.x + 58000000000), round(sun1.y + 0), 8, int(3.285 * (10 ** 23)), 0 + sun1.v_x, 47000 + sun1.v_y, (141, 124, 128), 0, 0, 0, "Mercury")
jupiter = Obj(round(sun1.x + 778000000000), round(sun1.y + 0), 10, int(1.89813 * (10 ** 27)), 0 + sun1.v_x, 13060 + sun1.v_y, (150, 159, 113), 0, 0, 0, "Jupiter")
saturn = Obj(round(sun1.x + 1400000000000), round(sun1.y + 0), 10, int(5.683 * (10 ** 26)), 0 + sun1.v_x, 9670 + sun1.v_y, (181, 69, 69), 0, 0, 0, "Saturn")
uranus = Obj(round(sun1.x + 2900000000000), round(sun1.y + 0), 10, int(8.681 * (10 ** 25)), 0 + sun1.v_x, 6810 + sun1.v_y, (141, 124, 128), 0, 0, 0, "Uranus")
neptune = Obj(round(sun1.x + 4500000000000), round(sun1.y + 0), 10, int(1.024 * (10 ** 26)), 0 + sun1.v_x, 5450 + sun1.v_y, (10, 10, 250), 0, 0, 0, "Neptune")
moon = Obj(round(earth.x + (earth.radius * scale) + 3840000000), round(earth.y + 0), 3, int(7.34767309 * (10 ** 22)), 0 + earth.v_x, 1022 + earth.v_y, (150, 150, 150), 0, 0, 0, "The Moon")
# comet = Obj(400, 2139200000000, 3, int(1.285 * (10 ** 23)), 0, -10000, (255, 255, 255), 0, 0, 0, "Comet")

# earth = Obj(round(sun1.x + 149000000000), round(sun1.y + 0), 16, int(5.97219 * (10 ** 24)), 0 + sun1.v_x, 0 + sun1.v_y, (128, 154, 240), 0, 0, 0, "Earth")
# mars = Obj(round(sun1.x + 228000000000), round(sun1.y + 0), 12, int(6.41693 * (10 ** 23)), 0 + sun1.v_x, 0 + sun1.v_y, (236, 47, 85), 0, 0, 0, "Mars")
# venus = Obj(round(sun1.x + 108000000000), round(sun1.y + 0), 14, int(4.86732 * (10 ** 24)), 0 + sun1.v_x, 0 + sun1.v_y, (255, 255, 255), 0, 0, 0, "Venus")
# mercury = Obj(round(sun1.x + 58000000000), round(sun1.y + 0), 8, int(3.285 * (10 ** 23)), 0 + sun1.v_x, 0 + sun1.v_y, (141, 124, 128), 0, 0, 0, "Mercury")
# jupiter = Obj(round(sun1.x + 778000000000), round(sun1.y + 0), 10, int(1.89813 * (10 ** 27)), 0 + sun1.v_x, 0 + sun1.v_y, (150, 159, 113), 0, 0, 0, "Jupiter")
# saturn = Obj(round(sun1.x + 1400000000000), round(sun1.y + 0), 10, int(5.683 * (10 ** 26)), 0 + sun1.v_x, 0 + sun1.v_y, (181, 69, 69), 0, 0, 0, "Saturn")
# uranus = Obj(round(sun1.x + 2900000000000), round(sun1.y + 0), 10, int(8.681 * (10 ** 25)), 0 + sun1.v_x, 0 + sun1.v_y, (141, 124, 128), 0, 0, 0, "Uranus")
# neptune = Obj(round(sun1.x + 4500000000000), round(sun1.y + 0), 10, int(1.024 * (10 ** 26)), 0 + sun1.v_x, 0 + sun1.v_y, (10, 10, 250), 0, 0, 0, "Neptune")
# moon = Obj(round(earth.x + (earth.radius * scale) + 384000000), round(earth.y + 0), 3, int(7.34767309 * (10 ** 22)), 0 + earth.v_x, 1022 + earth.v_y, (150, 150, 150), 0, 0, 0, "The Moon")

star_list = []
obj_list = [sun1, mercury, venus, earth, mars]

focus = 0
def main():
    count = 0
    run = True
    while run:
        count += 1
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                try:
                    if int(event.unicode) < len(obj_list):
                        focus = int(event.unicode)
                except:
                    pass
        for i in range(len(obj_list)):
            obj_list[i].force_x = 0
            obj_list[i].force_y = 0
            for j in range(len(obj_list)):
                if j != i:
                    da = force(obj_list[i].x, obj_list[i].y, obj_list[i].mass, obj_list[j].x, obj_list[j].y, obj_list[j].mass)
                    obj_list[i].v_x += round(da[0] * linear_factor / FPS, ndigits=10)
                    obj_list[i].v_y -= round(da[1] * linear_factor / FPS, ndigits=10)
                    obj_list[i].force_x += da[3]
                    obj_list[i].force_y += da[4]

                obj_list[i].force = round(((obj_list[i].force_x ** 2) + (obj_list[i].force_y ** 2)) ** 0.5, ndigits=8)

        for i in range(len(obj_list)):
            if obj_list[i].x / scale + obj_list[i].radius > WIDTH:
                obj_list[i].v_x = -1 * obj_list[i].v_x
            if obj_list[i].x / scale - obj_list[i].radius < 0:
                obj_list[i].v_x = -1 * obj_list[i].v_x
            if obj_list[i].y / scale + obj_list[i].radius > HEIGHT:
                obj_list[i].v_y = -1 * obj_list[i].v_y
            if obj_list[i].y / scale - obj_list[i].radius < 0:
                obj_list[i].v_y = -1 * obj_list[i].v_y
            if obj_list[i].movable:
                obj_list[i].x += (obj_list[i].v_x * linear_factor / FPS)
                obj_list[i].y += (obj_list[i].v_y * linear_factor / FPS)
        # if sun1.x / scale + sun1.radius > WIDTH:
        #     temp_v_change = -2 * sun1.v_x
        #     for j in range(len(obj_list)):
        #          obj_list[j].v_x += temp_v_change
        # if sun1.x / scale - sun1.radius < 0:
        #     temp_v_change = -2 * sun1.v_x
        #     for j in range(len(obj_list)):
        #          obj_list[j].v_x += temp_v_change
        # if sun1.y / scale + sun1.radius > HEIGHT:
        #     temp_v_change = -2 * sun1.v_y
        #     for j in range(len(obj_list)):
        #          obj_list[j].v_y += temp_v_change
        # if sun1.y / scale - sun1.radius < 0:
        #     temp_v_change = -2 * sun1.v_y
        #     for j in range(len(obj_list)):
        #          obj_list[j].v_y += temp_v_change
        
        WIN.fill((0, 0, 0))

        for i in range(len(obj_list)):
            if obj_list[i].x > 0 and obj_list[i].y > 0:
                pygame.draw.circle(WIN, obj_list[i].color, (obj_list[i].x / scale, obj_list[i].y / scale), obj_list[i].radius)
        try:
            if count % 30 == 0:
                count = 0
                focus_planet = str(obj_list[focus].name)
                planet_text = FONT.render(focus_planet, 1, (255, 255, 255))
                focus_force = str(round(obj_list[focus].force, ndigits=8))
                force_text = FONT.render("Magnitude of Force: " + focus_force + " N", 1, (255, 255, 255))
                focus_acceleration = str(round((round(obj_list[focus].force, ndigits=8) / (obj_list[focus].mass)), ndigits=8))
                acceleration_text = FONT.render("Magnitude of Acceleration: " + focus_acceleration + " m/s^2", 1, (255, 255, 255))
                speed = str(round(((((obj_list[focus].v_x ** 2) + (obj_list[focus].v_y ** 2)) ** 0.5) / 1000), ndigits=4))
                text_speed = FONT.render("Speed: " + speed + " km/s", 1, (255, 255, 255))
                distance = str(round((((((sun1.x - obj_list[focus].x) ** 2) + (sun1.y - obj_list[focus].y) ** 2) ** 0.5)/1000), ndigits=8))
                text_distance = FONT.render("Distance from Sun: " + distance + " km", 1, (255, 255, 255))

            WIN.blit(text_speed, (10, 660))
            WIN.blit(planet_text, (10, 630))
            WIN.blit(force_text, (10, 690))
            WIN.blit(acceleration_text, (10,720))
            WIN.blit(text_distance, (10, 750))
        except:
            pass
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
