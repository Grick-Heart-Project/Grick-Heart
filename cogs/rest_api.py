import asyncio
import datetime
import json
from datetime import datetime
from typing import Dict, List, Union

import aiohttp_cors
import discord
import tortoise
from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound, HTTPForbidden, HTTPBadRequest, HTTPInternalServerError
from discord.ext import tasks

from utils.cog_class import Cog

class UptimeCog(Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.app = web.Application()
        self.cors = aiohttp_cors.setup(self.app)
        self.runner = web.AppRunner(self.app, access_log=self.bot.logger.logger)
        self.site = None
        self.bot.reload_config()
        self.user_callbacks: Dict[int, asyncio.Task] = {}
        self.done_user_callbacks: Dict[int, asyncio.Task] = {}
        bot.loop.create_task(self.run())

    def cog_unload(self):
        self.bot.logger.info(f"Grick-Heart JSON API is shutting down...")
        self.bot.loop.create_task(self.site.stop())
    
    async def onlineCheck(self, request):
        result = "online"
        return web.json_response(result)
    async def run(self):
        await self.bot.wait_until_ready()
        routes = [
            ('GET', '/', self.onlineCheck),
        ]
        for route_method, route_path, route_coro in routes:
            resource = self.cors.add(self.app.router.add_resource(route_path))
            self.cors.add(
                resource.add_route(route_method, route_coro), {
                    "*": aiohttp_cors.ResourceOptions(
                        allow_credentials=True,
                        allow_headers=("X-Requested-With", "Content-Type", "Authorization",),
                        max_age=3600,
                    )
                }
            )

        await self.runner.setup()
        self.site = web.TCPSite(self.runner, '0.0.0.0', 5001)
        await self.site.start()
        self.bot.logger.info(f"Grick Heart JSON API listening")
        await self.bot.wait_until_ready()
        app = web.Application()
        routes = web.RouteTableDef()

setup = UptimeCog.setup
