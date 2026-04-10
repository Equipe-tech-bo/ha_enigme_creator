DOMAIN = "enigme_creator"

# Template des 10 entités à créer pour chaque énigme
# {prefix} sera remplacé par le préfixe de l'énigme (ex: SM)
# {prefix_lower} sera remplacé par le préfixe en minuscules (ex: sm)
# {name} sera remplacé par le nom complet (ex: Socle Magie)

ENTITY_TEMPLATES = [
    {
        "platform": "input_select",
        "id_suffix": "action",
        "label_suffix": "Action",
        "config": {
            "options": ["DISABLE", "ENABLE", "UNTOUCHED", "STARTED", "SOLVED"],
            "initial": "DISABLE",
            "icon": "mdi:list-status"
        }
    },
    {
        "platform": "input_text",
        "id_suffix": "final_time",
        "label_suffix": "Final_Time",
        "config": {
            "initial": "",
            "max": 20,
            "icon": "mdi:flag-checkered"
        }
    },
    {
        "platform": "input_text",
        "id_suffix": "global_time",
        "label_suffix": "Global_Time",
        "config": {
            "initial": "",
            "max": 20,
            "icon": "mdi:timer-outline"
        }
    },
    {
        "platform": "input_button",
        "id_suffix": "reset",
        "label_suffix": "Reset",
        "config": {
            "icon": "mdi:restart"
        }
    },
    {
        "platform": "input_boolean",
        "id_suffix": "show_details",
        "label_suffix": "Show_Details",
        "config": {
            "initial": False,
            "icon": "mdi:eye"
        }
    },
    {
        "platform": "input_datetime",
        "id_suffix": "start_time",
        "label_suffix": "Start_Time",
        "config": {
            "has_date": False,
            "has_time": True,
            "icon": "mdi:clock-start"
        }
    },
    {
        "platform": "input_text",
        "id_suffix": "state",
        "label_suffix": "State",
        "config": {
            "initial": "FERMETURE",
            "max": 20,
            "icon": "mdi:state-machine"
        }
    },
    {
        "platform": "input_text",
        "id_suffix": "status",
        "label_suffix": "Status",
        "config": {
            "initial": "DISABLE",
            "max": 20,
            "icon": "mdi:list-status"
        }
    },
    {
        "platform": "input_number",
        "id_suffix": "timer_atstart",
        "label_suffix": "Timer_AtStart",
        "config": {
            "initial": 0,
            "min": 0,
            "max": 3600,
            "step": 1,
            "unit_of_measurement": "s",
            "icon": "mdi:timer-sand"
        }
    },
    {
        "platform": "input_boolean",
        "id_suffix": "valide",
        "label_suffix": "Valide",
        "config": {
            "initial": False,
            "icon": "mdi:check-circle"
        }
    },
]
