import os
import random

maps_cfg_path = 'Mods/ModWarfare'
maps_cfg_filename = 'maps.cfg'
maps_folder = "usermaps"
command = "gametype"
gametype = "koth map"
default_maps = ["mp_backlot", "mp_bloc", "mp_bog", "mp_carentan",
                "mp_cargoship", "mp_citystreets", "mp_convoy", "mp_countdown",
                "mp_crash", "mp_crash_snow", "mp_creek", "mp_crossfire",
                "mp_farm", "mp_killhouse", "mp_overgrown", "mp_pipeline",
                "mp_shipment", "mp_showdown", "mp_strike", "mp_vacant"]


def change_map_rotation(sv_map_rotation):
    maps_cfg_fullpath = f"{maps_cfg_path}/{maps_cfg_filename}"
    set_map_rotation = 'set sv_mapRotation'

    with open(maps_cfg_fullpath, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if set_map_rotation in line:
            lines[i] = f"{set_map_rotation} \"{sv_map_rotation}\"\n"

    with open(maps_cfg_fullpath, 'w') as file:
        file.writelines(lines)


def generate_command(server_maps):
    sliced_server_maps = server_maps[:20]
    command_maps = [f"{gametype} {map}" for map in sliced_server_maps]
    return f"{command} {' '.join(command_maps)}"


def generate_random_map():
    result = {'default': len(default_maps)}
    custom_maps = os.listdir(maps_folder)
    result['custom'] = len(custom_maps)
    server_maps = default_maps + custom_maps
    result['total'] = len(server_maps)
    random.shuffle(server_maps)
    sv_map_rotation = generate_command(server_maps)
    change_map_rotation(sv_map_rotation)
    return result
