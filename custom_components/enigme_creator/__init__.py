import logging
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import entity_registry as er
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, ENTITY_TEMPLATES

_LOGGER = logging.getLogger(__name__)


# ══════════════════════════════════════════════════════════
#  FONCTION PRINCIPALE
# ══════════════════════════════════════════════════════════

async def create_enigme_entities(hass: HomeAssistant, prefix: str, enigme_name: str):
    """
    Crée les 10 entités standard pour une énigme.

    Args:
        hass        : instance Home Assistant
        prefix      : préfixe court de l'énigme  (ex: "SM", "SO", "RdS")
        enigme_name : nom complet de l'énigme     (ex: "Socle Magie")
    """

    prefix_lower = prefix.lower()   # sm / so / rds
    prefix_upper = prefix.upper()   # SM / SO / RDS

    results = {
        "created": [],
        "skipped": [],
        "errors":  []
    }

    registry = er.async_get(hass)

    for template in ENTITY_TEMPLATES:

        platform     = template["platform"]
        id_suffix    = template["id_suffix"]
        label_suffix = template["label_suffix"]
        config       = template["config"].copy()

        # ── Construction des identifiants ──────────────────────────── #
        # entity_id  : input_boolean.sm_valide
        # Nom affiché: SM_Valide
        entity_id    = f"{platform}.{prefix_lower}_{id_suffix}"
        display_name = f"{prefix_upper}_{label_suffix}"

        # ── Vérification existence ─────────────────────────────────── #
        if registry.async_get(entity_id):
            _LOGGER.info(f"[EnigmeCreator] ⏭️  Ignoré (déjà existant) : {entity_id}")
            results["skipped"].append(entity_id)
            continue

        # ── Préparation du payload ─────────────────────────────────── #
        config["name"] = display_name

        # ── Appel du service de création ───────────────────────────── #
        try:
            await hass.services.async_call(
                platform,
                "create",          # service HA natif
                config,
                blocking=True
            )
            _LOGGER.info(f"[EnigmeCreator] ✅ Créé : {entity_id}  ({display_name})")
            results["created"].append(entity_id)

        except Exception as e:
            _LOGGER.error(f"[EnigmeCreator] ❌ Erreur pour {entity_id} : {e}")
            results["errors"].append({"entity_id": entity_id, "error": str(e)})

    # ── Résumé ─────────────────────────────────────────────────────── #
    _LOGGER.info(
        f"[EnigmeCreator] Résumé pour '{enigme_name}' ({prefix_upper}) — "
        f"Créés: {len(results['created'])} | "
        f"Ignorés: {len(results['skipped'])} | "
        f"Erreurs: {len(results['errors'])}"
    )

    return results


# ══════════════════════════════════════════════════════════
#  SETUP DE L'INTEGRATION
# ══════════════════════════════════════════════════════════

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:

    hass.data.setdefault(DOMAIN, {})

    # ── Service appelable depuis HA ────────────────────────────────── #
    async def handle_create_enigme(call: ServiceCall):
        prefix      = call.data["prefix"]
        enigme_name = call.data["enigme_name"]
        await create_enigme_entities(hass, prefix, enigme_name)

    hass.services.async_register(
        DOMAIN,
        "create_enigme",
        handle_create_enigme,
        schema=vol.Schema({
            vol.Required("prefix"):      cv.string,
            vol.Required("enigme_name"): cv.string,
        })
    )

    _LOGGER.info("[EnigmeCreator] Service 'enigme_creator.create_enigme' enregistré")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.services.async_remove(DOMAIN, "create_enigme")
    return True
