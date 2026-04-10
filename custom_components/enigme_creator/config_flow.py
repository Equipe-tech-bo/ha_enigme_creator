from homeassistant import config_entries
from .const import DOMAIN

class EnigmeCreatorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow minimal pour HACS."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        
        if user_input is not None:
            return self.async_create_entry(
                title="Enigme Creator",
                data={}
            )

        return self.async_show_form(step_id="user")
