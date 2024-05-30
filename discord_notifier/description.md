##### Description
This plugin sends notifications on task success/failure to Discord using embeds.

- Configure the plugin with your Discord webhook URL.
- Minimally, this should be a URL corresponding to the Discord webhook you want to use. To get a webhook URL, follow the instructions in the [Discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
- Add `discord_notifier` to your plugin stack and position accordingly in the post-processor marking task success/failure flow.
- Upon task completion, the `discord_notifier` plugin will send a notification with an embed message to your specified Discord channel.
- The embed message will include the file name and status of the task (successfully processed or failed to process) with appropriate coloring (green for success, red for failure).
