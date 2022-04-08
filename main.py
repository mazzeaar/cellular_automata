import ca
import ui
import pygame
import numpy as np
import tkinter as tk

cellsize = 1
num_starting_cells = 2

root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
root.destroy()

pygame.init()

font = pygame.font.SysFont(None, HEIGHT//25)
UI = ui.ui(13, 13, WIDTH//8, HEIGHT//21)

def main(rule):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    saved = False
    paused = False

    # instantiate cellular automaton
    cellular = ca.CA(width=WIDTH, height=HEIGHT, 
                cell_size=cellsize, rule=rule,
                num_starting_cells=num_starting_cells)

    #pixels = pygame.surfarray.pixels2d(screen)
    pygame.display.set_caption("RULE: " + str(int(cellular.RULE, 2)))

    original_text = str(rule)
    text = str(rule)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'done'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return 'done'
                elif event.key == pygame.K_RETURN:
                    if text == '': return -1
                    return str(int(text) % 255) # rules only range from 0 to 255
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                elif event.key > 47 and event.key < 58:
                    text += str(event.key - 48)

        if paused:
            pygame.draw.rect(screen, (255, 0, 0), UI.get_coordinates())
            draw_text(text, screen)
            pygame.display.flip()

        if not paused:
            # print one line and update as long as the cellular-automata hasn't reached the bottom of the screen
            if not cellular.reached_end():
                draw_cells(cellular.row, screen, cellsize, cellular)
                cellular.increment_row_count()
                cellular.get_next_row()

            # when the bottom is reached display the rule again and save a screenshot
            elif not saved:
                draw_text(original_text, screen)
                pygame.image.save(screen, "./images/rule" + str(int(cellular.RULE, 2))
                                            + '_cellsize'+str(cellsize)
                                            + '_sources' + str(num_starting_cells)
                                            + ".png")
                saved = True

            # draw the box where the text is rendered
            pygame.draw.rect(screen, (200, 200, 200), UI.get_coordinates())

            draw_text(text, screen)

            # update the screen
            pygame.display.flip()

def draw_text(text, screen):
    text_surf = font.render('Rule: ' + text, True, (0, 0, 0))
    screen.blit(text_surf, (20,25,100,100))

# draw the cells on the screen
def draw_cells(row, screen, cellsize, cellular):
    for i in range(len(row)):
        if row[i] == 1:
            pygame.draw.rect(screen, (255, 255, 255), 
                            (i * cellsize, cellular.row_count * cellsize, 
                            cellsize, cellsize))

def run():
    rule_list = [18, 22, 30, 45, 60, 73, 75, 82, 86, 89, 101, 105, 110, 129,
                135, 149, 150, 153, 154, 161, 165, 169, 181, 182, 195, 225]
    rule = np.random.choice(rule_list)
    while True:
        rule = main(int(rule))
        if rule == -1 or rule == None:  rule = np.random.choice(rule_list)
        elif rule == 'done': break

if __name__ == "__main__":
    run()