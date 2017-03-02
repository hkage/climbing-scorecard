import click
from PIL import Image, ImageDraw, ImageFont


ROUTE_COLORS = (
    ('OE', 1),
    ('GB', 1),
    ('GN', 2),
    ('RT', 3),
    ('BL', 4),
    ('GN', 5),
    ('SZ', 6),
    ('PK', 3))


def draw_route_box(draw, base_x, base_y, label, points):
    pass


@click.command()
@click.option('--start-number', default=1, help="First route number")
@click.option('--end-number', default=100, help="last route number")
def render(start_number, end_number):
    font = ImageFont.truetype('Hack-Regular.ttf', 14)
    img = Image.new('RGBA', (2501, 2501), (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    x1, y1 = 0, 0
    x2, y2 = 250, 250
    for x in range(start_number, end_number):

        # Draw the outline per route
        draw.rectangle(((x1, y1), (x2, y2)), fill='lightgrey', outline='black')

        # Draw the inner boxes
        draw.rectangle(((x1 + 10, y1 + 30), (x1 + 40, y1 + 60)), fill='white', outline='black')
        draw.text((x1 + 17, y1 + 37), "OE", (0, 0, 0), font=font)

        draw.rectangle(((x1 + 40, y1 + 30), (x1 + 70, y1 + 60)), fill='white', outline='black')

        draw.rectangle(((x1 + 10, y1 + 60), (x1 + 40, y1 + 90)), fill='white', outline='black')
        draw.rectangle(((x1 + 40, y1 + 60), (x1 + 70, y1 + 90)), fill='white', outline='black')

        # Add the route number as a text
        draw.text((x1 + 10, y1 + 10), str(x), (0, 0, 0), font=font)

        x1 += 250
        x2 += 250
    img.save('scorecard.png')


if __name__ == '__main__':
    render()


"""
0     0       250     250
250   0       500     250
500   0       750     250
"""
