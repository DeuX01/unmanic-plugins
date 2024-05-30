import logging
import requests
from unmanic.libs.unplugins.settings import PluginSettings

# Configure plugin logger
logger = logging.getLogger("Unmanic.Plugin.task_notifier")

class Settings(PluginSettings):
    settings = {
        'discord_webhook_url': '',  # Add your Discord webhook URL here
    }

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

def send_discord_embed(webhook_url, title, description, color):
    payload = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color,
            }
        ]
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(webhook_url, json=payload, headers=headers)
    
    if response.status_code != 204:
        logger.error(f"Failed to send Discord message: {response.status_code}, {response.text}")
        return False
    return True

def on_postprocessor_task_results(data):
    """
    Runner function - provides a means for additional postprocessor functions based on the task success.

    The 'data' object argument includes:
        final_cache_path                - The path to the final cache file that was then used as the source for all destination files.
        library_id                      - The library that the current task is associated with.
        task_processing_success         - Boolean, did all task processes complete successfully.
        file_move_processes_success     - Boolean, did all postprocessor movement tasks complete successfully.
        destination_files               - List containing all file paths created by postprocessor file movements.
        source_data                     - Dictionary containing data pertaining to the original source file.

    :param data:
    :return:
    """
    # Configure settings object (maintain compatibility with v1 plugins)
    if data.get('library_id'):
        settings = Settings(library_id=data.get('library_id'))
    else:
        settings = Settings()

    status = data.get('task_processing_success')
    task_status = "successfully processed" if status else "failed to process"
    source = data.get('source_data')["basename"]

    discord_webhook_url = settings.get_setting('discord_webhook_url')
    if not discord_webhook_url:
        logger.error("Discord webhook URL not configured.")
        return data

    # Create embed message for Discord
    title = "Unmanic Task Status"
    description = f"**File:** `{source}`\n**Status:** `{task_status}`"
    color = 3066993 if status else 15158332  # Green for success, red for failure

    # Send the notification to Discord
    result = send_discord_embed(discord_webhook_url, title, description, color)
    if not result:
        logger.error("Error sending Discord notification.")

    return data
