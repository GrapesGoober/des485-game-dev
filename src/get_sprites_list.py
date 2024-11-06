import pygame

def get_sprites_list(
        sheet: pygame.Surface, 
        tile_size: tuple[int, int]
    ) -> list[pygame.Surface]:
    """
    Returns a list of sprites from a single larger tile sprite sheet.
    This always set the colorkey to transparent alpha.
    
    Arguments: 
        - `sheet` pygame Surface object for the entire sprite sheet
        - `tile_size` the width and height for each sprite tile
    
    Return: a list of `Surface`, each with size of `tile_size`
    """

    img_width, img_height = sheet.get_size()
    tile_width, tile_height = tile_size
    
    sheet_width = img_width//tile_width
    sheet_height = img_height//tile_height

    return_list = []

    for y in range(sheet_height):
        for x in range(sheet_width):
            tile = pygame.Surface((tile_width, tile_height))
            tile.blit(sheet, (0, 0), (x*tile_width, y*tile_height, tile_width, tile_height))
            tile.set_colorkey((0,0,0,0), pygame.RLEACCEL)
            return_list.append(tile)
    return return_list
