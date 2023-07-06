import pygame
import time

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
LIGHT_BLUE = (51, 153, 255)
DARK_BLUE = (0, 0, 128)
GRAY = (200, 200, 200)
RED = (255, 51, 51)

pygame.font.init()


def is_button_clicked(position, button_rect):
    x, y = position
    x1, y1, width, height = button_rect
    return x1 <= x <= x1 + width and y1 <= y <= y1 + height


def draw_rounded_rect(surface, rect, color, corner_radius):
    pygame.draw.rect(surface, color, rect.inflate(-2 * corner_radius, 0))
    pygame.draw.rect(surface, color, rect.inflate(0, -2 * corner_radius))

    pygame.draw.circle(surface, color, rect.topleft, corner_radius)
    pygame.draw.circle(surface, color, rect.topright, corner_radius)
    pygame.draw.circle(surface, color, rect.bottomleft, corner_radius)
    pygame.draw.circle(surface, color, rect.bottomright, corner_radius)


def display_sudoku(initial, solution):
    # Set up display
    pygame.display.set_caption("Sudoku Solver")
    screen = pygame.display.set_mode((500, 550))

    font = pygame.font.Font(None, 40)
    button_font = pygame.font.Font(None, 30)

    running = True
    solved = False

    while running:
        # Draw the grid
        screen.fill(GRAY)
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 450, 450))

        for i in range(10):
            thickness = 5 if i % 3 == 0 else 1
            pygame.draw.line(screen, BLACK, (50 * i, 0), (50 * i, 450), thickness)  # vertical lines
            pygame.draw.line(screen, BLACK, (0, 50 * i), (450, 50 * i), thickness)  # horizontal lines

        # Fill in the grid with numbers
        for i in range(9):
            for j in range(9):
                if initial[i][j] != 0:
                    text = font.render(str(initial[i][j]), True, DARK_BLUE)
                    screen.blit(text, (j * 50 + 20, i * 50 + 15))
                elif solved:
                    text = font.render(str(solution[i][j]), True, GREEN)
                    screen.blit(text, (j * 50 + 20, i * 50 + 15))

        # Draw the solve button
        solve_button_rect = pygame.Rect(100, 470, 100, 50)
        draw_rounded_rect(screen, solve_button_rect, LIGHT_BLUE if not is_button_clicked(pygame.mouse.get_pos(), solve_button_rect) else RED, 10)
        solve_button_text = button_font.render("Solve", True, WHITE)
        text_rect = solve_button_text.get_rect(center=solve_button_rect.center)
        screen.blit(solve_button_text, text_rect)

        # Draw the reset button
        reset_button_rect = pygame.Rect(300, 470, 100, 50)
        draw_rounded_rect(screen, reset_button_rect, LIGHT_BLUE if not is_button_clicked(pygame.mouse.get_pos(), reset_button_rect) else RED, 10)
        reset_button_text = button_font.render("Reset", True, WHITE)
        text_rect = reset_button_text.get_rect(center=reset_button_rect.center)
        screen.blit(reset_button_text, text_rect)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_button_clicked(pygame.mouse.get_pos(), solve_button_rect):
                    solved = True
                if is_button_clicked(pygame.mouse.get_pos(), reset_button_rect):
                    solved = False

        # Update display
        pygame.display.update()
        time.sleep(0.1)

    # Close the Pygame window
    pygame.quit()


if __name__ == "__main__":
    # Sample initial and solution grids
    initial = [[0 for _ in range(9)] for _ in range(9)]
    solution = [[0 for _ in range(9)] for _ in range(9)]

    display_sudoku(initial, solution)
