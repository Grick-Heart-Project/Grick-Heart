Logger = require('../modules/logger');
logger = new Logger('main');
const Discord = require('discord.js')
const client = new Discord.Client()
const config = require('../config.json');
const package = require('../package.json')
module.exports ={
    name: "version",
    description: "responds with version number/build info",
    args: true,
    execute(message, args){
        message.channel.send(`Running Grick-Heart version ${package.version} on Node.js version ${(Number(process.version.slice(1).split(".")[0]))}\nSupport available at https://discord.gg/vgmsVm2wbt`)
    }
}