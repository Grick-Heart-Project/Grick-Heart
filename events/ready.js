Logger = require('../modules/logger');
logger = new Logger('main');

module.exports = async client => {
    // Log that the bot is online.
    logger.info(`${client.user.tag}, ready to serve ${client.users.cache.size} users in ${client.guilds.cache.size} servers.`, "ready");
  
    // Make the bot play something
    client.user.setActivity('Waterdeep: Dungeon of the Mad Mage', { type: 'PLAYING' }, { link: 'https://dnd.wizards.com/products/tabletop-games/rpg-products/waterdeep-dungeon-mad-mage'})
  };