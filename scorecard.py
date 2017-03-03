import click
from PIL import Image, ImageDraw, ImageFont


ROUTE_COLORS = (
    ('OE', 1),
    ('GB', 1),
    ('GN', 2),
    ('RT', 3),
    ('BL', 4),
    ('GU', 5),
    ('SZ', 6),
    ('PK', 3))

BOXES_PER_ROW = 10
COLORS_PER_ROW = 3

font = ImageFont.truetype('Hack-Regular.ttf', 14)


def draw_route_box(draw, base_x, base_y, label, points):
    # Add the route label
    draw.rectangle(((base_x + 10, base_y + 30), (base_x + 40, base_y + 60)), fill='white', outline='black')
    draw.text((base_x + 17, base_y + 37), label, (0, 0, 0), font=font)
    # Add the points
    draw.rectangle(((base_x + 40, base_y + 30), (base_x + 70, base_y + 60)), fill='white', outline='black')
    draw.text((base_x + 51, base_y + 37), str(points), (0, 0, 0), font=font)
    # Two boxes for: route completed and route added to the online ranking
    draw.rectangle(((base_x + 10, base_y + 60), (base_x + 40, base_y + 90)), fill='white', outline='black')
    draw.rectangle(((base_x + 40, base_y + 60), (base_x + 70, base_y + 90)), fill='white', outline='black')


@click.command()
@click.option('--start-number', default=1, help="First route number")
@click.option('--end-number', default=100, help="last route number")
@click.option('--outfile', '-o', default='scorecard.png', help="Name of the output file")
def render(start_number, end_number, outfile):

    img = Image.new('RGBA', (2501, 2501), (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    row = 1
    x1, y1 = 0, 0
    x2, y2 = 250, 250
    for x in range(start_number, end_number + 1):

        # Draw the outline per route
        draw.rectangle(((x1, y1), (x2, y2)), fill='lightgrey', outline='black')
        # Add the route number as a text
        draw.text((x1 + 10, y1 + 10), str(x), (0, 0, 0), font=font)

        # Draw the inner boxes
        color_row = 1
        route_x = x1
        route_y = y1

        for no_color, data in enumerate(ROUTE_COLORS):
            name, points = data

            draw_route_box(draw, route_x, route_y, name, points)
            if (no_color + 1) % COLORS_PER_ROW == 0:
                color_row += 1
                route_x = x1
                route_y += 70
            else:
                route_x += 70

        if x % BOXES_PER_ROW == 0:
            row += 1
            x1 = 0
            x2 = 250
            y1 = (row - 1) * 250
            y2 = row * 250
        else:
            x1 += 250
            x2 += 250

    img.save(outfile)


if __name__ == '__main__':
    render()
