# Task Notifier with Discord Embeds

## Overview
The Task Notifier with Discord Embeds plugin for Unmanic sends notifications about task success or failure to a specified Discord channel using embeds. This allows for clear and visually appealing notifications.

## Features
- Sends task completion notifications to Discord using embed messages.
- Configurable Discord webhook URL.
- Includes file name and task status (success or failure) in the notification.
- Uses color coding (green for success, red for failure) for easy status identification.

## Requirements
- Unmanic version 2 or higher.
- `requests` library for sending HTTP requests.

## Installation

### Step 1: Install the Plugin
1. Download the zip file.
2. In the settings > plugins section of unmanic choose instal plugin from file and select the zip file.

### Step 2: Configure the Plugin
Update your Unmanic configuration to include the Discord webhook URL. This URL can be obtained from the Discord server where you want to send the notifications. Follow the [Discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to create a webhook URL.

### Settings
Ensure the `discord_webhook_url` is set in your Unmanic settings.

## Usage
Add `discord_notifier` to your plugin stack and position it accordingly in the post-processor marking task success/failure flow.

Upon task completion, the plugin will send a notification with an embed message to your specified Discord channel. The embed message includes:
- The file name
- The status of the task (successfully processed or failed to process)
- Color-coded status (green for success, red for failure)

## Changelog
**<span style="color:#56adda">1.0.0</span>**
- Initial version
- Send task notifications using Discord embeds
- Ensure proper formatting and inclusion of colors in Discord notifications

## License
This plugin is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Contact
For support or questions, please contact Geralt.

---
