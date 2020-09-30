import xml.etree.ElementTree as ElementTree
from switch_board import Switch
import datetime

# time_range_switch3 = [{"start": datetime.time(0, 0, 0), "end": datetime.time(0, 15, 0)},
#                       {"start": datetime.time(14, 0, 0), "end": datetime.time(16, 0, 0)},
#                       {"start": datetime.time(0, 30, 0), "end": datetime.time(1, 51, 0)}]
# switches = [Switch("Garaż", 10, True, switch_types["impulse_switch"]),
#             Switch("Lampy chodnik", 12, True, switch_types["time_switch"], time_range_switch3),
#             Switch("Taras", 16, True, switch_types["normal_switch"]),
#             Switch("Wolny", 18, False, switch_types["not_defined"])]


# This function is reading configuration xml file and creating switches list based on it
def read_switches_config():
    switches = []
    config_file = ElementTree.parse('alibaba_config.xml')
    root = config_file.getroot()
    switches_el = root.find('switches')
    for switch_el in switches_el:
        name = switch_el.attrib['name']
        enable = switch_el.attrib['enable'].lower() == 'true'
        pin_nr = switch_el.find('pin_nr').text
        switch = Switch(name, pin_nr, enable)
        switches.append(switch)
        if switch_el.find('switch_type') is not None:
            switch.switch_type = int(switch_el.find('switch_type').text)
        if switch_el.find('time_ranges') is not None:
            time_ranges_list = []
            for time_range in switch_el.findall('./time_ranges/time_range'):
                start_str = time_range.find('start').text + ':00'
                end_str = time_range.find('end').text + ':00'
                start = datetime.time.fromisoformat(start_str)
                end = datetime.time.fromisoformat(end_str)
                time_range_dict = {
                    'start': start,
                    'end': end
                }
                time_ranges_list.append(time_range_dict)
            switch.time_ranges = time_ranges_list
    return switches


# This function is reading configuration xml file and returning position
def read_position_config():
    config_file = ElementTree.parse('alibaba_config.xml')
    root = config_file.getroot()
    latitude = float(root.find('./position/latitude').text)
    longitude = float(root.find('./position/longitude').text)
    position = {
        'latitude': latitude,
        'longitude': longitude
    }
    return position
