import { Client, Events, GatewayIntentBits } from 'discord.js';

const discordUserID = ''
const discordToken = ''

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});

client.login(discordToken);

console.log(client.users)

client.users.send(discordUserID, 'A new file has been uploaded to your Google Drive!')

setTimeout(function() {
  process.exit(0)
}, 2500);
