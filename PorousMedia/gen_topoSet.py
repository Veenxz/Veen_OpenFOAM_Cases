# -*- coding: utf-8 -*-

# Libraries

# -------------------------------------- #
#         Function definitions           #
# -------------------------------------- #


def headerLines(cl, loc, obj):
    h = [
        "/*--------------------------------*- C++ -*----------------------------------*|",
        "| =========                 |                                                 |",
        "| \\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |",
        "|  \\\    /   O peration     | Website:  https://openfoam.org                  |",
        "|   \\\  /    A nd           | Version:  8                                     |",
        "|    \\\/     M anipulation  |                                                 |",
        "\*---------------------------------------------------------------------------*/",
        "FoamFile", "{", "    version     2.0;", "    format      ascii;",
        "    class       {};", '    location    "{}";', "    object      {};",
        "}",
        "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //",
        ""
    ]

    h[11] = h[11].format(cl)
    h[12] = h[12].format(loc)
    h[13] = h[13].format(obj)
    return h


# -------------------------------------- #
#           Define  poperties            #
# -------------------------------------- #

# [xmin ymin zmin xmax ymax zmax]
mesh_box = [-0.4, -0.4, -0.4, 0.4, 0.4, 0.4]
# region hight
deltax = 0.02
# region size
n = 2
# region name
name = 'porous'

bl = '    '
loc = "system"
cl = "dictionary"
obj = "topoSetDict"

# system/topoSetDict
f = open(loc + '/' + obj, "w")

header = headerLines(cl, loc, obj)
for l in range(len(header)):
    f.write("{}\n".format(header[l]))

print(
    'actions\n(\n'+bl+'{\n',
    2*bl+'name    '+name+';\n',
    2*bl+'type    cellZoneSet;\n',
    2*bl+'action  new;\n',
    2*bl+'source  boxToCell;\n',
    2*bl+'sourceInfo\n'+2*bl+'{\n',
    3*bl+'box ('+"%.2f" % mesh_box[0]+' '+"%.2f" % (-deltax*n)+' '+"%.2f" % mesh_box[2]+') ',
    '('+"%.2f" % mesh_box[3]+' '+"%.2f" % (deltax*n)+' '+"%.2f" % mesh_box[5]+');\n'+2*bl+'}\n',
    bl+'}\n'+');',
    sep='',file=f)

# footer
f.write(
    '// ************************************************************************* //'
)

f.close()

print(obj + ' Generation Finshed!')