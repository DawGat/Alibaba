import xml.etree.ElementTree as ElementTree
from switch_board import Switch
from time_ranges import TimeRange

# TODO Add validation for correctness of input data
# This function is reading configuration xml file and creating switches list based on it
def read_switches_config():
    switches = []
    config_file = ElementTree.parse('alibaba_config.xml')
    root = config_file.getroot()
    switches_el = root.find('switches')
    for switch_el in switches_el:
        name = switch_el.attrib['name']
        enable = switch_el.attrib['enable'].lower() == 'true'
        pin_nr = int(switch_el.find('pin_nr').text)
        switch = Switch(name, pin_nr, enable)
        switches.append(switch)
        if switch_el.find('switch_type') is not None:
            switch.switch_type = int(switch_el.find('switch_type').text)
        if switch_el.find('time_ranges') is not None:
            time_ranges_list = []
            for time_range in switch_el.findall('./time_ranges/time_range'):
                start_hour = int(time_range.find('start_hour').text)
                start_minute = int(time_range.find('start_minute').text)
                if time_range.find('start_sun_relation') is not None:
                    start_sun_relation = time_range.find('start_sun_relation').text
                else:
                    start_sun_relation = None
                end_hour = int(time_range.find('end_hour').text)
                end_minute = int(time_range.find('end_minute').text)
                if time_range.find('end_sun_relation') is not None:
                    end_sun_relation = time_range.find('end_sun_relation').text
                else:
                    end_sun_relation = None
                cur_time_range = TimeRange(start_hour, start_minute, end_hour, end_minute,
                                           start_sun_relation, end_sun_relation)
                time_ranges_list.append(cur_time_range)
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
