const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.GuildMembers,
        GatewayIntentBits.MessageContent
    ]
});

client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('messageCreate', message => {
    if (message.author.bot) return;

    if (message.content.includes('discord.gg/') || message.content.includes('https://')) {
        message.delete().catch(console.error);
        message.channel.send(`${message.author}, ممنوع نشر الرابط هنا!`).then(msg => {
            setTimeout(() => msg.delete().catch(console.error), 5000);
        });
    }
});

client.login(MTM0Mjg3MzYwNzczMDIzNzQ1MQ.GYarx3.41K6fJwmcCPmBNlDRaGruUMG7uOqbFYSmzh3Wo);
