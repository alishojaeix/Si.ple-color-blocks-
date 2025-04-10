import pygame
import random
import sys
from typing import List, Tuple, Optional

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 8
BLOCK_SIZE = 60
MARGIN = 10
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Purple
    (0, 255, 255),  # Cyan
]

class Block:
    def __init__(self, row: int, col: int, color: Tuple[int, int, int]):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calculate_position()
    
    def calculate_position(self):
        """Calculate screen position based on grid position"""
        self.x = MARGIN + self.col * (BLOCK_SIZE + MARGIN)
        self.y = MARGIN + self.row * (BLOCK_SIZE + MARGIN)
    
    def draw(self, screen: pygame.Surface):
        """Draw the block on the screen"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE), 2)

class ColorBlocksGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Color Blocks Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 36)
        self.score = 0
        self.grid: List[List[Optional[Block]]] = []
        self.selected_block: Optional[Block] = None
        self.initialize_grid()
    
    def initialize_grid(self):
        """Create a grid filled with random colored blocks"""
        self.grid = []
        for row in range(GRID_SIZE):
            grid_row = []
            for col in range(GRID_SIZE):
                color = random.choice(COLORS)
                grid_row.append(Block(row, col, color))
            self.grid.append(grid_row)
    
    def draw(self):
        """Draw all game elements"""
        self.screen.fill((240, 240, 240))
        
        # Draw grid background
        grid_width = GRID_SIZE * (BLOCK_SIZE + MARGIN) + MARGIN
        grid_height = GRID_SIZE * (BLOCK_SIZE + MARGIN) + MARGIN
        pygame.draw.rect(self.screen, (200, 200, 200), 
                        (MARGIN, MARGIN, grid_width, grid_height))
        
        # Draw all blocks
        for row in self.grid:
            for block in row:
                if block:
                    block.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (20, grid_height + 20))
        
        # Draw instructions
        instructions = self.font.render("Click adjacent blocks to swap colors", True, (0, 0, 0))
        self.screen.blit(instructions, (20, grid_height + 60))
        
        pygame.display.flip()
    
    def get_block_at_pos(self, pos: Tuple[int, int]) -> Optional[Block]:
        """Get block at mouse position"""
        x, y = pos
        for row in self.grid:
            for block in row:
                if block and block.x <= x <= block.x + BLOCK_SIZE and block.y <= y <= block.y + BLOCK_SIZE:
                    return block
        return None
    
    def are_adjacent(self, block1: Block, block2: Block) -> bool:
        """Check if two blocks are adjacent"""
        return ((abs(block1.row - block2.row) == 1 and block1.col == block2.col) or \
               ((abs(block1.col - block2.col) == 1 and block1.row == block2.row))
    
    def swap_blocks(self, block1: Block, block2: Block):
        """Swap two blocks in the grid"""
        # Swap grid positions
        self.grid[block1.row][block1.col], self.grid[block2.row][block2.col] = \
            self.grid[block2.row][block2.col], self.grid[block1.row][block1.col]
        
        # Swap row and col attributes
        block1.row, block2.row = block2.row, block1.row
        block1.col, block2.col = block2.col, block1.col
        
        # Recalculate their screen positions
        block1.calculate_position()
        block2.calculate_position()
        
        # Check for matches after swap
        matches = self.find_matches()
        if matches:
            self.remove_matches(matches)
            self.score += len(matches) * 10
        else:
            # No matches, swap back
            self.grid[block1.row][block1.col], self.grid[block2.row][block2.col] = \
                self.grid[block2.row][block2.col], self.grid[block1.row][block1.col]
            block1.row, block2.row = block2.row, block1.row
            block1.col, block2.col = block2.col, block1.col
            block1.calculate_position()
            block2.calculate_position()
    
    def find_matches(self) -> List[Block]:
        """Find all matching blocks (3 or more in a row/column)"""
        matches = set()
        
        # Check horizontal matches
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE - 2):
                if self.grid[row][col] and self.grid[row][col+1] and self.grid[row][col+2]:
                    if (self.grid[row][col].color == self.grid[row][col+1].color == 
                        self.grid[row][col+2].color):
                        matches.update([self.grid[row][col], self.grid[row][col+1], self.grid[row][col+2]])
        
        # Check vertical matches
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE - 2):
                if self.grid[row][col] and self.grid[row+1][col] and self.grid[row+2][col]:
                    if (self.grid[row][col].color == self.grid[row+1][col].color == 
                        self.grid[row+2][col].color):
                        matches.update([self.grid[row][col], self.grid[row+1][col], self.grid[row+2][col]])
        
        return list(matches)
    
    def remove_matches(self, matches: List[Block]):
        """Remove matched blocks and shift down"""
        # Mark matched blocks as None
        for block in matches:
            self.grid[block.row][block.col] = None
        
        # Shift blocks down
        for col in range(GRID_SIZE):
            empty_spots = []
            for row in range(GRID_SIZE-1, -1, -1):
                if self.grid[row][col] is None:
                    empty_spots.append(row)
                elif empty_spots:
                    # Move block down to the lowest empty spot
                    lowest_empty = empty_spots.pop(0)
                    self.grid[lowest_empty][col] = self.grid[row][col]
                    self.grid[row][col] = None
                    self.grid[lowest_empty][col].row = lowest_empty
                    self.grid[lowest_empty][col].calculate_position()
                    empty_spots.append(row)
        
        # Fill empty spots at top with new blocks
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                if self.grid[row][col] is None:
                    self.grid[row][col] = Block(row, col, random.choice(COLORS))
        
        # Check for new matches after filling
        new_matches = self.find_matches()
        if new_matches:
            self.remove_matches(new_matches)
            self.score += len(new_matches) * 10
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_block = self.get_block_at_pos(event.pos)
                    if clicked_block:
                        if self.selected_block is None:
                            self.selected_block = clicked_block
                        else:
                            if self.are_adjacent(self.selected_block, clicked_block):
                                self.swap_blocks(self.selected_block, clicked_block)
                            self.selected_block = None
            
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
