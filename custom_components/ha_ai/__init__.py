import homeassistant.helpers.event as event_helper
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect

DOMAIN = "ha_ai_assistant"

async def async_setup_entry(hass: HomeAssistant, entry):
    entities = entry.data.get("entities", [])

    # Listen for state changes
    def handle_state_change(event):
        entity_id = event.data["entity_id"]
        new_state = event.data["new_state"].state
        old_state = event.data["old_state"].state if event.data["old_state"] else None

        # Log meaningful changes
        if old_state != new_state:
            hass.log(f"Meaningful change in {entity_id}: From '{old_state}' to '{new_state}'")

    # Register the listener
    event_helper.async_track_state_change(
        hass, entities, handle_state_change
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    # Remove listener if needed
    return True
