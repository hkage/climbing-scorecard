import click
from click.exceptions import BadParameter
from PIL import Image, ImageDraw, ImageFont


BOXES_PER_ROW = 10
COLORS_PER_ROW = 3

font = ImageFont.truetype('fonts/RobotoMono-Regular.ttf', 14)


def draw_route_box(draw, base_x, base_y, label, points):
    """
    Render a single route.

    :param draw: The :class:`ImageDraw` instance
    :param int base_x: The base x coordinate for the box
    :param int base_y: The base y coordinate for the box
    :param str label: The name or label of the route
    :param int points: The points for the route
    """
    # Add the route label
    draw.rectangle(((base_x + 10, base_y + 30), (base_x + 40, base_y + 60)), fill='white', outline='black')
    draw.text((base_x + 17, base_y + 37), label, (0, 0, 0), font=font)
    # Add the points
    draw.rectangle(((base_x + 40, base_y + 30), (base_x + 70, base_y + 60)), fill='white', outline='black')
    draw.text((base_x + 51, base_y + 37), str(points), (0, 0, 0), font=font)
    # Two boxes for: route completed and route added to the online ranking
    draw.rectangle(((base_x + 10, base_y + 60), (base_x + 40, base_y + 90)), fill='white', outline='black')
    draw.rectangle(((base_x + 40, base_y + 60), (base_x + 70, base_y + 90)), fill='white', outline='black')


def validate_routes(ctx, param, value):
    """
    Validate the route options.

    :param ctx: click Context
    :param param: click option
    :param value: The value to validate, in this case the route tuples.
    :raise BadParameter: If the validation fails.
    """
    if not value:
        raise BadParameter("Define at least one route.")
    for name, points in value:
        if points > 9 or points < 1:
            raise BadParameter("Route points must be 1-9, not {}.".format(points))
        if len(name) > 3:
            raise BadParameter("Route names have to consist of 1-3 characters, not {}.".format(len(name)))
    return value


@click.command()
@click.option('--route', '-r', type=(unicode, int), multiple=True,
              callback=validate_routes,
              help="One or many route definitions, defined as tuples, e.g. -r RT 3 -r BU 4")
@click.option('--start-number', default=1, help="Starting range for route numbers.")
@click.option('--end-number', default=100, help="End range for route numbers.")
@click.option('--outfile', '-o', default='scorecard.png', help="Name of the output file")
def render(route, start_number, end_number, outfile):
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
        route_x = x1 + 5
        route_y = y1 + 5
        for no_color, data in enumerate(route):
            name, points = data
            draw_route_box(draw, route_x, route_y, name, points)
            if (no_color + 1) % COLORS_PER_ROW == 0:
                route_x = x1 + 5
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
    # Save the file
    img.save(outfile)


if __name__ == '__main__':
    render()
