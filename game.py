import pygame

WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

backgroud_color = (63, 63, 63)
black = (0 ,0 ,0)
level = 3

FPS = 60




def draw_window():
    WIN.fill(backgroud_color)

    #Plane drawing
    plane_size = 600
    borderline_thickness = 11
    innerline_thickness = borderline_thickness - (borderline_thickness/3) *2

    def horizontal_line(x,y,thickness):return (x,y,plane_size,thickness)
    def vertical_line(x,y,thickness): return (x,y,thickness,plane_size)
    step = (plane_size - borderline_thickness) / level

    for l in range(level):

        #box
        for b in range(level-1):
            pygame.draw.rect(WIN, black, horizontal_line(0,(l * step)+borderline_thickness - innerline_thickness + (b+1)*((step-borderline_thickness-(innerline_thickness*(level-1)))/level+ innerline_thickness), innerline_thickness))
            pygame.draw.rect(WIN, black, vertical_line((l * step)+borderline_thickness - innerline_thickness + (b+1)*((step-borderline_thickness-(innerline_thickness*(level-1)))/level+ innerline_thickness),0, innerline_thickness))


        pygame.draw.rect(WIN, black, horizontal_line(0, l * step, borderline_thickness))
        pygame.draw.rect(WIN, black, vertical_line(l * step, 0, borderline_thickness))

    pygame.draw.rect(WIN, black, horizontal_line(0, level * step, borderline_thickness)) 
    pygame.draw.rect(WIN, black, vertical_line(level * step, 0, borderline_thickness))





    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()




if __name__ == "__main__":
    main()