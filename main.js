const Discord = require("discord.js");
const Enmap = require("enmap");
const fs = require("fs");
const request = require('request');

const client = new Discord.Client();
const config = require("./config.json");
client.config = config;
Logger = require('./modules/logger');
client.logger = new Logger('main');
client.commands = new Enmap();
client.aliases = new Enmap();

const url = "https://raw.githubusercontent.com/hydrostaticcog/Grick-Heart/master/package.json";
let options = {json: true};
let GHversion = require('./package.json')

client.logger.info(`Starting Grick Heart version ${GHversion.version} running Node version ${(Number(process.version.slice(1).split(".")[0]))}`);
if (Number(process.version.slice(1).split(".")[0]) < 12) {
  let errorN = new Error("Node 12.0.0 or higher is required. Update Node on your system.");
  client.logger.error(errorN)
}

request(url, options, (error, res, body) => {
  if (error) {
      return  console.log(error)
  };

  if (!error && res.statusCode == 200) {
    let GHversion = require("./package.json")
    if (body.version > GHversion.version) {
      console.log("**************** YOU ARE RUNNING A OLD VERSION OF GRICK HEART ****************")
      console.log(`******* YOU ARE RUNNING VERSION ${GHversion.version}. LATEST VERSION IS VERSION ${body.version} *******`)
    }
  }
})

fs.readdir("./events/", (err, files) => {
  if (err) return client.logger.error(err);
  files.forEach(file => {
    client.logger.info(`Attempting to load event ${file}`);
    const event = require(`./events/${file}`);
    let eventName = file.split(".")[0];
    client.on(eventName, event.bind(null, client));
    client.logger.info(`Successfully loaded event ${file}`);
  });
});

fs.readdir("./commands/", (err, files) => {
  if (err) return client.logger.error(err);
  files.forEach(file => {
    if (!file.endsWith(".js")) return;
    let props = require(`./commands/${file}`);
    let commandName = file.split(".")[0];
    client.logger.info(`Attempting to load command ${commandName}`);
    client.commands.set(commandName, props);
    client.logger.info(`Successfully loaded command ${commandName}`);
  });
});

client.login(config.token);
 
 