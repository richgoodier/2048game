import random
import copy
import pygame
import sys

# Let's user play the game 2048

# Initialize Pygame
pygame.init()

# Set up some constants
WINDOW_SIZE = 500
GRID_SIZE = 4
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

def main():
    print("Welcome to 2048.  Use the arrow keys to play.")
    game = Game2048()
    game.play()
    

class Game2048:
    def __init__(self):
        self.board = [["-" for _ in range(4)] for _ in range(4)]
        self.add_number_to_board()
        self.turn = 1
        
    def play(self):
        
        while True:
            self.draw_board()
            pygame.display.update()
            #print(f"Turn: {self.turn}")
            
            # Check lose state
            if self.check_lose_state():
                print("You lose!")
                break
            
            direction = self.listen_for_move()
            
            # Calculate new board
            try:
                calculated_board = self.calculate_board(direction)
            except Exception as e:
                print(f"Error: {e}")
            # Ensure the move is legal
            if self.board != calculated_board:
                self.board = calculated_board
                
                # Add a new number to the board
                self.add_number_to_board()
                
                # Uptate turn
                self.turn += 1
            
            # Check win state
            if self.check_win_state():
                self.draw_board()
                print("You win!")
                break

    def listen_for_move(self):
        # Capture user input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Check for keydown events
                if event.type == pygame.KEYDOWN:
                    # Check which key was pressed
                    if event.key == pygame.K_LEFT:
                        return "l"
                    elif event.key == pygame.K_RIGHT:
                        return "r"
                    elif event.key == pygame.K_UP:
                        return "u"
                    elif event.key == pygame.K_DOWN:
                        return "d"

    def calculate_board(self, direction):
        new_board = copy.deepcopy(self.board)
        
        if direction == "r":
            # Shift tiles
            for _ in range(3):
                for column in range(3, 0, -1):
                    for row in range(4):
                        if (new_board[row][column] == '-') and (new_board[row][column - 1] != '-'):
                            new_board[row][column] = new_board[row][column - 1]
                            new_board[row][column - 1] = '-'
                        
            # Combine tiles
            for column in range(3, 0, -1):
                for row in range(4):
                    if (new_board[row][column] != '-') and (new_board[row][column] == new_board[row][column - 1]):
                        new_board[row][column] = 2 * new_board[row][column]
                        new_board[row][column - 1] = '-'
            
            # Shift tiles
            for column in range(3, 0, -1):
                for row in range(4):
                    if (new_board[row][column] == '-') and (new_board[row][column - 1] != '-'):
                        new_board[row][column] = new_board[row][column - 1]
                        new_board[row][column -1] = '-'
            
            return new_board
        
        elif direction == "l":
            # Shift tiles
            for _ in range(3):
                for column in range(3):
                    for row in range(4):
                        if (new_board[row][column] == '-') and (new_board[row][column + 1] != '-'):
                            new_board[row][column] = new_board[row][column + 1]
                            new_board[row][column + 1] = '-'
                        
            # Combine tiles
            for column in range(3):
                for row in range(4):
                    if (new_board[row][column] != '-') and (new_board[row][column] == new_board[row][column + 1]):
                        new_board[row][column] = 2 * new_board[row][column]
                        new_board[row][column + 1] = '-'
            
            # Shift tiles
            for column in range(3):
                for row in range(4):
                    if (new_board[row][column] == '-') and (new_board[row][column + 1] != '-'):
                        new_board[row][column] = new_board[row][column + 1]
                        new_board[row][column + 1] = '-'
            
            return new_board
        
        elif direction == "u":
            # Shift tiles
            for _ in range(3):
                for row in range(3):
                    for column in range(4):
                        if (new_board[row][column] == '-') and (new_board[row + 1][column] != '-'):
                            new_board[row][column] = new_board[row + 1][column]
                            new_board[row + 1][column] = '-'
            
            # Combine tiles
            for row in range(3):
                for column in range(4):
                    if (new_board[row][column] != '-') and (new_board[row][column] == new_board[row + 1][column]):
                        new_board[row][column] = 2 * new_board[row][column]
                        new_board[row + 1][column] = '-'
            
            # Shift tiles
            for row in range(3):
                for column in range(4):
                    if (new_board[row][column] == '-') and (new_board[row + 1][column] != '-'):
                        new_board[row][column] = new_board[row + 1][column]
                        new_board[row + 1][column] = '-'
            
            return new_board

        elif direction == "d":
            # Shift tiles
            for _ in range(3):
                for row in range(3, 0, -1):
                    for column in range(4):
                        if (new_board[row][column] == '-') and (new_board[row - 1][column] != '-'):
                            new_board[row][column] = new_board[row - 1][column]
                            new_board[row - 1][column] = '-'
            
            # Combine tiles
            for row in range(3, 0, -1):
                for column in range(4):
                    if (new_board[row][column] != '-') and (new_board[row][column] == new_board[row - 1][column]):
                        new_board[row][column] = 2 * new_board[row][column]
                        new_board[row - 1][column] = '-'
            
            # Shift tiles
            for row in range(3, 0, -1):
                for column in range(4):
                    if (new_board[row][column] == '-') and (new_board[row - 1][column] != '-'):
                        new_board[row][column] = new_board[row - 1][column]
                        new_board[row - 1][column] = '-'
            
            return new_board

        else:
            print("Error: calculate_board function failed.")
            return 

    def add_number_to_board(self):
        empty_spots = []
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] == '-':
                    empty_spots.append((i,j))
        if not empty_spots:
            print("Error: All spaces filled")
        
        while True:
            if random.randint(0, 9) > 0:
                two_or_four = 2
            else:
                two_or_four = 4
            
            spot = random.choice(empty_spots)
            i = spot[0]
            j = spot[1]
            
            if self.board[i][j] == "-":
                self.board[i][j] = two_or_four
                break
            else:
                print("Error adding number to space.")

    def draw_board(self):
        window.fill(BLACK) # Reset the board before redrawing
        
        font = pygame.font.Font(None, 50)  # Choose the font for the text, None means the default font

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                cell_value = self.board[i][j]
                if cell_value != "-":
                    text = font.render(str(cell_value), True, WHITE, BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2)
                    window.blit(text, text_rect)

                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, WHITE, rect, 1)

    def check_win_state(self):
        for row in self.board:
            if 128 in row:
                return True
        return False

    def check_lose_state(self):
        for direction in ["u", "d", "l", "r"]:
            new_board = self.calculate_board(direction)
            for row in new_board:
                if "-" in row:
                    return False
        return True

if __name__ == "__main__":
    main()