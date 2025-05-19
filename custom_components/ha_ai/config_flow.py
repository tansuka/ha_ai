from homeassistant.helpers.config_entry_flow import config_flow

@config_flow.register("ha_ai_assistant")
class MeaningfulStateChangeFlow(config_flow.ConfigFlow):
    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.show_form()

        # Store selected entities in config entry
        return self.async_create_entry(title="HA AI Assistant", data=user_input)

    def show_form(self):
        return self.async_show_form(
            step_id="user",
            data_schema={
                "type": "form",
                "fields": {
                    "entities": {
                        "type": "selector",
                        "options": [{"entity_id": x.entity_id} for x in self.hass.states.async_all()],
                    }
                },
            },
        )
